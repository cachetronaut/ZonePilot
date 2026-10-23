# Sequenced prompts

Copy each prompt only after its preceding gate passes. Prefix every agent response, including failures, with `approximation=true`. A JSON export must instead carry `zone.approximation=true` and its method/limitations so the label survives outside the conversation.

## 0. Preflight and approved method

> Read docs/prd.md, docs/report-schema.md and docs/api-provenance.md. Check the recorded B02 approval and the remaining B01, B03 and B04 gates. Do not read, print or request the key. Confirm only whether the environment-backed x-api-key configuration is ready. Use approved fictional inputs only. B02 now approves route_time_at_points for customer classification only. Live acquisition remains blocked until B01/B03 prerequisites permit it, and B04 authenticated proof must be collected before claiming a completed live workflow. Synthetic offline import needs no key. Do not present invented fixture addresses as verified live inputs. Never substitute a distance circle or borrow the CLI polygon. Label this response approximation=true.

The build prompt proposed route-matrix boundary sampling, transform_geometry, customer predicates and measure_geometry statistics. The PRD requires an explicit sampling density, search extent, road/barrier/hole treatment, error oracle and credit ceiling before accepting that method. None was supplied. Keep that proposed sequence blocked. `transform_geometry` has transforms and centers, not an operation that manufactures an isochrone from route measurements. A convex hull must not silently fill barriers or holes.

The owner approved the smaller per-customer method on 2026-10-23: method=route_time_at_points; parameters contain exactly budget_seconds equal to settings.budget_seconds. A known normalized outbound time at or below the budget is in_zone (including equality); a greater known time is out_of_zone; missing, failed or unreachable routes imply unknown membership. There is no continuous polygon and no inference between points. Include the exact limitation "Route-time classification only at measured points; no continuous zone." in every report. One matrix call covers the origin and at most 20 resolved customer targets; no boundary sampling is authorized. The local importer tests this threshold oracle and rejects contradictory verdicts.

## 1. Discover and check schemas

> Once B01/B03 permit acquisition, initialize the configured Geoapify MCP connection and call tools/list. Compare with the pinned focused specs in docs/api-provenance.md. Save only sanitized evidence. Require geocode_address, reverse_geocode_coordinates, list_place_categories, search_places, calculate_route, calculate_route_matrix, transform_geometry, evaluate_spatial_relation and measure_geometry. Reject JSON-RPC errors and result.isError=true, even on HTTP 200. Read the operation-specific structuredContent schema. Never infer success from text content alone. Label the output approximation=true and report any inventory drift.

## 2. Resolve origin and customers

> Use geocode_address with query equal to the supplied address and limit=5. Do not send names/references. Preserve the input row_id, supplied name/reference/address, candidate count, rank.confidence, rank.confidence_building_level, rank.match_type and result_type. Apply PRD section 6.2 exactly. One eligible building is required. Ambiguous or imprecise origin aborts; unresolved customer rows remain visible. Do not replace missing values with guesses. Call reverse_geocode_coordinates for the accepted origin as a separate diagnostic; it does not overwrite forward resolution. Label all output approximation=true.

## 3. Measure outbound road times

> Call calculate_route_matrix once for the accepted origin and every resolved customer. Specify sources and targets as objects with named lon/lat, mode=drive, units=metric, type=balanced, traffic=free_flow and no avoid options. Match returned cells by indexes. Missing/no-route cells stay null; never zero. Record sanitized inputs and structured output. Call calculate_route for one resolved customer with the same settings to satisfy the separate route evidence requirement. Record differences without replacing matrix evidence. Apply the approved point-time rule above; retain every disagreement with the CLI by row on identical inputs. Never override the CLI polygon verdict or the MCP time verdict to make them agree. Label all output approximation=true.

## 4. Search category candidates

> This step remains blocked for live Places evidence under B03 and for report competitor membership until its route-evidence/search-extent contract is approved. Skip acquisition now; export competitors.status=not_requested with null category/extent/counts/coverage/cap and empty records. Do not claim the nine-tool acceptance criterion is complete. After those approvals, call list_place_categories and record the exact chosen category. The pinned list has no plumbing-specific category. Do not invent one or describe broad service results as verified plumbing competitors. Call search_places once with the approved category, origin, approved search radius and limit=20. Record that search extent; it is not a service zone. Deduplicate by provider ID or exact coordinate/name tuple, count unclassified candidates, and report sampled coverage even below the cap. Classify candidates only with the B02-approved method and its acquired evidence. Unavailable search is not zero competitors. Label all output approximation=true.

## 5. Separate geometry diagnostics

> Use this authored synthetic geometry only for diagnostics, never as the primary MCP zone: {"type":"Polygon","coordinates":[[[-102.2,31.9],[-102.0,31.9],[-102.0,32.1],[-102.2,32.1],[-102.2,31.9]]]}. Call transform_geometry with operation=center and geometry equal to that object. Call evaluate_spatial_relation with operation=contains, geometry equal to that polygon, and other_geometry equal to each Point at [-102.1,32.0] and [-102.3,32.0]. Call measure_geometry with operation=area and that polygon; the pinned operation reports square metres. Preserve the typed structuredContent results. Do not conflate hosted boundary semantics with ZonePilot's local boundary-included rule. Label every result approximation=true and diagnostic_only=true.

## 6. Export acquired evidence, render locally

> Produce plain JSON without fences conforming to docs/report-schema.md. path=mcp, zone.approximation=true, zone.method=route_time_at_points, zone.parameters={"budget_seconds":<the settings budget>}, and the exact limitation "Route-time classification only at measured points; no continuous zone." are required. Keep the competitor section not_requested while its gates remain open. Omit summary and run_status. Supply route_within_budget, borderline and membership_route_disagreement as null. Include resolvable evidence IDs and relative artifact paths/hashes. Missing tool evidence stays missing and fails validation; do not repair it from model knowledge. Put no secrets, raw error messages or machine paths in artifacts. Use the local importer, which makes no network calls, to validate and calculate both report formats. Retain partial states and nulls.

## 7. Compare and prepare evidence

> Compare CLI and MCP reports on exactly the same approved inputs, budget and routing settings. Show method, approximation flag, row-level verdicts, unknowns, route differences, search extents, sampled counts and candidate-set differences. Equal verdicts are not guaranteed. Link sanitized evidence for each of the nine tools and preserve source attribution. The comparison and all commentary must say approximation=true for the MCP path. Stop publication if B03 has not approved the real returned records. Do not manufacture screenshots or successful invocations.
