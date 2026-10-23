# API provenance

Read as data on 2026-10-22. No downloaded code was executed.

Pinned revision: `dd07a5f8faafab533b067d5de6edeeda04daa5a3`.

Source: [official Geoapify specifications](https://github.com/geoapify/geoapify-openapi-specs/tree/dd07a5f8faafab533b067d5de6edeeda04daa5a3/api-specs).

## Adapter authoring

B06: AI-assisted handwritten standard-library adapters. The build agent read the pinned request and response schemas before implementation. No generator or dependency installation. HTTP header `x-api-key` is supported by the pinned REST specs. Secrets come only from the environment.

## Category snapshot

`zonepilot/categories.json` contains all 833 PlaceCategory enum values from the pinned Places 2.2.1 schema. SHA-256: `6ad927eb2a18a4c66c0515896542db3374d8f02a2a403170c241240dff717ffa`.

The official snapshot and [category list](https://apidocs.geoapify.com/docs/places/) contain no plumber or plumbing category. Do not invent `service.plumber`. The offline example selects `service` as a deliberately broad service-business candidate category, not proof of plumbing competitors. Reports carry that limitation. An exact plumbing competition demo remains B03-pending.

## Contract discrepancies

FR-18 requires rectangle search plus authoritative local membership, so the CLI uses GET /v2/places with a rectangle. POST polygon filtering is supported by the pinned spec but is not the selected PRD contract.

The 2026-10-22 public MCP table lists eleven tools including geocode_structured_address and combine_geometries; nine plus two is eleven. No isoline tool appears. The prompt claims twelve. Authenticated tools/list is PENDING.

Route Matrix has per-array maxima of 1,000, and a 1,000-cell regular-request limit in the pinned error example. One source and twenty targets is within both. No larger capacity claim is needed.

Isoline documentation describes HTTP 202 and retrieval by ID, but the pinned OpenAPI responses omit 202. The adapter explicitly handles bounded polling; live shape verification is pending.

## File hashes

| File | SHA-256 |
| --- | --- |
| `api-specs/forward-geocoding/forward-geocoding-api-openapi-specs.json` | `33561e7e2765365fcad5ff6816ffc909ba452a20252ad40b66d2918c954f5d61` |
| `api-specs/isoline/isoline-api-openapi-specs.json` | `d526aca958a20c4504e39f6e48027449ae92893565c51909917c787abdf5efa9` |
| `api-specs/mcp/mcp-api-openapi-specs.json` | `29895791e5fe3f843ca2524fdaa4848af0951f52014edb51196a74d8df39db84` |
| `api-specs/mcp/tools/calculate-route-matrix-openapi-spec.json` | `b96d877bf0904b99e95a15439f1fc977728fad4fefd69c7c7685c0d1148f416b` |
| `api-specs/mcp/tools/calculate-route-openapi-spec.json` | `e9100b99ebd35d187961e6afacf5fc3d4bfe4097ca3a56351b97367b0c13e9cb` |
| `api-specs/mcp/tools/combine-geometries-openapi-spec.json` | `0ce9c4e749580f08bf6d8e7b12f133f4cf166196d07d496be34fc93a3ca67683` |
| `api-specs/mcp/tools/evaluate-spatial-relation-openapi-spec.json` | `ed96b7128e2c9858a864357c1c883bee00eaae5d2ec97ac3bbd87abeaaa9103b` |
| `api-specs/mcp/tools/geocode-address-openapi-spec.json` | `982d239a531ade9d7c0fca2505d06741f4fb5e56273a4021da03350e56160aac` |
| `api-specs/mcp/tools/geocode-structured-address-openapi-spec.json` | `746bca1c75caef6ac164e7b2d1c2e74e8f76710848b42ac93303c639c1952ebb` |
| `api-specs/mcp/tools/index.json` | `193c6a7474527b4f32d0f3210040b8038142a445b8cd85c6af10d8da4188e492` |
| `api-specs/mcp/tools/list-place-categories-openapi-spec.json` | `7488013e51c4782fdf7e10323742b50eda3dad7354977314aec8836bf01012da` |
| `api-specs/mcp/tools/measure-geometry-openapi-spec.json` | `960f1d051ebe1bb808953032e4f66447672ccc1a4436faf34d0695bd9bc8dde2` |
| `api-specs/mcp/tools/reverse-geocode-coordinates-openapi-spec.json` | `b14e5edb1c8953169bcbbf1269955f69fcdf6ad017b4376e76a70b2bb4e4c633` |
| `api-specs/mcp/tools/search-places-openapi-spec.json` | `f1a6c49b1cf64507235da7cb1f530e1baa8a07699803a6ef50fbea837af42148` |
| `api-specs/mcp/tools/transform-geometry-openapi-spec.json` | `d438b3578947f4af966107176ec8d63521f473d5859b4ca3968dce07a5e1c9d7` |
| `api-specs/places/places-api-openapi-specs.json` | `777c9c10b3aaae648e791dd95972b4b46c8cc6dffa96ab6d1a4cabb4a132edf3` |
| `api-specs/route-matrix/route-matrix-api-openapi-specs.json` | `a2171512e921c77d67bb9cfd002e0d1b0a44cbeee90b6cdbd47d5397a8904dda` |
| `api-specs/routing/routing-api-openapi-specs.json` | `20029c716cb51ebb1d3618a8dddb98464d54010528da2ebb3ed737c521efcad4` |
