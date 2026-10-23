# ZonePilot prompt log

## 2026-10-22, build session opened

Instruction summary: build PRD Stages 1–2 and the Stage 3 agent pack using stock Python and no dependencies; keep this repository private; use the GitHub noreply identity; scrub owner credit and replace history before code; verify locally, then drive Sol xhigh review rounds on a PR. The PRD wins conflicts. No credential was supplied or requested.

Read both authoritative documents fully before coding. No product code existed. Changed the owner to Scout Squad and the supported runtime to Python 3.14.9 minimum, Python 3.15.1 target. No downloaded code or installers were run.

Observed environment failures: the first GitHub request failed with `error connecting to api.github.com` inside the sandbox. Retrying with authorized network access succeeded and confirmed the repository is private. The requested Python policy path was missing; found and read the same policy in the installed plugin. Python 3.15.1 is not installed; Python 3.14.9 is available. Target-runtime verification remains PENDING, with no interpreter installation attempted.

Live runs: PENDING. GEOAPIFY_API_KEY is absent. No live Geoapify request was attempted.

PRD conflicts identified: the build prompt asks for a polygon Places filter, but FR-18 and section 11 require rectangle metadata and local membership. Follow the PRD. The prompt requests synthetic samples in live-demo paths, but section 12 reserves those for B03-approved inputs. Keep fixtures separate pending clarification. The requested sampled-boundary agent method lacks the PRD-required accuracy/cost contract; asked the owner whether to approve the smaller per-customer route-time method instead. Do not silently implement a hull.

Adapter authoring decision B06: AI-assisted, manually inspected standard-library adapters derived from the pinned official OpenAPI specifications. Read specifications as data only. No third-party generator.

Build coordinator decision B07: no persistent cache; output directory defaults to reports/run and contains report.json, report.md and evidence artifacts. Refuse an existing output directory. Socket timeout 10 seconds, whole acquisition deadline 120 seconds, at most 60 HTTP attempts, three attempts per request, backoffs 1 and 2 seconds, at most five isoline polls spaced one second apart, response cap 2 MiB, geometry cap 2,000 total vertices and 32 rings. Retry only transport failures, 429 and 5xx within the deadline. Bound Retry-After and stop when it cannot fit. These are implementation budgets, not account-entitlement claims.

## Specification retrieval

The first spec-catalog request failed in zsh because its URL query was unquoted. Quoting the URL fixed it; the pinned catalog and 18 JSON spec files downloaded successfully as data. Their hashes are in docs/api-provenance.md. Public MCP documentation lists eleven tools, contrary to the prompt's twelve. The official category enum has no plumber/plumbing entry; the fixture uses broad `service` candidates with an explicit limitation. No live category claim was manufactured.

## Fixture authoring

The first locally authored fixture-generation helper failed with `TypeError: feature() got multiple values for argument 'name'`: its positional formatted-address parameter collided with the optional place name keyword. Renamed the helper parameter to `address`; re-running generated the twenty-row fixture and input CSV successfully. This is a genuine build failure, not a deliberately failing product test. The helper is not shipped; fixtures retain authored-synthetic provenance.

## First integrated verification

The geometry subtask completed with 48 tests and 30,000 independent oracle checks; no geometry-test failures were reported. The first integrated suite passed 76 tests on Python 3.14.9. A full twenty-row replay published both reports and evidence. Processing/rendering over twenty iterations had a 0.010481-second median with a five-position synthetic zone. The fixture produced 13 in-zone, 7 outside, 2 borderline and 2 disagreements. Generated golden reports were saved separately from authored response fixtures for review and byte regression checks.

Read official Claude, Codex and Cursor configuration references; recorded installed Codex 0.163.0 and Claude Code 2.1.308 versions. Cursor was not on PATH. No client was connected to Geoapify. B02/B03 questions remain pending; agent instructions and importer fail at the unresolved method gate rather than inventing approval. The report component's independent test work continues.

## Integration failure and fix

