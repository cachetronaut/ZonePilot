# ZonePilot: PRD and technical design

**Product:** ZonePilot

**Owner:** Scout Squad

**Program:** Geoapify Open Geospatial Program, Batch #2

**Final deadline:** November 15, 2026

**Internal finish target:** November 8, 2026

**Project license:** MIT

**Status:** Reviewed design, with explicit pre-build and submission gates in Section 17. This is not evidence that the product has been built or accepted.

## 1. Executive summary

ZonePilot helps a single-location service business decide whether a customer falls within its chosen outbound driving-time budget. It reports evidence for an owner's serve, decline or reprice decision. It does not calculate profit, prescribe a surcharge or guarantee arrival time. Labor cost, job duration, pricing, live traffic and return journeys are outside the model.

The CLI obtains a real road-network drive-time polygon from Geoapify's Isoline API and tests customer points locally. The conversational workflow uses the hosted Geoapify MCP tools. Its zone method is an explicitly labeled approximation because the published MCP inventory has no isoline tool. On 2026-10-23 the owner approved the B02 per-customer route-time method with no continuous polygon; the sampled-boundary alternative remains unapproved. Neither path may substitute a distance circle for a drive-time zone.

Both paths answer the same business question on identical approved inputs and emit one versioned JSON report contract plus its Markdown rendering. The acquisition and membership methods differ; equal verdicts are not guaranteed. Shared local aggregation and rendering make the comparison reproducible. The tutorial must show differences, missing evidence and failures rather than claim computational equivalence.

## 2. Problem and audience

Small service businesses need a repeatable record of which jobs fit their travel budget. A straight-line radius ignores river crossings, divided roads and the road network. ZonePilot supports customer-list review, a single inquiry through a one-row CSV, boundary comparisons across separate runs, and category-based competitor observations.

Primary users are business owners and operations leads. Secondary users are Geoapify reviewers and developers reproducing the OpenAPI plus MCP workflow. Examples must remain about service businesses, delivery zones and customer decisions. Resident access to libraries, clinics, transit or other civic services is excluded by program agreement.

## 3. Design principles

1. Use road-network drive time for the service decision. A candidate-search circle is only a search extent, never zone membership.
2. Share the report contract, aggregation and rendering. Keep REST and hosted MCP acquisition separate and visible.
3. Make fixture replay deterministic, including its clock, order and error states. Treat live API data as changeable.
4. Require only stock Python 3.14.9 or later (build/test target 3.15.1) for ZonePilot and its offline tests. AI clients are separate external prerequisites.
5. Preserve evidence and limitations. Do not hide missing routes, ambiguous geocodes, sampled competitors or blocked acceptance gates.

## 4. Scope and exclusions

The initial release covers one origin, 1–20 customer CSV rows, outbound driving, one optional competitor category, JSON and Markdown reports, and a documented conversational workflow. The bounded batch protects the four-day implementation budget; larger batches and multi-origin optimization are deferred.

No web app, hosted ZonePilot service, local MCP server, resident-access analysis, dispatch, CRM, live traffic, departure-time model or persistent database is included. No automated profitability or pricing model is included. The sample, fixtures, screenshots and published evidence must contain only fictional demonstration data under Section 10.6. No real customer data is allowed in the deliverable.

## 5. Use cases

| ID | Business action | Required evidence |
| --- | --- | --- |
| UC-1 | Review a customer list | Every input row remains visible, including unresolved rows; route and membership states are separate. |
| UC-2 | Screen one inquiry | A one-row CSV uses the same pipeline, schema and errors as a batch. |
| UC-3 | Compare budgets | Separate reports retain their budget and method; the owner compares them manually. |
| UC-4 | Observe competitors | Report the searched category, extent, cap and observed in-zone count; never imply a complete market census. |
| UC-5 | Ask conversationally | Hosted MCP evidence is normalized and rendered using the same report contract; approximation labels remain visible. |

## 6. Functional requirements

Must requirements block submission. Should requirements may be deferred with a recorded reason only if no Must or application commitment depends on them. Could requirements are excluded from the four-day estimate. A blocked Must remains required; a gate is not a waiver.

### 6.1 Inputs

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-01 | Accept `--business-address` and optional `--business-name`. Use the literal display label `Business` when the name is absent. | Must |
| FR-02 | Accept `--minutes` as a whole number from 5 through 60. Reject 61–120 rather than promise undocumented entitlement; any later extension needs verified limits and acceptance updates. | Must |
| FR-03 | Accept `--customers` as UTF-8 CSV, allowing a UTF-8 BOM, with required header `address` and optional `name` and `reference`. Preserve row order and optional values. | Must |
| FR-04 | Ship an approved 20-row fictional sample demonstrating inside, borderline and outside outcomes. Sample selection and live geocodability remain blocked by B03. | Must |
| FR-05 | Collect all discoverable local validation errors before any network call. Identify argument or CSV record/physical line. A parse error that prevents reading later rows is reported as such, not as a complete scan. | Must |
| FR-06 | Live CLI requests read a nonblank `GEOAPIFY_API_KEY` only from the environment. Replay and report rendering need no key and make no network requests. | Must |

Preflight rejects missing/duplicate/unknown headers, malformed CSV, empty or whitespace-only addresses, zero or more than 20 records, and unreadable inputs. Quoted commas/newlines must parse correctly. Preserve duplicate customer rows with distinct one-based `row_id` values; optional references need not be unique. Trim surrounding address whitespace only for lookup. Keep the supplied address separately. Do not send names or references to geocoding. Category syntax and known-category membership are checked against a committed category snapshot before API calls. Record its official category-document or list_place_categories source, retrieval date and checksum in docs/api-provenance.md. Refreshing it is a deliberate build step, not a preflight network request. API-level resolution is not local validation.

### 6.2 Geocoding

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-07 | Resolve the business and retain its input, resolved address, WGS84 coordinates and resolution evidence. Failure or ambiguity aborts the analysis. | Must |
| FR-08 | Resolve each customer independently. No match, ambiguous candidates, invalid coordinates or a request failure leave the record unresolved; continue other records unless a global error occurs. | Must |
| FR-09 | Never silently pick a candidate. Record candidate count, `rank.confidence`, `rank.confidence_building_level`, `rank.match_type` and `result_type` when present. Missing evidence is null. | Must |

