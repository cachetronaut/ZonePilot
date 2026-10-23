# ZonePilot

ZonePilot helps a single-location service business review a 5–60 minute outbound driving budget. It geocodes addresses, obtains a road-network Isoline polygon, classifies points locally, measures routes and optionally observes category-based competitors. JSON and Markdown come from one validated schema.

Built for the [Geoapify Open Geospatial Program](https://geoapify.com). This repository remains private. The internal target is November 8, 2026; submission is due November 15.

## Current status

The offline CLI is implemented with stock Python and zero dependencies. No pip installation or build step is needed. Minimum supported Python is 3.14.9; the build/test target is 3.15.1. Local execution has used Python 3.14.9 on macOS arm64. Python 3.15.1 is not installed here; target-runtime and Linux/Windows checks are PENDING.

Live runs are PENDING: GEOAPIFY_API_KEY was absent during this build. Synthetic fixtures are authored examples, not recorded successful API calls. B01 account entitlement, B02 agent method approval, B03 permitted live sample/evidence, and B04 authenticated client proof remain open. See [build decisions](docs/build-decisions.md), [local evidence](docs/evidence/local-checks.md) and the [PRD](docs/prd.md).

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

## Live run contract, pending approved inputs

Before running live, close PRD B01 and B03. `data/sample_business.json` and `data/sample_customers.csv` are intentionally pending because the PRD reserves those paths for approved live-demo inputs. Do not present the offline fixture as geocodable live data.

Once approved, the command shape is:

```sh
python3.15 -m zonepilot.cli --business-address '<approved fictional address>' --business-name 'Main Street Plumbing' --minutes 20 --customers data/sample_customers.csv --competitor-category service --output-dir reports/live-demo
```

This shape is not a runnable approved sample. `service` is a broad category, not a verified plumbing category. The official snapshot contains no plumber/plumbing entry. Choose a supported category deliberately and keep the limitation visible.

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

Only a unique building candidate with both confidence measures at least 0.95 is accepted. Unresolved customers remain visible. Polygon/MultiPolygon membership includes every exterior and hole boundary within 1e-9 degrees; strict hole interiors are outside. Geometry validation rejects malformed topology, ambiguous touching rings/components, antimeridian spans, latitudes beyond 85 degrees, and shapes above 2,000 positions or 32 rings.

The authoritative CLI verdict is local polygon membership. Measured time supplies separate within-budget, borderline and disagreement fields. Borderline means strictly over the budget and at most 110 percent of it. Missing route data is null, never zero. The model uses free-flow, balanced, outbound driving without avoid options. It does not estimate congestion, return travel, profit or prices.

FR-18 requires a Places bounding-rectangle search with local membership filtering, even though the API also supports POST polygon filters. One search retrieves at most twenty candidates without pagination. Coverage remains sampled even below the cap. Duplicates and unclassified records are counted. Distances to competitors are great-circle metres, not road distances. No complete market census is claimed.

Requests use a 10-second socket timeout, 120-second run deadline and 60-attempt cap. Each request allows three attempts, only for transport errors, HTTP 429 or 5xx, with 1/2-second backoff and bounded Retry-After. Isoline allows five one-second polls. Responses are capped at 2 MiB. Authentication errors stop the run. There is no persistent cache and no speculative route fallback for arbitrary matrix failures.

## Hosted agent pack

[Client snippets](zonepilot/agent/README.md) cover Claude Code, Codex CLI and Cursor with environment-backed headers. [Sequenced prompts](zonepilot/agent/prompts.md) name all nine promised tools, normalization, diagnostic geometry, comparison and export steps. Every MCP output labels the approximation.

The PRD requires an approved approximation contract before execution. The requested sampled-boundary method is not yet approved; the importer fails safely while B02 is open. The proposed smaller route-time-at-points method is not silently enabled. Agent import makes no network calls:

```sh
python3.15 -m zonepilot.report --import-agent evidence.json --output-dir reports/agent
```

This currently returns the method-pending diagnostic for otherwise valid MCP input. It is not a completed Stage 3 acceptance check. AI clients and subscriptions are separate prerequisites, outside the zero-dependency Python claim.

## Manual acceptance checklist

The [test record](docs/evidence/local-checks.md) maps tested cases and pending gates. CI is intentionally skipped; PR titles include `[skip ci]`.

- [x] Offline input validation and no-network preflight/replay: FR-01–03, FR-05–06, AC-01.
- [x] Conservative geocoding and geometry cases: FR-07–11, AC-02–03.
- [x] Indexed matrix, nullable routes, borderline and disagreements: FR-14–16, AC-04.
- [x] Category validation and bounded sampled competitor handling: FR-17–19, AC-05.
- [x] Shared strict reports, aggregation, escaping and deterministic publication: FR-13, FR-20–23, AC-06.
- [x] Incremental [PROMPTLOG.md](PROMPTLOG.md): FR-27, CR-12. Genuine build failures are distinguished from controlled negative tests.
- [ ] Approved twenty-customer live sample and live run: FR-04, AC-08, B01/B03.
- [ ] Approved agent method, full comparison, nine hosted calls and second-client smoke: FR-12, FR-25–26, AC-07, B02/B04.
- [ ] Authenticated setup/screenshots, tutorial feedback and evidence: FR-28, AC-10.
- [ ] Python 3.15.1 and Linux/Windows command verification: NFR-06, AC-09. Python 3.14.9 macOS verified.
- [ ] Final [tutorial](TUTORIAL.md), dev.to URL and synchronized revision: CR-06–08, CR-13–14, CR-17, AC-10.
- [ ] Owner-controlled public release, final license-holder confirmation and submission sweep: CR-03, NFR-09, AC-11. Repository stays private.

[Schema](docs/report-schema.md) · [API provenance](docs/api-provenance.md) · [PRD review log](docs/prd-review-log.md)

Project code is MIT, retaining the existing cachetronaut copyright. Geoapify and [OpenStreetMap contributors](https://www.openstreetmap.org/copyright) have separate data attribution. Synthetic fixtures contain no live map records. Geoapify may publish an adapted tutorial with credit to Scout Squad when the tutorial and its evidence pass the publication gates.
