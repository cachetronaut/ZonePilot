"""Reviewed stdlib adapters; secrets never enter URLs, diagnostics or evidence."""

import datetime as dt
import email.utils
import json
import http.client
import math
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request

MAX_RESPONSE_BYTES = 2 * 1024 * 1024
MESSAGES = {
    'missing_key': 'Set a nonblank GEOAPIFY_API_KEY environment variable before a live run.',
    'authentication': 'Geoapify rejected authentication or authorization. Check the environment key.',
    'request_failed': 'Geoapify request failed. No provider error text was retained.',
    'invalid_response': 'Geoapify returned an invalid or unsupported response.',
    'request_budget': 'The bounded request or time budget was exhausted.',
    'pending_exhausted': 'Isoline calculation did not complete within the polling budget.',
    'unsupported_geometry': 'The zone geometry is invalid or outside supported geometry limits.',
    'origin_unresolved': 'The business address did not resolve to one sufficiently precise building.',
}


class APIError(Exception):
    def __init__(self, code='invalid_response', retryable=False):
        self.code = code if code in MESSAGES else 'invalid_response'
        self.retryable = bool(retryable)
        super().__init__(MESSAGES[self.code])

    def record(self, row_ids=()):
        return {'code': self.code, 'message': str(self), 'retryable': self.retryable,
                'row_ids': list(row_ids)}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def finite_number(value):
    try:
        return type(value) in (int, float) and math.isfinite(value)
    except (OverflowError, ValueError):
        return False


def parse_json(data):
    def reject_constant(_):
        raise ValueError('invalid_json')

    def unique_pairs(pairs):
        obj = {}
        for key, value in pairs:
            if key in obj:
                raise ValueError('invalid_json')
            obj[key] = value
        return obj

    try:
        return json.loads(data, parse_constant=reject_constant, object_pairs_hook=unique_pairs)
    except (ValueError, TypeError, UnicodeError, RecursionError):
        raise APIError() from None


def environment_key():
    key = os.environ.get('GEOAPIFY_API_KEY', '').strip()
    if not key:
        raise APIError('missing_key')
    if any(ord(c) < 33 or ord(c) > 126 for c in key):
        raise APIError('missing_key')
    return key


