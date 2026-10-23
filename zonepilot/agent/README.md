# Hosted agent pack

Every agent output must say `approximation=true`. The authenticated hosted inventory has twelve tools and no Isoline tool. The owner approved `route_time_at_points` and the bounded competitor evidence contract on October 23, 2026. Claude Code 2.1.309 completed all nine required tools and the final twenty-customer report. Codex CLI 0.163.0 completed a separate successful geocode smoke call. See [session evidence](../../docs/evidence/stage4/README.md) and the [live comparison](../../docs/evidence/stage4/live/comparison.md).

Main Street Plumbing and all customer identities are fictional; `data/sample_*` uses labeled real public Midland demo addresses with no affiliation or customer relationship. Geoapify receives tool arguments; the AI provider can receive prompts and results. Never put the key in prompts, URLs, source files or literal config values. Use environment-backed headers; stop if authentication fails. No query-key fallback.

## Client configuration

Historical setup record, 2026-10-22: Codex CLI 0.163.0 and Claude Code 2.1.308. Cursor was not available on PATH. No authenticated connections were tested in that earlier session; Stage 4 results are linked above. These snippets follow the official references below and contain environment references only. Launch the client from a process where GEOAPIFY_API_KEY is set. Confirm it is nonblank without printing it before connecting. GUI apps may need a restart from that environment.

Claude Code, project `.mcp.json`:

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

Codex CLI, merge this table into the user's Codex `config.toml`:

```toml
[mcp_servers.geoapify]
url = "https://api.geoapify.com/v1/mcp"
env_http_headers = { "x-api-key" = "GEOAPIFY_API_KEY" }
```

Cursor, project `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "geoapify": {
      "url": "https://api.geoapify.com/v1/mcp",
      "headers": {"x-api-key": "${env:GEOAPIFY_API_KEY}"}
    }
  }
}
```

Documentation checked 2026-10-22: [Claude environment expansion](https://code.claude.com/docs/en/mcp#environment-variable-expansion-in-mcp-json), [Codex environment headers](https://developers.openai.com/codex/mcp), [Cursor interpolation](https://cursor.com/docs/mcp#config-interpolation), [Geoapify authentication](https://www.geoapify.com/mcp/). Snippet parsing is not proof that a particular installed client can authenticate or export evidence.

## Run and export

Follow [prompts.md](prompts.md) in order. Require the gate check before acquisition. Record client version, date, sanitized tool arguments, structured results, status and purpose. Capture tools/list before calls. The pinned/public list has eleven names. Stage 4 Claude discovery returned twelve, adding get_timezone and still no isoline. This observed drift does not replace any promised tool. Compare live schemas before later calls.

The importer uses the [shared schema](../../docs/report-schema.md). The agent exports the root contract without summary or run_status, with the three derived customer booleans null. Export only acquired evidence, never invented measurements. Each evidence artifact needs a relative path and SHA-256. Place artifacts beside the import file. Local import is keyless:

```sh
python3.15 -m zonepilot.report --import-agent evidence.json --output-dir reports/agent
```

This command accepts acquired `route_time_at_points` evidence: a known outbound time at or below the budget is in zone; a larger time is outside; missing, failed or unreachable routes have unknown membership. There is no continuous zone or coverage claim between points. The report must include the exact limitation `Route-time classification only at measured points; no continuous zone.` and `zone.approximation=true`. Sampled hulls and primary diagnostic polygons remain rejected. Requested competitors follow the [approved contract](../../docs/mcp-competitor-contract.md): category service, business-centered 20,000-metre search, limit20, no pagination, acquired routes for unique valid candidates and sampled counts checked against a normalized evidence artifact. This does not verify plumbing competition.

## Verified capture and remaining owner evidence

The live Claude run used ephemeral configuration, disabled shell/file tools and no session persistence. Its stream presents tool structured output as a JSON text copy. The [Stage 4 normalizer](../../docs/evidence/stage4/normalize_mcp.py) parses typed results, validates exact captured arguments and indexes, builds the shared input and keeps approximation labels. It does not call a network service. The final twenty-target matrix supersedes the preliminary nineteen-target matrix after a wrong-street geocode was replaced; both sessions remain available.

Codex exec initially blocked the geocoder because its noninteractive approval policy was never. The successful smoke used this additional narrowly scoped table for the owner-authorized call, as documented by [Codex configuration](https://learn.chatgpt.com/docs/config-file/config-reference):

```toml
[mcp_servers.geoapify.tools.geocode_address]
approval_mode = "approve"
```

The smoke exposed only `geocode_address` via `enabled_tools`, used `required=true`, an ephemeral session and read-only shell sandbox. Interactive reviewers can instead approve the call when prompted. This is not a reason to authorize unrelated tools. No persistent client configuration changed.

Actual setup screenshots remain owner handoff. Capture only a verified view containing environment references, never expanded headers, account details or local paths. A configuration snippet is not a screenshot. Cursor's snippet remains untested; the successful named clients are Claude Code and Codex CLI. No client installation, local MCP server or dependency is included in ZonePilot.
