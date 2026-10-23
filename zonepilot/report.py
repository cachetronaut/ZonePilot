"""Strict shared reports and keyless hosted-agent evidence import. Stdlib only."""

from __future__ import annotations

import argparse
import copy
from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN, localcontext
import hashlib
import html
import json
import math
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
from urllib.parse import urlsplit


# Owner approved the point-only method on 2026-10-23; sampled hulls remain unapproved.
APPROVED_AGENT_METHOD = "route_time_at_points"
AGENT_LIMITATION = "Route-time classification only at measured points; no continuous zone."
MCP_COMPETITOR_OPERATION = "mcp_competitor_classification"
BOUNDARY_RULE = (
    "All ring boundaries are in zone; segment-distance tolerance 1e-9 degrees."
)
_DIAGNOSTICS = {
    "invalid_report": "Report fields or invariants are invalid.",
    "invalid_number": "A finite nonnegative numeric measurement is required.",
    "serialization_failed": "The value cannot be serialized as finite JSON.",
    "invalid_import": "Agent input must contain acquired MCP evidence only.",
    "agent_method_pending": "The agent membership method requires B02 approval.",
    "invalid_artifact": "Evidence paths, contents, or checksums are invalid.",
    "input_read_failed": "The agent evidence input could not be read.",
    "output_exists": "The output destination already exists.",
    "output_write_failed": "The report bundle could not be published.",
    "invalid_arguments": "Use --import-agent INPUT --output-dir NEW_DIRECTORY.",
}


class ReportError(ValueError):
    """A fixed diagnostic that never includes caller or provider text."""

    def __init__(self, code: str = "invalid_report") -> None:
        self.code = code if type(code) is str and code in _DIAGNOSTICS else "invalid_report"
        super().__init__(f"{self.code}: {_DIAGNOSTICS[self.code]}")


_ROOT = {
    "schema_version", "path", "data_mode", "run_status", "run_timestamp_utc",
    "business", "settings", "zone", "customers", "summary", "competitors",
    "errors", "warnings", "evidence", "attributions",
}
_GEOCODE = {
    "candidate_count", "confidence", "confidence_building_level", "match_type",
    "result_type",
}
_FLAGS = {"route_within_budget", "borderline", "membership_route_disagreement"}
_CUSTOMER = {
    "row_id", "name", "reference", "input_address", "resolved_address",
    "coordinates", "geocode_status", "geocode_reason", "geocode_evidence",
    "verdict", "route_status", "time_seconds", "distance_meters",
    "evidence_refs",
} | _FLAGS
_COUNTS = {
    "total", "resolved", "unresolved", "in_zone", "out_of_zone",
    "unknown_membership", "known_routes", "missing_routes", "borderline",
    "disagreements", "classified_denominator",
}
_AGGREGATES = {
    "in_zone_percent", "out_of_zone_percent", "median_in_zone_seconds",
    "max_time_seconds",
}
_COMP_COUNTS = {
    "returned_count", "duplicate_count", "unclassified_count",
    "observed_in_zone_count", "observed_out_of_zone_count",
}
_VERDICTS = {"in_zone", "out_of_zone", "unknown"}
_TIMESTAMP = re.compile(
    r"\d{4}-\d{2}-\d{2}T(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d(?:\.\d+)?(?:Z|\+00:00)\Z"
)
_HASH = re.compile(r"[0-9a-f]{64}\Z")
_CATEGORIES = frozenset(json.loads(Path(__file__).with_name('categories.json').read_text(encoding='utf-8')))


def supported_category(value: object) -> bool:
    """The pinned provider snapshot defines the accepted single categories."""
    return type(value) is str and value in _CATEGORIES


def _require(condition: bool, code: str = "invalid_report") -> None:
    if not condition:
        raise ReportError(code)


def _object(value: object, keys: set[str]) -> dict:
    _require(type(value) is dict and set(value) == keys)
    return value


def _string(value: object, *, nullable: bool = False, blank: bool = True) -> None:
    if nullable and value is None:
        return
    _require(type(value) is str)
    _require(blank or bool(value.strip()))
    try:
        value.encode("utf-8")
    except UnicodeError:
        raise ReportError() from None


def _integer(value: object, maximum: int | None = None) -> None:
    _require(type(value) is int and value >= 0)
    if maximum is not None:
        _require(value <= maximum)


def _number(value: object) -> None:
    _require(type(value) in (int, float))
    try:
        _require(math.isfinite(value))
    except (OverflowError, ValueError, TypeError):
        raise ReportError() from None