Request up to five candidates. ZonePilot's conservative acceptance policy is to resolve only when exactly one returned candidate has `result_type=building`, finite valid coordinates, `rank.confidence >= 0.95`, and `rank.confidence_building_level >= 0.95`. More than one eligible candidate is ambiguous. No eligible candidate with nonempty results is `insufficient_precision`; an empty result is `no_match`. This threshold is a product rule, not a Geoapify guarantee. Pin tests for missing fields and candidates tied at the threshold. A street or city centroid must not silently stand in for a customer's premises. B03 must establish that approved demonstration inputs can satisfy this policy; do not lower it to manufacture success.

### 6.3 Zone and drive measurement

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-10 | CLI requests a single Isoline time range of `minutes * 60`, `mode=drive`, `type=time`, `format=geojson`, `units=metric`, `traffic=free_flow`, `route_type=balanced`, with no avoid options. Validate response range and mode. | Must |
| FR-11 | CLI membership is local point-in-polygon against the full returned Polygon or MultiPolygon under Section 10.3. | Must |
| FR-12 | Hosted MCP uses the B02-approved road-time approximation. Record its name, parameters and limits; do not invent a polygon or silently borrow the CLI polygon for its primary analysis. | Must |
| FR-13 | Every JSON and Markdown file identifies path, zone method, approximation flag and method limitations. | Must |
| FR-14 | Obtain outbound business-to-customer seconds and metres for every resolved customer through Route Matrix or Routing. Keep units and applicable routing settings consistent with FR-10. | Must |
| FR-15 | Attempt measurement for inside and outside customers alike. Record unavailable/no-route values as null, never zero. | Must |
| FR-16 | `borderline=true` exactly when measured seconds satisfy `budget_seconds < time_seconds <= 1.1 * budget_seconds`. Missing time yields null; all other known times yield false. This flag does not replace the membership verdict. | Must |

Use one source and up to 20 explicit targets for the sample matrix. Match cells by source/target index, never by assumed response order. Null or omitted cells affect those customers only. A documented matrix limitation can use individual Routing requests under the same request budget; record the fallback. Both route tools must still appear in the application evidence under Section 8.2.

### 6.4 Competitors

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-17 | Accept optional `--competitor-category`, a single supported Geoapify category. Free-text category inference is excluded. | Must |
| FR-18 | CLI queries Places within the isoline bounding rectangle and applies the same local membership function. MCP searches nearby matching candidates, then uses its approved method to classify them. A search extent is not a zone. | Must |
| FR-19 | Report observed in-zone competitors with name, categories, address, coordinates and geodesic distance in metres, plus search/cap/completeness metadata. Real API evidence publication remains gated by B03. | Must |

For the bounded first release, request at most 20 candidate places once per path, with no pagination. Sort returned candidates by provider ID for stable output, and deduplicate by provider ID; if absent, use exact coordinates plus name. Count discarded duplicates. Do not exclude a result merely because its name matches the origin label. Set `coverage=sampled` for any successful search, even when fewer than 20 results return. Set `cap_reached=true` at 20 returned results. Counts mean observed places only. A failed lookup is `unavailable`, not a count of zero. Keep invalid-coordinate records counted as unclassified. Competitor distance is great-circle distance using the standard-library haversine formula with radius 6,371,008.8 metres, not driving distance. It never determines membership.

REST supports richer polygon filters, but the bounding rectangle plus local filter keeps FR-11 authoritative and avoids payload limits. The MCP tool accepts category and center with optional radius, not the REST polygon interface. Its search extent must be recorded when B02/B03 close. The two paths' candidate sets can differ; report that in the comparison.

### 6.5 Reports and agent evidence

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-20 | Render one validated result object into paired JSON and Markdown files, retaining every Section 11 field in both. | Must |
| FR-21 | Include counts, explicit percentage denominators, known-time aggregates and competitor search state under Section 11. | Must |
| FR-22 | Preserve every customer row with identity, supplied/resolved address, resolution status, membership, route evidence, discrepancy and borderline fields. | Must |
| FR-23 | Include business identity, UTC run time, budget, routing settings, method, data mode, warnings and source attribution. | Must |
| FR-24 | Add ranked farthest-inside and nearest-outside callouts. | Could |
| FR-25 | Document the hosted MCP workflow for both Claude Code and Codex CLI. Capture one full 20-row comparative analysis and smoke evidence from the other client, under B04. | Must |
| FR-26 | Agent exports schema-valid evidence and JSON; local validation, aggregation and rendering produce both standard report formats without acquiring missing API evidence. | Must |
| FR-27 | Maintain an incremental, sanitized prompt log from the first build session, covering CLI generation and MCP work, including failed attempts and corrections. | Must |
| FR-28 | Include versioned setup instructions and sanitized screenshots for both named clients, plus evidence links and Geoapify feedback. | Must |

## 7. Non-functional requirements

| ID | Contract and verification |
| --- | --- |
| NFR-01 | Stock Python 3.14.9 or later (build/test target 3.15.1) and standard library only for product and offline tests; no install, build or third-party executable generation step. |
| NFR-02 | No credentials in tracked content, local report/log output, screenshots or history. Never print request headers, raw exceptions or credential-bearing URLs. Test with synthetic sentinel strings, not real credentials. |
| NFR-03 | Record local processing time for the fixed 20-row fixture benchmark, excluding simulated network delays, with machine/runtime and geometry size. Target under one second on the measured machine; investigate regressions without promising a universal latency bound. |
| NFR-04 | Record failures at their actual scope: customer, competitor section or whole run. Never report a partial run as complete. |
| NFR-05 | Fixed inputs, response fixtures and clock produce byte-identical UTF-8 JSON and Markdown with LF newlines on supported systems. No network, locale or wall-clock dependency in replay. |
| NFR-06 | Verify the documented commands on Python 3.14.9 and Python 3.15.1 on available macOS, Linux and Windows environments; missing platform checks remain pending, not passed. No CI is required. |
| NFR-07 | Plain modules/functions, explicit contracts, reviewed stdlib adapters; no framework or third-party runtime. Type annotations using the standard library are allowed. |
| NFR-08 | Escape Markdown table pipes, line breaks, HTML and link syntax from input/API text so rows cannot alter document structure. Use ordinary headings and labeled units. |
| NFR-09 | MIT license for project code; copyright identity confirmed under B05. Preserve upstream data attribution separately. |

