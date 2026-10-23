"""Offline report contract checks. Fixtures are authored, never API recordings."""

import copy
from decimal import Decimal, localcontext
import hashlib
import html
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from zonepilot import report


EXAMPLES = Path(__file__).resolve().parents[1] / "docs" / "examples"
FLAGS = ("route_within_budget", "borderline", "membership_route_disagreement")


def example(name="complete"):
    return json.loads((EXAMPLES / (name + ".json")).read_text(encoding="utf-8"))


def acquired(value=None):
    value = copy.deepcopy(example() if value is None else value)
    value.pop("summary")
    value.pop("run_status")
    for row in value["customers"]:
        for field in FLAGS:
            row[field] = None
    return value


def not_requested(value):
    value["competitors"] = {
        "status": "not_requested", "category": None, "search_extent": None,
        "coverage": None, "cap_reached": None, "returned_count": None,
        "duplicate_count": None, "unclassified_count": None,
        "observed_in_zone_count": None, "observed_out_of_zone_count": None,
        "records": [],
    }


def agent_input():
    value = acquired()
    not_requested(value)
    value["path"] = "mcp"
    value["zone"].update(
        method="route_time_at_points", approximation=True,
        parameters={"budget_seconds": 1200},
        limitations=["Route-time classification only at measured points; no continuous zone."],
    )
    value["customers"][1]["verdict"] = "out_of_zone"
    return value


def artifacts(value):
    return {entry["artifact"]: (EXAMPLES / entry["artifact"]).read_bytes() for entry in value["evidence"]}


def walk(value, path=()):
    yield path, value
    if isinstance(value, dict):
        for key, item in value.items():
            yield from walk(item, path + (key,))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from walk(item, path + (index,))


def at(value, path):
    for part in path:
        value = value[part]
    return value


class NumericTests(unittest.TestCase):
    def test_decimal_half_even_boundaries_and_precision(self):
        for value, places, expected in (
            ("1.2345665", 6, 1.234566), ("1.2345675", 6, 1.234568),
            ("15725.3545", 3, 15725.354), ("15725.3555", 3, 15725.356),
            ("12.345", 2, 12.34), ("12.355", 2, 12.36),
            ("0", 6, 0.0), ("2.5", 0, 2.0),
        ):
            with self.subTest(value=value, places=places):
                self.assertEqual(report.normalize_number(Decimal(value), places), expected)
        self.assertEqual(report.normalize_number(1.2345675), 1.234568)

    def test_rejects_nonfinite_negative_bool_and_coercions(self):
        for value in (True, False, -1, -0.0000001, float("nan"), float("inf"), -float("inf"), Decimal("NaN"), Decimal("Infinity"), Decimal("1e1000"), "2", None, [], {}):
            with self.subTest(value=repr(value)):
                with self.assertRaises(report.ReportError):
                    report.normalize_number(value)
        for places in (-1, True, 1.5):
            with self.assertRaises(report.ReportError):
                report.normalize_number(1, places)

    def test_normalization_does_not_depend_on_callers_decimal_precision(self):
        with localcontext() as context:
            context.prec = 2
            self.assertEqual(report.normalize_number(Decimal("1234.1234565")), 1234.123456)

    def test_json_is_sorted_utf8_lf_and_strict(self):
        self.assertEqual(report.dumps({"z": "café", "a": 0}), '{\n  "a": 0,\n  "z": "café"\n}\n')
        for value in (float("nan"), float("inf"), {1: "a"}, (1, 2), {"a": Decimal("1")}, "\ud800"):
            with self.subTest(value=repr(value)):
                with self.assertRaises(report.ReportError):
                    report.dumps(value)
        cyclic = []
        cyclic.append(cyclic)
        with self.assertRaises(report.ReportError):
            report.dumps(cyclic)


