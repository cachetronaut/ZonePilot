# Report schema 1.0

This is the shared CLI and hosted-agent report contract from PRD Section 11.
Every listed field is required. Objects reject extra fields. JSON null means
unavailable; an empty array means no entries; zero means a known zero. Boolean
values never count as integers or numbers. Numbers must be finite JSON numbers.
All coordinate arrays use WGS84 `[longitude, latitude]` with longitude in
`[-180, 180]` and latitude in `[-90, 90]`. Strings must be valid UTF-8 text.

The authored [complete example](examples/complete.json) and
[partial example](examples/partial.json) precede renderer implementation. Their
evidence files are synthetic, not API recordings. Labels and coordinates are
deliberately invented. They do not establish live geocodability or hosted calls.

## Root

| Key | Exact type and rule |
| --- | --- |
| `schema_version` | String, `1.0`. |
| `path` | String, `cli` or `mcp`. |
| `data_mode` | String, `live` or `synthetic`. |
| `run_status` | String, `complete` or `partial`, derived locally. |
| `run_timestamp_utc` | Valid RFC3339 UTC string, `YYYY-MM-DDTHH:MM:SS[.fraction]Z` or the same with `+00:00`. Nonzero and unknown offsets are rejected. |
| `business` | Business object. |
| `settings` | Settings object. |
| `zone` | Zone object. |
| `customers` | Array of 1 through 20 customer objects in input order. |
| `summary` | Summary object, derived locally. |
| `competitors` | Competitor section object. |
| `errors` | Error array in acquisition stage/row order. |
| `warnings` | Array of safe strings in acquisition order. |
| `evidence` | Evidence array in acquisition order. |
| `attributions` | Attribution array in acquisition order. |

## Business and geocoding

| Object | Keys, types, and rules |
| --- | --- |
| Business | `name`: nonblank string, use `Business` when omitted at input. `input_address`, `resolved_address`: nonblank strings. `coordinates`: coordinate array. `geocode_evidence`: accepted geocode evidence object. |
| Geocode evidence | `candidate_count`: null or integer from 0 through 5. `confidence`, `confidence_building_level`: null or numbers in `[0, 1]`. `match_type`, `result_type`: null or strings. |

An accepted geocode has `candidate_count` from 1 through 5,
`confidence >= 0.95`, `confidence_building_level >= 0.95`, and
`result_type=building`. `match_type` may be null. The acquisition layer must prove
exactly one eligible candidate and retain the actual candidate count in evidence.
The root evidence index includes origin geocoding evidence with its operation.
Validation of the report alone cannot prove the contents of an external response.

Unresolved geocodes have null confidence, building confidence, match type, and
result type. Preserve a known candidate count; use null if no valid response was
read. `no_match` requires count 0. `ambiguous` requires count at least 2.
`insufficient_precision` requires a positive count. Other safe failure reasons
are nonblank strings and retain whatever count was actually read.

## Settings and zone

| Object | Keys, types, and rules |
| --- | --- |
| Settings | `budget_seconds`: integer multiple of 60 from 300 through 3600. `mode=drive`, `traffic=free_flow`, `route_type=balanced`, `units=metric`, `direction=outbound`: strings. `boundary_rule`: nonblank string describing the boundary convention. |
| Zone | `method`: nonblank string. `approximation`: boolean. `parameters`: object. `limitations`: nonempty array of nonblank strings. `evidence_refs`: nonempty array of distinct evidence ID strings. |
| CLI parameters | Exactly `range_seconds`: integer equal to `settings.budget_seconds`; `boundary_tolerance_degrees`: number equal to `1e-9`. |
| Approved agent parameters | Exactly `budget_seconds`: integer equal to `settings.budget_seconds`. |

CLI uses `method=geoapify_isoline` and `approximation=false`. Its full validated
Polygon or MultiPolygon is an evidence artifact. Ring boundaries, including hole
boundaries, are in zone with segment-distance tolerance `1e-9` degrees. A hole's
strict interior is out of zone. Every component and hole participates. Reports
retain this numerical convention and the free-flow, outbound model limits.

The owner approved B02 customer classification on 2026-10-23.
`APPROVED_AGENT_METHOD = "route_time_at_points"` enables offline MCP import.
This method requires `approximation=true`, the exact approved parameters above,
and the literal limitation "Route-time classification only at measured points; no continuous zone."
Additional truthful limitations are allowed. Missing labels/limitations and
continuous-polygon methods are rejected.
Membership is `in_zone` exactly when known normalized time is at most the budget;
it is `out_of_zone` for larger known time and `unknown` for missing routes.
The incoming verdict must agree; validation never invents measurements or a
polygon. Requested MCP competitors remain rejected with
`agent_competitors_pending` until their route-evidence/extent contract is approved.

## Customers

