# ZonePilot submission pack

Updated November 2, 2026 for the [Geoapify Open Geospatial Program](https://geoapify.com), Batch #2. The [repository](https://github.com/cachetronaut/ZonePilot) is PUBLIC. Fresh private and anonymous public clones passed the corrected privacy scan at release HEAD `a17946fc491d58a81556c3654b3d3a091a9963a1`. MIT is unchanged. Only `main` was pushed and the recreated repository's PR list is empty. Publication verification is complete; final submission acceptance remains pending. No email was sent and no dev.to article was published. Internal target: November 8. Final deadline: November 15, 2026.

October 23 evidence records both live report pairs, all nine hosted tools, the second-client smoke and 156 passing tests at the then-tested implementation. Those are historical runtime results; November 2 verification inspected Git history and documents without executing project code or running CI. This docs-only reconciliation preserves the release implementation. Owner credit is Scout Squad. The November 2 instruction supersedes the original private-publication gate and makes the dev.to draft optional.

## Actual live results

The [CLI JSON](docs/evidence/stage4/live/cli/report.json), [CLI Markdown](docs/evidence/stage4/live/cli/report.md), [MCP JSON](docs/evidence/stage4/live/mcp/report.json) and [MCP Markdown](docs/evidence/stage4/live/mcp/report.md) use the same final twenty-row input and 1,200-second budget. Both resolve all twenty customers with twenty known routes, twenty inside, 100% of twenty classified, an in-zone median of 488 seconds, and a maximum of 1,085 seconds. The maximum is row 12, `DEMO-12`, 9600 Wright Dr, at 21,635 driving metres. There are no outside or borderline customers. The [comparison](docs/evidence/stage4/live/comparison.json) retains row-level results and input hashes.

The CLI uses full REST Isoline geometry. MCP uses `route_time_at_points`, `approximation=true`: route-time classification only at measured points; no continuous zone. CLI broad `service` observations are 19 inside and 1 outside from 20 returned; MCP observations are 20 inside and 0 outside from 20 returned. Both have `coverage=sampled` and `cap_reached=true`, with no pagination. These are not verified plumbing competitors. Their search extents differ; the MCP 20,000-metre circle selects candidates only, which are then classified by acquired routes.

Main Street Plumbing and all twenty customer identities are fictional. The origin, 300 N Loraine St at Midland City Hall, and customer addresses are real public demo locations, without affiliation or actual customer relationships. [Data provenance](data/README.md) records this owner-approved distinction. Row 4 changed from 700 S Jackson St to 2700 FM 1379 after hosted MCP returned South Street at confidence 1.0 while REST returned South Jackson Street. The preliminary session remains preserved; the final reports use the replacement and final twenty-target matrix.

## Compliance matrix

| Item | Status | Evidence and remaining action |
| --- | --- | --- |
| CR-01 dates and one fix round | Recorded; final completion pending | November 8 internal target, November 15 deadline. One permitted fix round of up to seven days; no extension assumed. |
| CR-02 business-only scope | Met in current artifacts | [Tutorial](TUTORIAL.md): outbound service-budget decisions, no resident-access analysis. |
| CR-03 public MIT repository | Public repository verified November 2 | [LICENSE](LICENSE) unchanged; private and anonymous public clean clones passed. Final program acceptance remains pending. |
| CR-04 clean-clone README run | Passed on macOS / Python 3.14.9 | [October 23 runtime clone](docs/evidence/stage4/live/fresh-clone.json) at `4a250b7`: 156 tests, byte-identical synthetic and captured MCP reports, successful live CLI with the same metrics. The PR branch was selected before merge; runtime commands match README. Temporary clone removed. |
| CR-05 environment-only key | Environment-backed configuration and scan evidenced | [Claude config](docs/evidence/stage4/live/mcp-preflight.json) and [Codex override](docs/evidence/stage4/live/codex-smoke-approved.json) use environment-backed headers. No persistent client configuration was changed. The [October 23 privacy scan](docs/evidence/stage4/privacy-scan.json) checked the actual key, identity, email and local-path patterns with zero current-branch hits. November 2 scans did not read the key. |
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
| CR-17 repo and dev.to tutorial | Repository tutorial public; dev.to optional and unpublished | [Canonical tutorial](TUTORIAL.md) reflects publication. [dev.to draft](docs/drafts/devto.md) retains October 23 text. No dev.to URL exists; owner made publication optional November 2. Program acceptance of that difference remains unconfirmed. |

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

## Publication verification

The recreated repository existed private and empty on November 2. The confirmed repository-scoped read/write deploy key pushed only `main` at `a17946fc491d58a81556c3654b3d3a091a9963a1`. No token was requested during this continuation and no keychain access occurred. Private clone verification passed before visibility changed. Anonymous HTTPS cloning with credential helpers disabled then passed after publication.

Each fresh clone contained four commits, 205 reachable objects and 190 files. Scans covered reachable blob contents, commit metadata/messages and paths for owner identity, personal email, absolute local paths and credential contexts. Four 32-hex hits were ID fields; reviewed candidates were environment references or synthetic sentinels. Git integrity passed, MIT SHA-256 was `48e6c1016b798bf298753aaba5caafa96505ed2a7bb626ddaefac5a452a59b67`, and the PR list was empty. The actual Geoapify key was not read or compared. The owner's unchanged-HEAD October 23 exact-key scan remains historical evidence.

The [old scan](docs/evidence/stage4/privacy-scan.json) describes the former repository's retained PR #1 objects. Those refs were not transferred. This verification covers the recreated remote's advertised history and fresh clones, not inaccessible GitHub caches or local audit objects. Former PR links in historical evidence no longer resolve to reviews in this new repository.

## Remaining submission steps

1. Verify Python 3.15.1 and Linux/Windows commands and deterministic report comparisons. No new runtime checks were run for publication.
2. Capture actual Claude Code and Codex CLI setup screenshots only after establishing credential-safe views without account details, local paths or unrelated windows. No safe view was established in this continuation; screenshots remain pending.
3. Retain the FR-04/AC-08 live outcome-diversity gap for final review. The live sample has no outside or borderline customers; offline fixtures alone exercise those outcomes.
4. Confirm final program acceptance, including license-holder confirmation and the outstanding evidence. Keep payment/account details outside the repository.
5. The dev.to draft is optional and unpublished under the November 2 owner instruction. If later chosen, reconcile it with the canonical public tutorial, rewrite relative links and record the real URL. No publication is authorized by this task.
6. Review the filled [UNSENT email draft](docs/drafts/geoapify-email.md). It cites the verified public repository and exact implementation release revision. Do not send it during this task; required evidence and final owner acceptance remain pending.

## Review disposition

Historical local evidence records the Sol review and 156 tests from October 23. No new implementation review or runtime pass is claimed. November 2 work used Sol High only, skipped CI and changed documentation only after the verified release push. Public visibility does not establish final program compliance.
