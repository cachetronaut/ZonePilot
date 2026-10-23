# ZonePilot PRD review log

Reviewer: Astra. Review date: 2026-10-22. Scope: documentation only.

Baseline: `32956ab`, the six supplied PRD parts concatenated in order with their message wrappers removed. The supplied program facts and application promises govern this review. The repository remains private. No key, live authenticated API request, installation, product execution, or CI run is needed or performed.

## Pass 1: full review of the supplied PRD

Verdict: changes required. Twenty fixable findings and seven blocked findings. Severity means impact on implementation or submission, not editorial preference. Sections below refer to the baseline.

| ID | Severity | Exact section | Finding and required change | Status |
| --- | --- | --- | --- | --- |
| F01 | Medium | 1; 2; 3; 5.1 | Drive time alone cannot establish profitability, and free-flow routing cannot demonstrate congestion. Describe a drive-budget decision aid, with no profit, surcharge, or live-traffic guarantee. | Open |
| F02 | High | 1; 3 principle 2; 10.1–10.4 | The diagram never connects the agent to the shared engine or reports. A hosted MCP workflow cannot be assumed to run local Python. Specify separate acquisition paths, a shared normalized report contract and deterministic aggregation, and an explicit agent export/import boundary. Preserve the same business analysis while disclosing membership-method differences. | Open |
| F03 | Critical | CR-09–CR-10; 10.5; 13 | The four families are misidentified and the nine tools are not enumerated or tested. Make OpenAPI plus MCP explicit, list all nine verbatim, and require evidence for every tool. Places and geometry coverage cannot be deferred with Should features. Isoline is an additional REST requirement. | Open |
| F04 | High | 9.1–9.3; 10.5 | An unspecified generator may add dependencies or require executing third-party code. Pin official OpenAPI files/revision and define a reviewed stdlib adapter approach that does not require a third-party executable. Remove unsupported comparative language and the 20-line geometry estimate. Record generation-method choice as B06. | Open |
| F05 | High | FR-02; FR-10; 10.3 | The Isoline specification's regular-request error example caps time at 3,600 seconds. The 120-minute promise is unsupported. Restrict the initial contract to 5–60 minutes; use seconds, one outbound range, explicit routing settings, Polygon/MultiPolygon parsing, and bounded handling of HTTP 202. Raised account limits remain B01. | Open |
| F06 | High | FR-11; 10.3–10.5; 13 | Geometry rules omit holes, edge tolerance, malformed shapes, coordinate order, and unsupported antimeridian cases. Define these and corresponding negative tests. Keep CLI polygon membership authoritative as already specified; any change or agent comparison policy remains B02. | Open |
| F07 | High | FR-08–FR-09; 10.3; 10.7 | Ambiguity is Should in one place and fatal elsewhere. Make conservative geocode handling Must; distinguish ambiguous from failed, never silently choose, and record actual confidence fields and a deterministic acceptance policy. | Open |
| F08 | High | FR-20–FR-23; 11 | A list of report sections is not a shared schema. Define field names, nullability, states, units, denominators, empty aggregates, ties, rounding, row identity, route failures, and evidence provenance. | Open |
| F09 | High | NFR-02; NFR-04; 10.7 | Verbatim API errors can expose credentials; global auth errors are not individual failures. Define safe error codes, redaction, abort/degradation rules, bounded retries, and incomplete-output behavior. Concrete runtime limits remain B07. | Open |
| F10 | High | FR-17–FR-19; 10.3; 11.4 | Search terms, taxonomy, extent, pagination, duplicate results, distance type, and completeness are undefined. Distinguish REST polygon support from MCP radius/proximity search, retain local CLI filtering, and report observed counts and truncation rather than a market census. | Open |
| F11 | Medium | FR-01–FR-06; UC-2; 12.3 | No exact CSV/header or CLI contract exists; business name has no input source. Define syntax-level preflight, duplicate-row behavior, single-row screening, output pairing, and platform setup. B07 tracks unresolved operational choices. | Open |
| F12 | High | 3 principle 3; NFR-03; NFR-05; 13 | Timestamps break byte determinism; live results cannot be fixture-pinned; performance is circular. Separate offline reproducibility from live observations, inject a fixed clock for tests, and make performance a recorded benchmark rather than an unqualified cross-machine promise. | Open |
| F13 | High | FR-25–FR-28; 10.4; 12.2 | The application requires both Claude Code and Codex CLI setup screenshots. Specify both, retain JSON and Markdown requirements, and distinguish Geoapify auth from AI-client subscription/runtime prerequisites. Actual environment-only auth and capture validation remain B04. | Open |
| F14 | High | FR-27; CR-06; CR-12–CR-14; 12 | dev.to publication and root TUTORIAL.md are missing. Require both, a day-one prompt log across the build, three genuine failures, redaction markers, feedback, and credited adaptation permission. Never invent incidents to satisfy a count. | Open |
| F15 | Critical | FR-04; CR-16; 10.6; 12.2–12.3; 13 | Fictional addresses may not geocode, and live Places returns real businesses. Sanitized recordings are not automatically fictional. Separate hand-authored synthetic fixtures from live evidence; do not publish real address/business outputs or call altered recordings genuine. Keep program interpretation blocked under B03. | Open |
| F16 | High | 12.3; 13 | Acceptance omits most failure cases and all-nine-tool proof, and conflates private build completion with public submission. Add traceable offline, live, editorial, and owner-controlled submission gates, all run manually without CI. | Open |
| F17 | High | 14; 15 | Four days assumes away the key, sample, agent method, and evidence gates; logging begins too late. Put prerequisites before four build days, log from the first session, include documentation daily, and prohibit deferring application commitments. | Open |
| F18 | Medium | 12.2; 16 | Payment route, account product, timing, and paperwork are asserted beyond the supplied authoritative terms. Keep EUR 300 after acceptance and both discretionary EUR 500 awards; keep personal finance administration private and unverified details blocked under B05. | Open |
| F19 | High | FR-06; NFR-02; 10.6; 12.3 | MCP authentication is absent and query-string key examples conflict with secret hygiene. The pinned spec recommends x-api-key. Require environment-sourced headers, no literal secrets in client config or prompts, and failure rather than an unsafe URL fallback. B04 covers actual client support. | Open |
| F20 | Medium | 8; 12; 13; 15 | MIT project licensing does not replace upstream data attribution. Preserve required source credits while keeping fixture data synthetic; distinguish program backlink from API data attribution. Retain current LICENSE until B05 resolves the holder. | Open |

