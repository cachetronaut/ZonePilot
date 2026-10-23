# Build decisions, 2026-10-22

The owner authorized offline implementation, privacy history replacement, PR review and a merge only when clean and safe. The repository stays private.

## Pre-build decisions

- Owner credit is Scout Squad; commit identity is the supplied GitHub noreply address. Python minimum is 3.14.9 and target is 3.15.1. The latter is unavailable locally; no interpreter download or installation was attempted.
- B06 is closed for implementation: AI-assisted handwritten stdlib adapters from the pinned official schemas, with recorded hashes and no generator execution.
- The build coordinator ratifies B07 limits in PROMPTLOG.md and README: finite deadlines/retries/polls, 2 MiB response cap, 2,000 geometry positions and 32 rings, no cache, new output directory containing a complete report bundle. These do not assert program-account allowances.
- B05 public visibility and final license-holder confirmation remain owner-controlled. Existing MIT holder cachetronaut is preserved.

## Prompt/PRD conflicts

| Prompt | Authoritative PRD and build handling |
| --- | --- |
| POST polygon Places filter | FR-18 and section 11 explicitly choose rectangle metadata plus local membership. Implemented that contract; polygon support is documented, not denied. |
| Invented sample under data/sample_* | Section 12 reserves those for B03-approved live inputs. The authored Main Street Plumbing example and twenty customers live under tests/fixtures/sample. data/README.md explains the pending live files. |
| Recorded offline fixtures | Section 10.6 calls for authored synthetic API-shaped responses, explicitly not recordings. Fixtures are labeled synthetic. |
| Sampled-boundary MCP approximation | Owner approved route-time-at-points on 2026-10-23. Enable that point-only importer; sampled-boundary/hull methods still lack their required contract and remain rejected. |
| Twelve hosted tools | The pinned/public table lists eleven, including geocode_structured_address and combine_geometries. Authenticated tools/list remains pending. No isoline tool is listed. |
| Live sample if a key is present | No key was present. Even with one, B01 entitlement and B03 permitted-evidence policy must close before signing off or publishing real outputs. |
| README run contract section 12.3 | In the checked-in PRD it is section 12.2; section 12.3 describes tutorial deliverables. Both were followed within this build scope. |

## History cleanup

The private default branch was replaced using a force-with-lease push with one scrubbed initial commit, b2dff88. The old docs/prd-review branch was deleted in the same atomic push because it retained the former history. Local reflogs expired and unreachable objects were pruned. The initial local reachable-history count was one, and git log -p plus all tracked files passed scans for the former legal name, personal email patterns, credential patterns and absolute machine paths.

New implementation commits follow that clean root. GitHub may retain hidden historical PR refs, cached diffs or server backups. A force push cannot prove those server-side objects were erased. Before eventual public release, the owner must resolve any retained server-side history with GitHub or publish a new clean repository; this build does not claim private cached objects were purged.

## Remaining gates

B02 customer method selection is approved on 2026-10-23. B01, B03 and B04 remain open; MCP competitor route-evidence/search-extent approval is also pending. The owner confirmed that wholly fictional samples stay under tests/fixtures/sample and live data/sample_* remain pending. Stage 4 still needs tutorial completion, permitted live comparison and screenshots, all nine hosted tools, platform/target-runtime checks, dev.to publication, final attribution/privacy review, owner-controlled visibility and program submission. Offline test success does not close these gates.
