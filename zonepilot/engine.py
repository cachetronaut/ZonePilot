"""Acquisition and normalization shared by live REST and authored fixture replay."""

import hashlib
import json
from decimal import Decimal, ROUND_HALF_EVEN, InvalidOperation

from .client import APIError, finite_number
from .geometry import GeometryError, bounds, contains, haversine, valid_point, validate_geometry
from .report import ReportError, dumps

BOUNDARY_RULE = 'All ring boundaries are in zone; segment-distance tolerance 1e-9 degrees.'


def number(value, places=6):
    if not finite_number(value) or value < 0:
        raise APIError()
    try:
        return float(Decimal(str(value)).quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_EVEN))
    except InvalidOperation:
        raise APIError() from None


def features(data, cap):
    if not isinstance(data, dict) or data.get('type') != 'FeatureCollection':
        raise APIError()
    rows = data.get('features')
    if not isinstance(rows, list) or len(rows) > cap:
        raise APIError()
    if any(not isinstance(f, dict) or f.get('type') != 'Feature'
           or not isinstance(f.get('properties'), dict)
           or not isinstance(f.get('geometry'), dict) for f in rows):
        raise APIError()
    return rows


def blank_geocode():
    return {'candidate_count': None, 'confidence': None, 'confidence_building_level': None,
            'match_type': None, 'result_type': None}


def geocode_result(data):
    candidates = features(data, 5)
    evidence = blank_geocode()
    evidence['candidate_count'] = len(candidates)
    eligible = []
    for feature in candidates:
        p, geometry = feature['properties'], feature['geometry']
        rank = p.get('rank', {})
        if not isinstance(rank, dict):
            continue
        if (geometry.get('type') == 'Point' and valid_point(geometry.get('coordinates'))
                and p.get('result_type') == 'building'
                and isinstance(p.get('formatted'), str) and p['formatted'].strip()
                and all(finite_number(rank.get(k)) and .95 <= rank[k] <= 1
                        for k in ('confidence', 'confidence_building_level'))
                and (rank.get('match_type') is None or isinstance(rank['match_type'], str))):
            eligible.append(feature)
    if len(eligible) != 1:
        reason = 'no_match' if not candidates else 'ambiguous' if len(eligible) > 1 else 'insufficient_precision'
        return None, None, evidence, reason
    chosen = eligible[0]
    rank = chosen['properties']['rank']
    evidence.update({k: rank.get(k) for k in ('confidence', 'confidence_building_level', 'match_type')})
    evidence['result_type'] = 'building'
    return chosen['properties']['formatted'], chosen['geometry']['coordinates'], evidence, None


def geocode_artifact(data):
    """Retain candidate decision evidence without unrelated contact/provider fields."""
    return {'type': 'FeatureCollection', 'features': [
        {'type': 'Feature', 'geometry': f['geometry'], 'properties': {
            k: f['properties'][k] for k in ('formatted', 'result_type', 'rank') if k in f['properties']}}
        for f in features(data, 5)]}


def zone_geometry(data, origin, seconds):
    if isinstance(data, dict) and 'crs' in data:
        raise APIError('unsupported_geometry')
    polygons = []
    for feature in features(data, 32):
        if 'crs' in feature or 'crs' in feature['geometry']:
            raise APIError('unsupported_geometry')
        p = feature['properties']
        if (p.get('mode') != 'drive' or p.get('type') != 'time'
                or not finite_number(p.get('range')) or p['range'] != seconds
                or not valid_point([p.get('lon'), p.get('lat')])
                or [p['lon'], p['lat']] != origin
                or any(p.get(k, v) != v for k, v in {
                    'route_type': 'balanced', 'traffic': 'free_flow', 'units': 'metric'}.items())
                or p.get('avoid', [])):
            raise APIError()
        geometry = feature['geometry']
        if geometry.get('type') == 'Polygon':
            polygons.append(geometry.get('coordinates'))
        elif geometry.get('type') == 'MultiPolygon':
            coordinates = geometry.get('coordinates')
            if not isinstance(coordinates, list):
                raise APIError()
            polygons.extend(coordinates)
        else:
            raise APIError('unsupported_geometry')
    geometry = {'type': 'MultiPolygon', 'coordinates': polygons}
    try:
        validate_geometry(geometry)
    except GeometryError:
        raise APIError('unsupported_geometry') from None
    return geometry


