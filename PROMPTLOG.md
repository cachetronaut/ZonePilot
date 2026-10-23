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


## 2026-10-23, owner-approved agent method

The owner answered the pending questions: approve per-customer route-time classification with no continuous polygon and approximation labels; keep invented addresses in tests/fixtures/sample and live sample/data paths and real Places evidence pending. Recorded the decision in the PRD and review log before completing dependent integration. Enabled only the existing route_time_at_points customer method, retained unknown membership for absent routes, and kept requested MCP competitors and sampled-boundary methods rejected. Updated prompts to avoid claiming nine-tool or live acceptance while those gates remain open. Required the point-only limitation in imported reports and labeled importer error diagnostics as approximations. Tests now exercise the shipped default rather than patching an approval constant.

Verification: all 135 offline unittest tests passed on Python 3.14.9. Added explicit below/equal/above-budget and missing/failed/unresolved-route checks, exercised keyless import without patching approval, required approximation labels in JSON/Markdown and error diagnostics, and retained rejection of unapproved methods, parameters, memberships and requested competitors. Privacy and whitespace scans passed. No test failure occurred during this approval integration. No live run, installation, or target-runtime/platform acceptance was claimed.

## 2026-10-23, Stage 4 opened

Owner request: verify the Keychain key with one geocoding call; run the shipped twenty-customer example live and from a fresh clone; exercise the shipped hosted MCP prompt sequence in an installed AI client; prepare the tutorial, dev.to draft, compliance matrix and owner-sent email draft. Keep the repository private, preserve the license, send nothing, install nothing, scan files/history, and drive Sol xhigh review before any safe squash merge.

Read the PRD, this log, README and local-check record before execution. The initial sandbox GitHub request failed; authorized network access confirmed PRIVATE and cloned main at 5169b27. The requested external Python policy path was missing; read the installed plugin policy. Stock Python 3.14.9 passed all 135 tests. Python 3.15.1 is absent. No dependency workflow was used.

The Stage 4 instruction authorizes trying the shipped fictional inputs. It does not make returned real map records fictional or approve publication of real premises. Keep B03 open and retain only safe failure metadata. One credential verification call returned HTTP 200 but five city-level candidates, no eligible building. No returned addresses or coordinates were persisted. See stage4/key-verification.json under docs/evidence. Do not weaken geocoding policy or replace fictional inputs with real addresses to manufacture success.

## Stage 4 live and client results

The inspected CLI ran with the shipped fictional origin, twenty customer rows, 20 minutes and broad service category. One measured HTTP attempt ended in origin_unresolved, exit 1, no report pair and no customers evaluated. Percentages and median live drive time are unavailable. A fresh remote clone at 5169b27 passed 135 offline tests on Python 3.14.9, matched both golden files byte for byte, and produced the same live-origin failure. Python 3.15.1 was not installed; no installation was attempted.

Using the agent pack's gate/discovery/origin instructions, Claude Code 2.1.309 connected through an environment-backed x-api-key header and called geocode_address once. It returned five city candidates and no eligible building. The session stopped before customer acquisition. Every assistant result and persisted MCP artifact carries approximation=true; raw returned map records were omitted before persistence. The inventory had twelve tools, adding get_timezone to the eleven pinned names, still with no isoline. Later prompts were not run after the origin gate failed.

Codex CLI 0.163.0 smoke first exposed no Geoapify tools. A documented required-server startup override exposed one geocode attempt that failed; the initial capture omitted its error payload. A final diagnostic retry exposed no tools again, so the root cause remains unknown. Three bounded sessions, no successful Codex smoke and no fabricated fix. Session files under docs/evidence/stage4 retain these separate outcomes. No persistent client configuration was changed and no screenshots were captured because a credential-free authenticated settings view was not established. Owner screenshots remain pending.

## Stage 4 privacy and editorial work

Fetched all advertised branch/tag/PR refs for a wider history scan. The current files and main have no detected sensitive content after removing only generated ignored bytecode, but three older blobs reachable from PR #1 still contain owner-identity text. The earlier cleanup did not remove that advertised PR ref. Reported object IDs and affected refs only; did not repeat the private text. The actual key value was checked in memory and had no hits. GitHub's service noreply identities were distinguished from personal emails. Full-history zero-hit acceptance is blocked, and repository visibility stays private.

Wrote the canonical tutorial, a separate unpublished dev.to draft, all seventeen section 8 compliance rows, the nine-tool matrix, an unsent owner email draft and exact remaining owner steps. The three fixed tutorial incidents come from recorded build evidence: fallback-ID serialization mismatch, rejected optional matrix snaps and rejected tex-mex category. The unresolved live input and Codex failures are separately described, not invented fixed incidents. No license change, public post, email, install or CI run occurred.

## Stage 4 Sol review round 1 and response

Sol, Codex provider gpt-6.1-sol with reasoningEffort=xhigh, reviewed exact head f2141b4 and posted a review on PR #4. Zero actionable documentation defects were found. Independent verification passed 135 tests, byte-identical golden reports, eight JSON artifacts and 83 local links/anchors.

Accepted Sol's separate acceptance blockers: retained owner-identity blobs in old PR #1, incomplete live/customer/tool evidence and Codex smoke, and remaining screenshot/runtime/publication gates. No fixable finding was disputed. Kept the PR draft/open and the repository private; no merge, visibility change, license change, external publication or email. Recorded the response and requested a final Sol check of this review-record delta and refreshed privacy evidence.

## Stage 4 continuation: owner resolves demo-data and history gates