class ValidationTests(unittest.TestCase):
    def test_complete_and_partial_authored_examples_validate(self):
        for name in ("complete", "partial"):
            value = example(name)
            report.validate(value)
            self.assertEqual(value["run_status"], name)
            for entry in value["evidence"]:
                self.assertEqual(hashlib.sha256((EXAMPLES / entry["artifact"]).read_bytes()).hexdigest(), entry["sha256"])

    def test_every_object_rejects_missing_and_extra_fields(self):
        baseline = example()
        for path, value in walk(baseline):
            if not isinstance(value, dict):
                continue
            for key in value:
                with self.subTest(path=path, removed=key):
                    changed = copy.deepcopy(baseline)
                    del at(changed, path)[key]
                    with self.assertRaises(report.ReportError):
                        report.validate(changed)
            with self.subTest(path=path, extra=True):
                changed = copy.deepcopy(baseline)
                at(changed, path)["unexpected"] = "untrusted text"
                with self.assertRaises(report.ReportError):
                    report.validate(changed)

    def test_numbers_and_counts_never_accept_booleans(self):
        baseline = example()
        for path, value in walk(baseline):
            if type(value) not in (int, float):
                continue
            with self.subTest(path=path):
                changed = copy.deepcopy(baseline)
                at(changed, path[:-1])[path[-1]] = True
                with self.assertRaises(report.ReportError):
                    report.validate(changed)

    def test_invalid_enums_and_container_types_fail_safely(self):
        paths = [
            ("path",), ("data_mode",), ("run_status",), ("schema_version",),
            ("settings", "mode"), ("settings", "traffic"), ("settings", "route_type"),
            ("settings", "units"), ("settings", "direction"), ("zone", "method"),
            ("customers", 0, "geocode_status"), ("customers", 0, "verdict"),
            ("customers", 0, "route_status"), ("competitors", "status"),
            ("competitors", "coverage"), ("evidence", 0, "kind"),
        ]
        for path in paths:
            for wrong in ("unexpected", None, {}, []):
                with self.subTest(path=path, wrong=wrong):
                    value = example()
                    at(value, path[:-1])[path[-1]] = wrong
                    with self.assertRaises(report.ReportError):
                        report.validate(value)

    def test_timestamps_are_real_utc_rfc3339(self):
        for timestamp in ("2026-01-01T00:00:00Z", "2026-01-01T00:00:00.123456Z", "2026-01-01T00:00:00+00:00"):
            value = example()
            value["run_timestamp_utc"] = timestamp
            report.validate(value)
        for timestamp in ("2026-02-30T00:00:00Z", "2026-01-01", "2026-01-01T00:00:00", "2026-01-01T00:00:00-00:00", "2026-01-01T01:00:00+01:00", "2026-01-01t00:00:00z", "2026-01-01T24:00:00Z"):
            with self.subTest(timestamp=timestamp):
                value = example()
                value["run_timestamp_utc"] = timestamp
                with self.assertRaises(report.ReportError):
                    report.validate(value)

    def test_budget_range_whole_minutes_and_zone_range_are_enforced(self):
        for seconds in (0, 299, 301, 3601, 3660, 1200.0, True):
            value = example()
            value["settings"]["budget_seconds"] = seconds
            with self.assertRaises(report.ReportError):
                report.validate(value)
        for field, bad in (("range_seconds", 600), ("boundary_tolerance_degrees", 1e-8)):
            value = example()
            value["zone"]["parameters"][field] = bad
            with self.assertRaises(report.ReportError):
                report.validate(value)

    def test_coordinates_confidence_and_accepted_geocode_are_required(self):
        for point in ([181, 0], [0, -91], [1], [True, 2], [float("nan"), 2], [1, 2, 3]):
            value = example()
            value["business"]["coordinates"] = point
            with self.assertRaises(report.ReportError):
                report.validate(value)
        for field, bad in (("candidate_count", 0), ("candidate_count", 6), ("confidence", None), ("confidence", 0.949999), ("confidence_building_level", 1.1), ("result_type", "street")):
            value = example()
            value["customers"][0]["geocode_evidence"][field] = bad
            with self.assertRaises(report.ReportError):
                report.validate(value)
        value = example()
        value["business"]["geocode_evidence"].update(confidence=0.95, confidence_building_level=0.95, match_type=None)
        report.validate(value)

    def test_row_identity_order_and_optional_strings_are_preserved(self):
        value = acquired()
        value["customers"][1]["input_address"] = value["customers"][0]["input_address"]
        value["customers"][0].update(name="", reference="duplicate", input_address="  Synthetic input  ")
        value["customers"][1]["reference"] = "duplicate"
        result = report.finalize(value)
        self.assertEqual(result["customers"][0]["name"], "")
        self.assertEqual(result["customers"][0]["input_address"], "  Synthetic input  ")
        for row_id in (0, 2, "1", True):
            changed = example()
            changed["customers"][0]["row_id"] = row_id
            with self.assertRaises(report.ReportError):
                report.validate(changed)
        for rows in ([], example()["customers"] * 7):
            changed = example()
            changed["customers"] = rows
            with self.assertRaises(report.ReportError):
                report.validate(changed)

    def test_route_states_cannot_turn_missing_measurements_into_zero(self):
        for updates in (
            {"time_seconds": None}, {"distance_meters": None},
            {"route_status": "no_route"}, {"route_status": "error"},
            {"route_status": "not_attempted"}, {"time_seconds": -1},
            {"distance_meters": float("inf")}, {"time_seconds": 1.1234567},
            {"verdict": "unknown"},
        ):
            value = example()
            value["customers"][0].update(updates)
            with self.subTest(updates=updates), self.assertRaises(report.ReportError):
                report.validate(value)

    def test_unresolved_rows_retain_only_unknown_states(self):
        baseline = example("partial")
        for updates in (
            {"verdict": "out_of_zone"}, {"resolved_address": "Synthetic value"},
            {"coordinates": [0, 0]}, {"time_seconds": 0}, {"route_status": "no_route"},
            {"geocode_reason": None}, {"borderline": False},
        ):
            value = copy.deepcopy(baseline)
            value["customers"][1].update(updates)
            with self.subTest(updates=updates), self.assertRaises(report.ReportError):
                report.validate(value)
        for evidence in (
            {"candidate_count": None}, {"candidate_count": 1}, {"confidence": 0.99},
        ):
            value = copy.deepcopy(baseline)
            value["customers"][1]["geocode_evidence"].update(evidence)
            with self.assertRaises(report.ReportError):
                report.validate(value)

    def test_summary_status_and_derived_flags_cannot_be_spoofed(self):
        for field in example()["summary"]:
            value = example()
            current = value["summary"][field]
            value["summary"][field] = [1] if isinstance(current, list) else 17
            with self.subTest(field=field), self.assertRaises(report.ReportError):
                report.validate(value)
        for field in FLAGS:
            value = example()
            value["customers"][0][field] = not value["customers"][0][field]
            with self.assertRaises(report.ReportError):
                report.validate(value)
        value = example("partial")
        value["run_status"] = "complete"
        with self.assertRaises(report.ReportError):
            report.validate(value)

    def test_evidence_ids_and_references_are_unique_and_resolvable(self):
        for mutation in ("duplicate_id", "unknown_ref", "duplicate_ref", "empty_zone_ref", "missing_customer_ref", "bad_hash", "no_origin", "wrong_kind"):
            value = example()
            if mutation == "duplicate_id":
                value["evidence"][1]["id"] = value["evidence"][0]["id"]
            elif mutation == "unknown_ref":
                value["customers"][0]["evidence_refs"] = ["missing"]
            elif mutation == "duplicate_ref":
                value["zone"]["evidence_refs"] *= 2
            elif mutation == "empty_zone_ref":
                value["zone"]["evidence_refs"] = []
            elif mutation == "missing_customer_ref":
                value["customers"][0]["evidence_refs"] = []
            elif mutation == "bad_hash":
                value["evidence"][0]["sha256"] = "A" * 64
            elif mutation == "no_origin":
                for item in value["evidence"]:
                    item["operation"] = "routing"
            else:
                value["evidence"][0]["kind"] = "rest"
            with self.subTest(mutation=mutation), self.assertRaises(report.ReportError):
                report.validate(value)

    def test_paths_are_relative_portable_and_cannot_collide(self):
        for path in ("/absolute.json", "../escape.json", "a/./b", "a//b", "a/../b", "C:/file", "\\\\host\\file", "a\\b", "https://example.test/a", "a?query", "a#fragment", "a%2fb", "a\nb", "report.json", "REPORT.MD", "report.json/x", "con", "aux.txt", "a.", "a "):
            value = example()
            for entry in value["evidence"]:
                entry["artifact"] = path
            with self.subTest(path=path), self.assertRaises(report.ReportError):
                report.validate(value)
        for paths in (("evidence/a", "evidence/a/b"), ("evidence/A", "evidence/a")):
            value = example()
            value["evidence"][0]["artifact"], value["evidence"][1]["artifact"] = paths
            with self.assertRaises(report.ReportError):
                report.validate(value)

    def test_error_rows_and_attribution_urls_are_checked(self):
        for bad in ([0], [4], [True], [1, 1], "1"):
            value = example("partial")
            value["errors"][0]["row_ids"] = bad
            with self.assertRaises(report.ReportError):
                report.validate(value)
        for url in ("https://user:password@localhost", "https://example.test/?apiKey=sentinel", "http://example.test", "file:fixture-example", "https://localhost", "https://example.test/#secret"):
            value = example()
            value["attributions"][0]["url"] = url
            with self.assertRaises(report.ReportError):
                report.validate(value)