def _point(value: object) -> None:
    _require(type(value) is list and len(value) == 2)
    for coordinate in value:
        _number(coordinate)
    _require(-180 <= value[0] <= 180 and -90 <= value[1] <= 90)


def _strings(value: object, *, nonempty: bool = False) -> None:
    _require(type(value) is list and (not nonempty or bool(value)))
    for item in value:
        _string(item, blank=False)


def _json_value(value: object) -> None:
    """Reject Python coercions such as tuple arrays and non-string object keys."""
    if value is None or type(value) in (bool, str):
        if type(value) is str:
            _string(value)
    elif type(value) in (int, float):
        _number(value)
    elif type(value) is list:
        for item in value:
            _json_value(item)
    elif type(value) is dict:
        for key, item in value.items():
            _string(key)
            _json_value(item)
    else:
        raise ReportError()


def dumps(obj: object) -> str:
    """Serialize finite JSON deterministically, with exactly one trailing LF."""
    try:
        _json_value(obj)
        return json.dumps(
            obj, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False
        ) + "\n"
    except (ReportError, ValueError, TypeError, OverflowError, RecursionError):
        raise ReportError("serialization_failed") from None


def normalize_number(value: object, places: int = 6) -> float:
    """Round a nonnegative measurement using decimal, never binary, half-even."""
    _require(type(places) is int and places >= 0, "invalid_number")
    _require(type(value) in (int, float, Decimal), "invalid_number")
    try:
        decimal = Decimal(str(value))
        _require(decimal.is_finite() and decimal >= 0, "invalid_number")
        _require(math.isfinite(float(decimal)), "invalid_number")
        with localcontext() as context:
            context.prec = max(34, len(decimal.as_tuple().digits), decimal.adjusted() + places + 2)
            result = decimal.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_EVEN)
        number = float(result)
        _require(math.isfinite(number), "invalid_number")
        return 0.0 if number == 0 else number
    except (InvalidOperation, OverflowError, ValueError, TypeError):
        raise ReportError("invalid_number") from None


def _measurement(value: object, places: int = 6) -> None:
    _number(value)
    _require(value >= 0 and value == normalize_number(value, places))


def _safe_path(value: object) -> str:
    _string(value, blank=False)
    _require(
        not any(ord(c) < 32 or ord(c) == 127 for c in value)
        and not any(c in value for c in "\\:%?#<>\"|*")
        and all(part not in ("", ".", "..") for part in value.split("/")),
        "invalid_artifact",
    )
    # Windows strips trailing dots/spaces and reserves these device names.
    for part in value.split("/"):
        _require(part == part.rstrip(" ."), "invalid_artifact")
        stem = part.split(".", 1)[0].casefold()
        _require(
            stem not in {"con", "prn", "aux", "nul"}
            and re.fullmatch(r"(?:com|lpt)[1-9]", stem) is None,
            "invalid_artifact",
        )
    return value


def _artifact_index(report: dict) -> dict[str, str]:
    _require(type(report["evidence"]) is list and bool(report["evidence"]))
    ids: set[str] = set()
    artifacts: dict[str, str] = {}
    expected_kind = "synthetic" if report["data_mode"] == "synthetic" else (
        "rest" if report["path"] == "cli" else "mcp"
    )
    for item in report["evidence"]:
        _object(item, {"id", "kind", "operation", "artifact", "sha256"})
        _string(item["id"], blank=False)
        _require(item["id"] not in ids)
        ids.add(item["id"])
        _require(item["kind"] == expected_kind)
        _string(item["operation"], blank=False)
        path = _safe_path(item["artifact"])
        _string(item["sha256"])
        _require(_HASH.fullmatch(item["sha256"]) is not None)
        _require(path not in artifacts or artifacts[path] == item["sha256"])
        artifacts[path] = item["sha256"]
    _require(any("geocod" in item["operation"].lower() for item in report["evidence"]))
    names = ["report.json", "report.md", *artifacts]
    lowered = [name.casefold() for name in names]
    _require(len(set(lowered)) == len(lowered), "invalid_artifact")
    for i, name in enumerate(lowered):
        _require(
            not any(other.startswith(name + "/") for other in lowered[i + 1:])
            and not any(name.startswith(other + "/") for other in lowered[i + 1:]),
            "invalid_artifact",
        )
    return artifacts


def _refs(value: object, ids: set[str], *, required: bool = False) -> None:
    _strings(value, nonempty=required)
    _require(len(value) == len(set(value)) and all(ref in ids for ref in value))