## 8. Program and application compliance

### 8.1 Submission requirements

| ID | Submission-blocking requirement |
| --- | --- |
| CR-01 | Finish internally November 8, 2026; final deadline November 15, 2026. Exactly one fix round of up to seven days is permitted; do not assume another round or an extension. |
| CR-02 | Business-only focus; no resident-access analysis. |
| CR-03 | Public MIT repository at final submission. Keep this review/build repository private until the owner-controlled publication gate. This PR does not authorize a visibility change. |
| CR-04 | README supports the complete sample run and manual test checklist from a clean clone. |
| CR-05 | Environment-only API key sourcing; no key in source, fixtures or committed configuration. |
| CR-06 | Tutorial includes the prompt log and lessons learned. Redactions are explicit, not silent omissions. |
| CR-07 | Both README and tutorial link to [Geoapify](https://geoapify.com). |
| CR-08 | State permission for Geoapify to publish an adapted tutorial with author credit. |
| CR-09 | Deliver the official Combine OpenAPI + MCP track: deterministic spec-derived CLI and conversational hosted MCP workflow for the same business analysis and report contract. |
| CR-10 | Exercise all nine named tools across the four families in Section 8.2 and retain evidence; additionally use real REST Isoline drive-time geometry. |
| CR-11 | CLI service areas are drive-time polygons. A radius-only design cannot pass. |
| CR-12 | Prompt log starts with the first build session and is committed incrementally. Do not reconstruct missing sessions. |
| CR-13 | Tutorial documents at least three genuine encountered failures, each with observed evidence, diagnosis, fix and recheck. Controlled tests are labeled tests, not invented build incidents. Fewer than three real cases means this criterion is pending. |
| CR-14 | Tutorial includes Claude Code and Codex CLI setup screenshots and dedicated Geoapify feedback, including the missing isoline tool. |
| CR-15 | README carries a completed, evidence-linked manual test checklist for Section 13. Pending/blocked checks are not checkmarks. |
| CR-16 | All demonstration data is fictional; live sample and public evidence policy must close B03. Do not erase provenance or relabel real records as fictional. |
| CR-17 | Publish tutorial in the repo at `TUTORIAL.md` and on dev.to. Record the external URL and synchronized revision. |

### 8.2 Nine-tool evidence matrix

The four promised families are geocoding, places, routing and geometry. The hosted inventory currently lists eleven tools; the two extra tools do not replace any promised tool. Successful request/response evidence is required for each row below, with tool name, sanitized arguments, result status, date and tutorial purpose. Synthetic offline responses alone cannot prove a hosted invocation.

| Family | Required tool | Bounded evidence purpose |
| --- | --- | --- |
| Geocoding | `geocode_address` | Resolve approved origin and customer inputs. |
| Geocoding | `reverse_geocode_coordinates` | Check the approved origin coordinate's address context; do not overwrite its accepted forward result. |
| Places | `list_place_categories` | Select and document the approved sample category. |
| Places | `search_places` | Retrieve candidate competitors, with sampling limits visible. |
| Routing | `calculate_route` | Inspect one customer's outbound route and compare its time with a matrix cell. |
| Routing | `calculate_route_matrix` | Measure the one-origin customer batch. |
| Geometry | `transform_geometry` | Calculate the center of a synthetic service-analysis geometry as a diagnostic, not as an isochrone. |
| Geometry | `evaluate_spatial_relation` | Check an interior and exterior synthetic point against that diagnostic polygon; distinguish tool semantics from local boundary rules. |
| Geometry | `measure_geometry` | Measure the same diagnostic polygon's area and record units. |

Geometry diagnostics are a small tutorial exercise separate from the primary MCP zone approximation. They do not justify calling a buffer a drive-time area. Use the pinned operation-specific schemas; require geometry evidence even if competitor results are empty. The full workflow must remain useful, not just a tool checklist.

## 9. Stack and API contracts

### 9.1 Implementation boundary

Use Python 3.14.9 or later (build/test target 3.15.1), `urllib.request`, `json`, `csv`, `argparse`, `math`, `pathlib` and `unittest`. Zero third-party dependencies applies to ZonePilot source and tests, not to preinstalled AI clients or their subscriptions. Do not execute third-party generators or downloaded scripts. The OpenAPI contract informs the adapter source and fixture assertions. Record the adapter authoring method under B06 before implementation; AI-assisted source generation from specs is a proposal, not a claimed completed generation step.

### 9.2 Pinned sources

Read-only verification on 2026-10-22 used [Geoapify's official specification repository at revision dd07a5f8faafab533b067d5de6edeeda04daa5a3](https://github.com/geoapify/geoapify-openapi-specs/tree/dd07a5f8faafab533b067d5de6edeeda04daa5a3/api-specs). Paths below are relative to `api-specs/`. Pin that revision plus checksums in implementation provenance; do not silently generate against moving `main`.

| Use | Spec file | `info.version` |
| --- | --- | --- |
| Forward geocoding | `forward-geocoding/forward-geocoding-api-openapi-specs.json` | 1.1.2 |
| Isoline | `isoline/isoline-api-openapi-specs.json` | 1.1.1 |
| Routing | `routing/routing-api-openapi-specs.json` | 1.2.1 |
| Route Matrix | `route-matrix/route-matrix-api-openapi-specs.json` | 1.1.1 |
| Places | `places/places-api-openapi-specs.json` | 2.2.1 |
| Hosted MCP input catalog | `mcp/mcp-api-openapi-specs.json` | 1.1.2 |

Use the focused MCP specifications under `mcp/tools/` at the same revision for full output contracts: `geocode-address-openapi-spec.json`, `reverse-geocode-coordinates-openapi-spec.json`, `search-places-openapi-spec.json`, `list-place-categories-openapi-spec.json`, `calculate-route-openapi-spec.json`, `calculate-route-matrix-openapi-spec.json`, `transform-geometry-openapi-spec.json`, `evaluate-spatial-relation-openapi-spec.json` and `measure-geometry-openapi-spec.json`. These paths are verified against `mcp/tools/index.json`. Record their checksums before Stage 1 is complete. The catalog and live `tools/list` can drift; compare them at Stage 3 and record differences before changing contracts.

### 9.3 Verified facts and limits

- [Isoline](https://apidocs.geoapify.com/docs/isolines/) returns a FeatureCollection with Polygon or MultiPolygon geometry. Time ranges are seconds. HTTP 202 requires later retrieval by ID. The pinned spec contains a 3,600-second regular-request limit error example; 60 minutes is the initial ceiling, not a claim about special program entitlements.
- [Route Matrix](https://apidocs.geoapify.com/docs/route-matrix/) returns seconds/metres with source/target indexes. The public prose inconsistently describes the 1,000 limit as locations or values. The pinned MCP schema states sources times targets must not exceed 1,000; 1-by-20 is safely below either interpretation. Do not infer unlimited matrices from per-array maxima.
- [Places](https://apidocs.geoapify.com/docs/places/) supports rectangle/stored-geometry GET filters and inline Polygon/MultiPolygon POST filtering. Inline geometry limits exist. This release chooses rectangle plus local membership; that is a scope choice, not an API limitation.
- [Forward geocoding](https://apidocs.geoapify.com/docs/geocoding/forward-geocoding/) exposes optional confidence and match fields. Confidence is evidence, not proof that a fictional address represents a real premises.
- [MCP documentation](https://apidocs.geoapify.com/docs/mcp/) lists eleven tools, no isoline. [Geoapify's MCP page](https://www.geoapify.com/mcp/) and the pinned specification recommend `x-api-key`; some reference examples still show query-key URLs. Use header authentication from the environment and verify it in both clients under B04.

These are documentation findings, not authenticated endpoint test results.

### 9.4 Credits and rate budget

Published [pricing details](https://www.geoapify.com/pricing-details/) imply an illustrative 20-customer CLI run at 20 minutes costs 45 base credits: 21 forward geocodes, 4 for the isoline and 20 for a 1-by-20 matrix. One Places call requesting at most 20 candidates adds 1, for 46. This assumes unique inputs, short routes below 500 km, no avoid options, no retries and no isoline polling. It excludes MCP diagnostic calls, second-client tests and any route fallback. The 20-minute value is arithmetic only; it is not the sample-budget decision.

Record actual attempts, polling and credits where observable. Plan cost headroom for retries, repeated geocodes, comparison calls and geometry diagnostics. B01 must supply the account's daily credits and requests-per-second allowance before live testing. Neither free-plan advertising nor the cost estimate answers how many program runs are affordable.

## 10. Architecture and data flow

### 10.1 Contracts between components

CLI acquisition produces normalized business, zone, customer, route and competitor evidence. MCP acquisition produces the same evidence categories where supported, plus its approximation parameters. Both feed shared local validation, aggregation and rendering. The agent never fills missing measurements from model knowledge.

Each stage accepts the previous validated evidence plus run settings and returns `{status, result, errors}`. Status is `succeeded`, `partial` or `failed`; errors carry stable `code`, safe `message`, `retryable` and affected row IDs. This is an in-memory boundary, not a framework or persistent orchestration system. Failure states survive aggregation.

### 10.2 Component responsibilities

| Component | Responsibility |
| --- | --- |
| `zonepilot/cli.py` | Local preflight, CLI orchestration and exit codes. |
| `zonepilot/client.py` | Spec-derived REST adapters, environment authentication, response validation, safe errors and bounded request policy. |
| `zonepilot/engine.py` | CLI acquisition and evidence normalization. |
| `zonepilot/geometry.py` | Local Polygon/MultiPolygon membership and competitor geodesic distance. |
| `zonepilot/report.py` | Shared result validation, aggregation, JSON/Markdown rendering and agent-evidence import without network access. |
| `zonepilot/agent/README.md`, `prompts.md` | Client setup, tool sequence, export contract and limitations. |
| `tests/fixtures/` | Authored synthetic responses and expected outputs with provenance. |
| `docs/api-provenance.md` | Spec revision, selected focused files, hashes and adapter-generation record. |
| `docs/prompt-log.md`, `docs/evidence/` | Incremental sanitized prompts and permitted evidence. |
| `TUTORIAL.md` | Canonical tutorial, linked from README and published on dev.to. |

### 10.3 CLI stages and geometry rules

1. Preflight validates local inputs and configuration. Missing live credentials stop before network use. Replay bypasses credential checks and prohibits network use.
2. Resolve the business using Section 6.2; fail the run if unresolved. Capture outbound routing settings once.
3. Request and validate one isoline range. A 202 response is pending, not an empty service area. Poll by ID within the B07-approved bounds. Fail on missing ID, exhausted polling, empty/invalid successful geometry or mismatched range.
4. Resolve customers, retaining unresolved records. Classify each resolved point locally, then obtain outbound route measurements for all resolved points. A route error does not erase a CLI polygon verdict.
5. If requested, retrieve and classify competitor candidates. A competitor failure does not abort customer reporting.
6. Aggregate the validated evidence and write both formats. Failed global runs produce a safe terminal diagnostic and no successful report pair.

All internal coordinate arrays and GeoJSON use WGS84 `[longitude, latitude]`. REST isoline/geocoding parameters are named `lat`/`lon`; REST Routing waypoints serialize `lat,lon`; REST matrix locations use `[lon,lat]`; MCP point inputs use the named properties in the pinned schema. Test each adapter with deliberately unequal longitude and latitude. Normalize distance to metres and duration to seconds before calculations. Map internal `route_type=balanced` to Isoline `route_type`, but to REST Routing/Route Matrix and MCP route-tool `type`. Do not confuse that with Isoline `type=time`. Normalize REST FeatureCollections and MCP `structuredContent` through their distinct pinned schemas. A JSON-RPC error or `isError=true` is a tool failure even with HTTP 200; require the focused tool result contract before accepting measurements.

Membership is the union of polygon components. Within each polygon, a point must be inside its exterior and outside the strict interior of every hole. Any ring boundary, including a hole boundary, counts as in zone. Use a segment-distance tolerance of `1e-9` degrees for boundary detection, with an expanded segment bounding-box check; state that numerical convention in reports. A point in a hole's interior is out. Ring winding must not change the answer. Preserve all components and holes; never use only the first ring or polygon.

Require finite coordinates, closed rings with at least three distinct points, valid nesting and supported geometry types. Add negative fixtures for malformed rings and invalid topology. To keep planar geometry bounded, reject shapes crossing the antimeridian, ring edges spanning more than 180 degrees of longitude, and latitudes outside -85 through 85 with `unsupported_geometry`; never flatten them into a plausible zone. Validate topology or reject a response whose topology cannot be established. Geometry complexity and response-size caps must be recorded under B07 before implementation.

CLI membership remains the polygon result. Also compute `route_within_budget` from known time and `membership_route_disagreement` when both decisions are known. A disagreement is evidence for manual review, not an automatic verdict override. Compare the approved agent point-time verdict and CLI polygon verdict by row on identical inputs; retain disagreements for manual review without changing either path's verdict. The agent comparison is labeled an approximation.

### 10.4 Hosted MCP workflow and the unresolved choice

The mandatory workflow is prompt, tool calls, evidence export, local report validation/rendering, and comparison with the CLI on identical inputs. The AI client must preserve customer row IDs and source references. Export accepted measurements and statuses, not free-form guesses. JSON must parse without prose or fences. Validate it before aggregation; a missing/invalid field yields an actionable validation failure, not a repaired or fabricated value. The renderer writes both formats from the validated object. The import object uses the Section 11 root contract with `summary` and `run_status` omitted. The importer rejects those derived root fields if supplied and computes them locally. Customer `route_within_budget`, `borderline` and `membership_route_disagreement` are present but null on import; the importer computes them from acquired evidence. CLI verdicts come from local geometry; MCP verdicts must be validated under the B02-approved method. Root `path` must be `mcp` for this import mode. Validating source references and measurements does not by itself establish that a live tool was called; B04 evidence must prove that separately.

Owner decision, 2026-10-23: B02 approves `route_time_at_points`, route-time classification at supplied customer points with no continuous polygon. The test oracle is the accepted normalized outbound matrix time under the shared routing settings: `in_zone` when time is at most the budget (including equality), `out_of_zone` when greater, and `unknown` for missing, failed or unreachable routes. No spatial coverage between or beyond tested points may be claimed. Every agent output is labeled an approximation; JSON carries `zone.approximation=true`, and reports disclose "Route-time classification only at measured points; no continuous zone." Tests must cover below/equal/above budget, unresolved customers, missing/failed routes, mismatched verdicts and rejected polygon methods. One matrix call covers the accepted origin and at most 20 resolved customer targets; no boundary probes or polygon construction are part of this method. Separate required tool demonstrations remain diagnostics and do not override classification. Retain row-level CLI/MCP disagreements on identical inputs without overriding either result. This does not approve MCP competitor route evidence/search extent, live sample data or authenticated evidence.

Probe sampling plus a derived hull remains unapproved: it requires a separate sampling, hole/barrier, validation-error and call-budget contract. The owner also confirmed that invented sample addresses remain under tests/fixtures/sample and that data/sample_* and live Places evidence stay pending under B03.

Label all MCP output `approximation=true`, including a file viewed outside the tutorial. A separate diagnostic can compare MCP spatial predicates with synthetic polygons; it must not be presented as native hosted isoline support. The feedback section should request an isoline capability and describe needed inputs, outputs and error handling as a proposal to Geoapify.

The hosted server uses Geoapify services. The AI client may send prompt data to its model provider; do not claim that all agent data goes only to Geoapify. Use fictional, approved inputs and never include a key in prompts. Client installation and subscription are reviewer prerequisites, outside the zero-install CLI claim. B04 must establish supported environment-backed header configuration and capture/export for both clients. Do not prescribe an unverified client flag or persist a literal key in a settings file.

### 10.5 Failure and output contract

| Condition | Required behavior |
| --- | --- |
| Invalid local input, missing live key or unratified required runtime settings | Exit 2 before network calls; list safe, discoverable errors. |
| Global authentication/authorization error | Stop subsequent calls, exit 1; do not retry credentials or degrade every row separately. |
| Business resolution or zone failure | Exit 1; no completed report pair and no radius fallback. |
| Customer resolution failure | Keep unresolved row and safe reason; continue. |
| Route failure or no reachable road path | Null time/distance, distinct `route_status`; preserve CLI membership. Approved agent point-time membership is unknown. |
| Places failure | Section `unavailable`; no zero-result success claim; continue customer analysis. |
| Transient network, HTTP 429 or 5xx | Retry only within B07 bounds. Respect Retry-After within the total deadline; if it exceeds the remaining budget, stop retrying. Do not retry other 4xx. |
| Invalid response schema or nonfinite measurement | Fail the affected stage/record safely; do not coerce into a valid measurement. |
| Report validation or output-write failure | Exit 1. Do not announce completion or leave a new pair that appears complete. |
| Valid full/partial report | Exit 0 for complete; exit 3 for partial, with reason and output locations. |

Before API calls, validate output directory access and absence of the proposed pair. Do not overwrite existing reports in the initial release. Write both files through temporary files; publish the pair only after both renders succeed. On partial publication failure, remove only newly created files from that attempt and report failure. Never delete pre-existing output. Exact directory/name defaults and request/poll/response-size limits remain B07; the build cannot start those operations with unspecified bounds. Do not add persistent caching until its policy is decided.

Map errors to fixed operator-facing codes and safe descriptions. Never surface raw API messages, headers, response bodies or full request URLs. Sanitize before persistence, including prompt/session evidence. Check both working files and reachable Git history before publication. Actual credential incidents block publication until private remediation; do not record credential material in a review note.

### 10.6 Fictional data and provenance

Offline fixtures are hand-authored synthetic API-shaped responses, marked `synthetic`, with fictional labels and deliberately chosen geometry. They test contracts without pretending to be API recordings. Sanitizing a real response does not make its remaining address, coordinate-linked premises, identifiers or business details fictional.

Live geocoding of wholly invented addresses is not guaranteed. Live Places/reverse-geocoding may return real businesses or premises even when the query label is fictional. This is B03, a critical acceptance gate. Do not commit or publish such output, alter it and call it authentic, or substitute mocked calls for promised live evidence. Until the owner/program resolves what demonstration inputs and evidence are permitted, offline implementation can proceed but the live sample, full MCP proof, screenshots and tutorial cannot be signed off. No communications are sent by this review task.

Preserve required upstream attribution separately from MIT project licensing. For approved live evidence, document the returned data source attribution and applicable usage terms; the Geoapify backlink alone is not a substitute. Do not copy sample credentials or unrelated personal contact details from public documentation.

## 11. Shared report contract

Version `1.0`. The build must document these exact keys and their types in `docs/report-schema.md`, with complete and partial synthetic examples before renderer implementation. Unknown scalar values use JSON null, arrays use empty arrays when genuinely empty, and zero is reserved for a measured/countable zero. All fields below are required unless explicitly nullable. Reject nonfinite JSON numbers.

| Object | Keys and meaning |
| --- | --- |
| Root | `schema_version` string; `path` = `cli` or `mcp`; `data_mode` = `live` or `synthetic`; `run_status` = `complete` or `partial`; `run_timestamp_utc` RFC3339 string; `business`, `settings`, `zone`, `customers`, `summary`, `competitors`, `errors`, `warnings`, `evidence`, `attributions`. `customers`, `errors`, `warnings`, `evidence` and `attributions` are arrays; the other named containers are objects. `warnings` contains safe strings. |
| `business` | `name`, `input_address`, `resolved_address` strings; `coordinates` two-number lon/lat array; `geocode_evidence` as below. |
| `settings` | `budget_seconds` integer; `mode=drive`, `traffic=free_flow`, `route_type=balanced`, `units=metric`, `direction=outbound`; `boundary_rule` string. |
| `zone` | `method` string; `approximation` boolean; `parameters` object; `limitations` string array; `evidence_refs` string array. CLI parameters contain `range_seconds` integer and `boundary_tolerance_degrees` number. CLI method is `geoapify_isoline`; MCP uses `route_time_at_points`, `approximation=true`, and exactly `{budget_seconds}` matching settings. Store the authoritative CLI geometry separately as evidence, not as an invented agent polygon. |
| Customer | `row_id` integer; `name`/`reference` nullable strings; `input_address` string; `resolved_address` nullable string and `coordinates` nullable lon/lat array; `geocode_status` = `resolved` or `unresolved`; `geocode_reason` nullable string; `geocode_evidence`; `verdict` = `in_zone`, `out_of_zone` or `unknown`; `route_status` = `ok`, `no_route`, `error` or `not_attempted`; nullable nonnegative numbers `time_seconds`, `distance_meters`; nullable booleans `route_within_budget`, `borderline`, `membership_route_disagreement`; `evidence_refs` string array. |
| `geocode_evidence` | `candidate_count` nullable nonnegative integer, null when no valid response was read; nullable numeric `confidence`, `confidence_building_level`; nullable strings `match_type`, `result_type`. For unresolved results, confidence/match/type fields are null; candidate_count retains the actual count when known. Safe candidate evidence is referenced separately. |
| `summary` | Integer counts `total`, `resolved`, `unresolved`, `in_zone`, `out_of_zone`, `unknown_membership`, `known_routes`, `missing_routes`, `borderline`, `disagreements`; integer `classified_denominator`; nullable numbers `in_zone_percent`, `out_of_zone_percent`, `median_in_zone_seconds`, `max_time_seconds`; integer-array `max_time_row_ids`. |
| `competitors` | `status` = `not_requested`, `ok`, `partial` or `unavailable`; nullable string `category`; nullable object `search_extent`; nullable `coverage` string, either `sampled` or null; nullable boolean `cap_reached`; nullable nonnegative integers `returned_count`, `duplicate_count`, `unclassified_count`; nullable integer `observed_in_zone_count`, `observed_out_of_zone_count`; `records` array. |
| Competitor record | `id` string; nullable `name`, `address`; `categories` string array; `coordinates` lon/lat array; `verdict`; numeric `geodesic_distance_meters`. Only classified, in-zone records appear individually; unclassified/outside counts remain visible. |
| Evidence | `id` string unique within the report; `kind` = `rest`, `mcp` or `synthetic`; `operation` string; `artifact` repository-relative or report-bundle-relative path; `sha256` lowercase hexadecimal content hash. References resolve to these IDs. Only approved sanitized artifacts are persisted; never absolute paths or credential URLs. |
| Error | `code`, `message` strings; `retryable` boolean; `row_ids` integer array, empty for section-level errors. |
| Attribution | `source`, `text`, `url` strings, restricted to approved public attribution. |

Evidence for the origin is included in root `evidence` with its operation name; customer and zone `evidence_refs` identify their specific artifacts. Candidate counts must match captured results, and confidence numbers must be in [0,1]. Define `search_extent` as `{method, parameters}`, where method is `rectangle` or `proximity` or `circle`, with the corresponding bbox, center or center/radius numeric parameters. CLI uses a rectangle. B02/B03 must choose the MCP extent.

For `not_requested`, competitor category/extent/coverage/cap and all counts are null, and records are empty. For `unavailable`, retain the requested category/extent, but coverage/cap/counts are null and records are empty. Successful responses set all counts, including real zeros. Set `status=partial` if any candidate cannot be classified; otherwise `ok`. `returned_count - duplicate_count = observed_in_zone_count + observed_out_of_zone_count + unclassified_count`. Assign a missing provider ID a stable `synthetic-id:` prefix plus SHA-256 of the canonical coordinate/name tuple; this is an internal identity, not a claim that the provider returned it.

A resolved customer requires nonnull resolved address/coordinates and a successful accepted geocode. A route is `ok` only when both time and distance are finite and nonnegative; otherwise keep both null with the relevant status. A resolved customer must have a route attempt. Unresolved customers keep resolved address/coordinates, route measurements and derived booleans null. Membership is unknown for unresolved customers. Known CLI geometry verdicts survive missing route evidence.

Arithmetic rules:

- `total = resolved + unresolved = in_zone + out_of_zone + unknown_membership`. Unresolved rows always have unknown membership and `route_status=not_attempted`.
- `classified_denominator = in_zone + out_of_zone`. Percentages use this denominator and are null if it is zero. Show resolved and unknown counts beside percentages so route failures on the agent path cannot inflate apparent coverage unnoticed.
- `known_routes` counts `route_status=ok`; `missing_routes = resolved - known_routes`. Median includes only in-zone customers with known times. Maximum includes all known customer times; all tied row IDs appear in input order. Empty aggregates are null, with an empty maximum-row list.
- Borderline and discrepancy counts count true values only; null is unknown. Compare normalized six-decimal measurements before display-unit rounding. Do not overwrite polygon membership when a measured route crosses the threshold.
- Keep raw seconds/metres in JSON and Markdown. Optional display minutes/kilometres are derived labels. Percentage presentation rounds to two decimal places with ties-to-even; raw counts remain authoritative.
- Normalize acquired times/distances to six decimal places using decimal half-even before calculations, and serialize derived median/maximum values at that precision. Compute borderline comparisons using decimal arithmetic. Serialize computed geodesic metres at three decimal places and percentages at two, using half-even. Cross-platform fixture tests must include the numeric rounding boundaries; a mismatch blocks reproducibility acceptance. Stable ordering is customer input order, competitor ID order and error stage/row order. JSON uses sorted object keys, two-space indentation, UTF-8 and one trailing LF. Tests inject the timestamp; live runs capture it once at start.

Markdown contains a header, summary, customer table, competitor state/table, and evidence/errors/attribution details. Every JSON field must be accessible in Markdown, using detail tables for long fields. Render absent values as `unavailable`, never a blank that resembles zero. Parity testing compares values field by field, not just headings. A successful bounded competitor search remains sampled; this warning alone does not make a run partial. Any unresolved customer, missing route for a resolved customer, unknown membership on a resolved customer, or unavailable/partial requested competitor section makes the report partial.

## 12. Repository and deliverables

### 12.1 Required files

Deliver `LICENSE`, `README.md`, root `TUTORIAL.md`, the Section 10.2 modules/docs, approved live-demo `data/sample_business.json` and `data/sample_customers.csv` after B03 closes, offline tests, report contract/examples and API provenance. Wholly authored offline inputs live separately under `tests/fixtures/sample/`; the fixture bundle is `tests/fixtures/sample/run.json`. The public live sample is gated by B03 and must not be silently represented by an offline fixture. Preserve `docs/prd.md` and `docs/prd-review-log.md` as the design history. Generated reports, local secrets and raw sessions are ignored by default; only reviewed permitted evidence is deliberately committed.

### 12.2 README run contract

Document the actual sample address/budget/category only after B03 closes. The command shape is `python -m zonepilot.cli --business-address "<approved address>" --minutes <approved minutes> --customers data/sample_customers.csv`, with optional `--business-name` and `--competitor-category`. Angle-bracket values here describe future documented values, not a runnable sample. B07 must establish output flags/defaults and the README must then name the exact resulting files. No `__main__.py` is required for this module invocation.

The final README sequence is clone, enter the repository, confirm Python 3.14.9 or later (build/test target 3.15.1), supply the key through the environment, run the fully specified sample command, then open both outputs. There is no dependency installation or product build step. Document `python3` on macOS/Linux and `py -3.15` or the installed 3.15.1 interpreter on Windows. Show a masked interactive secret entry appropriate to each shell rather than a literal credential in shell history. PowerShell uses the process environment variable `$env:GEOAPIFY_API_KEY`; POSIX shells export `GEOAPIFY_API_KEY`. Verify the final commands on each claimed platform.

Also document `python -m zonepilot.cli --replay tests/fixtures/sample/run.json` and `python -m zonepilot.report --import-agent <evidence.json>`, plus `python -m unittest discover -s tests`, all offline. Replay is mutually exclusive with live input/category arguments; its bundle contains the input rows/settings, fixed timestamp and synthetic API responses needed to exercise the same CLI pipeline. Import uses the evidence contract in Section 10.4 and never calls an API. Both modes use the B07-defined output policy and require no key. Replay is demonstration/testing evidence, not the live sample acceptance. Include exit codes, limits, attribution, fixture provenance and links to the tutorial, schema and manual checklist. AI-client setup is a separate section with prerequisites and B04-verified configuration for both clients.

### 12.3 Tutorial and closing deliverables

`TUTORIAL.md` and the dev.to publication contain the OpenAPI input/version and adapter-generation record, full sanitized prompt-log link, three genuine failures/fixes with rechecks, client screenshots, both-path comparison, limitations, lessons and dedicated Geoapify feedback. Both publications link back to Geoapify and the repository. Keep screenshots free of keys, personal data, account details and absolute local paths. Mark every redaction with its reason. Preserve the real sequence and do not invent missing evidence.

External publication is a later deliverable, not an action authorized for this docs review. Private payment administration never enters the public repository.

## 13. Acceptance checklist

Every Must and CR row must link to evidence in the final README checklist. These are future product checks, not checks executed by the PRD review. Perform them manually; no GitHub Actions or CI runs are required for this project workflow.

| Gate | Required evidence and negative cases |
| --- | --- |
| AC-01 inputs, FR-01–06 | Valid 1/20-row inputs; invalid 0/21 rows, minutes 4/61/noninteger, malformed CSV, duplicate headers, missing/unknown columns, BOM, quoted newlines, blank addresses, duplicate rows, missing key and unwritable/existing output. Prove zero calls on failed preflight and replay. |
| AC-02 geocoding, FR-07–09 | One eligible building, two eligible candidates, missing confidence, low confidence, no matches, invalid coordinates; fatal origin versus per-customer unresolved behavior. |
| AC-03 geometry, FR-10–13 | Polygon, holes, MultiPolygon/disconnected components, interior/exterior, every ring edge/vertex, reversed winding, tolerance cases, malformed/unsupported geometry, mismatched range, 202-to-success and exhausted polling. |
| AC-04 routes, FR-14–16 | Outbound direction, coordinate-order conversion, reordered/missing matrix cells, no route, zero valid time, budget exact/just-over/110-percent/just-over-110-percent, membership/time disagreement, bounded fallback/retries. |
| AC-05 competitors, FR-17–19 | Valid/invalid category, inside/outside points, duplicates, invalid coordinates, zero successful results versus failure, cap reached and sample warning. No completeness claim. |
| AC-06 reports, FR-20–23 | All resolved/unresolved, no known times, tied maximum, partial routes, unavailable competitors, null semantics, zero denominator, Markdown escaping, output failure rollback, field parity and fixed-clock byte reproducibility. |
| AC-07 hosted workflow, FR-25–28; CR-09–10 | Approved B02 method, matching inputs, full schema-valid pair, every nine-tool evidence row, separate client smoke proof, and honest membership/candidate differences. No inference of data missing from tools. |
| AC-08 live sample | B01/B03 closed; 20 approved fictional customers with inside, borderline and outside outcomes; recorded live data/settings and explanation of differences from fixtures. No promise of byte-identical live responses. |
| AC-09 portability | Clean-clone README sequence and keyless tests on the NFR-06 environment matrix. Record missing checks as pending. |
| AC-10 editorial/program | Business-only scope; OpenAPI provenance; incremental prompt log; three real failures; both client screenshots; Geoapify feedback/backlinks/adaptation permission; root tutorial and dev.to URL. |
| AC-11 publication | Owner-controlled public visibility and correct MIT holder; privacy/secret/path sweep of files, images and Git history; required attribution preserved; no unreviewed real demonstration data. |

Build acceptance requires AC-01–10, with no unclosed blocking gates. Submission additionally requires AC-11 by November 15. Review completion of this PRD means a full pass with no unresolved fixable findings; it does not satisfy the product checks above.

## 14. Four-day plan and deadline

Resolve B01–B04, B06 and B07 before committing to four uninterrupted build days. Offline scaffold/fixture work can proceed without the key, but live gates cannot. B05 must close before publication/payment administration. Allocate the approximately four build days to finish by November 8; do not consume the single fix-round reserve as planned feature time.

| Stage | Work | Gate |
| --- | --- | --- |
| Day 1 | Start prompt log immediately; pin specs/authoring method; document schema; stdlib adapters and synthetic geometry/response tests. | AC-01–03 baseline; all adapter inputs traced to specs. |
| Day 2 | CLI pipeline, bounded errors, paired output and competitor sampling; draft README and failure notes. | Offline AC-04–06; approved live sample check when prerequisites are closed. |
| Day 3 | Both AI-client setups, approved MCP method, nine-tool evidence and matched-input comparison; capture screenshots and failures as they happen. | AC-07–08 evidence. |
| Day 4 | Final tutorial/dev.to content, checklist, clean-clone/platform verification and private compliance review; owner-controlled publication. | AC-09–11 and every CR row verified. |

Do not defer any promised tool, either client, prompt log, real drive-time CLI, tutorial publication or three-failure requirement to fit the estimate. Exclude Could features first. If a required gate cannot close, report a schedule risk with its evidence; do not invent a waiver. Submission coordination must allow review and the one permitted fix round within the final deadline; review turnaround itself is not guaranteed.

## 15. Risks and controls

| Risk | Control |
| --- | --- |
| Fictional data cannot satisfy live geocoding/Places evidence | B03 blocks live acceptance and publication; synthetic tests are useful but not a substitute. |
| Agent method produces different membership | B02-approved semantics, labeled method and row-level comparison; no equality claim. |
| Quota or rate restrictions | B01 entitlement check, bounded batches, offline tests, measured request counts and retry/poll budget. |
| Four-day effort expands | No GUI, hull implementation without approval, free-text categories, larger batches, persistent cache or extra callouts in the baseline. |
| API/client contracts drift | Pin specs and client versions; compare live tools/list later; document deviations before changing adapters. |
| Prompt/evidence gaps | Log from session one, record redactions, capture real failure/recheck pairs incrementally. |
| Privacy leak in raw responses or screenshots | Safe errors, environment-only headers, deliberate evidence review and history/image checks before publication. |

## 16. Payment and closing terms

EUR 300 is payable once the finished project passes Geoapify's final review. EUR 500 best-app and EUR 500 best-tutorial awards are discretionary, not guaranteed income. Quality, clarity and practical usefulness guide the deliverables.

Payment route, account upgrade requirements, transfer timing and invoice/receipt details are not confirmed by the authoritative facts supplied for this review. B05 tracks private owner verification. Keep account, invoice, address and verification material out of the repository and tutorial. Closing administration does not change the November 15 deadline.

## 17. Open-question disposition and gates

No blocked answer below is invented or treated as approved. The review log owns B01–B07 and the evidence needed to close them. This table accounts for all 24 supplied questions.

| Questions | Disposition |
| --- | --- |
| Q1 key, tier; Q2 costs/rates; Q21 acceptance | B01. Key not issued. Section 9.4 supplies a conditional cost estimate; account allowances, acceptance status and affordable runs remain unknown. |
| Q3 isoline specifics | Public units, geometry and regular-limit example verified in Section 9.3. Raised limits are B01; holes/disconnected geometry have explicit local tests. |
| Q4 matrix shape | A 1-by-20 matrix fits published limits. Runtime entitlement remains B01; no larger-matrix implementation is promised. |
| Q5 Places filter/category | REST polygon support verified; MCP has a narrower search contract. Category and permitted sample competitors remain B03. |
| Q6 nine tools/specs/generator | Nine tools and spec revision fixed in Sections 8.2/9.2. Authoring-method choice remains B06; no third-party execution allowed. |
| Q7 confidence fields | Verified optional fields and explicit conservative product policy in Section 6.2. Sample compatibility remains B03. |
| Q8 current MCP inventory | Eleven publicly documented tools, no isoline; authenticated tools/list validation belongs to B04 when credentials exist. |
| Q9 approximation; Q17 disagreement | B02. CLI polygon authority is preserved from the settled design. Owner approved point-time classification on 2026-10-23; preserve row-level differences and approximation labels. Sampled hulls remain unapproved. |
| Q10 clients; Q11 export; Q12 auth | Both clients are mandatory, not an open choice. B04 gates actual setup/export evidence. Header authentication is documented; no key or client setup is requested in this task. |
| Q13 fictional/geocodable; Q14 city; Q15 targets | B03. No city, address permission, budget or exact mix is selected. Require at least one inside, one outside and one borderline in the eventual approved sample. |
| Q16 coordinate convention; Q18 geometry cases | Defined in Section 10.3 and AC-03/04. |
| Q19 operating values | B07. Exact retry/time/poll/size limits, cache policy and output flags/defaults must be ratified. Single-row CSV covers screening; no separate flag is required. |
| Q20 Windows environment | Section 12.2 requires process-scoped PowerShell setup and an explicit interpreter; commands need platform verification. |
| Q22 visibility/holder; Q23 payment | B05. Keep private now, public at submission through owner control. Current LICENSE names cachetronaut; holder and private financial details await confirmation. |
| Q24 tutorial destination | Resolved by the accepted application: repo `TUTORIAL.md` plus dev.to, not repo-only. Geoapify may adapt it with credit. |
