import contextlib
import copy
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from zonepilot.client import APIError, Client, ReplayClient
from zonepilot.engine import acquire, competitors_result, geocode_result, matrix_results, zone_geometry
from zonepilot.cli import main, read_customers, categories, validate_inputs
from zonepilot.report import ReportError, finalize, dumps, render_markdown, validate

FIXTURE = Path(__file__).parent / 'fixtures/sample/run.json'


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.bundle=json.loads(FIXTURE.read_text())

    def run_bundle(self, bundle=None):
        b=bundle or self.bundle
        envelope,artifacts=acquire(ReplayClient(b['responses']), b['inputs'], b['run_timestamp_utc'], 'synthetic')
        return finalize(envelope['result']), artifacts

    def test_twenty_rows_boundary_borderline_disagreement_and_tied_max(self):
        report,_=self.run_bundle()
        self.assertEqual(report['summary']['total'],20)
        self.assertEqual(report['customers'][12]['verdict'],'in_zone')
        self.assertEqual(report['summary']['borderline'],2)
        self.assertEqual(report['summary']['max_time_row_ids'],[19,20])
        self.assertEqual(report['customers'][0]['time_seconds'],0)
        self.assertFalse(report['customers'][10]['borderline'])
        self.assertTrue(report['customers'][11]['borderline'])
        self.assertTrue(report['customers'][12]['borderline'])
        self.assertFalse(report['customers'][13]['borderline'])
        self.assertTrue(report['customers'][11]['membership_route_disagreement'])

    def test_fixed_clock_reports_match_reviewable_golden_files(self):
        report, _ = self.run_bundle()
        expected = FIXTURE.parent.parent / 'expected'
        self.assertEqual(dumps(report), (expected / 'report.json').read_text(encoding='utf-8'))
        self.assertEqual(render_markdown(report), (expected / 'report.md').read_text(encoding='utf-8'))

    def test_competitor_cap_reached_and_missing_ids_stable(self):
        b = self.bundle
        template = b['responses'][-1]['response']['features'][0]
        candidates = []
        for index in range(20):
            candidate = copy.deepcopy(template)
            candidate['properties']['place_id'] = f'fixture-{index:02d}'
            candidates.append(candidate)
        b['responses'][-1]['response']['features'] = candidates
        report, _ = self.run_bundle()
        self.assertTrue(report['competitors']['cap_reached'])
        self.assertEqual(report['competitors']['coverage'], 'sampled')
        del candidates[0]['properties']['place_id']
        first, _ = self.run_bundle()
        second, _ = self.run_bundle()
        self.assertEqual(first['competitors'], second['competitors'])
        self.assertTrue(any(r['id'].startswith('synthetic-id:') for r in first['competitors']['records']))

    def test_geocode_candidate_policy(self):
        base=self.bundle['responses'][0]['response']
        self.assertIsNone(geocode_result(base)[3])
        self.assertEqual(geocode_result({'type':'FeatureCollection','features':[]})[3],'no_match')
        double=copy.deepcopy(base);double['features']*=2
        self.assertEqual(geocode_result(double)[3],'ambiguous')
        for change in ('rank','precision','coordinate','centroid'):
            data=copy.deepcopy(base); f=data['features'][0]
            if change=='rank':del f['properties']['rank']['confidence_building_level']
            if change=='precision':f['properties']['rank']['confidence']=.949999
            if change=='coordinate':f['geometry']['coordinates']=[181,32]
            if change=='centroid':f['properties']['result_type']='street'
            self.assertEqual(geocode_result(data)[3],'insufficient_precision')
        data=copy.deepcopy(base)
        data['features'][0]['properties']['rank'].update(confidence=.95,confidence_building_level=.95)
        self.assertIsNone(geocode_result(data)[3])

    def test_unresolved_customer_kept_and_route_targets_adjusted(self):
        b=self.bundle
        b['responses'][2]['response']['features']=[]
        matrix=b['responses'][-2]['response'];matrix['targets']=matrix['targets'][1:]
        matrix['sources_to_targets'][0]=[dict(c,target_index=c['target_index']-1) for c in matrix['sources_to_targets'][0] if c['target_index']>0]
        report,_=self.run_bundle()
        self.assertEqual(report['run_status'],'partial')
        self.assertEqual(report['customers'][0]['geocode_reason'],'no_match')
        self.assertEqual(report['customers'][0]['route_status'],'not_attempted')
        self.assertEqual(report['summary']['total'],20)

    def test_origin_failure_and_global_auth_abort(self):
        self.bundle['responses'][0]['response']['features']=[]
        with self.assertRaisesRegex(APIError,'business'): self.run_bundle()
        b=json.loads(FIXTURE.read_text());b['responses'][2]={'operation':'geocode','error':'authentication'}
        with self.assertRaisesRegex(APIError,'authentication'): self.run_bundle(b)

    def test_matrix_cell_missing_no_route_and_invalid_measurement(self):
        matrix=self.bundle['responses'][-2]['response']
        matrix['sources_to_targets'][0]=[c for c in matrix['sources_to_targets'][0] if c['target_index']!=0]
        for c in matrix['sources_to_targets'][0]:
            if c['target_index']==1:c.update(time=None,distance=None)
            if c['target_index']==2:c['time']=-1
        report,_=self.run_bundle()
        self.assertEqual([r['route_status'] for r in report['customers'][:3]],['no_route','no_route','error'])
        self.assertTrue(all(r['verdict']=='in_zone' for r in report['customers'][:3]))
        self.assertTrue(all(r['time_seconds'] is None for r in report['customers'][:3]))
        self.assertEqual(report['run_status'],'partial')

    def test_missing_measurement_fields_are_error_not_no_route(self):
        cells = self.bundle['responses'][-2]['response']['sources_to_targets'][0]
        cells[-1].pop('time')
        cells[-1].pop('distance')
        report, _ = self.run_bundle()
        self.assertEqual(report['customers'][0]['route_status'], 'error')
        self.assertEqual(report['customers'][1]['route_status'], 'ok')

    def test_bad_matrix_units_fail_only_route_stage(self):
        self.bundle['responses'][-2]['response']['units']='imperial'
        report,_=self.run_bundle()
        self.assertEqual(report['summary']['known_routes'],0)
        self.assertEqual(report['summary']['in_zone'],13)
        self.assertIsNone(report['summary']['max_time_seconds'])

    def test_competitor_duplicates_invalid_zero_failure_and_cap(self):
        candidates=self.bundle['responses'][-1]['response']['features']
        candidates.append(copy.deepcopy(candidates[0]))
        invalid=copy.deepcopy(candidates[0]);invalid['properties']['place_id']='invalid';invalid['geometry']['coordinates']=[181,32]
        candidates.append(invalid)
        report,_=self.run_bundle();c=report['competitors']
        self.assertEqual((c['returned_count'],c['duplicate_count'],c['unclassified_count']),(4,1,1))
        self.assertEqual(c['status'],'partial')
        self.bundle['responses'][-1]['response']['features']=[]
        report,_=self.run_bundle();self.assertEqual(report['competitors']['observed_in_zone_count'],0)
        self.bundle['responses'][-1]={'operation':'places','error':'request_failed'}
        report,_=self.run_bundle();self.assertIsNone(report['competitors']['observed_in_zone_count'])
        self.assertEqual(report['competitors']['status'],'unavailable')

    def test_isoline_mismatched_range_and_geometry_rejected(self):
        self.bundle['responses'][1]['response']['features'][0]['properties']['range']=900
        with self.assertRaises(APIError):self.run_bundle()

    def test_no_route_fallback_is_invented_for_generic_failure(self):
        self.bundle['responses'][-2]={'operation':'matrix','error':'request_failed'}
        report,_=self.run_bundle()
        self.assertTrue(all(r['route_status']=='error' for r in report['customers']))

    def test_mocked_http_malformed_evidence_retains_other_rows(self):
        for scope in ('customer', 'matrix'):
            with self.subTest(scope=scope):
                bundle = copy.deepcopy(self.bundle)
                matrix = bundle['responses'][-2]['response']
                if scope == 'customer':
                    bundle['responses'][2]['response']['features'][0]['properties']['formatted'] = chr(0xd800)
                    matrix['targets'] = matrix['targets'][1:]
                    matrix['sources_to_targets'][0] = [dict(c, target_index=c['target_index'] - 1)
                        for c in matrix['sources_to_targets'][0] if c['target_index'] > 0]
                else:
                    next(c for c in matrix['sources_to_targets'][0] if c['target_index'] == 0)['time'] = 1e309
                    matrix['unrelated_provider_metadata'] = chr(0xd800)
                responses = iter(bundle['responses'])
                def transport(request, timeout):
                    body = json.dumps(next(responses)['response']).replace('Infinity', '1e309').encode()
                    return 200, {}, body
                with patch.dict(os.environ, {'GEOAPIFY_API_KEY': 'SYNTHETIC_CREDENTIAL_SENTINEL'}, clear=True), \
                        patch('urllib.request.OpenerDirector.open', side_effect=AssertionError('network forbidden')):
                    client = Client(transport=transport)
                    envelope, artifacts = acquire(client, bundle['inputs'], bundle['run_timestamp_utc'], 'synthetic')
                report = finalize(envelope['result'])
                self.assertEqual(report['summary']['known_routes'], 19)
                self.assertEqual(report['run_status'], 'partial')
                self.assertTrue(all(row['route_status'] == 'ok' for row in report['customers'][1:]))
                for content in artifacts.values():
                    dumps(json.loads(content))
                self.assertEqual(client.attempts, 24)


