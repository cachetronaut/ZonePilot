# Full live isoline geometry contract

Stage 4 offline verification, 2026-10-23. This change supports the complete
saved provider geometry in `docs/evidence/stage4/live/isoline-diagnostic.json`.
It does not simplify, round, repair, drop rings, or modify the input object.
The old 2,000-position cap rejected this response before topology validation.
The full response passes the retained topology checks with the new limits.

## Limits and validation

- At most 20,000 positions across all components and rings, including each
  closing position. Exactly 20,000 is supported; 20,001 is rejected.
- At most 32 rings across the full geometry, including exteriors and holes.
- At most 2,000,000 x-overlapping segment-pair candidates per validation.
  Attempting candidate 2,000,001 fails closed with the existing
  `unsupported_geometry` code and safe generic error message. The budget is
  shared by all rings and components, and resets for each validation call.

One x sweep checks all nonadjacent same-ring pairs and all cross-ring pairs.
It sorts segment starts and retains every edge whose maximum x plus the
existing tolerance reaches the current start. A heap expires edges without
repeated scans. Each active pair consumes budget before the y bounding-box
filter or adjacency exclusion, so even many y-disjoint overlapping x extents
cannot cause unbounded work. Remaining pairs use the unchanged segment-contact
predicate. Equal x events and gaps within tolerance remain candidates.

Adjacent edges still undergo the original backtracking and short-edge checks.
Ring closure, unique vertices, nondegenerate area, self-contact, intersections,
hole containment, hole nesting/overlap, and component contact/overlap checks
remain enforced. Islands strictly inside holes remain supported. Longitude
span/edge limits, supported latitude limits, CRS rejection, and finite-number
checks are unchanged. Exterior and hole boundaries still count as inside within
1e-9 degrees, using distance to the finite segment. Strict hole interiors remain
outside. Winding remains immaterial.

Validation uses O(V log V + C + R*V) time and O(V) space, where V is positions,
R is rings, and C is the budgeted x-overlapping pair count. A valid pathological
shape can exceed the work budget and be rejected; exceeding it never produces
an accepted partial validation. Membership uses the full validated geometry.

## Saved response verification

The actual 1,200-second drive response is a MultiPolygon with one component,
one exterior and two holes. Ring lengths, including closure, are 13,506, 603,
and 649, totaling 14,758 positions. Its canonical geometry SHA-256 is
`9fe4139275986bfc5c6cff0780c6fa4892e32cafbb5226f8abdfa4e949cb717d`.
Canonical encoding uses `json.dumps(geometry, sort_keys=True, separators=(",", ":"))`
encoded as UTF-8.

On Python 3.14.9, macOS arm64, nine offline validation runs measured 0.0344 to
0.0399 seconds, median 0.0385 seconds. These timings exclude JSON loading and
network acquisition. A separate instrumented run counted 215,994 candidates.
Validation returned the original object, with all coordinates and metadata
unchanged. The CLI engine's `zone_geometry` response validation also passed
for the saved response at 1,200 seconds.

All twenty customer coordinates matched by exact input address from the saved
`discovery.json` and `discovery-additional.json` records were inside this
geometry. The twenty membership calls took 0.0360 seconds. The origin was also
inside. These are offline checks against captured live-derived data, not a new
live CLI or MCP run. They make no claim about route-time borderline outcomes
or an inside/outside demonstration mix.

To repeat the full response validation without credentials or network calls,
run from the repository root:

```sh
python3.14 -B - <<'PYCODE'
import json
from pathlib import Path
from time import perf_counter
from zonepilot.engine import zone_geometry

root = Path("docs/evidence/stage4/live")
response = json.loads((root / "isoline-diagnostic.json").read_text())["response"]
business = json.loads(Path("data/sample_business.json").read_text())
records = [record for name in ("discovery.json", "discovery-additional.json")
           for record in json.loads((root / name).read_text())["records"]]
origin = next(record["coordinates"] for record in records
              if record["input_address"] == business["address"]
              and record["reason"] is None)
started = perf_counter()
geometry = zone_geometry(response, origin, 1200)
assert geometry == response["features"][0]["geometry"]
print("Validated complete geometry in", perf_counter() - started, "seconds")
PYCODE
```

## Regression evidence and integration

`python3.14 -B -m unittest discover -s tests -p test_geometry.py` passed all
54 geometry tests. `python3.14 -B -m unittest discover -s tests` passed all
156 tests in 1.060 seconds on the shared checkout at verification time.
Existing negative topology and boundary-tolerance tests remain intact.
New synthetic tests cover the 20,000-position boundary, large geometry with
holes and an island, a hole crossing hidden among thousands of edges, x/y
filter tolerance, a globally shared budget including y-disjoint/adjacent
pairs, and a valid pathological shape rejected by the actual two-million
budget. Eighty seeded synthetic ring sets compare sweep results against
exhaustive segment-contact checks. All fixtures remain authored synthetic
data; the provider response is used only in the separate offline verification.

Integration completed: the [live CLI](evidence/stage4/live/cli/report.md) and
[fresh-clone rerun](evidence/stage4/live/fresh-clone.json) both accept the full
geometry and evaluate all twenty customers. README and build decisions record
the revised cap. No live calls,
credential reads, dependency installs, commits, pushes, license changes, or
repository visibility changes were part of this geometry task.
