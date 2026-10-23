import io
import http.client
import json
import os
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

from zonepilot.client import APIError, Client, MAX_RESPONSE_BYTES, NoRedirect, parse_json


class Clock:
    def __init__(self): self.value = 0
    def now(self): return self.value
    def sleep(self, seconds): self.value += seconds


class ClientTests(unittest.TestCase):
    def setUp(self):
        self.env = patch.dict(os.environ, {'GEOAPIFY_API_KEY': 'SYNTHETIC_CREDENTIAL_SENTINEL'}, clear=True)
        self.env.start()
        self.addCleanup(self.env.stop)
        self.clock = Clock()
        self.requests = []

    def client(self, entries):
        script = iter(entries)
        def transport(request, timeout):
            self.requests.append((request, timeout))
            entry = next(script)
            if isinstance(entry, Exception): raise entry
            return entry
        return Client(transport=transport, monotonic=self.clock.now, sleep=self.clock.sleep)

    def test_missing_key_never_calls_transport(self):
        os.environ.clear()
        with self.assertRaisesRegex(APIError, 'environment'):
            self.client([])
        self.assertEqual(self.requests, [])

    def test_key_is_only_a_header_and_response_echo_is_redacted(self):
        client = self.client([(200, {}, b'{"message":"SYNTHETIC_CREDENTIAL_SENTINEL"}')])
        data = client.geocode('  fictional address  ')
        request, timeout = self.requests[0]
        self.assertNotIn('SYNTHETIC_CREDENTIAL_SENTINEL', request.full_url)
        self.assertEqual(request.get_header('X-api-key'), 'SYNTHETIC_CREDENTIAL_SENTINEL')
        self.assertNotIn('SYNTHETIC_CREDENTIAL_SENTINEL', str(data))
        self.assertEqual(parse_qs(urlsplit(request.full_url).query)['limit'], ['5'])
        self.assertEqual(timeout, 10)

    def test_matrix_outbound_coordinate_order_and_settings(self):
        self.client([(200, {}, b'{}')]).matrix([-102,32], [[-103,33]])
        request = self.requests[0][0]
        body = json.loads(request.data)
        self.assertEqual(body['sources'], [{'location':[-102,32]}])
        self.assertEqual(body['targets'], [{'location':[-103,33]}])
        self.assertEqual(body['type'], 'balanced')
        self.assertNotIn('route_type', body)

    def test_routing_uses_lat_lon_and_places_rectangle(self):
        client = self.client([(200,{},b'{}'), (200,{},b'{}')])
        client.route([-102,32],[-103,33]); client.places('service',[-103,31,-101,33])
        self.assertEqual(parse_qs(urlsplit(self.requests[0][0].full_url).query)['waypoints'], ['32,-102|33,-103'])
        self.assertEqual(parse_qs(urlsplit(self.requests[1][0].full_url).query)['filter'], ['rect:-103,31,-101,33'])

    def test_isoline_202_then_success(self):
        client = self.client([(202,{},json.dumps({'id':'a'*32}).encode()),(200,{},b'{"features":[]}')])
        self.assertEqual(client.isoline([-102,32],1200), {'features':[]})
        initial = parse_qs(urlsplit(self.requests[0][0].full_url).query)
        self.assertEqual(initial['range'], ['1200']); self.assertEqual(initial['route_type'], ['balanced'])
        self.assertEqual(self.clock.value, 1)
        self.assertEqual(parse_qs(urlsplit(self.requests[1][0].full_url).query)['id'], ['a'*32])

    def test_isoline_pending_exhaustion_and_missing_id(self):
        pending=(202,{},json.dumps({'id':'b'*32}).encode())
        with self.assertRaisesRegex(APIError,'polling'):
            self.client([pending]*6).isoline([-102,32],1200)
        self.assertEqual(len(self.requests),6)
        with self.assertRaises(APIError): self.client([(202,{},b'{}')]).isoline([-102,32],1200)

    def test_auth_is_global_without_retry_or_raw_body(self):
        for status in (401,403):
            with self.subTest(status=status):
                client = self.client([(status,{},b'SYNTHETIC_CREDENTIAL_SENTINEL')])
                with self.assertRaises(APIError) as cm: client.geocode('fictional')
                self.assertEqual(cm.exception.code,'authentication')
                self.assertNotIn('SYNTHETIC_CREDENTIAL_SENTINEL',str(cm.exception))
                self.assertEqual(client.attempts,1)

    def test_bounded_retries_and_retry_after(self):
        client=self.client([(429,{'Retry-After':'4'},b'private'),(503,{},b'private'),(200,{},b'{}')])
        client.geocode('fictional')
        self.assertEqual(client.attempts,3); self.assertEqual(self.clock.value,6)

    def test_excessive_retry_after_stops_without_sleep(self):
        with self.assertRaisesRegex(APIError,'budget'):
            self.client([(429,{'Retry-After':'121'},b'')]).geocode('fictional')
        self.assertEqual(self.clock.value,0)

    def test_other_4xx_not_retried(self):
        client=self.client([(400,{},b'private')])
        with self.assertRaises(APIError): client.geocode('fictional')
        self.assertEqual(client.attempts,1)

    def test_network_exception_is_sanitized(self):
        client=self.client([http.client.IncompleteRead(b'SYNTHETIC_CREDENTIAL_SENTINEL')]*3)
        with self.assertRaises(APIError) as cm: client.geocode('fictional')
        self.assertNotIn('SYNTHETIC_CREDENTIAL_SENTINEL',str(cm.exception))

    def test_invalid_json_size_and_nonfinite(self):
        for payload in (b'NaN',b'{"a":1,"a":2}',b'{"n":Infinity}',b'[1]',b'x'*(MAX_RESPONSE_BYTES+1)):
            with self.subTest(size=len(payload)):
                with self.assertRaises(APIError): self.client([(200,{},payload)]).geocode('fictional')

    def test_attempt_deadline_and_redirect_limits(self):
        client=self.client([]); client.attempts=60
        with self.assertRaisesRegex(APIError,'budget'): client.geocode('fictional')
        client=self.client([]); self.clock.value=121
        with self.assertRaisesRegex(APIError,'budget'): client.geocode('fictional')
        self.assertIsNone(NoRedirect().redirect_request(None,None,302,'',{},'https://example.com'))


if __name__ == '__main__': unittest.main()