def matrix_results(data, origin, targets):
    if (not isinstance(data, dict)
            or any(data.get(k) != v for k, v in {'mode': 'drive', 'units': 'metric', 'distance_units': 'meters'}.items())
            or any(data.get(k, v) != v for k, v in {'traffic': 'free_flow', 'type': 'balanced'}.items())
            or data.get('avoid', [])):
        raise APIError()
    for key, expected in (('sources', [origin]), ('targets', targets)):
        points = data.get(key)
        if not isinstance(points, list) or len(points) != len(expected):
            raise APIError()
        for point, original in zip(points, expected):
            if (not isinstance(point, dict) or point.get('original_location') != original
                    or ('location' in point and not valid_point(point['location']))):
                raise APIError()
    matrix = data.get('sources_to_targets')
    if not isinstance(matrix, list) or len(matrix) != 1 or not isinstance(matrix[0], list) or len(matrix[0]) > len(targets):
        raise APIError()
    result, seen = {}, set()
    for cell in matrix[0]:
        if cell is None:
            continue
        if not isinstance(cell, dict):
            raise APIError()
        source, target = cell.get('source_index'), cell.get('target_index')
        if type(source) is not int or source != 0 or type(target) is not int or not 0 <= target < len(targets) or target in seen:
            raise APIError()
        seen.add(target)
        if not {'time', 'distance'} <= cell.keys():
            result[target] = ('error', None, None)
        elif cell['time'] is None and cell['distance'] is None:
            result[target] = ('no_route', None, None)
        else:
            try:
                result[target] = ('ok', number(cell.get('time')), number(cell.get('distance')))
            except APIError:
                result[target] = ('error', None, None)
    return [result.get(i, ('no_route', None, None)) for i in range(len(targets))]


def competitor_blank(category=None, bbox=None):
    return {'status': 'not_requested' if category is None else 'unavailable', 'category': category,
            'search_extent': None if bbox is None else {'method': 'rectangle', 'parameters': {'bbox': bbox}},
            'coverage': None, 'cap_reached': None, 'returned_count': None, 'duplicate_count': None,
            'unclassified_count': None, 'observed_in_zone_count': None, 'observed_out_of_zone_count': None,
            'records': []}


def valid_text(value, *, nullable=False, nonblank=False):
    if value is None and nullable:
        return True
    if not isinstance(value, str) or (nonblank and not value.strip()):
        return False
    try:
        value.encode('utf-8')
    except UnicodeError:
        return False
    return True


def competitors_result(data, category, geometry, origin):
    candidates = features(data, 20)
    section = competitor_blank(category, bounds(geometry))
    section.update(status='ok', coverage='sampled', cap_reached=len(candidates) == 20,
                   returned_count=len(candidates), duplicate_count=0, unclassified_count=0,
                   observed_in_zone_count=0, observed_out_of_zone_count=0)
    seen = set()
    for feature in candidates:
        p, g = feature['properties'], feature['geometry']
        point = g.get('coordinates')
        name, address, categories = p.get('name'), p.get('formatted'), p.get('categories')
        identifier = p.get('place_id')
        if not isinstance(identifier, str) or not identifier:
            try:
                canonical = json.dumps([point, name], sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False)
                identifier = 'synthetic-id:' + hashlib.sha256(canonical.encode('utf-8')).hexdigest()
            except (ValueError, TypeError, UnicodeError):
                section['unclassified_count'] += 1
                continue
        if identifier in seen:
            section['duplicate_count'] += 1
            continue
        seen.add(identifier)
        if (g.get('type') != 'Point' or not valid_point(point)
                or not valid_text(identifier, nonblank=True)
                or not valid_text(name, nullable=True)
                or not valid_text(address, nullable=True)
                or not isinstance(categories, list)
                or any(not valid_text(c, nonblank=True) for c in categories)):
            section['unclassified_count'] += 1
            continue
        if not contains(geometry, point):
            section['observed_out_of_zone_count'] += 1
            continue
        section['records'].append({'id': identifier, 'name': name, 'address': address, 'categories': categories,
            'coordinates': point, 'verdict': 'in_zone', 'geodesic_distance_meters': number(haversine(origin, point), 3)})
        section['observed_in_zone_count'] += 1
    section['records'].sort(key=lambda x: x['id'])
    if section['unclassified_count']:
        section['status'] = 'partial'
    return section