| Key | Exact type and rule |
| --- | --- |
| `row_id` | Integer, contiguous one-based input position. Duplicate input rows remain separate. |
| `name`, `reference` | Null or strings; optional values are preserved, including empty strings. |
| `input_address` | Nonblank string, preserving supplied whitespace. |
| `resolved_address` | Null or nonblank string. |
| `coordinates` | Null or coordinate array. |
| `geocode_status` | String, `resolved` or `unresolved`. |
| `geocode_reason` | Null for resolved rows; nonblank safe string for unresolved rows. |
| `geocode_evidence` | Geocode evidence object. |
| `verdict` | String, `in_zone`, `out_of_zone`, or `unknown`. |
| `route_status` | String, `ok`, `no_route`, `error`, or `not_attempted`. |
| `time_seconds`, `distance_meters` | Null or nonnegative numbers normalized to six decimal places. |
| `route_within_budget`, `borderline`, `membership_route_disagreement` | Null or booleans, derived locally. |
| `evidence_refs` | Array of distinct evidence IDs; nonempty for resolved rows and known candidate responses. |

Resolved rows require accepted geocoding, nonnull resolved address/coordinates,
and a route attempt. CLI resolved rows have a known polygon verdict, including
when their route is missing. Unresolved rows have unknown membership,
`route_status=not_attempted`, and null resolved address, coordinates, measurements,
and derived booleans. A route is `ok` only when both measurements are present.
Every other route status requires both measurements null.

For known normalized time `t` and budget `b`, `route_within_budget = (t <= b)` and
`borderline = (b < t <= 1.1 * b)`. These comparisons use decimal arithmetic.
`membership_route_disagreement` compares the known membership with
`route_within_budget`. Missing time makes all three values null. A CLI polygon
verdict is never replaced with a route result.

## Summary and run status

All count fields below are nonnegative integers. A derived report must match
these calculations exactly; supplying a self-consistent but false summary fails.

| Keys | Calculation or type |
| --- | --- |
| `total`, `resolved`, `unresolved` | Row count and geocode counts; `total = resolved + unresolved`. |
| `in_zone`, `out_of_zone`, `unknown_membership` | Verdict counts; their sum is `total`. |
| `known_routes`, `missing_routes` | Count `route_status=ok`; `missing_routes = resolved - known_routes`. |
| `borderline`, `disagreements` | Count true row flags only; null is unknown. |
| `classified_denominator` | `in_zone + out_of_zone`. |
| `in_zone_percent`, `out_of_zone_percent` | Null if denominator is zero; otherwise corresponding count times 100 divided by denominator, rounded to two decimals. |
| `median_in_zone_seconds` | Null without known in-zone times; otherwise median of those times, rounded to six decimals. |
| `max_time_seconds` | Null without known routes; otherwise maximum over every known customer time, rounded to six decimals. |
| `max_time_row_ids` | Integer array of every tied maximum row in input order, empty without known routes. |

The run is partial if any customer is unresolved, a resolved customer has a
missing route or unknown membership, or a requested competitor section is
unavailable/partial. Otherwise it is complete. A sampled-search warning alone
does not make a run partial. Errors describe the actual affected scope; warnings
and errors do not override these evidence-based run-status rules.

## Competitors

| Key | Exact type and rule |
| --- | --- |
| `status` | String, `not_requested`, `ok`, `partial`, or `unavailable`. |
| `category` | Null or one exact category from the committed official snapshot. Preflight and report validation use the same membership check, including supported hyphenated names. |
| `search_extent` | Null or search extent object. |
| `coverage` | Null or string `sampled`. A successful bounded search is always sampled. |
| `cap_reached` | Null or boolean; true exactly when `returned_count=20`. |
| `returned_count`, `duplicate_count`, `unclassified_count` | Null or integers in `[0, 20]`. |
| `observed_in_zone_count`, `observed_out_of_zone_count` | Null or integers in `[0, 20]`. |
| `records` | Array containing exactly the observed in-zone records, sorted by `id`, with unique IDs. |

`not_requested` requires null category, extent, coverage, cap, and all counts, and
empty records. `unavailable` retains requested category and extent but has null
coverage, cap, and every count, and empty records. Successful sections require
all counts and `coverage=sampled` even for zero results. They obey
`returned_count - duplicate_count = observed_in_zone_count + observed_out_of_zone_count + unclassified_count`.
Status is partial exactly when `unclassified_count > 0`; otherwise it is ok.

| Object | Exact fields |
| --- | --- |
| Search extent | `method`: `rectangle`, `proximity`, or `circle`; `parameters`: object as specified below. |
| Rectangle parameters | `bbox`: four-number array `[west, south, east, north]`, geographic bounds with `west < east` and `south < north`, no antimeridian crossing. CLI requires rectangle. |
| Proximity parameters | `center`: coordinate array. |
| Circle parameters | `center`: coordinate array; `radius_meters`: finite nonnegative number. This is only a candidate-search extent. |
| Competitor record | `id`: nonblank string; `name`, `address`: null or strings; `categories`: string array; `coordinates`: coordinate array; `verdict`: string `in_zone`; `geodesic_distance_meters`: nonnegative number rounded to three decimals. |