class Client:
    """One run owns its deadline, attempt counter, and environment credential."""

    def __init__(self, *, transport=None, monotonic=time.monotonic, sleep=time.sleep,
                 wall_clock=lambda: dt.datetime.now(dt.timezone.utc)):
        self._key = environment_key()
        self._clock, self._sleep, self._wall = monotonic, sleep, wall_clock
        self._deadline = self._clock() + 120
        self.attempts = 0
        self.polls = 0
        self._transport = transport or self._http
        self._opener = urllib.request.build_opener(NoRedirect())

    def _remaining(self):
        remaining = self._deadline - self._clock()
        if remaining <= 0 or self.attempts >= 60:
            raise APIError('request_budget')
        return remaining

    def _http(self, request, timeout):
        try:
            with self._opener.open(request, timeout=timeout) as response:
                data = bytearray()
                while True:
                    if self._clock() >= self._deadline:
                        raise APIError('request_budget')
                    chunk = response.read1(min(65536, MAX_RESPONSE_BYTES + 1 - len(data)))
                    data.extend(chunk)
                    if len(data) > MAX_RESPONSE_BYTES:
                        raise APIError()
                    if not chunk:
                        return response.status, dict(response.headers), bytes(data)
        except urllib.error.HTTPError as error:
            # Deliberately do not read provider error bodies or follow redirects.
            code, headers = error.code, dict(error.headers or {})
            error.close()
            return code, headers, b''

    def _redact(self, value):
        if isinstance(value, str):
            return value.replace(self._key, '[redacted credential]')
        if isinstance(value, list):
            return [self._redact(x) for x in value]
        if isinstance(value, dict):
            return {self._redact(k): self._redact(v) for k, v in value.items()}
        return value

    def request(self, path, *, query=None, body=None):
        url = 'https://api.geoapify.com' + path
        if query:
            url += '?' + urllib.parse.urlencode(query)
        encoded = None if body is None else json.dumps(body, allow_nan=False).encode('utf-8')
        request = urllib.request.Request(url, data=encoded,
            headers={'x-api-key': self._key, 'Accept': 'application/json',
                     'Content-Type': 'application/json', 'User-Agent': 'ZonePilot/1.0'})
        for attempt in range(3):
            timeout = min(10, self._remaining())
            self.attempts += 1
            headers = {}
            try:
                status, headers, data = self._transport(request, timeout)
            except APIError:
                raise
            except (OSError, urllib.error.URLError, http.client.HTTPException, ValueError):
                status, data = 503, b''
            if self._clock() >= self._deadline:
                raise APIError('request_budget')
            if status in (401, 403):
                raise APIError('authentication')
            if status in (200, 202):
                if len(data) > MAX_RESPONSE_BYTES:
                    raise APIError()
                result = parse_json(data)
                if not isinstance(result, dict):
                    raise APIError()
                return status, self._redact(result)
            retryable = status == 429 or 500 <= status <= 599
            if not retryable or attempt == 2:
                raise APIError('request_failed', retryable)
            delay = 2 ** attempt
            retry_after = next((v for k, v in headers.items() if k.lower() == 'retry-after'), None)
            if retry_after is not None:
                try:
                    delay = max(delay, float(retry_after))
                except (ValueError, TypeError):
                    try:
                        date = email.utils.parsedate_to_datetime(retry_after)
                        delay = max(delay, (date - self._wall()).total_seconds())
                    except (ValueError, TypeError, OverflowError):
                        raise APIError('request_failed', True) from None
            if not math.isfinite(delay) or delay >= self._remaining():
                raise APIError('request_budget')
            self._sleep(delay)
        raise APIError('request_failed')

    def geocode(self, address):
        status, data = self.request('/v1/geocode/search', query={
            'text': address.strip(), 'limit': 5, 'format': 'geojson'})
        if status != 200:
            raise APIError()
        return data

    def isoline(self, origin, seconds):
        status, data = self.request('/v1/isoline', query={
            'lon': origin[0], 'lat': origin[1], 'range': seconds, 'mode': 'drive',
            'type': 'time', 'format': 'geojson', 'units': 'metric',
            'traffic': 'free_flow', 'route_type': 'balanced'})
        for _ in range(5):
            if status == 200:
                return data
            properties = data.get('properties', {})
            identifier = data.get('id') or (properties.get('id') if isinstance(properties, dict) else None)
            if not isinstance(identifier, str) or not re.fullmatch('[a-f0-9]{32}', identifier):
                raise APIError()
            if self._remaining() <= 1:
                raise APIError('request_budget')
            self._sleep(1)
            self.polls += 1
            status, data = self.request('/v1/isoline', query={'id': identifier, 'format': 'geojson'})
        if status == 200:
            return data
        raise APIError('pending_exhausted')

    def matrix(self, origin, targets):
        status, data = self.request('/v1/routematrix', body={
            'mode': 'drive', 'traffic': 'free_flow', 'type': 'balanced', 'units': 'metric',
            'sources': [{'location': origin}], 'targets': [{'location': x} for x in targets]})
        if status != 200:
            raise APIError()
        return data

    def route(self, origin, target):
        status, data = self.request('/v1/routing', query={
            'waypoints': '|'.join(f'{p[1]},{p[0]}' for p in (origin, target)),
            'mode': 'drive', 'traffic': 'free_flow', 'type': 'balanced',
            'units': 'metric', 'format': 'geojson'})
        if status != 200:
            raise APIError()
        return data

    def places(self, category, bbox):
        status, data = self.request('/v2/places', query={
            'categories': category, 'filter': 'rect:' + ','.join(str(x) for x in bbox), 'limit': 20})
        if status != 200:
            raise APIError()
        return data


class ReplayClient:
    """Synthetic scripted responses; deliberately has no network transport."""

    def __init__(self, responses):
        if not isinstance(responses, list):
            raise APIError()
        self.responses = iter(responses)
        self.attempts = 0

    def _next(self, operation):
        self.attempts += 1
        try:
            entry = next(self.responses)
        except StopIteration:
            raise APIError() from None
        if not isinstance(entry, dict) or entry.get('operation') != operation:
            raise APIError()
        if 'error' in entry:
            raise APIError(entry['error'])
        if not isinstance(entry.get('response'), dict):
            raise APIError()
        return entry['response']

    def geocode(self, address):
        return self._next('geocode')

    def isoline(self, origin, seconds):
        return self._next('isoline')

    def matrix(self, origin, targets):
        return self._next('matrix')

    def places(self, category, bbox):
        return self._next('places')

    def exhausted(self):
        try:
            next(self.responses)
        except StopIteration:
            return
        raise APIError()
