# ZonePilot

ZonePilot helps a single-location service business review a 5–60 minute outbound driving budget. It geocodes addresses, obtains a road-network Isoline polygon, classifies points locally, measures routes and optionally observes category-based competitors. JSON and Markdown come from one validated schema.

Built for the [Geoapify Open Geospatial Program](https://geoapify.com). The [repository](https://github.com/cachetronaut/ZonePilot) is public as of November 2, 2026. The internal target is November 8, 2026; submission is due November 15.

## Current status

The offline CLI is implemented with stock Python and zero dependencies. No pip installation or build step is needed. Minimum supported Python is 3.14.9; the build/test target is 3.15.1. Local execution has used Python 3.14.9 on macOS arm64. Python 3.15.1 is not installed here; target-runtime and Linux/Windows checks are PENDING.

Stage 4 live reports on October 23, 2026 evaluated all twenty fictional customer identities at labeled public Midland demo locations. Both paths classified 20/20 in zone (100%), with median in-zone drive time 488 seconds (8m 8s). The farthest was DEMO-12 at 1,085 seconds (18m 5s), 21,635 metres; no customer was outside or borderline. Sampled broad-service candidates: CLI 19 in zone, MCP 20. These are not verified plumbing competitors. [Live comparison and row-level evidence](docs/evidence/stage4/live/comparison.md).

Claude Code 2.1.309 completed all nine hosted tools; Codex CLI 0.163.0 passed a separate geocode smoke call. MCP is always `approximation=true`: route-time classification only at measured points; no continuous zone. [Evidence index](docs/evidence/stage4/README.md) preserves earlier failures separately from successful reports and offline fixtures.

The recreated public repository was verified on November 2, 2026 at release HEAD `a17946fc491d58a81556c3654b3d3a091a9963a1`. Only `main` was pushed; no old PR or audit refs were transferred. Fresh private and anonymous public clones passed the corrected privacy scan, with four commits, 205 reachable objects and 190 files. Four 32-hex matches were ID fields, not credentials. Credential candidates were environment references or synthetic test values. MIT was unchanged and the recreated repository had no pull requests. The actual Geoapify key was not read; the October 23 exact-key scan is historical evidence, not a new exact-key check. Subsequent documentation reconciliation preserves that implementation revision.

Screenshots, Python 3.15.1 and Linux/Windows checks, live outcome diversity and final acceptance remain pending. The dev.to draft is unpublished and optional under the November 2 owner instruction. The submission email remains unsent. See the [submission pack](SUBMISSION.md) and [public tutorial](TUTORIAL.md).

## Reproduce the offline example

Use this machine's trusted interpreter at the stated version. The commands below use the target interpreter name. On a machine with the minimum version installed instead, replace `python3.15` with `python3.14` and confirm it reports 3.14.9 or later.

```sh
git clone https://github.com/cachetronaut/ZonePilot.git
cd ZonePilot
python3.15 --version
python3.15 -m unittest discover -s tests
python3.15 -m zonepilot.cli --replay tests/fixtures/sample/run.json --output-dir reports/demo
```

Open `reports/demo/report.json` and `reports/demo/report.md`. The bundle also contains the referenced synthetic evidence with SHA-256 hashes. Pick a fresh output directory for each run; an existing directory is never overwritten. The clock, response order and inputs are fixed, so repeated replay produces identical report bytes. Replay never reads a key or opens a network connection.

The fixture is Main Street Plumbing, Midland TX with twenty fictional customers on Imaginary Fixture Lane. It exercises inside, outside, boundary, borderline, disagreement, zero-time and tied-maximum cases. Its simple authored rectangle is not a real road-time zone. Live execution requires a real Geoapify Isoline response. See [fixture provenance](tests/fixtures/sample/README.md).

## Live run contract

[Demo provenance](data/README.md) identifies real public locations used for fictional identities. Main Street Plumbing is fictional and is not based at City Hall; `300 N Loraine St, Midland, TX 79701` is only its demo origin. No public location is an actual customer or affiliated with this project. `data/sample_business.json` records settings and labeling; `data/sample_customers.csv` contains twenty fictional customer names/references at the approved demo addresses.

Set `GEOAPIFY_API_KEY` in the process environment through your trusted secret-entry method before a live run. Do not place its value in a file or command argument:

```sh
set +x
python3.14 -B -m zonepilot.cli --business-address '300 N Loraine St, Midland, TX 79701' --business-name 'Main Street Plumbing' --minutes 20 --customers data/sample_customers.csv --competitor-category service --output-dir reports/live-demo
unset GEOAPIFY_API_KEY
```

Use an installed supported interpreter; no installation is required. The recorded run exited 0 and published `report.json`, `report.md` and hashed evidence. Read the [live report](docs/evidence/stage4/live/cli/report.md) and [comparison](docs/evidence/stage4/live/comparison.md). Both searches are capped at twenty, without pagination; `service` is broad and does not identify verified plumbing competitors. Live values can change with upstream data.

The earlier invented origin failed with `origin_unresolved`; [historical evidence](docs/evidence/stage4/live-cli.json) is retained. It is not the current sample. The final real sample has no outside or borderline customer, so those branches remain demonstrated by the authored offline fixture rather than claimed as live outcomes.

The fresh-clone Stage 4 check is recorded in the [evidence index](docs/evidence/stage4/README.md). That October 23 runtime check is historical evidence. Clone `main` from the recreated public repository for the published files; no old PR branches exist there.

Set the key only in the process environment. For POSIX shells, this masked prompt passes the secret directly into the process environment without putting a literal key in shell history:

```sh
export GEOAPIFY_API_KEY="$(python3.15 -c 'import getpass; print(getpass.getpass("Geoapify key: "))')"
```

For PowerShell, using the installed target Python version:

```powershell
py -3.15 --version
$env:GEOAPIFY_API_KEY = py -3.15 -c 'import getpass; print(getpass.getpass("Geoapify key: "))'
py -3.15 -m unittest discover -s tests
py -3.15 -m zonepilot.cli --replay tests/fixtures/sample/run.json --output-dir reports/demo
```

Do not run shell tracing while entering credentials. Never place a key in a URL, command argument, CSV, config literal or prompt. Missing/blank keys produce a clean setup message before any network call. Reports and errors never print raw API error bodies or request URLs.

The CSV accepts UTF-8 with optional BOM. Required header is `address`; optional headers are `name` and `reference`. Unknown/duplicate headers, blank addresses, malformed CSV and batches outside 1–20 records fail preflight. Quoted commas and newlines work. Duplicate customers remain separate rows. A one-row CSV screens a single inquiry. Lookup trims address edges while reports preserve the supplied value. Names/references are not sent to geocoding. Omitted business name becomes `Business`.

Output defaults to `reports/run/report.json`, `reports/run/report.md` and `reports/run/evidence/`. Local validation checks output access before network use. Both reports and evidence are staged, then published together as a new directory. Failed global runs publish no report pair. Exits are 0 complete, 1 acquisition/report failure, 2 invalid setup/input, and 3 partial evidence.

## Interpretation and limits

Only a unique building candidate with both confidence measures at least 0.95 is accepted. Unresolved customers remain visible. Polygon/MultiPolygon membership includes every exterior and hole boundary within 1e-9 degrees; strict hole interiors are outside. Geometry validation rejects malformed topology, ambiguous touching rings/components, antimeridian spans, latitudes beyond 85 degrees, and shapes above 20,000 positions or 32 rings, or a 2,000,000-pair topology-work budget. [Full live geometry contract](docs/live-geometry-contract.md).

The authoritative CLI verdict is local polygon membership. Measured time supplies separate within-budget, borderline and disagreement fields. Borderline means strictly over the budget and at most 110 percent of it. Missing route data is null, never zero. The model uses free-flow, balanced, outbound driving without avoid options. It does not estimate congestion, return travel, profit or prices.

FR-18 requires a Places bounding-rectangle search with local membership filtering, even though the API also supports POST polygon filters. One search retrieves at most twenty candidates without pagination. Coverage remains sampled even below the cap. Duplicates and unclassified records are counted. Distances to competitors are great-circle metres, not road distances. No complete market census is claimed.

Requests use a 10-second socket timeout, 120-second run deadline and 60-attempt cap. Each request allows three attempts, only for transport errors, HTTP 429 or 5xx, with 1/2-second backoff and bounded Retry-After. Isoline allows five one-second polls. Responses are capped at 2 MiB. Authentication errors stop the run. There is no persistent cache and no speculative route fallback for arbitrary matrix failures.

## Hosted agent pack

[Client snippets](zonepilot/agent/README.md) cover Claude Code, Codex CLI and Cursor with environment-backed headers. [Sequenced prompts](zonepilot/agent/prompts.md) name all nine promised tools, normalization, diagnostic geometry, comparison and export steps. Every MCP output labels the approximation.

The owner approved `route_time_at_points`: known outbound time at or below the budget is in zone, larger known time is outside, and unknown routes have unknown membership. It classifies supplied customer points only, with no continuous polygon. Every agent report retains `approximation=true` and the required no-continuous-zone limitation. Sampled-boundary methods remain rejected. Requested MCP competitors use the [approved evidence contract](docs/mcp-competitor-contract.md): one 20,000-metre circle search, acquired outbound routes for unique valid candidates and import-time checks of counts/records. The circle determines only the candidate extent. Agent import makes no network calls:

```sh
python3.15 -m zonepilot.report --import-agent evidence.json --output-dir reports/agent
```

The importer accepts valid acquired point-time evidence without a key and writes both reports. The [live hosted bundle](docs/evidence/stage4/live/mcp/report.md) was produced by this keyless importer from captured client results, with no REST measurements substituted. AI clients and subscriptions are separate prerequisites, outside the zero-dependency Python claim.

## Manual acceptance checklist

The [test record](docs/evidence/local-checks.md) maps tested cases and pending gates. CI is intentionally skipped. The November 2 publication checks inspected Git objects and documents without running project or third-party code.

- [x] Offline input validation and no-network preflight/replay: FR-01–03, FR-05–06, AC-01.
- [x] Conservative geocoding and geometry cases: FR-07–11, AC-02–03.
- [x] Indexed matrix, nullable routes, borderline and disagreements: FR-14–16, AC-04.
- [x] Category validation and bounded sampled competitor handling: FR-17–19, AC-05.
- [x] Shared strict reports, aggregation, escaping and deterministic publication: FR-13, FR-20–23, AC-06.
- [x] Incremental [PROMPTLOG.md](PROMPTLOG.md): FR-27, CR-12. Genuine build failures are distinguished from controlled negative tests.
- [x] Approved labeled twenty-customer live sample and complete run: FR-04 input artifact and AC-08 execution portion, B01/B03. Full AC-08 acceptance retains the outcome-diversity gap below. [CLI report](docs/evidence/stage4/live/cli/report.md): 20 evaluated, 100% in zone, 488-second median; 25 HTTP attempts, no Isoline polling. Billed credits were not available.
- [ ] FR-04 live outcome diversity: this run has zero outside/borderline customers. Those cases pass in synthetic fixtures only; no live result was manufactured.
- [x] Owner-approved point-time method and sampled MCP competitor contract: FR-12, B02.
- [x] Complete identical-input comparison, all nine hosted tools and second-client smoke: FR-25–26, AC-07, B04. [MCP comparison, approximation=true](docs/evidence/stage4/live/comparison.md); [Codex success](docs/evidence/stage4/live/codex-smoke-approved.json).
- [ ] Actual credential-free setup screenshots in both clients: FR-28, AC-10, CR-14. Live text/config evidence is present; screenshots remain owner handoff.
- [x] Historical October 23 [fresh remote clone check](docs/evidence/stage4/live/fresh-clone.json), revision `4a250b7`: 156 tests, byte-identical synthetic and captured MCP reports, successful live CLI with the same 20/20 in-zone result and 488-second median. PR branch selected before merge; temporary clone removed.
- [ ] Python 3.15.1 and Linux/Windows command verification: NFR-06, AC-09. Current verified runtime is macOS Python 3.14.9.
- [x] [Tutorial](TUTORIAL.md) with setup, live comparison, three evidenced failures, lessons and Geoapify feedback; [dev.to draft](docs/drafts/devto.md) saved locally. Both README and tutorial link to geoapify.com.
- [x] Public repository and anonymous clean clone verified November 2, 2026; unchanged MIT and release implementation revision recorded above.
- [ ] Final program acceptance, screenshots, runtime/platform verification and submission email. Optional dev.to draft remains unpublished. [SUBMISSION.md](SUBMISSION.md) maps every Section 8 item.
- [x] Publication repository recreated and populated with clean `main` history only. Fresh private/public clone scans passed; PR list empty. The [October 23 scan](docs/evidence/stage4/privacy-scan.json) describes the deleted repository and local retained audit objects, not the recreated remote.

[Schema](docs/report-schema.md) · [API provenance](docs/api-provenance.md) · [PRD review log](docs/prd-review-log.md)

Project code is MIT, retaining the existing cachetronaut copyright. Geoapify and [OpenStreetMap contributors](https://www.openstreetmap.org/copyright) have separate data attribution. Synthetic fixtures contain no live map records. Geoapify may publish an adapted tutorial with credit to Cachetronaut when the tutorial and its evidence pass the publication gates.