Competitor distance uses the haversine formula, radius `6371008.8` metres, from
the report's business coordinate. It never determines membership. Duplicate
provider IDs are removed before counting observations. Without a provider ID,
use `synthetic-id:` plus lowercase SHA-256 of UTF-8 canonical JSON
`[coordinates, name]`, sorted keys, compact separators, no ASCII escaping, and no
trailing LF. Invalid-coordinate candidates remain counted as unclassified and
do not appear in `records`.

## Evidence, errors, and attribution

| Object | Exact fields |
| --- | --- |
| Evidence | `id`: nonblank unique string; `kind`: string `rest`, `mcp`, or `synthetic`; `operation`: nonblank string; `artifact`: safe relative path; `sha256`: string of 64 lowercase hexadecimal characters. |
| Error | `code`: nonblank safe string; `message`: nonblank safe string; `retryable`: boolean; `row_ids`: array of distinct existing customer row IDs, or empty for a section-level error. |
| Attribution | `source`, `text`: nonblank strings; `url`: approved public HTTPS URL without credentials, query, or fragment. |

References resolve to evidence IDs, with no repeated ID within a reference list.
Relative artifact paths use `/` separators and nonempty components. Reject
absolute, drive-qualified, UNC, backslash, dot, dot-dot, URI/query/fragment,
control-character, and percent-escaped paths. Paths cannot collide with
`report.json` or `report.md`, including case-insensitive collisions, or another
artifact's file/directory prefix. Synthetic reports use synthetic evidence;
live CLI reports use REST evidence; live MCP reports use MCP evidence.

The acquisition layer is responsible for evidence sanitization, attribution
approval, accepted candidate uniqueness, and truthful operation/results. Schema
validation checks typed values and references. Bundle publication additionally
checks every supplied artifact byte string against its indexed SHA-256. Hash
verification does not prove a live invocation or approve publication of data.
Do not pass raw Geoapify error text into `errors` or `warnings`. Report failures
use fixed diagnostics and never interpolate input, paths, URLs, or exceptions.

CLI Route Matrix artifacts use `representation: normalized_route_matrix` with
the validated origin, ordered targets, routing settings and one indexed
measurement per target. Each measurement has `source_index`, `target_index`,
`route_status`, `time_seconds` and `distance_meters`. Invalid measurements retain
status `error` and null measurements; no replacement time or distance is invented.
Unrelated provider fields and invalid raw values are not retained. A rejected
customer geocode artifact leaves that customer unresolved with an `invalid_response`
error and no artifact reference; it does not abort other customers.

## Serialization and local interfaces

`dumps(obj)` emits sorted keys, indentation of two spaces, UTF-8 text without ASCII
escaping, and exactly one trailing LF. It rejects nonfinite numbers and values
outside JSON types. Normalize acquired seconds/metres to six decimal places
using `Decimal(str(value))` and `ROUND_HALF_EVEN` before calculation.
`normalize_number(value, places=6)` accepts only finite nonnegative int/float or
Decimal values, rejects bool and numeric strings, and returns float. Geodesic
metres use three places, percentages two, and derived median/maximum six.

`finalize(acquired_dict)` takes a deep copy of the root contract without
`summary` and `run_status`. All customer fields remain present and the three
derived booleans must be null. It normalizes acquired measurements, validates
evidence/state invariants, derives row booleans, summary and run status, and
returns the validated report without mutating the caller's object.
`validate(report)` accepts a finished report or raises `ReportError`, a
`ValueError` subclass with a stable `code` and fixed safe message. It never
repairs a finished report.

`render_markdown(report)` validates first, then emits a header, summary, customer
table, competitor state/table, and evidence/error/attribution details. A complete
field/path table exposes every object, array, and scalar independently. Null is
`unavailable`; empty strings and collections remain explicitly distinguishable.
User/API text escapes pipes, line breaks, HTML, link syntax and other Markdown
punctuation. Raw seconds and metres remain accessible. Rendering has no clock,
locale, network, or key dependency.

`write_bundle(report, output_dir, artifacts)` requires a nonexistent destination
directory and an existing parent. The artifact mapping has exactly the indexed
relative paths and byte values. Publication writes `report.json`, `report.md`
and artifacts in a private staging directory on the same filesystem. It claims
the destination exclusively as an empty private reservation, then publishes the
finished directory with one rename. A failed rename removes
only files from this attempt and its newly created reservation. Existing files or
directories are never overwritten. Validation/render/hash failure publishes
nothing. The pair is announced only after the function returns successfully.

The keyless command is
`python -m zonepilot.report --import-agent evidence.json --output-dir output/new-run`.
It accepts an acquired object only with `path=mcp`, rejects supplied derived root
fields and nonnull row flags, and reads indexed artifacts relative to the import
file's parent without following symlinks. It never acquires missing API evidence.
The approved point-time method imports without a key; invalid or unapproved methods fail with exit 1. Import diagnostics retain the approximation label. Valid complete/partial
bundles return exit 0/3. Argument errors return exit 2 with a fixed usage message.
Input, artifact, validation and publication errors return exit 1 using fixed
diagnostics. This command does not use client or engine modules.