### Blocked findings

These are findings, not permission requests. The review can finish with these gates explicit; the product cannot pass the dependent acceptance criteria until the gates close.

| ID | Severity | PRD sections | Open questions | Required evidence to close |
| --- | --- | --- | --- | --- |
| B01 | High | 6.1; 9; 14 | Q1–2, Q21 | Program key is not issued. Owner confirms acceptance-email status, account tier, rate/credit limits and live-run allowance when available. Do not request or invent a key in this task. Published pricing does not establish account entitlements. |
| B02 | High | 10.3–10.4; 11; 13 | Q9, Q17 | Owner selects the agent approximation and approves how method disagreement is presented. Per-customer route thresholds without a polygon are the smaller proposal; a sampled hull requires a separate accuracy/cost contract. Do not silently make that choice. |
| B03 | Critical | 4.1; 6.1; 6.5; 10.6; 13 | Q5 taxonomy, Q13–15 | Owner/program interpretation of fictional-but-geocodable inputs and live Places evidence, then sample city, business category, budget and target counts. A real street address with an invented name does not become fictional. |
| B04 | High | 6.7; 10.4; 12.3 | Q10–12 | Both client names are already promised. Build-time proof must establish environment-only x-api-key auth, successful tools/list and calls, structured JSON export and sanitized screenshots/session evidence for installed client versions. No authenticated validation is possible in this task. |
| B05 | Medium | 7; 12; 16 | Q22–23 | Owner confirms copyright holder and privately handles payment prerequisites/paperwork. Existing LICENSE names cachetronaut. Repo stays private for this job; public release is a later owner-controlled submission gate. |
| B06 | Medium | 9.2; 10.5 | Q6 generation method | Official spec inputs are pinned by this review. Choose AI-assisted adapter authoring from those specs or a locally authored stdlib generator; no third-party generator execution. Record method/prompt provenance before client implementation. |
| B07 | Medium | 6.1; 10.7; 12.3 | Q19 | Owner/build coordinator ratifies exact retry/timeout/poll values, cache policy and output naming. One-row CSV already satisfies screening; a dedicated address flag is optional. Record choices before dependent implementation; no arbitrary numbers are represented as approved. |