class AggregationTests(unittest.TestCase):
    def test_finalize_matches_examples_without_mutating_input(self):
        for name in ("complete", "partial"):
            value = acquired(example(name))
            before = copy.deepcopy(value)
            result = report.finalize(value)
            self.assertEqual(value, before)
            self.assertEqual(result, example(name))
            result["customers"][0]["name"] = "changed copy"
            self.assertNotEqual(result["customers"][0]["name"], value["customers"][0]["name"])

    def test_finalizer_rejects_derived_input_instead_of_overwriting_it(self):
        with self.assertRaises(report.ReportError):
            report.finalize(example())
        value = acquired()
        value["customers"][0]["borderline"] = False
        with self.assertRaises(report.ReportError):
            report.finalize(value)

    def test_boundary_normalization_precedes_decimal_flags(self):
        for time, expected in ((1200, False), (1200.0000004, False), (1200.0000005, False), (1200.0000006, True), (1320, True), (1320.000001, False)):
            value = acquired()
            value["customers"][0]["time_seconds"] = time
            result = report.finalize(value)
            with self.subTest(time=time):
                self.assertIs(result["customers"][0]["borderline"], expected)
                self.assertEqual(result["customers"][0]["verdict"], "in_zone")
        value = acquired()
        value["customers"][0].update(time_seconds=0, distance_meters=0)
        result = report.finalize(value)
        self.assertEqual(result["summary"]["known_routes"], 3)
        self.assertIs(result["customers"][0]["route_within_budget"], True)

    def test_missing_routes_preserve_polygon_verdicts_and_partial_status(self):
        value = acquired()
        for row in value["customers"]:
            row.update(route_status="no_route", time_seconds=None, distance_meters=None)
        result = report.finalize(value)
        self.assertEqual(result["run_status"], "partial")
        self.assertEqual(result["summary"]["known_routes"], 0)
        self.assertEqual(result["summary"]["missing_routes"], 3)
        self.assertEqual(result["summary"]["in_zone"], 2)
        self.assertIsNone(result["summary"]["median_in_zone_seconds"])
        self.assertIsNone(result["summary"]["max_time_seconds"])
        self.assertEqual(result["summary"]["max_time_row_ids"], [])

    def test_all_unresolved_has_zero_denominator_and_unavailable_aggregates(self):
        value = acquired()
        unresolved = example("partial")["customers"][1]
        for index in range(3):
            value["customers"][index] = copy.deepcopy(unresolved)
            value["customers"][index]["row_id"] = index + 1
        result = report.finalize(value)
        summary = result["summary"]
        self.assertEqual(summary["classified_denominator"], 0)
        self.assertEqual(summary["unknown_membership"], 3)
        self.assertEqual(summary["missing_routes"], 0)
        for field in ("in_zone_percent", "out_of_zone_percent", "median_in_zone_seconds", "max_time_seconds"):
            self.assertIsNone(summary[field])
        self.assertEqual(summary["max_time_row_ids"], [])
        self.assertEqual(result["run_status"], "partial")

    def test_maximum_includes_outside_and_all_tied_rows_in_order(self):
        value = acquired()
        for row in value["customers"]:
            row["time_seconds"] = 1500
        result = report.finalize(value)
        self.assertEqual(result["summary"]["max_time_row_ids"], [1, 2, 3])
        self.assertEqual(result["summary"]["max_time_seconds"], 1500)
        value["customers"][2]["time_seconds"] = 1800
        self.assertEqual(report.finalize(value)["summary"]["max_time_row_ids"], [3])

    def test_even_median_uses_decimal_half_even_six_places(self):
        for times, expected in (((1.000001, 1.000002), 1.000002), ((1.000002, 1.000003), 1.000002)):
            value = acquired()
            for index, time in enumerate(times):
                value["customers"][index]["time_seconds"] = time
            self.assertEqual(report.finalize(value)["summary"]["median_in_zone_seconds"], expected)