The first expanded 125-test run failed when a competitor lacked a provider ID. Acquisition hashed pretty-printed JSON for the fallback identity, while the shared validator required compact canonical coordinate/name JSON. Standardized acquisition on the schema's compact UTF-8 form. The failing end-to-end test is retained; this was a genuine integration defect found by a newly added negative case.

## Privacy pre-push scan

The first broad scan flagged two synthetic negative URL fixtures in test_report.py: a userinfo URL resembled an email and a file URL contained a temporary-directory path. Neither was personal data or a real secret. Replaced those fixtures with equivalent nonpersonal rejection cases so the required zero-pattern sweep can remain literal. Nothing was pushed after the failed scan.

Recheck after the canonical-ID fix and negative-URL fixture adjustment: all 125 tests passed; the 39-file working-tree and reachable-history privacy sweep passed; stdlib-only import inspection, syntax compilation and diff whitespace checks passed. Python 3.15.1, Linux/Windows and live runs remain pending.

## Report module handoff

The report subtask finished 47 focused tests and 1,155 malformed-input checks. Its adversarial check found that datetime parsing alone accepted the invalid time `24:00:00`; explicit timestamp range checks fixed it and the regression is retained. Determinism, every-field Markdown parity, output rollback and privacy checks passed. Final integration also distinguishes absent matrix measurement fields as errors rather than no-route; all 126 tests passed after that addition.

## Sol PR review round 1

Reviewed implementation commit 4342973 with gpt-6.1-sol, reasoningEffort=xhigh. Sol posted three P2 findings on PR 2: absent optional snapped matrix coordinates erased all route measurements; blank competitor category metadata escaped normalization and aborted publication; Isoline normalization stripped CRS declarations before geometry validation. Accepted all three; no disputes.

Added no-network CLI regressions before fixing them. Seven assertions failed, reproducing the matrix loss, malformed category/ID publication failure and three CRS envelope levels. Changed matrix validation to check snapped locations only when present; original locations and index matching stay required. Candidate text now satisfies the shared nonblank/UTF-8 rules before records are appended, with invalid records counted as unclassified. Collection/feature/geometry CRS declarations are rejected before normalization. The expanded suite passed all 130 tests on Python 3.14.9, including malformed Unicode candidate metadata and present-but-invalid snapped coordinates.

The clean committed snapshot before round 1 also passed all 126 then-current tests and a full twenty-row replay whose JSON/Markdown matched the golden files. No live requests, installs or CI runs occurred. Python 3.15.1 and B01–B04 remain pending.

## Sol re-review provider failure

The first round 2 invocation failed with `Provider turn failed` before returning a review. Confirmed that no round 2 PR review comment was posted. This is an orchestration failure, not a clean review or a product-test failure. Retrying the required Sol review with the prior findings and fixes supplied explicitly.

## Sol PR review round 2

The retry completed against c571f17. Sol verified all three round 1 fixes and found two new P2 defects: strict evidence serialization promoted malformed customer/matrix data into whole-run failure, and both category regexes rejected the supported `catering.restaurant.tex-mex`. Accepted both; no disputes. Three new end-to-end regressions failed before fixes.

Capture now converts rejected evidence into a scoped acquisition error without adding an artifact or reference. Matrix artifacts explicitly retain normalized indexed measurements and routing settings, with invalid cells marked error/null; valid cells and polygon verdicts survive. They do not retain malformed values or unrelated provider metadata. CLI and report category validation now share exact membership in the pinned official snapshot. Unknown and multiple categories remain rejected.

The first full check after these changes passed the new regressions but failed the golden comparison because the normalized matrix artifact changed its evidence hash. Verified programmatically that this single hash was the only report-value change, then refreshed both golden reports. Added mocked HTTP transport regressions as well as CLI replays for lone-surrogate customer text and a `1e309` matrix measurement. All 134 tests passed on Python 3.14.9; all 833 snapshot values pass preflight. No network, live key, installs or CI runs were used for these tests.
