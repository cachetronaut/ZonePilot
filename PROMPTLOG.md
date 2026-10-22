# ZonePilot prompt log

## 2026-10-22, build session opened

Instruction summary: build PRD Stages 1–2 and the Stage 3 agent pack using stock Python and no dependencies; keep this repository private; use the GitHub noreply identity; scrub owner credit and replace history before code; verify locally, then drive Sol xhigh review rounds on a PR. The PRD wins conflicts. No credential was supplied or requested.

Read both authoritative documents fully before coding. No product code existed. Changed the owner to Scout Squad and the supported runtime to Python 3.14.9 minimum, Python 3.15.1 target. No downloaded code or installers were run.

Observed environment failures: the first GitHub request failed with `error connecting to api.github.com` inside the sandbox. Retrying with authorized network access succeeded and confirmed the repository is private. The requested Python policy path was missing; found and read the same policy in the installed plugin. Python 3.15.1 is not installed; Python 3.14.9 is available. Target-runtime verification remains PENDING, with no interpreter installation attempted.

Live runs: PENDING. GEOAPIFY_API_KEY is absent. No live Geoapify request was attempted.

PRD conflicts identified: the build prompt asks for a polygon Places filter, but FR-18 and section 11 require rectangle metadata and local membership. Follow the PRD. The prompt requests synthetic samples in live-demo paths, but section 12 reserves those for B03-approved inputs. Keep fixtures separate pending clarification. The requested sampled-boundary agent method lacks the PRD-required accuracy/cost contract; asked the owner whether to approve the smaller per-customer route-time method instead. Do not silently implement a hull.

Adapter authoring decision B06: AI-assisted, manually inspected standard-library adapters derived from the pinned official OpenAPI specifications. Read specifications as data only. No third-party generator.

Build coordinator decision B07: no persistent cache; output directory defaults to reports/run and contains report.json, report.md and evidence artifacts. Refuse an existing output directory. Socket timeout 10 seconds, whole acquisition deadline 120 seconds, at most 60 HTTP attempts, three attempts per request, backoffs 1 and 2 seconds, at most five isoline polls spaced one second apart, response cap 2 MiB, geometry cap 2,000 total vertices and 32 rings. Retry only transport failures, 429 and 5xx within the deadline. Bound Retry-After and stop when it cannot fit. These are implementation budgets, not account-entitlement claims.