class CompetitorTests(unittest.TestCase):
    def test_real_zero_result_success_is_sampled_and_complete(self):
        value = acquired()
        section = value["competitors"]
        section.update(returned_count=0, duplicate_count=0, unclassified_count=0, observed_in_zone_count=0, observed_out_of_zone_count=0, records=[])
        result = report.finalize(value)
        self.assertEqual(result["run_status"], "complete")
        self.assertEqual(result["competitors"]["coverage"], "sampled")

    def test_unclassified_candidates_make_section_and_run_partial(self):
        value = acquired()
        value["competitors"].update(status="partial", returned_count=4, unclassified_count=1)
        result = report.finalize(value)
        self.assertEqual(result["run_status"], "partial")
        self.assertEqual(result["competitors"]["unclassified_count"], 1)

    def test_state_counts_cap_and_records_cannot_contradict_each_other(self):
        for updates in (
            {"returned_count": 21}, {"duplicate_count": 4}, {"cap_reached": True},
            {"coverage": "complete"}, {"status": "partial"}, {"status": "unavailable"},
            {"observed_in_zone_count": 0}, {"unclassified_count": 1},
            {"status": "not_requested"}, {"records": []},
        ):
            value = example()
            value["competitors"].update(updates)
            with self.subTest(updates=updates), self.assertRaises(report.ReportError):
                report.validate(value)
        value = acquired()
        value["competitors"].update(returned_count=20, observed_out_of_zone_count=18, cap_reached=True)
        report.finalize(value)

    def test_unavailable_counts_are_null_and_not_requested_has_no_category(self):
        value = acquired()
        not_requested(value)
        result = report.finalize(value)
        self.assertEqual(result["run_status"], "complete")
        result["competitors"]["category"] = "service.locksmith"
        with self.assertRaises(report.ReportError):
            report.validate(result)
        value = example("partial")
        value["competitors"]["returned_count"] = 0
        with self.assertRaises(report.ReportError):
            report.validate(value)

    def test_record_order_identity_distance_and_search_extent(self):
        for updates in ({"verdict": "out_of_zone"}, {"geodesic_distance_meters": 0}, {"coordinates": [0, 91]}, {"id": "synthetic-id:incorrect"}):
            value = example()
            value["competitors"]["records"][0].update(updates)
            with self.assertRaises(report.ReportError):
                report.validate(value)
        for bbox in ([1, -1, -1, 1], [-1, 1, 1, -1], [-181, -1, 1, 1], [0, 0, 0, 0], [True, 0, 1, 1]):
            value = example()
            value["competitors"]["search_extent"]["parameters"]["bbox"] = bbox
            with self.assertRaises(report.ReportError):
                report.validate(value)
        value = example()
        value["competitors"]["search_extent"] = {"method": "circle", "parameters": {"center": [0, 0], "radius_meters": 1000}}
        with self.assertRaises(report.ReportError):
            report.validate(value)
        value = acquired()
        record = value["competitors"]["records"][0]
        canonical = json.dumps([record["coordinates"], record["name"]], ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        record["id"] = "synthetic-id:" + hashlib.sha256(canonical.encode()).hexdigest()
        report.finalize(value)


class MarkdownTests(unittest.TestCase):
    def test_every_json_field_and_value_is_independently_accessible(self):
        for name in ("complete", "partial"):
            value = example(name)
            markdown = report.render_markdown(value)
            details = markdown.split("## Complete field details\n", 1)[1]
            actual = {}
            for line in details.splitlines():
                if not line.startswith("| &#36;") and not line.startswith("| $"):
                    continue
                path, kind, cell = [html.unescape(part.strip()) for part in line.split("|")[1:-1]]
                actual[path] = kind, cell
            for path, item in walk(value):
                json_path = "$" + "".join(f"[{part}]" if isinstance(part, int) else "." + part for part in path)
                with self.subTest(name=name, path=json_path):
                    self.assertIn(json_path, actual)
                    if item is None:
                        self.assertEqual(actual[json_path], ("null", "unavailable"))
                    elif type(item) is str:
                        self.assertEqual(actual[json_path], ("string", item if item else '""'))
                    elif type(item) not in (list, dict):
                        self.assertEqual(json.loads(actual[json_path][1]), item)
                    elif not item:
                        self.assertEqual(actual[json_path][1], "[]" if isinstance(item, list) else "{}")

    def test_input_cannot_add_html_links_headings_or_table_rows(self):
        value = example()
        hostile = '<script>alert(1)</script>|[click](https://example.test)\n# heading\r\n`code`\\*x*\t'
        value["customers"][0]["name"] = hostile
        value["warnings"] = [hostile]
        value["errors"] = [{"code": "synthetic_error", "message": hostile, "retryable": False, "row_ids": [1]}]
        markdown = report.render_markdown(value)
        self.assertNotIn("<script>", markdown)
        self.assertNotIn("[click]", markdown)
        self.assertNotIn("\n# heading", markdown)
        self.assertNotIn("`code`", markdown)
        self.assertIn("&lt;script&gt;", markdown)
        self.assertIn("&#124;", markdown)
        for line in markdown.splitlines():
            if line.startswith("| ") and "&lt;script&gt;" in line:
                self.assertIn(line.count("|"), (3, 4, 12))

    def test_fixed_inputs_are_byte_identical_and_invalid_input_is_rejected(self):
        value = example()
        self.assertEqual(report.dumps(value).encode(), report.dumps(copy.deepcopy(value)).encode())
        self.assertEqual(report.render_markdown(value).encode(), report.render_markdown(copy.deepcopy(value)).encode())
        self.assertTrue(report.render_markdown(value).endswith("\n"))
        value["summary"]["total"] = 19
        with self.assertRaises(report.ReportError):
            report.render_markdown(value)


class BundleTests(unittest.TestCase):
    def test_publishes_complete_directory_with_hash_matched_artifacts(self):
        value = example()
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "new-run"
            original_rename = os.rename
            calls = []
            def inspect_rename(source, target):
                calls.append((source, target))
                self.assertEqual(list(Path(target).iterdir()), [])
                self.assertEqual((Path(source) / "report.json").read_bytes(), report.dumps(value).encode())
                self.assertEqual((Path(source) / "report.md").read_bytes(), report.render_markdown(value).encode())
                original_rename(source, target)
            with patch.object(report.os, "rename", side_effect=inspect_rename):
                report.write_bundle(value, destination, artifacts(value))
            self.assertEqual(len(calls), 1)
            self.assertEqual(sorted(p.name for p in Path(temporary).iterdir()), ["new-run"])
            for path, content in artifacts(value).items():
                self.assertEqual((destination / path).read_bytes(), content)

    def test_existing_directory_file_and_symlink_are_never_overwritten(self):
        value = example()
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            directory = base / "existing"
            directory.mkdir()
            (directory / "keep").write_bytes(b"keep")
            file = base / "file"
            file.write_bytes(b"keep")
            symlink = base / "symlink"
            symlink.symlink_to(directory, target_is_directory=True)
            for target in (directory, file, symlink):
                with self.subTest(target=target.name), self.assertRaises(report.ReportError) as caught:
                    report.write_bundle(value, target, artifacts(value))
                self.assertEqual(caught.exception.code, "output_exists")
            self.assertEqual(file.read_bytes(), b"keep")
            self.assertEqual((directory / "keep").read_bytes(), b"keep")
            self.assertTrue(symlink.is_symlink())

    def test_empty_existing_directory_is_not_reused(self):
        value = example()
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "existing-empty"
            target.mkdir()
            with self.assertRaises(report.ReportError):
                report.write_bundle(value, target, artifacts(value))
            self.assertEqual(list(target.iterdir()), [])

    def test_bad_hash_missing_extra_and_nonbytes_artifacts_publish_nothing(self):
        value = example()
        baseline = artifacts(value)
        name = next(iter(baseline))
        for supplied in ({}, {name: b"bad"}, {name: "not bytes"}, {**baseline, "extra.json": b"extra"}):
            with tempfile.TemporaryDirectory() as temporary:
                target = Path(temporary) / "new-run"
                with self.assertRaises(report.ReportError):
                    report.write_bundle(value, target, supplied)
                self.assertEqual(list(Path(temporary).iterdir()), [])

    def test_write_fsync_and_publish_failures_rollback_only_this_attempt(self):
        value = example()
        for operation in ("open", "fsync", "rename"):
            with self.subTest(operation=operation), tempfile.TemporaryDirectory() as temporary:
                base = Path(temporary)
                (base / "keep").write_bytes(b"keep")
                context = patch.object(Path, "open", side_effect=OSError("PRIVATE_SENTINEL")) if operation == "open" else patch.object(report.os, operation, side_effect=OSError("PRIVATE_SENTINEL"))
                supplied = artifacts(value)
                with context, self.assertRaises(report.ReportError) as caught:
                    report.write_bundle(value, base / "new-run", supplied)
                self.assertNotIn("PRIVATE_SENTINEL", str(caught.exception))
                self.assertEqual(sorted(p.name for p in base.iterdir()), ["keep"])
                self.assertEqual((base / "keep").read_bytes(), b"keep")

    def test_destination_created_by_another_writer_is_preserved(self):
        value = example()
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "new-run"
            resolved_target = target.resolve()
            original_mkdir = Path.mkdir
            def race(path, *args, **kwargs):
                if path == resolved_target:
                    original_mkdir(path)
                    (path / "other-writer").write_bytes(b"other")
                return original_mkdir(path, *args, **kwargs)
            with patch.object(Path, "mkdir", race), self.assertRaises(report.ReportError) as caught:
                report.write_bundle(value, target, artifacts(value))
            self.assertEqual(caught.exception.code, "output_exists")
            self.assertEqual((target / "other-writer").read_bytes(), b"other")
            self.assertEqual(sorted(p.name for p in Path(temporary).iterdir()), ["new-run"])


class AgentImportTests(unittest.TestCase):
    def write_input(self, base, value):
        source = base / "agent.json"
        source.write_text(report.dumps(value), encoding="utf-8")
        for path, content in artifacts(value).items():
            target = base / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        return source

    def test_default_gate_is_closed_and_no_network_is_used(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            source = self.write_input(base, agent_input())
            with patch.dict(os.environ, {}, clear=True), patch("socket.socket", side_effect=AssertionError("network used")), patch("sys.stderr") as stderr:
                self.assertEqual(report.main(["--import-agent", str(source), "--output-dir", str(base / "output")]), 1)
            self.assertIn("agent_method_pending", str(stderr.write.call_args_list))
            self.assertFalse((base / "output").exists())

    def test_approved_method_validates_thresholds_and_missing_route_unknown(self):
        with patch.object(report, "APPROVED_AGENT_METHOD", "route_time_at_points"):
            value = agent_input()
            result = report.finalize(value)
            self.assertEqual(result["summary"]["in_zone"], 1)
            self.assertEqual(result["summary"]["out_of_zone"], 2)
            self.assertEqual(result["summary"]["disagreements"], 0)
            value["customers"][0].update(route_status="no_route", time_seconds=None, distance_meters=None, verdict="unknown")
            result = report.finalize(value)
            self.assertEqual(result["run_status"], "partial")
            self.assertEqual(result["summary"]["unknown_membership"], 1)
            self.assertEqual(result["summary"]["classified_denominator"], 2)
            self.assertEqual(result["summary"]["out_of_zone_percent"], 100)
            value["customers"][0]["verdict"] = "out_of_zone"
            with self.assertRaises(report.ReportError):
                report.finalize(value)

    def test_agent_rejects_invented_method_parameters_membership_or_competitors(self):
        with patch.object(report, "APPROVED_AGENT_METHOD", "route_time_at_points"):
            for mutation in ("method", "parameters", "approximation", "membership", "competitors"):
                value = agent_input()
                if mutation == "method":
                    value["zone"]["method"] = "circle"
                elif mutation == "parameters":
                    value["zone"]["parameters"]["budget_seconds"] = 300
                elif mutation == "approximation":
                    value["zone"]["approximation"] = False
                elif mutation == "membership":
                    value["customers"][0]["verdict"] = "out_of_zone"
                else:
                    value["competitors"] = example()["competitors"]
                with self.subTest(mutation=mutation), self.assertRaises(report.ReportError):
                    report.finalize(value)

    def test_import_rejects_cli_derived_roots_and_nonnull_row_flags(self):
        for mutation in ("cli", "summary", "run_status", *FLAGS):
            value = agent_input()
            if mutation == "cli":
                value["path"] = "cli"
            elif mutation in ("summary", "run_status"):
                value[mutation] = example()[mutation]
            else:
                value["customers"][0][mutation] = False
            with tempfile.TemporaryDirectory() as temporary:
                base = Path(temporary)
                source = self.write_input(base, value)
                with self.subTest(mutation=mutation), self.assertRaises(report.ReportError) as caught:
                    report._read_import(source)
                self.assertEqual(caught.exception.code, "invalid_import")

    def test_approved_keyless_import_writes_complete_and_partial_bundles(self):
        with patch.object(report, "APPROVED_AGENT_METHOD", "route_time_at_points"):
            for partial in (False, True):
                value = agent_input()
                if partial:
                    value["customers"][0].update(route_status="error", time_seconds=None, distance_meters=None, verdict="unknown")
                with tempfile.TemporaryDirectory() as temporary:
                    base = Path(temporary)
                    source = self.write_input(base, value)
                    with patch.dict(os.environ, {}, clear=True), patch("socket.socket", side_effect=AssertionError("network used")):
                        code = report.main(["--import-agent", str(source), "--output-dir", str(base / "output")])
                    self.assertEqual(code, 3 if partial else 0)
                    result = json.loads((base / "output" / "report.json").read_bytes())
                    self.assertEqual(result["path"], "mcp")
                    self.assertIs(result["zone"]["approximation"], True)
                    report.validate(result)

    def test_bad_json_duplicate_keys_and_nonfinite_values_have_safe_diagnostics(self):
        for text in ('{"path":"mcp","path":"mcp"}', '{"x":NaN}', '{"x":Infinity}', 'PRIVATE_SENTINEL malformed JSON'):
            with tempfile.TemporaryDirectory() as temporary:
                source = Path(temporary) / "PRIVATE_SENTINEL.json"
                source.write_text(text)
                with self.assertRaises(report.ReportError) as caught:
                    report._read_import(source)
                self.assertNotIn("PRIVATE_SENTINEL", str(caught.exception))

    def test_import_rejects_hash_mismatch_missing_artifact_and_symlink(self):
        with patch.object(report, "APPROVED_AGENT_METHOD", "route_time_at_points"):
            for mutation in ("hash", "missing", "symlink"):
                with tempfile.TemporaryDirectory() as temporary:
                    base = Path(temporary)
                    value = agent_input()
                    source = self.write_input(base, value)
                    artifact = base / value["evidence"][0]["artifact"]
                    original = artifact.read_bytes()
                    if mutation == "hash":
                        artifact.write_bytes(b"not matching")
                    elif mutation == "missing":
                        artifact.unlink()
                    else:
                        artifact.unlink()
                        target = base / "other.json"
                        target.write_bytes(original)
                        artifact.symlink_to(target)
                    with self.subTest(mutation=mutation), self.assertRaises(report.ReportError):
                        report._read_import(source)

    def test_module_invocation_and_argument_errors_do_not_echo_untrusted_text(self):
        process = subprocess.run([sys.executable, "-m", "zonepilot.report", "--PRIVATE_SENTINEL"], capture_output=True, text=True, check=False)
        self.assertEqual(process.returncode, 2)
        self.assertEqual(process.stdout, "")
        self.assertIn("invalid_arguments", process.stderr)
        self.assertNotIn("PRIVATE_SENTINEL", process.stderr)
        with self.assertRaises(report.ReportError) as caught:
            report._read_import("PRIVATE_SENTINEL_missing.json")
        self.assertNotIn("PRIVATE_SENTINEL", str(caught.exception))
        self.assertNotIn("PRIVATE_SENTINEL", str(report.ReportError("PRIVATE_SENTINEL")))


if __name__ == "__main__":
    unittest.main()