def acquire(client, inputs, timestamp, data_mode):
    """Return a stage envelope and permitted evidence artifacts, never raw errors."""
    errors, warnings, evidence, artifacts = [], [], [], {}

    def capture(operation, data):
        identifier = f'e{len(evidence) + 1:03d}'
        path = f'evidence/{identifier}.json'
        try:
            content = dumps(data).encode('utf-8')
        except ReportError:
            # Evidence rejection is an acquisition failure at the caller's scope.
            # Do not publish a reference or artifact for rejected provider data.
            raise APIError() from None
        artifacts[path] = content
        evidence.append({'id': identifier, 'kind': 'synthetic' if data_mode == 'synthetic' else 'rest',
                         'operation': operation, 'artifact': path, 'sha256': hashlib.sha256(content).hexdigest()})
        return identifier

    raw = client.geocode(inputs['business_address'])
    resolved, origin, business_geocode, reason = geocode_result(raw)
    capture('geocode_business', geocode_artifact(raw))
    if reason:
        raise APIError('origin_unresolved')
    seconds = inputs['minutes'] * 60
    geometry = zone_geometry(client.isoline(origin, seconds), origin, seconds)
    zone_ref = capture('isoline', geometry)
    rows = []
    for item in inputs['customers']:
        row = {**item, 'input_address': item['address'], 'resolved_address': None, 'coordinates': None,
               'geocode_status': 'unresolved', 'geocode_reason': None, 'geocode_evidence': blank_geocode(),
               'verdict': 'unknown', 'route_status': 'not_attempted', 'time_seconds': None,
               'distance_meters': None, 'route_within_budget': None, 'borderline': None,
               'membership_route_disagreement': None, 'evidence_refs': []}
        del row['address']
        try:
            raw = client.geocode(item['address'])
            address, point, geocode, reason = geocode_result(raw)
            row['evidence_refs'].append(capture('geocode_customer', geocode_artifact(raw)))
            row.update(resolved_address=address, coordinates=point, geocode_evidence=geocode, geocode_reason=reason)
            if reason is None:
                row['geocode_status'] = 'resolved'
                row['verdict'] = 'in_zone' if contains(geometry, point) else 'out_of_zone'
        except APIError as error:
            if error.code in ('authentication', 'request_budget'):
                raise
            row['geocode_reason'] = error.code
            errors.append(error.record([item['row_id']]))
        rows.append(row)
    resolved_rows = [r for r in rows if r['geocode_status'] == 'resolved']
    if resolved_rows:
        try:
            targets = [r['coordinates'] for r in resolved_rows]
            raw = client.matrix(origin, targets)
            measurements = matrix_results(raw, origin, targets)
            reference = capture('route_matrix', {
                'representation': 'normalized_route_matrix',
                'origin': origin, 'targets': targets,
                'mode': 'drive', 'units': 'metric', 'distance_units': 'meters',
                'traffic': 'free_flow', 'type': 'balanced',
                'measurements': [
                    {'source_index': 0, 'target_index': index, 'route_status': state,
                     'time_seconds': time_value, 'distance_meters': distance}
                    for index, (state, time_value, distance) in enumerate(measurements)],
            })
            for row, (state, seconds_value, distance) in zip(resolved_rows, measurements):
                row.update(route_status=state, time_seconds=seconds_value, distance_meters=distance)
                row['evidence_refs'].append(reference)
                if state == 'error':
                    errors.append(APIError().record([row['row_id']]))
        except APIError as error:
            if error.code in ('authentication', 'request_budget'):
                raise
            for row in resolved_rows:
                row['route_status'] = 'error'
            errors.append(error.record([r['row_id'] for r in resolved_rows]))
    category = inputs['competitor_category']
    competitors = competitor_blank()
    if category is not None:
        competitors = competitor_blank(category, bounds(geometry))
        try:
            raw = client.places(category, bounds(geometry))
            competitors = competitors_result(raw, category, geometry, origin)
            # Retain normalized records/counts, not unrelated raw contact details.
            capture('places', competitors)
            warnings.append('Competitor coverage is sampled, at most 20 candidates and no pagination.')
            if category == 'service':
                warnings.append('The category service is broad; these candidates are not verified plumbing competitors.')
        except APIError as error:
            if error.code in ('authentication', 'request_budget'):
                raise
            errors.append(error.record())
    if data_mode == 'live':
        warnings.append(f'HTTP attempts: {client.attempts}; isoline polls: {client.polls}; billed credits unavailable.')
    if data_mode == 'synthetic':
        warnings.append('Authored synthetic fixtures, not a recording of live Geoapify calls.')
    acquired = {'schema_version': '1.0', 'path': 'cli', 'data_mode': data_mode, 'run_timestamp_utc': timestamp,
        'business': {'name': inputs['business_name'], 'input_address': inputs['business_address'],
                     'resolved_address': resolved, 'coordinates': origin, 'geocode_evidence': business_geocode},
        'settings': {'budget_seconds': seconds, 'mode': 'drive', 'traffic': 'free_flow', 'route_type': 'balanced',
                     'units': 'metric', 'direction': 'outbound', 'boundary_rule': BOUNDARY_RULE},
        'zone': {'method': 'geoapify_isoline', 'approximation': False,
                 'parameters': {'range_seconds': seconds, 'boundary_tolerance_degrees': 1e-9},
                 'limitations': ['Outbound free-flow road-time estimate; no live traffic, return trip or profitability model.',
                                BOUNDARY_RULE], 'evidence_refs': [zone_ref]},
        'customers': rows, 'competitors': competitors, 'errors': errors, 'warnings': warnings,
        'evidence': evidence, 'attributions': [
            {'source': 'Geoapify', 'text': 'API contracts and location services.', 'url': 'https://geoapify.com'},
            {'source': 'OpenStreetMap', 'text': 'Live map data: © OpenStreetMap contributors, ODbL. Synthetic fixtures contain no live map records.',
             'url': 'https://www.openstreetmap.org/copyright'}]}
    partial = any(r['geocode_status'] == 'unresolved' or r['route_status'] != 'ok' for r in rows)
    partial |= competitors['status'] in ('unavailable', 'partial')
    return {'status': 'partial' if partial else 'succeeded', 'result': acquired, 'errors': errors}, artifacts