The owner directed continuation in the canonical checkout on stage4/submission-pack, PR #4. New authorization: keep Main Street Plumbing and twenty customer identities fictional, but use honestly labeled, publicly listed Midland addresses as demo locations. Real returned geocoding/routing/Places data must remain labeled live-derived, with no claimed affiliation or actual customer relationship. Do not weaken the building-confidence rule to force a result. Record both live paths and actual metrics, then complete Sol xhigh review and merge if clean and nonbreaking.

The owner also changed the privacy completion boundary: current tree and current branch history must have zero hits. Retained old PR #1 history is a known pre-publication owner item, with GitHub Support purge or delete-and-recreate from clean squashed history as the two options. No force-push workaround or history rewrite is authorized. The repo must remain private until that decision is resolved.

Execution plan: bounded public-address discovery, one twenty-customer CLI run plus one fresh-clone verification, one hosted Claude analysis covering all nine tools, a separately bounded Codex smoke, shared local validation/rendering, and exact evidence-linked comparison. Use a 20,000-metre candidate-search circle for MCP service-category observations, at most twenty candidates without pagination; classify them by acquired outbound route times against the same budget. The circle selects candidates only. A narrow implementation task adds validation of those acquired competitor routes to the existing report contract. No sampled-boundary polygon, real customer identity, credential file, installation or public posting is introduced.


### Live continuation findings before report completion

Twenty public customer locations passed the unchanged unique-building confidence rule after 39 total address-discovery requests (including the City Hall origin and rejected attempts). The sample identities remain fictional and sources/labels are in data/README.md. The first CLI attempt reached a real Isoline response but failed the original 2,000-position validation cap. A separate one-call diagnostic retained the full 14,758-position, three-ring response; geometry support is being corrected without simplification or weaker topology rules.

Claude Code executed seven preflight/origin/category/diagnostic calls successfully. The client exposes hosted structured output as JSON text in tool-result content, with no separate structuredContent field in its stream. Evidence preserves and parses that JSON; assistant prose is not the measurement source. The 833-category response contains specific trades including electrician, so the feedback must say no general trade-services umbrella or plumbing category, not no electrical category.

Codex's next smoke attempt exposed the actual failure: its ephemeral exec approval policy was never and the geocode tool required approval. The next scoped configuration applies the owner's existing authorization to geocode_address only, using documented per-tool approval_mode=approve; it does not change persistent settings or authorize other tools. The earlier failure remains saved.


### Completed live acquisition and deterministic import

The original hosted customer pass completed20 geocodes, a19-target customer matrix, one separate route, one20-candidate service search and one competitor matrix. It withheld row 4 because the server returned 700South Street for 700SJackson St despite both confidence scores1.0; REST had returned South Jackson Street. The final sample replaced that location with the public Greenwood district address 2700 FM 1379. A hosted follow-up geocoded the replacement and acquired a full20-target matrix. Prior failed/preliminary evidence remains retained. No REST point/time was substituted into an MCP result.

The revised full-geometry CLI exited 0:20 customers,20 known routes,20 in zone,100%,median 488 seconds,max 1085 seconds at DEMO-12,21635 metres,no outside/borderline/unknowncustomers. CLI service candidates:19 inside,1 outside,20 returned. The keyless imported MCP report is complete, approximation=true, with identical customer coordinates/times/verdicts and 20 sampled service candidates inside. Only 2 in-zone candidate IDs overlap across the different extents. The single hosted route diagnostic gave 81.539 seconds versus matrix 81 seconds forrow 1, both 856 metres. No outcome was invented to create an outside/borderline example; live FR-04 diversity remains unproved, while the offline fixture covers those branches.

All nine hosted tools succeeded across 33 Claude calls. Codex's scoped approval retry succeeded with one building result and confidence 1.0. Contact objects were stripped from parsed JSON text before commit; keys, local paths and emails are never retained. docs/evidence/stage4/normalize_mcp.py rebuilds the acquired MCP input from actual captured tool results with exact-input/index checks. The shared importer verifies artifact hashes and normalized competitor evidence and renders both reports without a key.

## Stage 4 current fresh-clone verification

A fresh remote clone of PR revision `4a250b72bca5b7ae9f15722c495bfa238318b14f` passed 156 tests on Python 3.14.9/macOS arm64. Synthetic golden and reconstructed captured MCP reports matched byte for byte. The exact README live runtime command exited 0: 20 evaluated, 100% in zone, median 488 seconds, maximum 1085 seconds, no outside/borderline customers, 19 sampled service candidates inside and 1 outside. It recorded 24 HTTP attempts and no Isoline polls. Keychain supplied only the live child environment; offline children received no key. The temporary clone was removed. Evidence: [fresh clone](docs/evidence/stage4/live/fresh-clone.json). No target-runtime or cross-platform pass is inferred.

## Stage 4 Sol implementation review and response

Requested a read-only T3 review using Codex provider, gpt-6.1-sol, reasoningEffort=xhigh of exact `4a250b7` versus pinned main. The brief required geometry topology/work-budget checks, MCP competitor artifact validation, normalization provenance, live metrics, privacy scope and truthful owner gates. Sol posted zero actionable findings and independently verified 156 tests, golden reports, MCP reconstruction, artifacts and coverage. Accepted the result on PR #4 and supplied the successful fresh-clone follow-up. Requested a separate final exact-head review of documentation/evidence updates. Actual review and response links are in [the review record](docs/evidence/stage4/review.md). No future review outcome is presumed.
