"""Run a bounded service-zone analysis or replay synthetic fixtures, without installs."""

import argparse
import csv
import datetime as dt
import json
import os
from pathlib import Path
import re
import sys
import tempfile

from .client import APIError, Client, MAX_RESPONSE_BYTES, ReplayClient, environment_key, parse_json
from .engine import acquire
from .report import ReportError, finalize, supported_category, write_bundle


class InputError(ValueError):
    pass


class Parser(argparse.ArgumentParser):
    def error(self, message):
        # argparse's default error can echo secret-bearing user arguments.
        raise InputError('arguments: unsupported or missing argument; use --help.')


def categories():
    return set(json.loads(Path(__file__).with_name('categories.json').read_text(encoding='utf-8')))


def read_customers(path):
    rows, errors = [], []
    try:
        with Path(path).open(encoding='utf-8-sig', newline='') as stream:
            reader = csv.reader(stream, strict=True)
            header = next(reader, [])
            if (not header or len(set(header)) != len(header) or 'address' not in header
                    or set(header) - {'address', 'name', 'reference'}):
                errors.append('customers header: require address and only optional name/reference, without duplicates.')
            try:
                for index, values in enumerate(reader, 1):
                    if index > 20:
                        errors.append('customers: at most 20 records are supported; remaining records were not scanned.')
                        break
                    location = f'customers record {index}, physical line {reader.line_num}'
                    if len(values) != len(header):
                        errors.append(location + ': column count does not match header.')
                        continue
                    item = dict(zip(header, values))
                    if not item.get('address', '').strip():
                        errors.append(location + ': address must be nonblank.')
                    rows.append({'row_id': index, 'address': item.get('address', ''),
                                 'name': item.get('name'), 'reference': item.get('reference')})
            except csv.Error:
                errors.append(f'customers physical line {reader.line_num}: malformed CSV; later rows could not be scanned.')
    except (OSError, UnicodeError, ValueError, csv.Error):
        errors.append('customers: unreadable UTF-8 CSV input.')
    if not rows:
        errors.append('customers: at least one record is required.')
    return rows, errors


def validate_inputs(inputs):
    errors = []
    if not isinstance(inputs, dict) or set(inputs) != {'business_address', 'business_name', 'minutes', 'customers', 'competitor_category'}:
        return ['inputs: invalid input contract.']
    if not isinstance(inputs['business_address'], str) or not inputs['business_address'].strip():
        errors.append('business-address: a nonblank address is required.')
    if not isinstance(inputs['business_name'], str) or not inputs['business_name'].strip():
        errors.append('business-name: a nonblank name is required when supplied.')
    if type(inputs['minutes']) is not int or not 5 <= inputs['minutes'] <= 60:
        errors.append('minutes: use a whole number from 5 through 60.')
    category = inputs['competitor_category']
    if category is not None and not supported_category(category):
        errors.append('competitor-category: choose one value from the committed category snapshot.')
    rows = inputs['customers']
    if not isinstance(rows, list) or not 1 <= len(rows) <= 20:
        errors.append('customers: provide 1 through 20 records.')
    else:
        for index, row in enumerate(rows, 1):
            if (not isinstance(row, dict) or set(row) != {'row_id', 'name', 'reference', 'address'}
                    or type(row.get('row_id')) is not int or row['row_id'] != index
                    or not isinstance(row.get('address'), str) or not row['address'].strip()
                    or any(row.get(k) is not None and not isinstance(row.get(k), str) for k in ('name', 'reference'))):
                errors.append(f'customers record {index}: invalid row contract.')
    return errors


def check_output(path):
    try:
        destination = Path(path)
        if destination.exists() or destination.is_symlink():
            return ['output-dir: already exists; choose a new directory.']
        destination.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryFile(dir=destination.parent):
            pass
        return []
    except (OSError, ValueError):
        return ['output-dir: parent directory is not writable.']


def parser():
    p = Parser(description='ZonePilot: outbound road-time budget evidence, standard library only.')
    p.add_argument('--business-address')
    p.add_argument('--business-name')
    p.add_argument('--minutes')
    p.add_argument('--customers')
    p.add_argument('--competitor-category')
    p.add_argument('--replay', help='Replay a synthetic JSON bundle without a key or network.')
    p.add_argument('--output-dir', default='reports/run', help='New directory for report.json, report.md and evidence.')
    return p


def main(argv=None):
    try:
        args = parser().parse_args(argv)
    except InputError as error:
        print(str(error), file=sys.stderr)
        return 2
    errors = []
    if sys.version_info < (3, 14, 9):
        errors.append('runtime: Python 3.14.9 or later is required; build/test target is 3.15.1.')
    bundle = None
    if args.replay:
        if any(getattr(args, k) is not None for k in ('business_address', 'business_name', 'minutes', 'customers', 'competitor_category')):
            errors.append('replay: live input/category arguments are mutually exclusive with replay.')
        try:
            with Path(args.replay).open('rb') as stream:
                data = stream.read(MAX_RESPONSE_BYTES + 1)
            if len(data) > MAX_RESPONSE_BYTES:
                raise APIError()
            bundle = parse_json(data)
            if (not isinstance(bundle, dict) or set(bundle) != {'data_mode', 'inputs', 'run_timestamp_utc', 'responses'}
                    or bundle['data_mode'] != 'synthetic' or not isinstance(bundle['responses'], list)):
                raise APIError()
            timestamp = bundle['run_timestamp_utc']
            if not isinstance(timestamp, str) or not timestamp.endswith('Z'):
                raise APIError()
            dt.datetime.fromisoformat(timestamp)
            inputs = bundle['inputs']
            errors.extend(validate_inputs(inputs))
        except (APIError, ValueError, TypeError, OSError, OverflowError):
            errors.append('replay: unreadable or invalid synthetic fixture bundle.')
    else:
        rows, csv_errors = read_customers(args.customers) if args.customers else ([], ['customers: CSV input is required.'])
        errors.extend(csv_errors)
        minutes = int(args.minutes) if args.minutes and re.fullmatch(r'[0-9]{1,2}', args.minutes) else None
        inputs = {'business_address': args.business_address, 'business_name': args.business_name if args.business_name is not None else 'Business',
                  'minutes': minutes, 'customers': rows, 'competitor_category': args.competitor_category}
        errors.extend(validate_inputs(inputs))
        try:
            key = environment_key()
            if key in json.dumps(inputs, ensure_ascii=False) or key in str(args.output_dir):
                errors.append('inputs: credential material cannot appear in input or output names.')
        except APIError as error:
            errors.append(str(error))
        timestamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')
    errors.extend(check_output(args.output_dir))
    if errors:
        for error in dict.fromkeys(errors):
            print(error, file=sys.stderr)
        return 2
    try:
        client = ReplayClient(bundle['responses']) if bundle else Client()
        envelope, artifacts = acquire(client, inputs, timestamp, 'synthetic' if bundle else 'live')
        if bundle:
            client.exhausted()
        report = finalize(envelope['result'])
        write_bundle(report, args.output_dir, artifacts)
    except APIError as error:
        print(f'{error.code}: {error}', file=sys.stderr)
        return 1
    except (ReportError, OSError, ValueError, TypeError, KeyError, OverflowError, RecursionError):
        print('report_failed: Evidence validation or report publication failed; no completed pair was published.', file=sys.stderr)
        return 1
    print(f"{report['run_status']}: report.json and report.md published in the selected output directory.")
    return 0 if report['run_status'] == 'complete' else 3


if __name__ == '__main__':
    raise SystemExit(main())
