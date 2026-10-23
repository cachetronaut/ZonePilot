# Hosted agent pack

Every agent output must say `approximation=true`. There is no native hosted Isoline tool in the pinned inventory. This pack is a setup and sequencing artifact; authenticated setup, B02 method approval, B03 live inputs and B04 evidence are PENDING. It does not claim a completed live comparison.

Use only approved fictional inputs. Geoapify receives tool arguments; the chosen AI provider can also receive prompts and tool results. Never put the key in prompts, URLs, source files or literal configuration values. Stop if environment-backed header authentication fails. Do not fall back to a query-key URL.

## Client configuration

Observed locally on 2026-10-22: Codex CLI 0.163.0 and Claude Code 2.1.308. Cursor was not available on PATH. No authenticated connections were tested. These snippets follow the official references below and contain environment references only. Launch the client from a process where GEOAPIFY_API_KEY is set. Confirm it is nonblank without printing it before connecting. GUI apps may need a restart from that environment.

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

Follow [prompts.md](prompts.md) in order. Require the gate check before acquisition. Record client version, date, sanitized tool arguments, structured results, status and purpose. Capture tools/list before calls. The public list currently has eleven names including two beyond the promised nine. Treat any different live inventory as a contract change to inspect, not a reason to invent a missing tool.

The importer uses the [shared schema](../../docs/report-schema.md). The agent exports the root contract without summary or run_status, with the three derived customer booleans null. Export only acquired evidence, never invented measurements. Each evidence artifact needs a relative path and SHA-256. Place artifacts beside the import file. Local import is keyless:

```sh
python3.15 -m zonepilot.report --import-agent evidence.json --output-dir reports/agent
```

While B02 remains open, this command rejects MCP reports with a method-pending diagnostic. The pack does not silently turn a diagnostic polygon into a primary drive-time zone. A proposed route-time-at-points implementation exists behind an explicit approval gate; its customer verdicts follow measured outbound times, and it makes no coverage claim between points. Competitor membership needs its own acquired route evidence before that method can support requested competitor sections.

## Remaining evidence

- Full 20-row run in one named client and a smoke run in the other.
- All nine successful hosted tool calls and sanitized arguments/results.
- Client setup screenshots with no credentials, account information or local machine paths.
- Identical approved inputs across CLI and MCP and a row-by-row comparison retaining disagreements.
- Explicit sampled competitor search extent and method limitations in each standalone report.

No client installation, local MCP server or dependency is included in ZonePilot.
