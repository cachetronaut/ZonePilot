# Live comparison, approximation=true for MCP

Fictional business/customer identities at real public demo locations; no affiliation.
CLI uses the full REST Isoline. MCP uses route_time_at_points, approximation=true:
Route-time classification only at measured points; no continuous zone.
Both use the final twenty-row CSV and identical 1,200-second outbound drive/free_flow/balanced/metric settings.

| Metric | CLI | Hosted MCP, approximation=true |
| --- | --- | --- |
| Evaluated / known routes | 20 / 20 | 20 / 20 |
| In zone / denominator | 20 / 20 (100%) | 20 / 20 (100%) |
| Median in-zone seconds | 488 | 488 |
| Farthest | DEMO-12, 1085 seconds, 21635 metres | DEMO-12, 1085 seconds, 21635 metres |
| Outliers / borderline / unknown | 0 / 0 / 0 | 0 / 0 / 0 |
| Service candidates in / out / unknown | 19 / 1 / 0 | 20 / 0 / 0 |
| Search | Isoline bounding rectangle | Origin-centered 20000-metre circle |
| Cap / coverage | 20 reached / sampled | 20 reached / sampled |

Broad service candidates are not verified plumbing competitors. The candidate searches use different extents and ranking; equal counts or sets are not expected.
In-zone candidate ID overlap: 2; CLI only: 17; MCP only: 18.

All final customer coordinates, matrix times and verdicts agree. Equality for these points does not establish equivalence between a continuous polygon and point-only classification. The separate hosted route for row 1 returned81.539 seconds versus matrix 81 seconds, with both 856 metres; the matrix remains authoritative for report times.

| Row | Reference | CLI seconds | MCP seconds | CLI verdict | MCP verdict, approximation=true |
| --- | --- | --- | --- | --- | --- |
| 1 | DEMO-01 | 81 | 81 | in_zone | in_zone |
| 2 | DEMO-02 | 490 | 490 | in_zone | in_zone |
| 3 | DEMO-03 | 449 | 449 | in_zone | in_zone |
| 4 | DEMO-04 | 822 | 822 | in_zone | in_zone |
| 5 | DEMO-05 | 486 | 486 | in_zone | in_zone |
| 6 | DEMO-06 | 816 | 816 | in_zone | in_zone |
| 7 | DEMO-07 | 607 | 607 | in_zone | in_zone |
| 8 | DEMO-08 | 156 | 156 | in_zone | in_zone |
| 9 | DEMO-09 | 887 | 887 | in_zone | in_zone |
| 10 | DEMO-10 | 386 | 386 | in_zone | in_zone |
| 11 | DEMO-11 | 247 | 247 | in_zone | in_zone |
| 12 | DEMO-12 | 1085 | 1085 | in_zone | in_zone |
| 13 | DEMO-13 | 190 | 190 | in_zone | in_zone |
| 14 | DEMO-14 | 665 | 665 | in_zone | in_zone |
| 15 | DEMO-15 | 344 | 344 | in_zone | in_zone |
| 16 | DEMO-16 | 509 | 509 | in_zone | in_zone |
| 17 | DEMO-17 | 478 | 478 | in_zone | in_zone |
| 18 | DEMO-18 | 722 | 722 | in_zone | in_zone |
| 19 | DEMO-19 | 569 | 569 | in_zone | in_zone |
| 20 | DEMO-20 | 59 | 59 | in_zone | in_zone |

No live customer was outside or borderline. The offline fixture covers those cases; it is not live evidence. The preliminary hosted run's wrong-street result and 19-target matrix are preserved in mcp-customers.json. The final sample replaces that row and uses mcp-final-customers.json's20-target matrix. No CLI measurements supplied an MCP result.
