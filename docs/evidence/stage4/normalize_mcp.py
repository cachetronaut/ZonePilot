"""Rebuild Stage 4 MCP input from captured hosted tool results, without a key/network.

Run from the repository root as:
python3.14 -B -m docs.evidence.stage4.normalize_mcp --output-dir reports/mcp-input
Then import that directory's evidence.json with zonepilot.report.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path

from zonepilot.engine import geocode_result, number
from zonepilot.geometry import haversine, valid_point
from zonepilot.report import dumps, finalize

BASE = Path('docs/evidence/stage4/live')
LIMITATION = 'Route-time classification only at measured points; no continuous zone.'
SETTINGS = {'budget_seconds': 1200, 'mode': 'drive', 'traffic': 'free_flow',
            'route_type': 'balanced', 'units': 'metric', 'direction': 'outbound',
            'boundary_rule': 'Known outbound time at or below budget is in zone; no continuous boundary.'}


def require(condition):
    if not condition:
        raise ValueError('Captured MCP evidence does not satisfy the recorded acquisition contract.')


def calls(phase):
    session = json.loads((BASE / ('mcp-' + phase + '.json')).read_text())
    require(session['approximation'] is True and session['exit_code'] == 0)
    pending = {}
    result = []
    for event in session['session_events']:
        if event['event'] == 'tool_use':
            require(event['id'] not in pending)
            pending[event['id']] = event
        elif event['event'] == 'tool_result':
            call = pending.pop(event['tool_use_id'])
            require(not event['is_error'])
            # Claude's stream projects the typed structured result as JSON text.
            payload = json.loads(event['content'])
            require(isinstance(payload, dict) and not payload.get('isError', False)
                    and 'error' not in payload)
            result.append({'approximation': True, 'limitation': LIMITATION,
                           'session': 'mcp-' + phase + '.json',
                           'tool_use_id': call['id'],
                           'tool': call['name'].removeprefix('mcp__geoapify__'),
                           'arguments': call['arguments'], 'result': payload})
    require(not pending)
    return result


def geocode(call, address):
    args, result = call['arguments'], call['result']
    require(args == {'query': address, 'limit': 5} and result['query'] == address)
    require(type(result['count']) is int and result['count'] == len(result['results']))
    geojson = {'type': 'FeatureCollection', 'features': [
        {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [r.get('lon'), r.get('lat')]},
         'properties': r} for r in result['results']]}
    resolved, point, evidence, reason = geocode_result(geojson)
    require(reason is None)
    return resolved, point, evidence


def matrix(call, origin, targets):
    args, result = call['arguments'], call['result']
    require(args == {'sources': [{'lon': origin[0], 'lat': origin[1]}],
                     'targets': [{'lon': p[0], 'lat': p[1]} for p in targets],
                     'mode': 'drive', 'units': 'metric', 'type': 'balanced', 'traffic': 'free_flow'})
    require(result['units'] == 'metric' and result['distance_units'] == 'meters'
            and result['time_units'] == 'seconds')
    # Hosted output contains snapped locations, not original_location. Original
    # coordinates/settings are verified against the captured call arguments.
    for field, count in [('sources', 1), ('targets', len(targets))]:
        require(len(result[field]) == count)
        require(all(valid_point([p['lon'], p['lat']]) for p in result[field]))
    cells = result['sources_to_targets']
    require(len(cells) == 1 and len(cells[0]) <= len(targets))
    indexed = {}
    for cell in cells[0]:
        if cell is None:
            continue
        i = cell['target_index']
        require(type(cell['source_index']) is int and cell['source_index'] == 0
                and type(i) is int and 0 <= i < len(targets) and i not in indexed)
        if cell.get('time') is None and cell.get('distance') is None:
            indexed[i] = ('no_route', None, None)
        else:
            indexed[i] = ('ok', number(cell['time']), number(cell['distance']))
    return [indexed.get(i, ('no_route', None, None)) for i in range(len(targets))]


def rebuild(destination):
    preflight, preliminary, final = calls('preflight'), calls('customers'), calls('final-customers')
    business_input = json.loads(Path('data/sample_business.json').read_text())
    inputs = list(csv.DictReader(Path('data/sample_customers.csv').open()))
    require(len(inputs) == 20)
    evidence, artifacts = [], {}

    def capture(call, operation=None):
        identifier = f'e{len(evidence) + 1:03d}'
        artifact = f'evidence/{identifier}.json'
        content = dumps(call).encode()
        evidence.append({'id': identifier, 'kind': 'mcp',
                         'operation': operation or call['tool'],
                         'artifact': artifact, 'sha256': hashlib.sha256(content).hexdigest()})
        artifacts[artifact] = content
        return identifier

    origin_call = next(c for c in preflight if c['tool'] == 'geocode_address')
    resolved, origin, ge = geocode(origin_call, business_input['address'])
    capture(origin_call, 'geocode_business')
    business = {'name': business_input['name'], 'input_address': business_input['address'],
                'resolved_address': resolved, 'coordinates': origin, 'geocode_evidence': ge}
    geocodes = {c['arguments']['query']: c for c in preliminary + final if c['tool'] == 'geocode_address'}
    rows = []
    for i, item in enumerate(inputs, 1):
        call = geocodes[item['address']]
        resolved, point, ge = geocode(call, item['address'])
        rows.append({'row_id': i, 'name': item['name'], 'reference': item['reference'],
                     'input_address': item['address'], 'resolved_address': resolved,
                     'coordinates': point, 'geocode_status': 'resolved', 'geocode_reason': None,
                     'geocode_evidence': ge, 'evidence_refs': [capture(call, 'geocode_customer')],
                     'route_within_budget': None, 'borderline': None, 'membership_route_disagreement': None})
    customer_matrix = next(c for c in final if c['tool'] == 'calculate_route_matrix')
    ref = capture(customer_matrix, 'calculate_route_matrix_customers')
    for row, (state, seconds, distance) in zip(rows, matrix(customer_matrix, origin, [r['coordinates'] for r in rows])):
        row.update(route_status=state, time_seconds=seconds, distance_meters=distance,
                   verdict='unknown' if seconds is None else 'in_zone' if seconds <= 1200 else 'out_of_zone')
        row['evidence_refs'].append(ref)

    search = next(c for c in preliminary if c['tool'] == 'search_places')
    require(search['arguments'] == {'category': 'service', 'lat': origin[1], 'lon': origin[0],
                                    'radius_meters': 20000, 'limit': 20})
    places = search['result']
    require(places['category'] == 'service' and places['radius_meters'] == 20000
            and places['coordinates'] == {'lat': origin[1], 'lon': origin[0]}
            and places['count'] == len(places['results']) <= 20)
    capture(search)
    candidates, seen, duplicates, invalid = [], set(), 0, 0
    for place in places['results']:
        point = [place.get('lon'), place.get('lat')]
        identifier = place.get('place_id')
        if not identifier:
            encoded = json.dumps([point, place.get('name')], sort_keys=True, separators=(',', ':'), ensure_ascii=False)
            identifier = 'synthetic-id:' + hashlib.sha256(encoded.encode()).hexdigest()
        if identifier in seen:
            duplicates += 1
            continue
        seen.add(identifier)
        if not valid_point(point):
            invalid += 1
            continue
        candidates.append({'id': identifier, 'name': place.get('name'), 'address': place.get('formatted'),
                           'categories': place['categories'], 'coordinates': point})
    competitor_matrix = [c for c in preliminary if c['tool'] == 'calculate_route_matrix'][-1]
    capture(competitor_matrix, 'calculate_route_matrix_competitors')
    for candidate, (state, seconds, distance) in zip(candidates, matrix(competitor_matrix, origin, [c['coordinates'] for c in candidates])):
        candidate.update(route_status=state, time_seconds=seconds, distance_meters=distance)
    candidates.sort(key=lambda c: c['id'])
    extent = {'method': 'circle', 'parameters': {'center': origin, 'radius_meters': 20000}}
    normalized = {'representation': 'mcp_competitor_classification', 'approximation': True,
                  'category': 'service', 'search_extent': extent,
                  'settings': {k: v for k, v in SETTINGS.items() if k != 'boundary_rule'},
                  'max_candidates': 20, 'pagination': False, 'search_status': 'ok',
                  'returned_count': places['count'], 'duplicate_count': duplicates,
                  'invalid_coordinate_count': invalid, 'candidates': candidates}
    capture(normalized, 'mcp_competitor_classification')
    records, outside, unknown = [], 0, invalid
    for c in candidates:
        if c['route_status'] != 'ok':
            unknown += 1
        elif c['time_seconds'] > 1200:
            outside += 1
        else:
            records.append({k: c[k] for k in ('id', 'name', 'address', 'categories', 'coordinates')} |
                           {'verdict': 'in_zone', 'geodesic_distance_meters': number(haversine(origin, c['coordinates']), 3)})
    competitors = {'status': 'partial' if unknown else 'ok', 'category': 'service', 'search_extent': extent,
                   'coverage': 'sampled', 'cap_reached': places['count'] == 20,
                   'returned_count': places['count'], 'duplicate_count': duplicates, 'unclassified_count': unknown,
                   'observed_in_zone_count': len(records), 'observed_out_of_zone_count': outside, 'records': records}
    for c in preflight:
        if c['tool'] != 'geocode_address':
            c['diagnostic_only'] = c['tool'] in ('transform_geometry', 'evaluate_spatial_relation', 'measure_geometry', 'reverse_geocode_coordinates')
            capture(c)
    capture(next(c for c in preliminary if c['tool'] == 'calculate_route'))
    acquired = {'schema_version': '1.0', 'path': 'mcp', 'data_mode': 'live',
                'run_timestamp_utc': json.loads((BASE / 'mcp-final-customers.json').read_text())['completed_at_utc'],
                'business': business, 'settings': SETTINGS,
                'zone': {'method': 'route_time_at_points', 'approximation': True,
                         'parameters': {'budget_seconds': 1200}, 'limitations': [LIMITATION], 'evidence_refs': [ref]},
                'customers': rows, 'competitors': competitors, 'errors': [],
                'warnings': ['Fictional business/customer identities at real public demo locations; no affiliation or actual customer relationship.',
                             'Hosted acquisition spans captured sessions; final twenty-target matrix supersedes the preliminary nineteen-target matrix.',
                             'Competitor coverage is sampled, at most 20 candidates and no pagination.',
                             'The category service is broad; these candidates are not verified plumbing competitors.',
                             'Claude projects hosted structured results as JSON text; normalization validates typed results and captured arguments.'],
                'evidence': evidence, 'attributions': [
                    {'source': 'Geoapify', 'text': 'Live hosted MCP location services.', 'url': 'https://geoapify.com'},
                    {'source': 'OpenStreetMap', 'text': 'Live map data: © OpenStreetMap contributors, ODbL.', 'url': 'https://www.openstreetmap.org/copyright'}]}
    finalize(acquired)
    destination.mkdir(parents=True, exist_ok=False)
    for path, content in artifacts.items():
        target = destination / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    (destination / 'evidence.json').write_text(dumps(acquired))
    print('approximation=true: normalized captured hosted evidence; import still verifies all artifact hashes and competitor membership.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    rebuild(parser.parse_args().output_dir)
