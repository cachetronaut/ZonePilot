# Live demo inputs

Main Street Plumbing and all twenty customer names/references are fictional. The
addresses are real, publicly listed Midland locations used only to test geocoding
and routing. None is represented as a business premises, customer, endorsement or
affiliation. No personal household addresses or actual customer records are used.

The origin is [Midland City Hall](https://www.midlandtexas.gov/m/directory/department?did=22),
300 N Loraine St, Midland, TX 79701. Settings: 20 minutes, outbound drive,
free_flow, balanced, metric. `sample_business.json` records these inputs and the
label; the CLI takes the values as arguments. `sample_customers.csv` has exactly
twenty synthetic identities at the public locations below. Both live paths use
these exact files. Selection used public provenance, building geocodability and geographic spread. Discovery route checks are retained; no time or verdict was invented to obtain a desired outcome.

The owner approved this demo-location policy on 2026-10-23. The [discovery evidence](../docs/evidence/stage4/live/discovery.json)
and [additional checks](../docs/evidence/stage4/live/discovery-additional.json) retain
all attempts, including rejected imprecise/ambiguous matches. No confidence rule
was relaxed. Offline authored fixtures remain under `tests/fixtures/sample` and
are never described as live observations.

Public address sources: [school directory](https://apps.myplanware.com/schoolsearch/midland),
[housing authority public locations](https://www.mcha2.org/locations/list),
[city public facility list](https://www.midlandtexas.gov/DocumentCenter/View/8430/ED-Vote-Centers-Eng-Span-Including-Martin-County),
[High Sky Wing](https://commemorativeairforce.org/units/39), and
[Museum of the Southwest](https://www.museumsw.org/).

| Synthetic reference | Public demo address |
| --- | --- |
| DEMO-01 | 615 W Missouri Ave, Midland, TX 79701 |
| DEMO-02 | 3500 Neely Ave, Midland, TX 79707 |
| DEMO-03 | 909 Bonham St, Midland, TX 79703 |
| DEMO-04 | 2700 FM 1379, Midland, TX 79706 |
| DEMO-05 | 900 S Raymond Rd, Midland, TX 79703 |
| DEMO-06 | 5001 Preston Dr, Midland, TX 79707 |
| DEMO-07 | 2800 Moss Ave, Midland, TX 79705 |
| DEMO-08 | 201 W Dakota Ave, Midland, TX 79701 |
| DEMO-09 | 6000 Riverfront Dr, Midland, TX 79706 |
| DEMO-10 | 1400 N N St, Midland, TX 79701 |
| DEMO-11 | 100 E Gist Ave, Midland, TX 79701 |
| DEMO-12 | 9600 Wright Dr, Midland, TX 79706 |
| DEMO-13 | 1705 W Missouri Ave, Midland, TX 79701 |
| DEMO-14 | 3800 Norwood St, Midland, TX 79707 |
| DEMO-15 | 1700 E Magnolia Ave, Midland, TX 79705 |
| DEMO-16 | 2601 Wedgewood St, Midland, TX 79707 |
| DEMO-17 | 2400 Fannin Ave, Midland, TX 79705 |
| DEMO-18 | 4800 Graceland Dr, Midland, TX 79703 |
| DEMO-19 | 2503 W Loop 250 N, Midland, TX 79705 |
| DEMO-20 | 301 W Missouri Ave, Midland, TX 79701 |

Live Places responses may identify real places. `service` is a broad category,
not a trade-services category or a verified set of plumbing competitors. Counts
are bounded observations, not a market census.

The first hosted run returned 700 South Street for the proposed 700 S Jackson St row despite confidence 1.0, while REST returned South Jackson Street. That location was removed from the final sample, not silently corrected in evidence. DEMO-04 now uses the [Greenwood district public address](https://greenwood.esc18.net/accessibility). See [outer-location discovery](../docs/evidence/stage4/live/discovery-outer.json) and [route checks](../docs/evidence/stage4/live/discovery-outer-times.json). Final reports use the revised CSV; the earlier hosted session is retained as a failed preliminary attempt.