def _geocode(value: object, resolved: bool) -> None:
    _object(value, _GEOCODE)
    count = value["candidate_count"]
    if count is not None:
        _integer(count, 5)
    for field in ("confidence", "confidence_building_level"):
        if value[field] is not None:
            _number(value[field])
            _require(0 <= value[field] <= 1)
    for field in ("match_type", "result_type"):
        _string(value[field], nullable=True)
    if resolved:
        _require(count is not None and count >= 1)
        _require(value["result_type"] == "building")
        _require(all(value[field] is not None and value[field] >= 0.95 for field in (
            "confidence", "confidence_building_level"
        )))
    else:
        _require(all(value[field] is None for field in _GEOCODE - {"candidate_count"}))


def _row_flags(row: dict, budget: int) -> dict:
    if row["time_seconds"] is None:
        return dict.fromkeys(_FLAGS)
    time = Decimal(str(row["time_seconds"]))
    within = time <= budget
    return {
        "route_within_budget": within,
        "borderline": Decimal(budget) < time <= Decimal(budget) * Decimal("1.1"),
        "membership_route_disagreement": (
            None if row["verdict"] == "unknown" else (row["verdict"] == "in_zone") != within
        ),
    }


def _summary(rows: list[dict]) -> dict:
    resolved = sum(row["geocode_status"] == "resolved" for row in rows)
    inside = sum(row["verdict"] == "in_zone" for row in rows)
    outside = sum(row["verdict"] == "out_of_zone" for row in rows)
    known = [row for row in rows if row["route_status"] == "ok"]
    in_times = sorted(Decimal(str(row["time_seconds"])) for row in known if row["verdict"] == "in_zone")
    median = None
    if in_times:
        middle = len(in_times) // 2
        median = in_times[middle] if len(in_times) % 2 else (
            in_times[middle - 1] + in_times[middle]
        ) / 2
    maximum = max((row["time_seconds"] for row in known), default=None)
    denominator = inside + outside
    return {
        "total": len(rows), "resolved": resolved, "unresolved": len(rows) - resolved,
        "in_zone": inside, "out_of_zone": outside,
        "unknown_membership": len(rows) - inside - outside,
        "known_routes": len(known), "missing_routes": resolved - len(known),
        "borderline": sum(row["borderline"] is True for row in rows),
        "disagreements": sum(row["membership_route_disagreement"] is True for row in rows),
        "classified_denominator": denominator,
        "in_zone_percent": normalize_number(Decimal(inside) * 100 / denominator, 2) if denominator else None,
        "out_of_zone_percent": normalize_number(Decimal(outside) * 100 / denominator, 2) if denominator else None,
        "median_in_zone_seconds": normalize_number(median) if median is not None else None,
        "max_time_seconds": normalize_number(maximum) if maximum is not None else None,
        "max_time_row_ids": [row["row_id"] for row in known if row["time_seconds"] == maximum],
    }


def _run_status(report: dict) -> str:
    partial = any(
        row["geocode_status"] == "unresolved" or row["route_status"] != "ok"
        or row["verdict"] == "unknown" for row in report["customers"]
    ) or report["competitors"]["status"] in {"partial", "unavailable"}
    return "partial" if partial else "complete"


def _extent(extent: object, path: str) -> None:
    _object(extent, {"method", "parameters"})
    method = extent["method"]
    _require(method in {"rectangle", "proximity", "circle"})
    if path == "cli":
        _require(method == "rectangle")
    parameters = extent["parameters"]
    if method == "rectangle":
        _object(parameters, {"bbox"})
        bbox = parameters["bbox"]
        _require(type(bbox) is list and len(bbox) == 4)
        for value in bbox:
            _number(value)
        west, south, east, north = bbox
        _require(-180 <= west < east <= 180 and -90 <= south < north <= 90)
    else:
        _object(parameters, {"center", "radius_meters"} if method == "circle" else {"center"})
        _point(parameters["center"])
        if method == "circle":
            _number(parameters["radius_meters"])
            _require(parameters["radius_meters"] >= 0)


def _geodesic(origin: list, destination: list) -> float:
    lon1, lat1, lon2, lat2 = map(math.radians, [*origin, *destination])
    value = math.sin((lat2 - lat1) / 2) ** 2 + (
        math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2
    )
    return normalize_number(6371008.8 * 2 * math.asin(math.sqrt(min(1.0, max(0.0, value)))), 3)