class CLITests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)

    def call(self,args):
        out,err=io.StringIO(),io.StringIO()
        with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):result=main(args)
        return result,out.getvalue(),err.getvalue()

    def test_replay_without_key_no_network_and_deterministic_pair(self):
        with patch.dict(os.environ,{},clear=True),patch('urllib.request.OpenerDirector.open',side_effect=AssertionError('network forbidden')):
            for name in ('a','b'):
                code,_,error=self.call(['--replay',str(FIXTURE),'--output-dir',str(self.root/name)])
                self.assertEqual(code,0,error)
        for filename in ('report.json','report.md'):
            self.assertEqual((self.root/'a'/filename).read_bytes(),(self.root/'b'/filename).read_bytes())

    def replay_modified(self, label, mutate):
        bundle = json.loads(FIXTURE.read_text(encoding='utf-8'))
        mutate(bundle)
        source = self.root / (label + '.json')
        source.write_text(json.dumps(bundle), encoding='utf-8')
        destination = self.root / label
        with patch('urllib.request.OpenerDirector.open', side_effect=AssertionError('network forbidden')):
            code, output, error = self.call(['--replay', str(source), '--output-dir', str(destination)])
        report = json.loads((destination / 'report.json').read_text()) if destination.exists() else None
        return code, report, destination, error

    def test_missing_optional_snap_preserves_other_customer_routes(self):
        def mutate(bundle):
            matrix = bundle['responses'][-2]['response']
            del matrix['sources'][0]['location']
            del matrix['targets'][0]['location']
            for cell in matrix['sources_to_targets'][0]:
                if cell['target_index'] == 0:
                    cell.update(time=None, distance=None)
        code, report, destination, error = self.replay_modified('missing-snap', mutate)
        self.assertEqual(code, 3, error)
        self.assertEqual(report['summary']['known_routes'], 19)
        self.assertEqual(report['customers'][0]['route_status'], 'no_route')
        self.assertTrue(all(row['route_status'] == 'ok' for row in report['customers'][1:]))
        self.assertTrue((destination / 'report.md').is_file())

    def test_malformed_customer_evidence_is_scoped_to_one_row(self):
        def mutate(bundle):
            bundle['responses'][2]['response']['features'][0]['properties']['formatted'] = chr(0xd800)
            matrix = bundle['responses'][-2]['response']
            matrix['targets'] = matrix['targets'][1:]
            matrix['sources_to_targets'][0] = [dict(c, target_index=c['target_index'] - 1)
                for c in matrix['sources_to_targets'][0] if c['target_index'] > 0]
        code, report, destination, error = self.replay_modified('bad-customer-evidence', mutate)
        self.assertEqual(code, 3, error)
        self.assertEqual(report['summary']['known_routes'], 19)
        self.assertEqual(report['customers'][0]['geocode_reason'], 'invalid_response')
        self.assertEqual(report['customers'][0]['geocode_status'], 'unresolved')
        self.assertEqual(report['customers'][0]['evidence_refs'], [])
        self.assertEqual(report['errors'][0]['row_ids'], [1])
        self.assertTrue((destination / 'report.md').is_file())

    def test_nonfinite_matrix_cell_keeps_valid_routes_and_safe_evidence(self):
        def mutate(bundle):
            cells = bundle['responses'][-2]['response']['sources_to_targets'][0]
            next(c for c in cells if c['target_index'] == 0)['time'] = 1e309
        # Exercise the JSON number overflow case rather than a forbidden Infinity literal.
        bundle = json.loads(FIXTURE.read_text())
        mutate(bundle)
        source = self.root / 'overflow.json'
        source.write_text(json.dumps(bundle).replace('Infinity', '1e309'), encoding='utf-8')
        destination = self.root / 'overflow'
        with patch('urllib.request.OpenerDirector.open', side_effect=AssertionError('network forbidden')):
            code, _, error = self.call(['--replay', str(source), '--output-dir', str(destination)])
        self.assertEqual(code, 3, error)
        report = json.loads((destination / 'report.json').read_text())
        self.assertEqual(report['summary']['known_routes'], 19)
        self.assertEqual(report['customers'][0]['route_status'], 'error')
        self.assertTrue(all(r['route_status'] == 'ok' for r in report['customers'][1:]))
        self.assertEqual(report['summary']['in_zone'], 13)
        evidence = next(e for e in report['evidence'] if e['operation'] == 'route_matrix')
        artifact = json.loads((destination / evidence['artifact']).read_text())
        self.assertEqual(artifact['representation'], 'normalized_route_matrix')
        self.assertIsNone(artifact['measurements'][0]['time_seconds'])
        self.assertEqual(artifact['measurements'][0]['route_status'], 'error')
        self.assertTrue((destination / 'report.md').is_file())

    def test_snapshot_categories_accepted_and_unknown_or_multiple_rejected(self):
        bundle = json.loads(FIXTURE.read_text())
        for category in categories():
            bundle['inputs']['competitor_category'] = category
            self.assertEqual(validate_inputs(bundle['inputs']), [], category)
        def mutate(value):
            value['inputs']['competitor_category'] = 'catering.restaurant.tex-mex'
        code, report, _, error = self.replay_modified('tex-mex', mutate)
        self.assertEqual(code, 0, error)
        for category in ('service.nonexistent', 'service,catering.restaurant', 'service|catering.restaurant'):
            bundle['inputs']['competitor_category'] = category
            self.assertTrue(validate_inputs(bundle['inputs']))
            report['competitors']['category'] = category
            with self.assertRaises(ReportError):
                validate(report)

    def test_present_invalid_snap_is_still_rejected(self):
        def mutate(bundle):
            bundle['responses'][-2]['response']['targets'][0]['location'] = [181, 32]
        code, report, _, error = self.replay_modified('invalid-snap', mutate)
        self.assertEqual(code, 3, error)
        self.assertEqual(report['summary']['known_routes'], 0)
        self.assertTrue(all(row['route_status'] == 'error' for row in report['customers']))

    def test_malformed_competitor_metadata_preserves_customer_publication(self):
        mutations = [('categories', ['']), ('categories', ['   ']), ('place_id', '   '),
                     ('categories', [chr(0xd800)]), ('name', chr(0xd800)), ('formatted', chr(0xd800))]
        for index, (field, value) in enumerate(mutations):
            with self.subTest(field=field, value=value):
                def mutate(bundle):
                    bundle['responses'][-1]['response']['features'][0]['properties'][field] = value
                code, report, destination, error = self.replay_modified(f'bad-place-{index}', mutate)
                self.assertEqual(code, 3, error)
                self.assertEqual(report['summary']['known_routes'], 20)
                self.assertEqual(report['competitors']['status'], 'partial')
                self.assertEqual(report['competitors']['unclassified_count'], 1)
                self.assertEqual(report['competitors']['observed_out_of_zone_count'], 1)
                self.assertTrue((destination / 'report.md').is_file())

    def test_crs_on_any_isoline_envelope_fails_before_publication(self):
        for level in ('collection', 'feature', 'geometry'):
            with self.subTest(level=level):
                def mutate(bundle):
                    collection = bundle['responses'][1]['response']
                    feature = collection['features'][0]
                    target = {'collection': collection, 'feature': feature, 'geometry': feature['geometry']}[level]
                    target['crs'] = {'type': 'name', 'properties': {'name': 'EPSG:3857'}}
                code, report, destination, error = self.replay_modified('crs-' + level, mutate)
                self.assertEqual(code, 1)
                self.assertIsNone(report)
                self.assertFalse(destination.exists())
                self.assertIn('unsupported_geometry', error)

    def test_existing_output_never_overwritten(self):
        out=self.root/'existing';out.mkdir();(out/'report.json').write_text('keep')
        code,_,_=self.call(['--replay',str(FIXTURE),'--output-dir',str(out)])
        self.assertEqual(code,2);self.assertEqual((out/'report.json').read_text(),'keep')

    def test_missing_key_and_multiple_errors_no_network(self):
        csv=self.root/'bad.csv';csv.write_text('address,unknown\n ,x\n')
        with patch.dict(os.environ,{},clear=True),patch('zonepilot.cli.Client',side_effect=AssertionError('called')):
            code,_,error=self.call(['--minutes','61','--business-address',' ','--customers',str(csv),
                '--competitor-category','service.plumber','--output-dir',str(self.root/'bad')])
        self.assertEqual(code,2)
        for field in ('minutes','business-address','header','record 1','competitor-category','GEOAPIFY_API_KEY'):
            self.assertIn(field,error)

    def test_replay_mutual_exclusion_and_unknown_argument_do_not_echo_values(self):
        code,_,_=self.call(['--replay',str(FIXTURE),'--minutes','20','--output-dir',str(self.root/'x')])
        self.assertEqual(code,2)
        code,_,error=self.call(['--unknown','SYNTHETIC_CREDENTIAL_SENTINEL'])
        self.assertEqual(code,2);self.assertNotIn('SYNTHETIC_CREDENTIAL_SENTINEL',error)

    def test_csv_bom_quoted_commas_newlines_duplicates_and_optional_identity(self):
        f=self.root/'good.csv';f.write_text('\ufeffaddress,name,reference\n"A, B\nC",Demo,same\n"A, B\nC",Demo,same\n',encoding='utf-8')
        rows,errors=read_customers(f)
        self.assertEqual(errors,[]);self.assertEqual([r['row_id'] for r in rows],[1,2]);self.assertEqual(rows[0]['address'],'A, B\nC')

    def test_invalid_csv_cases(self):
        for text in ('address,address\na,b\n','name\na\n','address\n','address\n"unterminated','address\n'+''.join('x\n' for _ in range(21))):
            with self.subTest(text=text[:25]):
                f=self.root/'bad.csv';f.write_text(text)
                self.assertTrue(read_customers(f)[1])


if __name__=='__main__':unittest.main()