### Source checks

Official documentation and JSON specifications were read, never executed. Checked 2026-10-22. OpenAPI repository revision: `dd07a5f8faafab533b067d5de6edeeda04daa5a3`.

- [Official specification repository](https://github.com/geoapify/geoapify-openapi-specs/tree/dd07a5f8faafab533b067d5de6edeeda04daa5a3/api-specs): exact spec inputs and versioned schemas.
- [Isoline documentation](https://apidocs.geoapify.com/docs/isolines/): time units, geometry and asynchronous response behavior.
- [Route Matrix documentation](https://apidocs.geoapify.com/docs/route-matrix/): source-to-target data and costs. Its prose mixes points and values; the MCP input schema and pricing page state a 1,000-cell limit. A 1-by-20 request is below both descriptions.
- [Places documentation](https://apidocs.geoapify.com/docs/places/): REST supports inline polygon POST filters as well as stored geometry IDs. Do not assume MCP exposes every REST parameter.
- [Forward geocoding documentation](https://apidocs.geoapify.com/docs/geocoding/forward-geocoding/): optional confidence/match fields.
- [MCP documentation](https://apidocs.geoapify.com/docs/mcp/) and [product/authentication page](https://www.geoapify.com/mcp/): eleven published tools, no isoline; the nine promised tools remain required. Query-key examples differ from the header-recommending pinned specification; use the latter and verify actual clients later.
- [Pricing details](https://www.geoapify.com/pricing-details/): cost model, not proof of the program tier or quota.

No finding is closed solely by a green check or an unsupported statement of compliance.

## Revision after pass 1

| Finding | Response |
| --- | --- |
| F01 | Fixed: Sections 1–4 define outbound budget support and exclude profit, pricing and live-traffic guarantees. |
| F02 | Fixed: Sections 1, 3, 10 and 11 replace shared acquisition claims with explicit MCP evidence export plus shared local aggregation/rendering. B02 still blocks the approximation choice. |
| F03 | Fixed: CR-09/10 and Section 8.2 name the track, correct all four families and list all nine tools with evidence purposes. Competitors and borderline behavior are Must because the promised demo depends on them. |
| F04 | Fixed: Section 9 pins official input files/versions and prohibits third-party executable generators; B06 preserves the unresolved authoring choice. Removed speculative language/toolchain comparisons and the geometry line-count claim. |
| F05 | Fixed: FR-02/10 and Sections 9.3/10.3 set 5–60 minutes, seconds, explicit routing settings, validated geometry and bounded 202 handling. Account exceptions remain B01. |
| F06 | Fixed: Section 10.3 defines coordinate adapters, holes, components, boundary tolerance and unsupported/malformed geometry; AC-03/04 tests them. |
| F07 | Fixed: FR-09 is Must; Section 6.2 defines candidate acceptance and failure reasons using actual optional fields. This is explicitly a conservative product policy. |
| F08 | Fixed: Section 11 specifies the shared fields, nulls, units, denominators, ordering, aggregate rules and states; AC-06 requires parity and negative cases. |
| F09 | Fixed: Section 10.5 distinguishes global failures, record degradation, retry eligibility, safe error messages and failed output publication. B07 preserves unspecified operational limits. |
| F10 | Fixed: Section 6.4 uses a verified category, bounded candidate search, deduplication, geodesic distance and explicit sampled counts. REST/MCP filter differences are stated. |
| F11 | Fixed: Section 6.1 defines CSV/argument validation and row identity; Section 12.2 defines module invocation and single-row screening. B07 gates actual output flags/defaults. |
| F12 | Fixed: NFR-03/05, Section 11 and AC-08 separate measured performance, fixed-clock replay and mutable live observations. |
| F13 | Fixed: FR-25/28 and Section 12.2 require both clients and evidence, separating external client prerequisites from zero-install Python. B04 remains a live verification gate. |
| F14 | Fixed: CR-12–14/17 and Section 12.3 require day-one logging, genuine failure evidence, both publication destinations and credited adaptation permission. |
| F15 | Fixed: Section 10.6 distinguishes authored synthetic fixtures from real recordings and explicitly blocks live sample/publication under B03. No permission to publish real demo data is inferred. |
| F16 | Fixed: Section 13 supplies offline/live/editorial/publication gates mapped to requirements, with manual evidence and no CI. |
| F17 | Fixed: Section 14 separates prerequisite closure from four build days, requires daily logging/docs and excludes Could work. |
| F18 | Fixed: Section 16 retains confirmed compensation and defers unconfirmed private payment administration under B05. |
| F19 | Fixed: FR-06, NFR-02, Sections 9.3/10.4/10.5 require environment-backed headers and safe failures; no literal/query-key fallback. |
| F20 | Fixed: NFR-09 and Sections 10.6/13 distinguish project MIT from upstream attribution and retain the existing license pending B05. |

All twenty fixable findings addressed. No disagreements. B01–B07 remain blocked; revisions expose these dependencies rather than pretend to answer them.

## Pass 2: full review of revision `5c2f632`

Re-read Sections 1–17 against every application promise and open question, then traced input, CLI acquisition, agent acquisition, aggregation, output and submission failure paths. Three new fixable findings; B01–B07 unchanged. No previously closed finding is reopened.

| ID | Severity | Exact revised section | Finding and required change | Status |
| --- | --- | --- | --- | --- |
| F21 | High | 6.5 FR-23; 10.1/10.4; 11 | The schema lacks a warning field, evidence index and precise importer boundary. Failed geocodes cannot truthfully provide a candidate count; competitor failure counts must not imply observed zero. Complete types/state invariants, define derived-versus-acquired fields, and make evidence references resolvable. | Open |
| F22 | Medium | 6.1; 9.2; 10.3 | The adapter description leaves route_type-to-type translation implicit and defers exact focused MCP filenames despite a verified index. Pin the nine filenames and category-snapshot provenance; add REST/MCP envelope validation and the parameter mapping. | Open |
| F23 | Medium | 7 NFR-05; 11; 12.1–12.2 | Synthetic sample and approved live sample occupy the same stated paths, risking a false live run. Offline replay/import invocation is unspecified. Floating geodesic output lacks a serialization precision policy. Separate fixture/sample paths, specify keyless modes and numeric normalization; remove trailing whitespace reported by git diff --check. | Open |

Pass 2 verdict: revise, then perform another full pass. This pass checked published schemas as data only; no Python interpreter, install, product execution or CI operation was used.

## Revision after pass 2

- F21 fixed: Section 11 now includes warning/evidence fields, reference identity, nullable unread counts, competitor state/count invariants, explicit scalar types and route/geocode invariants. Section 10.4 defines the import object, excludes locally derived summary/status, and recomputes time-based flags. Live evidence remains gated; schema validity is not proof of an API call.
- F22 fixed: Sections 6.1, 9.2 and 10.3 identify category-snapshot provenance, all nine focused spec filenames, the `route_type` to `type` mapping, distinct REST/MCP envelopes and tool-level error checks. Focused geocode/route/matrix specs and the tool index were read as JSON data.
- F23 fixed: Sections 11/12 separate authored fixture paths from the approved live sample, define offline replay/import command shapes, and specify numeric normalization/serialization with cross-platform tests. Removed Markdown hard-break whitespace so `git diff --check` passes.

All three pass-2 findings addressed. No disagreements; blocked findings unchanged.

## Pass 3: full review of revision `fb75f7c`

Verdict: clean for this documentation review. Zero new findings and zero unresolved fixable findings. B01–B07 remain blocked; their dependent product acceptance gates are not passed.

This was a fresh read of all seventeen sections, not just a diff or a retest of prior findings. Review coverage:

- Program/application trace: dates, fix-round limit, business-only boundary, private-now/public-at-submission distinction, MIT, environment credentials, OpenAPI plus MCP, all nine tools, real CLI drive-time polygon, shared reports, prompt log, three real failures, both clients, dev.to, tutorial backlink and credited adaptation permission are retained.
- Implementer trace: followed CSV/preflight through origin resolution, isoline/polling, point membership, matrix cells, sampled competitors, normalization, failure states and paired output. Walked unresolved/all-null/zero-denominator/disagreement cases through the schema. Agent acquisition and local recomputation are distinct and the unresolved approximation is not silently selected.
- Buildability trace: stdlib-only modules, bounded 20-row/20-candidate scope, no UI or local MCP server, no unapproved hull work, explicit prerequisite gates and four build days. Full build readiness is conditional on the blocked answers, especially fictional/live evidence compatibility; the estimate is not asserted as a guarantee.
- Factual trace: checked the revised API claims against the pinned official specifications and documentation listed above, including focused geocode and routing contracts. No authenticated endpoint or client behavior is claimed verified.
- Acceptance trace: 28 FR, 9 NFR, 17 CR and 11 AC rows are uniquely numbered; all nine promised tool names are present. Reviewed all 24 supplied open questions against Section 17 and the seven blocked groups.
- Scope/privacy trace: only docs/prd.md and docs/prd-review-log.md differ from main. Reviewed the content and scanned all tracked text across reachable history for credential/email/absolute-machine-path patterns; no matches. The supplied owner credit is intentional project metadata, not private customer data. No payment/account identifiers or private email text were added.
- Repository checks: git diff --check passes. The repository is private, main is unprotected and there are zero Actions workflows. No CI was started or awaited. No dependencies, downloaded code, Python interpreter, product build or tests were executed during this docs-only task.

Final tally: 3 full review passes, 2 revision rounds, 30 total findings: 23 fixed, 7 blocked, 0 disagreed, 0 unresolved fixable. The original baseline identifier was `32956ab`; that history was removed by the owner-authorized privacy squash. Peak shape under the requested review stopping rule; not a declaration that the blocked build/submission decisions are resolved.

## Privacy correction, 2026-10-22

Owner credit is Scout Squad. Historical commit identifiers above describe prior review passes, not retained Git objects. The owner authorized replacing the repository history with one scrubbed initial commit. Python support now starts at 3.14.9, with 3.15.1 the build/test target. Earlier privacy review did not prohibit the former owner credit; this build does.


## Owner decisions, 2026-10-23

The owner explicitly approved the smaller per-customer route-time method for the agent pack, with no continuous polygon and approximation labels in every output. B02 customer method selection is closed by this decision. PRD section 10.4 now records the threshold oracle, unknown-route treatment, one-matrix customer scope and row-level disagreement presentation. The sampled-boundary alternative remains unapproved; MCP competitor evidence/search extent remains pending.

The owner also confirmed that Main Street Plumbing and the twenty fictional customers remain under tests/fixtures/sample. Live runs, data/sample_* and real Places evidence remain pending under B03. This is confirmation of fixture handling, not approval of live inputs or publication. B01/B03/B04 and runtime/platform acceptance checks remain open. Prior review entries above describe their original review dates, not the current approval state.