def _competitors(report: dict) -> None:
    section = _object(report["competitors"], {
        "status", "category", "search_extent", "coverage", "cap_reached", "records"
    } | _COMP_COUNTS)
    status = section["status"]
    _require(status in {"not_requested", "unavailable", "ok", "partial"})
    _require(type(section["records"]) is list)
    if status == "not_requested":
        _require(all(section[field] is None for field in (
            {"category", "search_extent", "coverage", "cap_reached"} | _COMP_COUNTS
        )) and not section["records"])
        return
    _string(section["category"], blank=False)
    _require(supported_category(section["category"]))
    _extent(section["search_extent"], report["path"])
    if report["path"] == "mcp":
        _require(section["search_extent"] == {
            "method": "circle", "parameters": {
                "center": report["business"]["coordinates"], "radius_meters": 20000,
            },
        })
        _require(sum(item["operation"] == MCP_COMPETITOR_OPERATION
                     for item in report["evidence"]) == 1, "invalid_artifact")
    if status == "unavailable":
        _require(all(section[field] is None for field in (
            {"coverage", "cap_reached"} | _COMP_COUNTS
        )) and not section["records"])
        return
    _require(section["coverage"] == "sampled" and type(section["cap_reached"]) is bool)
    for field in _COMP_COUNTS:
        _integer(section[field], 20)
    _require(section["cap_reached"] == (section["returned_count"] == 20))
    _require(section["returned_count"] - section["duplicate_count"] == (
        section["observed_in_zone_count"] + section["observed_out_of_zone_count"]
        + section["unclassified_count"]
    ))
    _require(status == ("partial" if section["unclassified_count"] else "ok"))
    _require(len(section["records"]) == section["observed_in_zone_count"])
    record_ids = []
    for record in section["records"]:
        _object(record, {"id", "name", "address", "categories", "coordinates", "verdict", "geodesic_distance_meters"})
        _string(record["id"], blank=False)
        record_ids.append(record["id"])
        _string(record["name"], nullable=True)
        _string(record["address"], nullable=True)
        _strings(record["categories"])
        _point(record["coordinates"])
        _require(record["verdict"] == "in_zone")
        _measurement(record["geodesic_distance_meters"], 3)
        _require(record["geodesic_distance_meters"] == _geodesic(report["business"]["coordinates"], record["coordinates"]))
        if record["id"].startswith("synthetic-id:"):
            canonical = json.dumps([record["coordinates"], record["name"]], sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
            _require(record["id"] == "synthetic-id:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest())
    _require(record_ids == sorted(set(record_ids)))


def _validate(report: object, *, acquired: bool) -> None:
    _object(report, _ROOT - {"summary", "run_status"} if acquired else _ROOT)
    _json_value(report)
    _require(report["schema_version"] == "1.0")
    _require(report["path"] in {"cli", "mcp"} and report["data_mode"] in {"live", "synthetic"})
    if report["path"] == "mcp":
        _require(APPROVED_AGENT_METHOD == "route_time_at_points", "agent_method_pending")
    timestamp = report["run_timestamp_utc"]
    _string(timestamp)
    _require(_TIMESTAMP.fullmatch(timestamp) is not None)
    try:
        datetime.fromisoformat(timestamp)
    except ValueError:
        raise ReportError() from None
    business = _object(report["business"], {"name", "input_address", "resolved_address", "coordinates", "geocode_evidence"})
    for field in ("name", "input_address", "resolved_address"):
        _string(business[field], blank=False)
    _point(business["coordinates"])
    _geocode(business["geocode_evidence"], True)
    settings = _object(report["settings"], {"budget_seconds", "mode", "traffic", "route_type", "units", "direction", "boundary_rule"})
    budget = settings["budget_seconds"]
    _integer(budget)
    _require(300 <= budget <= 3600 and budget % 60 == 0)
    for field, value in {"mode": "drive", "traffic": "free_flow", "route_type": "balanced", "units": "metric", "direction": "outbound"}.items():
        _require(settings[field] == value)
    _string(settings["boundary_rule"], blank=False)
    zone = _object(report["zone"], {"method", "approximation", "parameters", "limitations", "evidence_refs"})
    _require(type(zone["approximation"]) is bool)
    _strings(zone["limitations"], nonempty=True)
    if report["path"] == "cli":
        _require(zone["method"] == "geoapify_isoline" and zone["approximation"] is False)
        parameters = _object(zone["parameters"], {"range_seconds", "boundary_tolerance_degrees"})
        _integer(parameters["range_seconds"])
        _number(parameters["boundary_tolerance_degrees"])
        _require(parameters["range_seconds"] == budget and parameters["boundary_tolerance_degrees"] == 1e-9)
    else:
        _require(zone["method"] == APPROVED_AGENT_METHOD and zone["approximation"] is True)
        _require(AGENT_LIMITATION in zone["limitations"])
        parameters = _object(zone["parameters"], {"budget_seconds"})
        _integer(parameters["budget_seconds"])
        _require(parameters["budget_seconds"] == budget)
    _artifact_index(report)
    evidence_ids = {item["id"] for item in report["evidence"]}
    _refs(zone["evidence_refs"], evidence_ids, required=True)
    rows = report["customers"]
    _require(type(rows) is list and 1 <= len(rows) <= 20)
    for index, row in enumerate(rows, 1):
        _object(row, _CUSTOMER)
        _integer(row["row_id"])
        _require(row["row_id"] == index)
        for field in ("name", "reference"):
            _string(row[field], nullable=True)
        _string(row["input_address"], blank=False)
        _require(row["geocode_status"] in {"resolved", "unresolved"})
        _require(row["verdict"] in _VERDICTS)
        _require(row["route_status"] in {"ok", "error", "no_route", "not_attempted"})
        resolved = row["geocode_status"] == "resolved"
        _geocode(row["geocode_evidence"], resolved)
        _refs(row["evidence_refs"], evidence_ids, required=resolved or row["geocode_evidence"]["candidate_count"] is not None)
        if resolved:
            _string(row["resolved_address"], blank=False)
            _point(row["coordinates"])
            _require(row["geocode_reason"] is None and row["route_status"] != "not_attempted")
            if report["path"] == "cli":
                _require(row["verdict"] != "unknown")
        else:
            _string(row["geocode_reason"], blank=False)
            _require(row["resolved_address"] is None and row["coordinates"] is None)
            _require(row["verdict"] == "unknown" and row["route_status"] == "not_attempted")
            count = row["geocode_evidence"]["candidate_count"]
            reason = row["geocode_reason"]
            if reason == "no_match":
                _require(count == 0)
            elif reason in {"ambiguous", "insufficient_precision"}:
                _require(count is not None and count >= (2 if reason == "ambiguous" else 1))
        if row["route_status"] == "ok":
            _measurement(row["time_seconds"])
            _measurement(row["distance_meters"])
        else:
            _require(row["time_seconds"] is None and row["distance_meters"] is None)
        if report["path"] == "mcp":
            expected = "unknown" if row["time_seconds"] is None else (
                "in_zone" if Decimal(str(row["time_seconds"])) <= budget else "out_of_zone"
            )
            _require(row["verdict"] == expected)
        expected_flags = dict.fromkeys(_FLAGS) if acquired else _row_flags(row, budget)
        for field, expected in expected_flags.items():
            _require(row[field] is None or type(row[field]) is bool)
            _require(row[field] is expected)
    _competitors(report)
    _strings(report["warnings"])
    _require(type(report["errors"]) is list)
    for error in report["errors"]:
        _object(error, {"code", "message", "retryable", "row_ids"})
        _string(error["code"], blank=False)
        _string(error["message"], blank=False)
        _require(type(error["retryable"]) is bool and type(error["row_ids"]) is list)
        for row_id in error["row_ids"]:
            _integer(row_id)
            _require(1 <= row_id <= len(rows))
        _require(len(set(error["row_ids"])) == len(error["row_ids"]))
    _require(type(report["attributions"]) is list)
    for item in report["attributions"]:
        _object(item, {"source", "text", "url"})
        for field in ("source", "text", "url"):
            _string(item[field], blank=False)
        url = urlsplit(item["url"])
        _require(url.scheme == "https" and bool(url.hostname) and "." in url.hostname)
        _require(not url.username and not url.password and not url.query and not url.fragment)
        _require(not any(ord(char) < 33 for char in item["url"]))
    if not acquired:
        summary = _object(report["summary"], _COUNTS | _AGGREGATES | {"max_time_row_ids"})
        for field in _COUNTS:
            _integer(summary[field])
        for field in _AGGREGATES:
            if summary[field] is not None:
                _measurement(summary[field], 2 if field.endswith("percent") else 6)
        _require(type(summary["max_time_row_ids"]) is list)
        for row_id in summary["max_time_row_ids"]:
            _integer(row_id)
        _require(summary == _summary(rows))
        _require(report["run_status"] == _run_status(report))


def validate(report: object) -> None:
    """Validate a finished report; never repair evidence or derived fields."""
    try:
        _validate(report, acquired=False)
    except ReportError:
        raise
    except (ValueError, TypeError, KeyError, OverflowError, RecursionError, ArithmeticError):
        raise ReportError() from None


def finalize(acquired_dict: dict) -> dict:
    """Normalize acquired measurements and derive a validated, independent report."""
    try:
        _object(acquired_dict, _ROOT - {"summary", "run_status"})
        _json_value(acquired_dict)
        report = copy.deepcopy(acquired_dict)
        _require(type(report["customers"]) is list)
        for row in report["customers"]:
            _object(row, _CUSTOMER)
            for field in ("time_seconds", "distance_meters"):
                if row[field] is not None:
                    row[field] = normalize_number(row[field])
        section = report["competitors"]
        _require(type(section) is dict and type(section.get("records")) is list)
        for record in section["records"]:
            _require(type(record) is dict and "geodesic_distance_meters" in record)
            record["geodesic_distance_meters"] = normalize_number(record["geodesic_distance_meters"], 3)
        _validate(report, acquired=True)
        for row in report["customers"]:
            row.update(_row_flags(row, report["settings"]["budget_seconds"]))
        report["summary"] = _summary(report["customers"])
        report["run_status"] = _run_status(report)
        validate(report)
        return report
    except ReportError:
        raise
    except (ValueError, TypeError, KeyError, OverflowError, RecursionError, ArithmeticError):
        raise ReportError() from None


def _escape(value: str) -> str:
    # Entities remain text in Markdown and cannot create tags, links, or rows.
    escaped = html.escape(value, quote=True)
    return "".join(
        f"&#{ord(char)};" if char in "\\|`*_{}[]()#!+-.~:" or char in "\r\n\t" or ord(char) < 32 else char
        for char in escaped
    )


def _display(value: object) -> str:
    if value is None:
        return "unavailable"
    if type(value) is str:
        return _escape(value) if value else '&quot;&quot;'
    return _escape(json.dumps(value, ensure_ascii=False, sort_keys=True, allow_nan=False))


def _field_rows(value: object, path: str = "$"):
    if type(value) is dict:
        yield path, "object", "{}" if not value else "object"
        for key in sorted(value):
            yield from _field_rows(value[key], path + "." + key)
    elif type(value) is list:
        yield path, "array", "[]" if not value else f"{len(value)} entries"
        for index, item in enumerate(value):
            yield from _field_rows(item, f"{path}[{index}]")
    else:
        kind = "null" if value is None else (
            "boolean" if type(value) is bool else "string" if type(value) is str else "number"
        )
        yield path, kind, value


def render_markdown(report: dict) -> str:
    """Render readable tables plus a lossless field/path view of every JSON value."""
    validate(report)
    lines = ["# ZonePilot report", "", "## Run and method", "", "| Field | Value |", "| --- | --- |"]
    for field in ("schema_version", "path", "data_mode", "run_status", "run_timestamp_utc"):
        lines.append(f"| {_escape(field)} | {_display(report[field])} |")
    for field in ("method", "approximation", "parameters", "limitations"):
        lines.append(f"| zone.{_escape(field)} | {_display(report['zone'][field])} |")
    lines += ["", "## Summary", "", "| Field | Value |", "| --- | --- |"]
    for field, value in sorted(report["summary"].items()):
        lines.append(f"| {_escape(field)} | {_display(value)} |")
    lines += ["", "## Customers", "", "| Row | Name | Supplied address | Geocode | Membership | Route | Time, seconds | Distance, metres | Within budget | Borderline | Disagreement |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for row in report["customers"]:
        fields = ["row_id", "name", "input_address", "geocode_status", "verdict", "route_status", "time_seconds", "distance_meters", "route_within_budget", "borderline", "membership_route_disagreement"]
        lines.append("| " + " | ".join(_display(row[field]) for field in fields) + " |")
    lines += ["", "## Competitors", "", "Counts are observed places. Successful searches are sampled, not a market census.", "", "| Field | Value |", "| --- | --- |"]
    for field, value in sorted(report["competitors"].items()):
        if field != "records":
            lines.append(f"| {_escape(field)} | {_display(value)} |")
    lines += ["", "| ID | Name | Address | Categories | Coordinates, lon/lat | Membership | Geodesic distance, metres |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for record in report["competitors"]["records"]:
        lines.append("| " + " | ".join(_display(record[field]) for field in ("id", "name", "address", "categories", "coordinates", "verdict", "geodesic_distance_meters")) + " |")
    for title, key in (("Evidence", "evidence"), ("Errors", "errors"), ("Warnings", "warnings"), ("Attributions", "attributions")):
        lines += ["", f"## {title}", "", "| Entry | Value |", "| --- | --- |"]
        for index, item in enumerate(report[key]):
            lines.append(f"| {index} | {_display(item)} |")
        if not report[key]:
            lines.append("| entries | [] |")
    lines += ["", "## Complete field details", "", "Every JSON field is listed independently. Null means unavailable.", "", "| JSON path | Type | Value |", "| --- | --- | --- |"]
    for path, kind, value in _field_rows(report):
        lines.append(f"| {_escape(path)} | {kind} | {_display(value)} |")
    return "\n".join(lines) + "\n"


def _verify_mcp_competitors(report: dict, artifacts: dict[str, bytes]) -> None:
    """Bind sampled competitor counts and records to acquired point-route evidence."""
    section = report["competitors"]
    if report["path"] != "mcp" or section["status"] == "not_requested":
        return
    try:
        entries = [item for item in report["evidence"]
                   if item["operation"] == MCP_COMPETITOR_OPERATION]
        _require(len(entries) == 1)
        evidence = json.loads(
            artifacts[entries[0]["artifact"]].decode("utf-8"),
            object_pairs_hook=_no_duplicate_keys, parse_constant=_reject_constant,
        )
        _json_value(evidence)
        _object(evidence, {
            "representation", "approximation", "category", "search_extent", "settings",
            "max_candidates", "pagination", "search_status", "returned_count",
            "duplicate_count", "invalid_coordinate_count", "candidates",
        })
        _require(evidence["representation"] == MCP_COMPETITOR_OPERATION and evidence["approximation"] is True)
        _require(supported_category(evidence["category"]))
        _require(evidence["category"] == section["category"])
        _extent(evidence["search_extent"], "mcp")
        _require(evidence["search_extent"] == section["search_extent"])
        settings = _object(evidence["settings"], set(report["settings"]) - {"boundary_rule"})
        _integer(settings["budget_seconds"])
        _require(settings == {key: report["settings"][key] for key in settings})
        _integer(evidence["max_candidates"])
        _require(evidence["max_candidates"] == 20 and evidence["pagination"] is False)
        _require(evidence["search_status"] in {"ok", "unavailable"})
        candidates = evidence["candidates"]
        _require(type(candidates) is list and len(candidates) <= 20)
        counts = ("returned_count", "duplicate_count", "invalid_coordinate_count")
        if evidence["search_status"] == "unavailable":
            _require(section["status"] == "unavailable" and not candidates)
            _require(all(evidence[key] is None for key in counts))
            return
        _require(section["status"] in {"ok", "partial"})
        for key in counts:
            _integer(evidence[key], 20)
        _require(evidence["returned_count"] == evidence["duplicate_count"]
                 + evidence["invalid_coordinate_count"] + len(candidates))
        _require(all(evidence[key] == section[key]
                     for key in ("returned_count", "duplicate_count")))
        identifiers = []
        records = []
        outside = 0
        unknown = evidence["invalid_coordinate_count"]
        identity_fields = {"id", "name", "address", "categories", "coordinates"}
        for candidate in candidates:
            _object(candidate, identity_fields | {
                "route_status", "time_seconds", "distance_meters",
            })
            _string(candidate["id"], blank=False)
            identifiers.append(candidate["id"])
            _string(candidate["name"], nullable=True)
            _string(candidate["address"], nullable=True)
            _strings(candidate["categories"])
            _point(candidate["coordinates"])
            if candidate["id"].startswith("synthetic-id:"):
                canonical = json.dumps(
                    [candidate["coordinates"], candidate["name"]], sort_keys=True,
                    separators=(",", ":"), ensure_ascii=False, allow_nan=False,
                )
                _require(candidate["id"] == "synthetic-id:" + hashlib.sha256(
                    canonical.encode("utf-8")).hexdigest())
            _require(candidate["route_status"] in {"ok", "no_route", "error"})
            if candidate["route_status"] != "ok":
                _require(candidate["time_seconds"] is None
                         and candidate["distance_meters"] is None)
                unknown += 1
                continue
            _measurement(candidate["time_seconds"])
            _measurement(candidate["distance_meters"])
            if Decimal(str(candidate["time_seconds"])) > settings["budget_seconds"]:
                outside += 1
                continue
            records.append({
                **{key: candidate[key] for key in identity_fields},
                "verdict": "in_zone",
                "geodesic_distance_meters": _geodesic(
                    report["business"]["coordinates"], candidate["coordinates"]),
            })
        _require(identifiers == sorted(set(identifiers)))
        _require(section["observed_in_zone_count"] == len(records))
        _require(section["observed_out_of_zone_count"] == outside)
        _require(section["unclassified_count"] == unknown)
        _require(section["records"] == records)
    except (ValueError, TypeError, KeyError, OverflowError, RecursionError, ArithmeticError):
        raise ReportError("invalid_artifact") from None


def _verify_artifacts(report: dict, artifacts: object) -> dict[str, bytes]:
    expected = _artifact_index(report)
    _require(type(artifacts) is dict and set(artifacts) == set(expected), "invalid_artifact")
    for path, content in artifacts.items():
        _require(type(content) is bytes, "invalid_artifact")
        _require(hashlib.sha256(content).hexdigest() == expected[path], "invalid_artifact")
    _verify_mcp_competitors(report, artifacts)
    return artifacts


def write_bundle(report: dict, output_dir: str | os.PathLike, artifacts: dict[str, bytes]) -> None:
    """Publish a staged report directory; exclusively claim and never reuse output."""
    validate(report)
    _verify_artifacts(report, artifacts)
    json_bytes = dumps(report).encode("utf-8")
    markdown_bytes = render_markdown(report).encode("utf-8")
    stage: Path | None = None
    destination: Path | None = None
    reservation: tuple[int, int] | None = None
    try:
        destination = Path(output_dir)
        _require(destination.name not in ("", ".", ".."), "output_write_failed")
        parent = destination.parent.resolve(strict=True)
        destination = parent / destination.name
        if os.path.lexists(destination):
            raise ReportError("output_exists")
        stage = Path(tempfile.mkdtemp(prefix=".zonepilot-", dir=parent))
        for name, content in {"report.json": json_bytes, "report.md": markdown_bytes, **artifacts}.items():
            target = stage / name
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as stream:
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
        try:
            destination.mkdir(mode=0o700)
        except FileExistsError:
            raise ReportError("output_exists") from None
        metadata = destination.lstat()
        reservation = metadata.st_dev, metadata.st_ino
        # POSIX rename replaces only our own empty reservation, atomically.
        # Windows rename refuses any existing destination, so release it first.
        if os.name == "nt":
            destination.rmdir()
            reservation = None
        os.rename(stage, destination)
        stage = None
        reservation = None
    except ReportError:
        raise
    except (OSError, ValueError, TypeError):
        raise ReportError("output_write_failed") from None
    finally:
        if stage is not None:
            shutil.rmtree(stage, ignore_errors=True)
        if destination is not None and reservation is not None:
            try:
                metadata = destination.lstat()
                if (metadata.st_dev, metadata.st_ino) == reservation:
                    destination.rmdir()
            except OSError:
                pass


def _no_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        _require(key not in result, "invalid_import")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ReportError("invalid_import")


def _read_import(path: str | os.PathLike) -> tuple[dict, dict[str, bytes]]:
    try:
        source = Path(path)
        acquired = json.loads(source.read_text(encoding="utf-8"), object_pairs_hook=_no_duplicate_keys, parse_constant=_reject_constant)
    except ReportError:
        raise
    except (OSError, ValueError, TypeError, UnicodeError, RecursionError):
        raise ReportError("input_read_failed") from None
    _require(type(acquired) is dict and acquired.get("path") == "mcp", "invalid_import")
    _require("summary" not in acquired and "run_status" not in acquired, "invalid_import")
    _require(type(acquired.get("customers")) is list, "invalid_import")
    for row in acquired["customers"]:
        _require(type(row) is dict and all(field in row and row[field] is None for field in _FLAGS), "invalid_import")
    report = finalize(acquired)
    artifacts = {}
    try:
        base = source.parent.resolve(strict=True)
        for name in _artifact_index(report):
            target = base
            for component in name.split("/"):
                target = target / component
                _require(not target.is_symlink(), "invalid_artifact")
            _require(target.is_file(), "invalid_artifact")
            artifacts[name] = target.read_bytes()
    except ReportError:
        raise
    except (OSError, ValueError, TypeError):
        raise ReportError("invalid_artifact") from None
    _verify_artifacts(report, artifacts)
    return report, artifacts


class _Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise ReportError("invalid_arguments")


def main(argv: list[str] | None = None) -> int:
    parser = _Parser(description="approximation=true: Validate and render acquired hosted MCP evidence offline.")
    parser.add_argument("--import-agent", required=True, metavar="INPUT")
    parser.add_argument("--output-dir", required=True, metavar="NEW_DIRECTORY")
    try:
        args = parser.parse_args(argv)
        report, artifacts = _read_import(args.import_agent)
        write_bundle(report, args.output_dir, artifacts)
        return 0 if report["run_status"] == "complete" else 3
    except ReportError as error:
        print(f"approximation=true: {error}", file=sys.stderr)
        return 2 if error.code == "invalid_arguments" else 1


if __name__ == "__main__":
    raise SystemExit(main())
