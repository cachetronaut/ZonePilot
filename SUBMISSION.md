# ZonePilot submission pack

Prepared October 23, 2026 for the [Geoapify Open Geospatial Program](https://geoapify.com), Batch #2. Both live report pairs are complete, all nine required tools have successful invocation evidence, and the second-client Codex smoke succeeded. Final submission is NOT READY. The repository remains PRIVATE; nothing has been published or emailed. The existing MIT license is unchanged. Internal target: November 8. Final deadline: November 15, 2026.

The [PRD and owner amendment](docs/prd.md#owner-amendment-for-stage-4-2026-10-23) distinguish private Stage 4 completion from public submission. Private completion is allowed after recorded live results, a clean Sol xhigh review and no breaking changes, with zero hits in current working files and current branch history. Integrated and fresh-clone verification passed 156 tests, golden replay and captured MCP reconstruction. The fresh live CLI reproduced the recorded metrics. The refreshed privacy scan passes for current files and branch history; Sol xhigh found zero actionable findings in the implementation at `4a250b7`; the follow-up evidence and exact-head merge disposition are tracked in [PR #4](https://github.com/cachetronaut/ZonePilot/pull/4). Retained old PR #1 history is an owner pre-publication item, not a private Stage 4 blocker.

## Actual live results

The [CLI JSON](docs/evidence/stage4/live/cli/report.json), [CLI Markdown](docs/evidence/stage4/live/cli/report.md), [MCP JSON](docs/evidence/stage4/live/mcp/report.json) and [MCP Markdown](docs/evidence/stage4/live/mcp/report.md) use the same final twenty-row input and 1,200-second budget. Both resolve all twenty customers with twenty known routes, twenty inside, 100% of twenty classified, an in-zone median of 488 seconds, and a maximum of 1,085 seconds. The maximum is row 12, `DEMO-12`, 9600 Wright Dr, at 21,635 driving metres. There are no outside or borderline customers. The [comparison](docs/evidence/stage4/live/comparison.json) retains row-level results and input hashes.

The CLI uses full REST Isoline geometry. MCP uses `route_time_at_points`, `approximation=true`: route-time classification only at measured points; no continuous zone. CLI broad `service` observations are 19 inside and 1 outside from 20 returned; MCP observations are 20 inside and 0 outside from 20 returned. Both have `coverage=sampled` and `cap_reached=true`, with no pagination. These are not verified plumbing competitors. Their search extents differ; the MCP 20,000-metre circle selects candidates only, which are then classified by acquired routes.

Main Street Plumbing and all twenty customer identities are fictional. The origin, 300 N Loraine St at Midland City Hall, and customer addresses are real public demo locations, without affiliation or actual customer relationships. [Data provenance](data/README.md) records this owner-approved distinction. Row 4 changed from 700 S Jackson St to 2700 FM 1379 after hosted MCP returned South Street at confidence 1.0 while REST returned South Jackson Street. The preliminary session remains preserved; the final reports use the replacement and final twenty-target matrix.

## Compliance matrix

| Item | Status | Evidence and remaining action |
| --- | --- | --- |
| CR-01 dates and one fix round | Recorded; final completion pending | November 8 internal target, November 15 deadline. One permitted fix round of up to seven days; no extension assumed. |
| CR-02 business-only scope | Met in current artifacts | [Tutorial](TUTORIAL.md): outbound service-budget decisions, no resident-access analysis. |
| CR-03 public MIT repository | Owner publication gate pending | [LICENSE](LICENSE) unchanged; repository must stay private until the retained-history item below is resolved. Final holder confirmation remains owner-owned. |
| CR-04 clean-clone README run | Passed on macOS / Python 3.14.9 | [Current remote clone](docs/evidence/stage4/live/fresh-clone.json) at `4a250b7`: 156 tests, byte-identical synthetic and captured MCP reports, successful live CLI with the same metrics. The PR branch was selected before merge; runtime commands match README. Temporary clone removed. |
| CR-05 environment-only key | Environment-backed configuration and scan evidenced | [Claude config](docs/evidence/stage4/live/mcp-preflight.json) and [Codex override](docs/evidence/stage4/live/codex-smoke-approved.json) use environment-backed headers. No persistent client configuration was changed. The [privacy scan](docs/evidence/stage4/privacy-scan.json) checks the actual key, identity, email and local-path patterns; current files and branch history have zero hits. |
| CR-06 tutorial, prompt log, lessons | Draft prepared with actual results | [TUTORIAL.md](TUTORIAL.md), [PROMPTLOG.md](PROMPTLOG.md), failed-attempt records and final comparison. Capture omissions are explicit. |
| CR-07 Geoapify backlinks | Present in repository documents | [README](README.md) and [tutorial](TUTORIAL.md) link to Geoapify. Recheck the synchronized public versions before sending. |
| CR-08 adaptation permission | Recorded | Tutorial permits an adapted completed tutorial with Scout Squad author credit after publication gates pass. |
| CR-09 Combine OpenAPI + MCP track | Live comparative evidence recorded | [Pinned spec-derived adapters](docs/api-provenance.md), [shared report schema](docs/report-schema.md), both live report pairs and [comparison](docs/evidence/stage4/live/comparison.json). MCP remains an approximation. |
| CR-10 nine tools and real REST Isoline | Successful evidence recorded | Nine-tool matrix below; [full geometry record](docs/live-geometry-contract.md) and [CLI report](docs/evidence/stage4/live/cli/report.json). |
| CR-11 drive-time polygons | Live evidence recorded | CLI uses the full 14,758-position, three-ring Isoline, with local membership and no radius fallback. Sol xhigh reviewed the full geometry change with zero actionable findings. |
| CR-12 incremental prompt log | Retained build record present | [PROMPTLOG.md](PROMPTLOG.md) starts before implementation. The continuation records live failures, fixes, acquired results and fresh-clone checks; no reconstructed missing sessions are claimed. |
| CR-13 three genuine failures | Documented with evidence | Tutorial records fallback-ID encoding, optional matrix snaps and valid tex-mex category rejection, each with diagnosis, fix and recheck. |
| CR-14 two client screenshots and feedback | Partial; screenshots pending | Both clients now have successful invocation evidence. Dedicated missing-isoline feedback is written. No safe authenticated UI capture was established; actual screenshots remain owner handoff. |
| CR-15 completed manual checklist | Live and fresh-clone results recorded | The [README checklist](README.md#manual-acceptance-checklist) records actual passes. Runtime/platform, screenshot and publication items remain unchecked until evidenced. FR-04 live outcome diversity is not established. |
| CR-16 demo provenance and B03 | Owner-amended data policy applied | [PRD amendment](docs/prd.md#owner-amendment-for-stage-4-2026-10-23), [data sources](data/README.md): fictional identities, real public locations, live-derived provider evidence, no affiliation. Do not call the entire dataset fictional. |
| CR-17 repo and dev.to tutorial | Synchronized local drafts; publication pending | [Canonical tutorial](TUTORIAL.md), [unpublished dev.to draft](docs/drafts/devto.md). Owner must publish and record the actual URL and matching revision. |

FR-04 and AC-08 outcome diversity remains demonstrated by the offline fixture only. The live twenty-minute sample has no outside or borderline customer. This is disclosed under the owner's private-completion decision; it is not a claimed live Must pass or a waiver of final program review. Python 3.15.1, Linux and Windows verification remains pending under NFR-06/AC-09.

## Nine-tool evidence matrix

All hosted analysis retains `approximation=true`. Route-time classification only at measured points; no continuous zone. These rows cite successful captured results, not discovery alone. All captures are dated October 23, 2026 and retain sanitized arguments, tool IDs and result status.

| Family | Required tool | Successful evidence and purpose |
| --- | --- | --- |
| Geocoding | `geocode_address` | [Preflight](docs/evidence/stage4/live/mcp-preflight.json) accepts the origin; [customer session](docs/evidence/stage4/live/mcp-customers.json) records twenty initial geocodes; [final session](docs/evidence/stage4/live/mcp-final-customers.json) resolves the replacement row 4. A successful tool result can still fail address review. |
| Geocoding | `reverse_geocode_coordinates` | [Preflight](docs/evidence/stage4/live/mcp-preflight.json), one origin-context diagnostic; does not overwrite the accepted forward result. |
| Places | `list_place_categories` | [Preflight](docs/evidence/stage4/live/mcp-preflight.json), one successful category listing. No plumbing or general trade-services umbrella; specific electrician and carpenter categories exist. |
| Places | `search_places` | [Customer session](docs/evidence/stage4/live/mcp-customers.json), one `service` search centered on the origin, radius 20,000 metres, limit twenty; sampled broad-service observations only. |
| Routing | `calculate_route` | [Customer session](docs/evidence/stage4/live/mcp-customers.json), one row 1 route diagnostic: 81.539 seconds against the matrix's 81 seconds. It does not replace the matrix value. |
| Routing | `calculate_route_matrix` | [Customer session](docs/evidence/stage4/live/mcp-customers.json), preliminary nineteen-target customer matrix and twenty-candidate competitor matrix; [final session](docs/evidence/stage4/live/mcp-final-customers.json), authoritative twenty-target customer matrix. |
| Geometry | `transform_geometry` | [Preflight](docs/evidence/stage4/live/mcp-preflight.json), center of a synthetic diagnostic polygon; not a service zone. |
| Geometry | `evaluate_spatial_relation` | [Preflight](docs/evidence/stage4/live/mcp-preflight.json), two successful contains diagnostics for interior and exterior synthetic points. |
| Geometry | `measure_geometry` | [Preflight](docs/evidence/stage4/live/mcp-preflight.json), area and units for the same synthetic diagnostic polygon. |

Claude Code 2.1.309 recorded 7, 24 and 2 successful calls in those three sessions respectively. Its stream exposes structured JSON text in tool-result content, not a separate `structuredContent` field. The [deterministic normalizer](docs/evidence/stage4/normalize_mcp.py) produces [agent-input/evidence.json](docs/evidence/stage4/live/agent-input/evidence.json); local keyless import computes summaries and renders both formats from validated evidence. The final twenty-target matrix supersedes the preliminary nineteen-target matrix, with the rejected row 4 discrepancy retained.

[Codex CLI 0.163.0 smoke](docs/evidence/stage4/live/codex-smoke-approved.json) succeeded with one geocode under scoped `approval_mode=approve`. The [prior noninteractive failure](docs/evidence/stage4/live/codex-smoke.json) records the `never` approval-policy conflict. No persistent config was changed. The twelve-tool inventory still has no isoline; REST Isoline evidence remains distinct from hosted geometry diagnostics.

## Privacy disposition

The [refreshed scan](docs/evidence/stage4/privacy-scan.json) finds zero hits in current working files and current branch history for owner identity, personal emails, the actual key and absolute local paths. Three owner-identity blobs remain retained through old PR #1. The scan includes all locally stored objects and fetched advertised branch/tag/PR refs; inaccessible server caches are outside its coverage. This is not an all-history-clean claim.

Under the current owner amendment, retained old PR #1 history is a pre-publication owner item and does not alone block private Stage 4 completion. Before public visibility, the owner must choose and complete one of exactly two options:

1. Obtain a GitHub Support purge of the retained sensitive PR history, then verify removal and rescan.
2. Delete and recreate the repository from clean squashed history, then verify the new repository and rescan before making it public.

Keep the repository private until that resolution is complete. Deleting a local audit ref does not purge GitHub retention. No force push, history rewrite, repository deletion or visibility change is authorized or performed by this document task.

## Exact remaining owner steps

1. Complete Python 3.15.1 and Linux/Windows command verification and deterministic report comparisons. Record each environment and result. Keep unavailable checks pending, and retain the disclosed FR-04/AC-08 live outcome-diversity gap for final acceptance review.
2. Capture actual authenticated setup screenshots for Claude Code and Codex CLI only after establishing views without expanded credentials, account information, local paths or unrelated windows. If no safe view exists, leave the screenshots pending. Snippets are not screenshot evidence.
3. Resolve old PR #1 retention through GitHub Support purge OR delete-and-recreate from clean squashed history before public visibility. Verify the chosen result and rescan the publication repository. Keep it private until completed. No force-push workaround is authorized.
4. Confirm the MIT holder and private account/payment details outside the repository. The existing license remains unchanged. Successful captured calls establish the demonstrated operations, not unmeasured billing, quota or entitlement guarantees for future runs.
5. Reconcile every FR, NFR, AC and CR against evidence, including the disclosed live diversity limitation. Confirm the final submission is acceptable, then make the approved clean repository public yourself. Verify a public clean clone and update all links if the repository location changes.
6. Refresh the [dev.to draft](docs/drafts/devto.md) from the final canonical tutorial, rewriting relative links to the publication repository's GitHub `main` URLs. Publish it yourself. Record the actual dev.to URL and synchronized repository revision in README, TUTORIAL.md and this pack, then verify both backlinks.
7. Fill and send the [UNSENT Geoapify email draft](docs/drafts/geoapify-email.md) through the existing program contact channel only after the submission requirements pass. Include the public repository, tutorial URL and exact revision. Keep payment/account information outside the repository and retain the sent revision privately.

## Review disposition

The [Sol review record](docs/evidence/stage4/review.md) includes the clean implementation review of `4a250b7` and the implementer response. Integrated and fresh-clone verification passed. The [PR #4 discussion](https://github.com/cachetronaut/ZonePilot/pull/4) records the final exact-head follow-up review and merge disposition; private merge requires a clean review and no breaking changes. The previous live-origin and Codex blockers have successful continuation evidence; the old requirement to block private Stage 4 solely on retained PR #1 history is superseded by the owner amendment. Public release remains owner-gated.
