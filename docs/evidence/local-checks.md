# Local verification record

Date: 2026-10-22. Environment: macOS Darwin arm64, stock Python 3.14.9. No dependencies, installers, downloaded scripts or CI were executed. The requested Python 3.15.1 target is unavailable; its checks are PENDING. Linux and Windows are PENDING.

## Commands and observed results

- `python3.14 -m unittest discover -s tests -v`: first integrated pass, 76 tests passed. The final report-module suite is recorded below when complete.
- `python3.14 -m zonepilot.cli --replay tests/fixtures/sample/run.json --output-dir reports/first`: exit 0, complete paired reports and evidence.
- Fixed twenty-row fixture processing plus JSON/Markdown rendering, excluding network and disk publication: 20 iterations, median 0.010481 seconds, maximum 0.015511 seconds. Geometry has five positions including ring closure. This is a measured fixture benchmark, not a universal latency guarantee.
- Geometry subtask: 48 tests passed, plus 30,000 independent membership-oracle checks. Validation of a geometry at the 2,000-position cap took 0.355 seconds.
- First fixture report: 20 resolved, 13 in zone, 7 outside, 20 known routes, 2 borderline, 2 polygon/time disagreements, median known in-zone time 800 seconds, maximum 2,600 seconds shared by rows 19 and 20.

All fixtures are authored synthetic responses. No successful authenticated invocation is claimed.

## Acceptance evidence map

| Gate | Local coverage | Remaining evidence |
| --- | --- | --- |
| AC-01 | test_pipeline.CLITests: BOM, quoted multiline CSV, duplicates, malformed headers/records, 21 rows, missing key and collected errors, existing output, replay no-network | Exact target-runtime/platform commands |
| AC-02 | test_pipeline.PipelineTests: building acceptance, tied candidates, no matches, missing confidence, wrong result type, invalid coordinates; origin/global abort vs retained customer | Approved live geocodability |
| AC-03 | test_geometry: rings/holes/components, every boundary, winding, tolerance, malformed topology, caps, geographic limitations; client 202 success/exhaustion; pipeline range mismatch | Real asynchronous Isoline shape |
| AC-04 | test_client request contracts; test_pipeline indexed reordered/missing/null/invalid cells, exact budget boundaries, disagreement and zero/tied times | Hosted route/matrix comparison; no undocumented fallback implemented |
| AC-05 | test_pipeline category preflight, sampled candidates, duplicates, invalid coordinates, zero versus unavailable | Approved exact plumbing category alternative/live competitor policy |
| AC-06 | test_report schema/rounding/Markdown/publication tests; pipeline deterministic replay | Cross-platform byte comparison |
| AC-07 | Setup snippets and complete nine-tool sequence documented; invalid/unapproved import fails safely | B02 method, B04 authenticated evidence, full matching analysis and other-client smoke |
| AC-08 | Synthetic twenty-row demo only | B01/B03 and one approved live run |
| AC-09 | macOS Python 3.14.9 local commands | Python 3.15.1, Linux and Windows |
| AC-10 | Provenance, incremental prompt log, genuine build incidents and tutorial outline | Finished tutorial, live feedback, screenshots, dev.to URL |
| AC-11 | Private repo and scrubbed reachable branch history | Hidden GitHub retention resolution before public release, final owner gate |

## Integrated verification before PR

After the fallback-ID fix, `python3.14 -m unittest discover -s tests` passed all 125 tests. Source/test AST inspection found only standard-library or local imports. `python3.14 -m compileall -q zonepilot tests` and `git diff --check` passed. The literal privacy-pattern sweep passed for all 39 working files and reachable `git log -p`; all commit author emails use the approved noreply identity. No push occurred while a scan was failing.

Final initial-implementation suite: 126 tests passed. The report module contributed 47 focused tests and 1,155 malformed-input adversarial cases, including a fixed invalid-hour acceptance defect. Missing matrix measurement fields are now distinguished from explicit no-route values.

## PR review round 1 fixes

Sol reviewed 4342973 and reproduced three P2 defects. All were accepted and fixed. Regression tests first failed as expected, then the complete suite passed 130 tests on Python 3.14.9. Coverage now includes absent optional matrix snaps with 19 retained routes; present invalid snaps; blank/invalid UTF-8 competitor metadata with preserved customer publication; and CRS declarations rejected at all three Isoline envelope levels. Baseline golden reports remain unchanged. Review discussion is on PR 2.

## Review round 2 regression verification

Sol verified the round 1 fixes and identified two additional P2 defects. Fixed scoped evidence failures and shared snapshot category acceptance. All 134 offline unittest tests passed on Python 3.14.9. CLI replay and mocked HTTP tests retain 19 valid routes after either one malformed customer geocode or one overflowing matrix measurement. Normalized matrix evidence keeps an explicit error/null cell and discards unrelated malformed metadata. The baseline report's only value change is the matrix artifact hash. All 833 snapshot categories pass preflight; tex-mex passes report publication; unknown and multiple categories remain rejected.
