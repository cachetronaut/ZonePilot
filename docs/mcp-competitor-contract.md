# MCP competitor evidence contract

The owner approved point-time competitor classification on 2026-10-23. This
contract supersedes the pending MCP competitor gate in `report-schema.md`.
It preserves report schema `1.0`, its existing root and competitor fields, CLI
behavior, and MCP `not_requested` behavior.

Use one supported category from `zonepilot/categories.json`, such as `service`.
Search once with a circle centered on `business.coordinates`, radius exactly
20000 metres, limit 20, and no pagination. The circle is only a search extent.
It does not determine membership. A broad `service` search observes matching
places; it does not verify that every result competes with the fictional business.
Keep real returned place identities and label live evidence as live. Approved
public Midland addresses do not make real provider results fictional.

## Evidence index and artifact

Every requested MCP competitor section, including `unavailable`, requires exactly
one evidence entry whose `operation` is `mcp_competitor_classification`. Use the
existing evidence entry fields `id`, `kind`, `operation`, `artifact`, and `sha256`.
Use `kind=mcp` for live reports and `kind=synthetic` for authored offline tests.
The artifact path may be any existing-schema safe path, for example
`evidence/mcp-competitor-classification.json`. Hash the exact UTF-8 artifact bytes.
No new report field or evidence reference field is added.

The JSON artifact has exactly these fields. This example is synthetic and uses
one candidate solely to illustrate the shape. Replace all values with acquired
evidence and the actual report settings.

```json
{
  "representation": "mcp_competitor_classification",
  "approximation": true,
  "category": "service",
  "search_extent": {
    "method": "circle",
    "parameters": {"center": [0, 0], "radius_meters": 20000}
  },
  "settings": {
    "budget_seconds": 1200,
    "mode": "drive",
    "traffic": "free_flow",
    "route_type": "balanced",
    "units": "metric",
    "direction": "outbound"
  },
  "max_candidates": 20,
  "pagination": false,
  "search_status": "ok",
  "returned_count": 1,
  "duplicate_count": 0,
  "invalid_coordinate_count": 0,
  "candidates": [
    {
      "id": "authored-example",
      "name": "Synthetic example place",
      "address": null,
      "categories": ["service"],
      "coordinates": [0, 0],
      "route_status": "ok",
      "time_seconds": 1200,
      "distance_meters": 0
    }
  ]
}
```

The artifact always requires `approximation=true` so the method label survives separately from the report. All objects reject extra or missing fields. JSON rejects duplicate object keys,
nonfinite numbers, numeric strings and booleans used as numbers. `category` and
`search_extent` must equal the report competitor values. `settings` must equal
the six corresponding report settings, excluding `boundary_rule`.
`max_candidates` is integer 20; `pagination` is boolean false.

For a successful search, `search_status=ok`. All three counts are integers from
0 through 20. `returned_count` counts raw returned places before discards.
Deduplicate in provider order by provider ID. Without an ID, use the existing
`synthetic-id:` plus SHA-256 of canonical UTF-8 JSON `[coordinates, name]`, with
sorted keys, compact separators and no ASCII escaping. Keep the first occurrence.
Check duplicates before coordinates, as the existing CLI does.
`duplicate_count` counts discarded repetitions. `invalid_coordinate_count`
counts unique candidates discarded for invalid or absent WGS84 Point coordinates.
A candidate whose fallback identity cannot be encoded also counts as invalid.
Do not silently discard valid-coordinate candidates because their routes failed.
Malformed identity or display metadata must be corrected from source evidence
or rejected, not silently counted as invalid coordinates.

`candidates` contains every remaining unique valid-coordinate candidate, sorted
by `id`. Each object has exactly the eight fields shown above. IDs are nonblank
strings; name and address are strings or null; categories are arrays of nonblank
strings; coordinates are `[longitude, latitude]` within geographic bounds.
Fallback IDs must match the existing canonical hash. No candidate verdict is
supplied: validation derives it from the acquired route.

Attempt an outbound route from the report business to every candidate under the
recorded settings. `route_status=ok` requires both nonnegative finite measurements,
already normalized to six decimal places with decimal half-even rounding.
`route_status=no_route` or `error` requires both measurements null. Omitted route
cells use `no_route`; failed or invalid responses use `error`. `not_attempted`
is not accepted. Preserve sanitized hosted call evidence alongside this normalized
artifact where available. Normalization records acquired measurements; it must
never invent them. Hashes establish byte integrity, not proof of a hosted call.

For a failed search, use `search_status=unavailable`, null for all three counts,
and an empty `candidates` array. Retain the category, extent and settings. The
report section must be `unavailable` with existing null-count semantics.
A successful empty result instead uses `ok`, three zero counts and an empty array.

## Derived report section

For successful searches, require
`returned_count = duplicate_count + invalid_coordinate_count + len(candidates)`.
A known normalized time at or below `settings.budget_seconds` is in zone. A larger
known time is out of zone. Failed or missing routes remain unclassified.

Set `observed_in_zone_count` and `observed_out_of_zone_count` from these comparisons.
Set `unclassified_count` to `invalid_coordinate_count` plus the number of candidates
with `route_status` other than `ok`. Set `status=partial` exactly when this count
is positive, otherwise `ok`. Always set `coverage=sampled`, including empty results.
Set `cap_reached` exactly when `returned_count=20`. Copy the raw returned and
duplicate counts. Preserve the existing section arithmetic.

`records` contains exactly the in-zone candidates, sorted by ID, with the existing
record fields. Copy identity, name, address, categories and coordinates exactly;
set `verdict=in_zone`. Compute `geodesic_distance_meters` using the existing
haversine rule and three-place half-even rounding. Do not use acquired driving
distance as geodesic distance. Out-of-zone and unclassified candidates remain
in the evidence artifact and do not appear in report `records`.

## Validation boundary

`finalize` and `validate` require the evidence index entry and approved extent for
requested MCP competitors. They validate report shape and existing arithmetic.
They do not load external files. Keyless import and `write_bundle` additionally
verify hashes, parse this artifact strictly, and compare every count and record
against its routes. Missing artifacts, contradictory settings, falsified counts,
missing or extra records, changed metadata and wrong membership fail before any
output is published. `not_requested` needs no new artifact. CLI is unchanged.
