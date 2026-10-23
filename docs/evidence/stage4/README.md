# Stage 4 evidence, October 23, 2026

The `live/` directory contains real acquisitions after the owner approved labeled
public demo locations. Business/customer identities remain fictional; the addresses
and returned Places are real and imply no affiliation. Authored offline fixtures
remain under `tests/fixtures/sample`. Earlier failed attempts below are preserved.

## Completed live outcomes

| Check | Observed result | Evidence |
| --- | --- | --- |
| Approved input discovery | City Hall and final twenty customer locations pass unchanged unique-building confidence rules | [data provenance](../../../data/README.md), [initial](live/discovery.json), [additional](live/discovery-additional.json), [outer](live/discovery-outer.json), [route checks](live/discovery-outer-times.json) |
| CLI | Exit 0, 20 evaluated, 20 known routes, 100% in zone, 488-second median; maximum 1085 seconds/21635 metres at DEMO-12; 0 outside/borderline | [JSON](live/cli/report.json), [Markdown](live/cli/report.md) |
| Hosted MCP, approximation=true | Same 20 customer coordinates, times and verdicts; complete keyless import; no continuous zone | [JSON](live/mcp/report.json), [Markdown](live/mcp/report.md), [acquired input](live/agent-input/evidence.json) |
| Sampled Places | CLI 19 in/1 out; MCP 20 in/0 out; 20 returned and cap reached each; only 2 in-zone IDs overlap | [Comparison](live/comparison.md), [machine-readable comparison](live/comparison.json) |
| Nine hosted tools | All 9 successfully invoked across 33 Claude calls | [coverage](live/tool-coverage.json), [preflight](live/mcp-preflight.json), [preliminary customers/competitors](live/mcp-customers.json), [final 20 matrix](live/mcp-final-customers.json) |
| Second client | Codex 0.163.0 successful building geocode, confidence 1.0 | [successful scoped approval](live/codex-smoke-approved.json), [earlier policy failure](live/codex-smoke.json) |
| Full live Isoline | 14,758 positions, 3 rings, full shape accepted without simplification after bounded validator fix | [initial failure diagnostic](live/isoline-diagnostic.json), [geometry contract](../../live-geometry-contract.md) |
| Current privacy scope | Current tree/current branch zero hits; 3 retained PR #1 identity blobs remain owner pre-publication item | [scan](privacy-scan.json) |

The final comparison's MCP path is `approximation=true`: Route-time classification
only at measured points; no continuous zone. Customer times agree in this sample,
but the methods are not interchangeable. The separate hosted route for row 1 was
81.539 seconds versus matrix 81 seconds, both 856 metres. No live customer was outside
or borderline; synthetic fixtures alone demonstrate those branches. Broad service
candidates are not verified plumbing competitors or a market census.

## Acquisition and normalization

Claude Code 2.1.309 used ephemeral config, environment-backed headers, allowed
Geoapify tools only, no shell/file tools and no session persistence. The stream
projects structured results as JSON text; `structuredContent` is null in that
capture, so no separate field capture is claimed. Actual arguments and typed JSON
results are retained after redaction and removal of unrelated contact objects.
Assistant prose is not the source of measurements. Every session/result wrapper
and normalized competitor artifact carries approximation=true.

The preliminary hosted row 4 returned 700 South Street for 700 S Jackson St despite both
confidence values 1.0. REST had returned South Jackson Street. That input was replaced
with the documented public Greenwood district address, 2700 FM 1379. A new hosted
geocode and full 20-target matrix supply the final report. Earlier evidence is not
rewritten to hide this discrepancy. No REST coordinates or measurements were
substituted into MCP results.

The [normalizer](normalize_mcp.py) is a keyless, network-free reproducibility aid:

```sh
python3.14 -B -m docs.evidence.stage4.normalize_mcp --output-dir reports/mcp-input
python3.14 -B -m zonepilot.report --import-agent reports/mcp-input/evidence.json --output-dir reports/mcp-rebuilt
```

It verifies exact captured arguments, unique accepted geocodes, matrix indexes,
units and candidate identity mapping. The shared importer verifies hashes and
competitor counts/records against the acquired normalized route artifact. The
report timestamp uses the final session artifact's write time immediately after
client exit. Hashes prove byte integrity, not independent proof of server execution.

Codex's explicit policy error was `MCP tool call requires approval, but approval
policy is never`. The successful retry applied the owner's existing authorization
only to geocode_address via its documented per-tool approval setting, with only
that tool exposed. No persistent config changed. A client exit 0 alone never
establishes a successful tool call; the successful tool result is retained.

## Budget and capture boundary

The owner ceiling is 3,000 requests/day. This continuation recorded 46 REST discovery
requests, one separate Isoline diagnostic and 25 HTTP attempts in the completed CLI,
plus 33 Claude tool invocations and one successful Codex smoke. The first failed
CLI stopped after origin/Isoline; its exact retry count was not instrumented.
The [fresh-clone CLI](live/fresh-clone.json) added 24 HTTP attempts and zero Isoline polls; it reproduced the live metrics, passed 156 tests and matched both report pairs byte for byte. Its temporary clone was removed. Earlier failed-origin
work used only a handful of bounded calls. Client initialization/discovery exchanges
and billed credits are not an account-usage total; the key was never logged.
The work remains far below the daily request ceiling, with no pagination or
unbounded retries. No installs or downloaded code ran.

No client-config screenshots were captured because a credential-free authenticated
UI view was not established. The owner must verify the view contains only environment
references before taking either screenshot. Text snippets do not satisfy that item.
Python 3.15.1/Linux/Windows verification and public submission remain pending.

## Historical attempts, superseded for current live acceptance

- [Key verification](key-verification.json), [original CLI failure](live-cli.json),
  [old fresh-clone check](fresh-clone.json): invented origin returned cities; 0 customers.
- [Original Claude session](agent-session.json), approximation=true: connected,
  geocoded the invented origin and stopped. Real map payloads were then omitted
  under the earlier unamended data gate.
- [Codex initial](codex-smoke-initial.json), [required-server retry](codex-smoke-required.json)
  and [diagnostic retry](codex-smoke.json): did not prove successful smoke; earlier
  error omissions mean their cause cannot be retroactively asserted.

See [SUBMISSION.md](../../../SUBMISSION.md) for owner publication steps and
[review record](review.md) for the actual Sol review rounds.
