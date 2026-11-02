# ZonePilot: testing a service-area CLI beside a hosted MCP agent

The completed live CLI and hosted MCP reports both put all twenty demo customers inside a twenty-minute outbound driving budget. The median in-zone trip was 488 seconds, or 8m 8s. The CLI used a real REST Isoline polygon; hosted MCP used `route_time_at_points`, with `approximation=true`. Matching customer results do not make those methods equivalent.

This October 23, 2026 work record is the repository tutorial for the [Geoapify Open Geospatial Program](https://geoapify.com), Batch #2. The [repository](https://github.com/cachetronaut/ZonePilot) is public as of November 2, 2026. The internal target is November 8 and the final deadline is November 15. Public release and anonymous clean-clone privacy verification are complete. Screenshots, portability checks and final submission remain pending.

Main Street Plumbing and all twenty customer identities are fictional. Their addresses are real public demo locations in Midland, Texas, approved by the owner under the [PRD amendment](docs/prd.md#owner-amendment-for-stage-4-2026-10-23). The origin is City Hall at 300 N Loraine St. No affiliation, business tenancy or actual customer relationship is implied. [Data provenance](data/README.md) records the locations and sources. Provider results remain labeled live-derived; offline fixtures remain authored synthetic data.

ZonePilot records evidence for a service business's serve, decline or reprice decision. It does not calculate profit, set prices, predict traffic or include the return trip.

## Start with the contracts

The [PRD](docs/prd.md) records the original scope and October 23 owner amendment. The November 2 publication instruction supersedes its private-release gate and makes dev.to publication optional. The adapters were handwritten with AI assistance from Geoapify's OpenAPI specifications at revision `dd07a5f8faafab533b067d5de6edeeda04daa5a3`. [API provenance](docs/api-provenance.md) records the selected schemas and hashes. No third-party generator or dependency installation was used.

The product and offline tests use Python's standard library. Both paths feed the [same report schema](docs/report-schema.md), local aggregation and paired JSON/Markdown renderer. The CLI's local polygon membership remains authoritative for its report. MCP classifies only measured points by their outbound time and always carries `approximation=true`. Route-time classification only at measured points; no continuous zone. A search radius never determines zone membership.

The [prompt log](PROMPTLOG.md) starts before implementation and retains failed attempts and corrections. The [local check record](docs/evidence/local-checks.md) distinguishes genuine build defects from deliberate negative tests. Earlier records describe the inputs and code available at those dates, not the final live result below.

## Reproduce the CLI

Use an already-installed trusted Python 3.14.9 or later. Python 3.15.1 is the target; verification on that version, Linux and Windows remains pending. Recorded local execution used Python 3.14.9 on macOS arm64. There is no install or build step.

```sh
git clone https://github.com/cachetronaut/ZonePilot.git
cd ZonePilot
python3.14 --version
python3.14 -B -m unittest discover -s tests
python3.14 -B -m zonepilot.cli --replay tests/fixtures/sample/run.json --output-dir reports/demo
```

The public repository can be cloned without authentication. Use a fresh output directory for each run. Open `reports/demo/report.json` and `reports/demo/report.md`. Replay is keyless and makes no network calls. Its synthetic fixture has thirteen inside, seven outside, two borderline customers and an in-zone median of 800 seconds. Those values are test data, not the live results.

The [current fresh remote clone](docs/evidence/stage4/live/fresh-clone.json), revision `4a250b7`, passed all 156 tests and reproduced the synthetic golden reports and captured MCP reports byte for byte. Its live CLI run reproduced the twenty-customer results below with 24 HTTP attempts and no Isoline polling. Before merge the check selected the PR branch; all runtime commands match README. The temporary clone was removed. Integrated checks also passed; [geometry regression evidence](docs/live-geometry-contract.md#regression-evidence-and-integration) explains the added coverage.

For a new live run, supply `GEOAPIFY_API_KEY` through the process environment using the [README's credential instructions](README.md). Keep shell tracing off and keep the key out of prompts, URLs and configuration literals. The approved command is:

```sh
python3.14 -B -m zonepilot.cli --business-address '300 N Loraine St, Midland, TX 79701' --business-name 'Main Street Plumbing' --minutes 20 --customers data/sample_customers.csv --competitor-category service --output-dir reports/live-demo
```

The recorded run produced [CLI JSON](docs/evidence/stage4/live/cli/report.json) and [CLI Markdown](docs/evidence/stage4/live/cli/report.md). Its settings are outbound driving, free-flow traffic, balanced routes, metric units and a 1,200-second budget. New requests may produce different provider results. Names and references are not sent to geocoding.

The geocode policy still requires exactly one eligible building candidate, valid coordinates, and both confidence measures at least 0.95. The final sample did not require lowering those thresholds. Full Isoline geometry determines membership, including holes and boundaries. The [geometry contract](docs/live-geometry-contract.md) documents the 20,000-position, 32-ring and 2,000,000 segment-pair work limits. The saved live response has 14,758 positions across three rings; validation preserves the complete geometry.

## Run the hosted MCP workflow

All MCP analysis uses `approximation=true`. Route-time classification only at measured points; no continuous zone. An installed, authenticated AI client is a separate prerequisite. Recorded clients were Claude Code 2.1.309 and Codex CLI 0.163.0. No persistent client configuration was changed and no client was installed for these runs.

Follow the [agent pack](zonepilot/agent/README.md) and [prompt sequence](zonepilot/agent/prompts.md). Both clients use `https://api.geoapify.com/v1/mcp` with an environment-backed `x-api-key` header. The recorded Claude configuration was supplied for the session:

```json
{
  "mcpServers": {
    "geoapify": {
      "type": "http",
      "url": "https://api.geoapify.com/v1/mcp",
      "headers": {"x-api-key": "${GEOAPIFY_API_KEY}"}
    }
  }
}
```

The successful Codex smoke used this scoped configuration through a temporary command override, with no configuration file saved:

```toml
[mcp_servers.geoapify]
url = "https://api.geoapify.com/v1/mcp"
env_http_headers = { "x-api-key" = "GEOAPIFY_API_KEY" }
enabled_tools = ["geocode_address"]
required = true
startup_timeout_sec = 20
tool_timeout_sec = 20

[mcp_servers.geoapify.tools.geocode_address]
approval_mode = "approve"
```

This approval covers the owner's authorized geocode smoke only. It does not authorize every tool. The [successful Codex record](docs/evidence/stage4/live/codex-smoke-approved.json) contains one completed hosted geocode. The [preceding failure](docs/evidence/stage4/live/codex-smoke.json) retains the actual error, `MCP tool call requires approval, but approval policy is never`. The scoped override resolved that noninteractive policy conflict. Older smoke failures remain in the [evidence index](docs/evidence/stage4/README.md).

Claude's full acquisition spans three captured sessions:

- [Preflight](docs/evidence/stage4/live/mcp-preflight.json): seven successful calls for the accepted origin, reverse geocode, category list and four geometry diagnostics.
- [Customer session](docs/evidence/stage4/live/mcp-customers.json): twenty geocodes, a preliminary nineteen-target customer matrix, one route diagnostic, one Places search and one competitor matrix, totaling 24 successful tool calls. Row 4's geocode was rejected for an address discrepancy despite tool success.
- [Final customers](docs/evidence/stage4/live/mcp-final-customers.json): two successful calls for the replacement row 4 geocode and final twenty-target customer matrix. This matrix supersedes the preliminary nineteen-target matrix.

These captures evidence all nine required tools. The [submission matrix](SUBMISSION.md#nine-tool-evidence-matrix) links each tool to its purpose. Geometry calls operate on an authored diagnostic polygon; they do not create a road-time zone. The authenticated inventory contains twelve tools, including `get_timezone`, and no isoline tool.

Claude exposes the hosted structured result as JSON text in tool-result content, not as a separate `structuredContent` field in its captured stream. The deterministic [normalizer](docs/evidence/stage4/normalize_mcp.py) parses that JSON and validates captured arguments, typed results, row mapping and evidence references. Assistant prose is not the measurement source. The [normalized import bundle](docs/evidence/stage4/live/agent-input/evidence.json) feeds the keyless report importer:

```sh
python3.14 -B -m zonepilot.report --import-agent docs/evidence/stage4/live/agent-input/evidence.json --output-dir reports/agent
```

To rebuild the import bundle from the saved captures, choose new output directories:

```sh
python3.14 -B -m docs.evidence.stage4.normalize_mcp --output-dir reports/mcp-input
python3.14 -B -m zonepilot.report --import-agent reports/mcp-input/evidence.json --output-dir reports/agent-rebuilt
```

These commands acquire no new evidence and require no key. The resulting [MCP JSON](docs/evidence/stage4/live/mcp/report.json) and [MCP Markdown](docs/evidence/stage4/live/mcp/report.md) retain `approximation=true` and the no-continuous-zone limitation.

## Compare the final identical inputs

Both reports use the revised twenty-row CSV, the City Hall demo origin and the same routing settings. The [comparison record](docs/evidence/stage4/live/comparison.json) retains input hashes and every row's comparison.

| Evidence | Live CLI | Hosted MCP, approximation=true |
| --- | --- | --- |
| Membership method | REST Isoline plus local point-in-polygon | Route-time threshold at measured points; no continuous zone |
| Resolved customers and known routes | 20 of 20; 20 of 20 | 20 of 20; 20 of 20 |
| Customers inside | 20 of 20 classified, 100% | 20 of 20 classified, 100% |
| Customers outside / borderline | 0 / 0 | 0 / 0 |
| Median in-zone time | 488 seconds, 8m 8s | 488 seconds, 8m 8s |
| Maximum customer time | 1,085 seconds, 18m 5s, row 12 | 1,085 seconds, 18m 5s, row 12 |
| Broad service candidates returned | 20 | 20 |
| Candidate classifications, inside / outside | 19 / 1 | 20 / 0 |
| Candidate search extent | Isoline bounding rectangle | 20,000-metre circle centered on origin |
| Coverage / cap reached | `sampled` / `true` | `sampled` / `true` |

Row 12 is `DEMO-12`, 9600 Wright Dr, with a measured driving distance of 21,635 metres. There are no outside or borderline customer outliers in this live sample. FR-04's outcome diversity is demonstrated only by the offline fixture; the live sample does not establish that part of FR-04 or AC-08. The owner's private Stage 4 completion decision allows the actual results with a clean Sol review; it does not turn these missing live outcomes into passes.

All final customer coordinates, matrix times and verdicts agree across paths. The separate single-route diagnostic for row 1 returned 81.539 seconds against its 81-second matrix cell, a 0.539-second difference. That diagnostic did not replace the matrix value.

Competitor observations differ. Each path makes one capped search with no pagination, but the extents and membership methods differ. Only two in-zone candidate IDs overlap. The circle is a candidate search extent, never a service-area boundary. Broad `service` places are not verified plumbing competitors, and neither count is a market census. The [MCP competitor contract](docs/mcp-competitor-contract.md) requires acquired routes for classification and leaves missing routes unclassified.

## Three real build failures, fixes and rechecks

These three incidents were recorded during the build. Their regression tests preserve encountered defects; they are not invented live incidents.

1. Fallback competitor IDs disagreed. The first integrated 125-test run failed for a candidate without a provider ID. Acquisition hashed pretty-printed JSON while validation expected compact canonical coordinate/name JSON. Using the same compact encoding fixed the mismatch, and all 125 tests passed. See the [failure and fix](PROMPTLOG.md#integration-failure-and-fix) and [recheck](docs/evidence/local-checks.md#integrated-verification-before-pr).
2. Optional matrix snaps erased good routes. Sol reproduced a case where absent optional snapped coordinates caused the entire matrix to be rejected. Validation now checks those coordinates only when present, retaining original-location and index checks. The regression preserves nineteen valid routes; all 130 tests passed after the first review fixes. See [review round 1](PROMPTLOG.md#sol-pr-review-round-1) and its [recheck](docs/evidence/local-checks.md#pr-review-round-1-fixes).
3. A valid taxonomy value failed local validation. Sol found that regexes rejected the supported `catering.restaurant.tex-mex` category. Preflight and report validation now share exact membership in the pinned snapshot. All 833 categories pass preflight, unknown/multiple categories remain rejected, and all 134 tests passed. See [review round 2](PROMPTLOG.md#sol-pr-review-round-2) and its [recheck](docs/evidence/local-checks.md#review-round-2-regression-verification).

## Live work record and lessons

The initial invented origin returned only city-level candidates, so both paths correctly stopped before customer processing. [Earlier live evidence](docs/evidence/stage4/live-cli.json) preserves that failure. The owner then approved real public demonstration addresses with fictional identities. Authentication success alone had not established a usable sample.

The first live CLI attempt with the approved origin reached Isoline but hit the old 2,000-position cap. The [saved diagnostic](docs/evidence/stage4/live/isoline-diagnostic.json) contains the full 14,758-position, three-ring response. The revised validator accepts the full geometry under the [bounded contract](docs/live-geometry-contract.md), without simplification, dropped holes or weaker topology checks. The final CLI report records the successful run. Sol xhigh reviewed these changes at `4a250b7` with zero actionable findings; the [review record](docs/evidence/stage4/review.md) links the verification and discussion.

The preliminary row 4 query, 700 S Jackson St, returned 700 South Street through hosted MCP with confidence 1.0. REST returned South Jackson Street. We rejected the hosted match and preserved it in the customer session. The final input explicitly changes row 4 to 2700 FM 1379, and both final reports use that replacement. This is a documented input revision, not a silent correction of provider evidence. Confidence 1.0 did not establish address correctness.

The captured Codex approval failure also remains in the work record beside its successful scoped retry. A client connection and a listed tool do not prove a successful invocation. Keeping the result and the failed attempt makes the setup reproducible.

## Geoapify feedback: the hosted MCP server still has no isoline tool

The authenticated twelve-tool inventory still has no isoline. A hosted tool should accept origin, mode, seconds range and routing settings, then return the full Polygon/MultiPolygon with holes, typed errors and bounded pending-status handling. This would support a closer CLI/MCP comparison. Geometry transforms cannot substitute for road-time acquisition.

The [pinned Places taxonomy](zonepilot/categories.json) has no plumbing category or general trade-services umbrella. Specific categories do exist, including `service.electrician` and `service.carpenter`. `commercial.trade` is not a plumbing-contractor category. A documented plumbing category or supported alternative would improve this use case; broad `service` search results cannot establish plumbing competition.

The recorded hosted South Street/South Jackson discrepancy deserves investigation because its confidence was 1.0. The public MCP table recorded during Stage 4 listed eleven tools while authenticated discovery exposed twelve. Aligning the public inventory with the live server would help reproduction. The Isoline asynchronous 202 documentation/schema gap also needs a typed response contract.

## Publication status and credit

The [submission pack](SUBMISSION.md) maps all seventeen compliance items and the nine required tools. The [dev.to draft](docs/drafts/devto.md) remains unpublished and optional. It preserves the October 23 text and has not been reconciled with this publication update. There is no published dev.to URL and the [email draft](docs/drafts/geoapify-email.md) is UNSENT.

Both client setup screenshots remain an owner handoff. No credential-free authenticated UI was established, so no screenshots were captured. Text configuration snippets do not satisfy CR-14. The owner must capture views with no expanded key, account information, local paths or unrelated windows. If a safe view cannot be established, leave that evidence pending.

On November 2, 2026, the owner-authorized recreated repository was populated with `main` only at `a17946fc491d58a81556c3654b3d3a091a9963a1`. Fresh private and anonymous public clones each contained four commits, 205 reachable objects and 190 files. Their privacy scans passed; four 32-hex strings were ID fields. Reviewed credential candidates were environment references or synthetic sentinels. MIT remained intact, and the recreated repository's PR list was empty. No old PR or audit refs were pushed. The actual key and Mac keychain were not read. The October 23 exact-key scan remains historical evidence.

The [October 23 scan](docs/evidence/stage4/privacy-scan.json) and PR review records describe the former repository. Old PR URLs no longer provide review evidence in the recreated repository; retained local records preserve the historical results. No new runtime tests or CI ran for publication. This docs-only reconciliation leaves the implementation unchanged. Python 3.15.1 and Linux/Windows verification, safe client screenshots, live outcome diversity and final acceptance remain pending. The [submission pack](SUBMISSION.md) records the remaining steps.

Geoapify may publish an adapted completed tutorial with author credit to Scout Squad after the evidence and publication gates pass. Project code retains its existing MIT license and cachetronaut copyright. API services are attributed to [Geoapify](https://geoapify.com), with separate [OpenStreetMap attribution](https://www.openstreetmap.org/copyright) for underlying map data. Capture records identify sanitization and omissions. Sanitized provider results remain live-derived.
