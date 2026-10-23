# ZonePilot report

## Run and method

| Field | Value |
| --- | --- |
| schema&#95;version | 1&#46;0 |
| path | cli |
| data&#95;mode | synthetic |
| run&#95;status | complete |
| run&#95;timestamp&#95;utc | 2026&#45;10&#45;22T12&#58;00&#58;00Z |
| zone.method | geoapify&#95;isoline |
| zone.approximation | false |
| zone.parameters | &#123;&quot;boundary&#95;tolerance&#95;degrees&quot;&#58; 1e&#45;09, &quot;range&#95;seconds&quot;&#58; 1200&#125; |
| zone.limitations | &#91;&quot;Outbound free&#45;flow road&#45;time estimate; no live traffic, return trip or profitability model&#46;&quot;, &quot;All ring boundaries are in zone; segment&#45;distance tolerance 1e&#45;9 degrees&#46;&quot;&#93; |

## Summary

| Field | Value |
| --- | --- |
| borderline | 2 |
| classified&#95;denominator | 20 |
| disagreements | 2 |
| in&#95;zone | 13 |
| in&#95;zone&#95;percent | 65&#46;0 |
| known&#95;routes | 20 |
| max&#95;time&#95;row&#95;ids | &#91;19, 20&#93; |
| max&#95;time&#95;seconds | 2600&#46;0 |
| median&#95;in&#95;zone&#95;seconds | 800&#46;0 |
| missing&#95;routes | 0 |
| out&#95;of&#95;zone | 7 |
| out&#95;of&#95;zone&#95;percent | 35&#46;0 |
| resolved | 20 |
| total | 20 |
| unknown&#95;membership | 0 |
| unresolved | 0 |

## Customers

| Row | Name | Supplied address | Geocode | Membership | Route | Time, seconds | Distance, metres | Within budget | Borderline | Disagreement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Fictional customer 01 | 90001 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | in&#95;zone | ok | 0&#46;0 | 0&#46;0 | true | false | false |
| 2 | Fictional customer 02 | 90002 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | in&#95;zone | ok | 300&#46;0 | 3600&#46;0 | true | false | false |
| 3 | Fictional customer 03 | 90003 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | in&#95;zone | ok | 450&#46;0 | 5400&#46;0 | true | false | false |
| 4 | Fictional customer 04 | 90004 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | in&#95;zone | ok | 500&#46;0 | 6000&#46;0 | true | false | false |
| 5 | Fictional customer 05 | 90005 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | in&#95;zone | ok | 600&#46;0 | 7200&#46;0 | true | false | false |
| 6 | Fictional customer 06 | 90006 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | in&#95;zone | ok | 700&#46;0 | 8400&#46;0 | true | false | false |
| 7 | Fictional customer 07 | 90007 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | in&#95;zone | ok | 800&#46;0 | 9600&#46;0 | true | false | false |
| 8 | Fictional customer 08 | 90008 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | in&#95;zone | ok | 900&#46;0 | 10800&#46;0 | true | false | false |
| 9 | Fictional customer 09 | 90009 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | in&#95;zone | ok | 1000&#46;0 | 12000&#46;0 | true | false | false |
| 10 | Fictional customer 10 | 90010 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | in&#95;zone | ok | 1100&#46;0 | 13200&#46;0 | true | false | false |
| 11 | Fictional customer 11 | 90011 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | in&#95;zone | ok | 1200&#46;0 | 14400&#46;0 | true | false | false |
| 12 | Fictional customer 12 | 90012 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | in&#95;zone | ok | 1200&#46;000001 | 14400&#46;000012 | false | true | true |
| 13 | Fictional customer 13 | 90013 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | in&#95;zone | ok | 1320&#46;0 | 15840&#46;0 | false | true | true |
| 14 | Fictional customer 14 | 90014 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | out&#95;of&#95;zone | ok | 1320&#46;000001 | 15840&#46;000012 | false | false | false |
| 15 | Fictional customer 15 | 90015 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | out&#95;of&#95;zone | ok | 1400&#46;0 | 16800&#46;0 | false | false | false |
| 16 | Fictional customer 16 | 90016 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | out&#95;of&#95;zone | ok | 1600&#46;0 | 19200&#46;0 | false | false | false |
| 17 | Fictional customer 17 | 90017 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | out&#95;of&#95;zone | ok | 2000&#46;0 | 24000&#46;0 | false | false | false |
| 18 | Fictional customer 18 | 90018 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | out&#95;of&#95;zone | ok | 2300&#46;0 | 27600&#46;0 | false | false | false |
| 19 | Fictional customer 19 | 90019 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | out&#95;of&#95;zone | ok | 2600&#46;0 | 31200&#46;0 | false | false | false |
| 20 | Fictional customer 20 | 90020 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; | resolved | out&#95;of&#95;zone | ok | 2600&#46;0 | 31200&#46;0 | false | false | false |

## Competitors

Counts are observed places. Successful searches are sampled, not a market census.

| Field | Value |
| --- | --- |
| cap&#95;reached | false |
| category | service |
| coverage | sampled |
| duplicate&#95;count | 0 |
| observed&#95;in&#95;zone&#95;count | 1 |
| observed&#95;out&#95;of&#95;zone&#95;count | 1 |
| returned&#95;count | 2 |
| search&#95;extent | &#123;&quot;method&quot;&#58; &quot;rectangle&quot;, &quot;parameters&quot;&#58; &#123;&quot;bbox&quot;&#58; &#91;&#45;102&#46;2, 31&#46;9, &#45;102&#46;0, 32&#46;1&#93;&#125;&#125; |
| status | ok |
| unclassified&#95;count | 0 |

| ID | Name | Address | Categories | Coordinates, lon/lat | Membership | Geodesic distance, metres |
| --- | --- | --- | --- | --- | --- | --- |
| fixture&#45;service&#45;a | Fictional repair shop A | Synthetic service storefront A | &#91;&quot;service&quot;&#93; | &#91;&#45;102&#46;12, 32&#46;01&#93; | in&#95;zone | 2189&#46;281 |

## Evidence

| Entry | Value |
| --- | --- |
| 0 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e001&#46;json&quot;, &quot;id&quot;&#58; &quot;e001&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;business&quot;, &quot;sha256&quot;&#58; &quot;0ab2fd5a2567113eeb4ac88c99d8a94abb660bf27ca7c5cbafd104281348913b&quot;&#125; |
| 1 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e002&#46;json&quot;, &quot;id&quot;&#58; &quot;e002&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;isoline&quot;, &quot;sha256&quot;&#58; &quot;d7b7602c60bc04406df33ca616ac28c282cca1f5d2eff735d66caf4b906995ab&quot;&#125; |
| 2 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e003&#46;json&quot;, &quot;id&quot;&#58; &quot;e003&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;f52d5bbc2df373b6c6cc35743294d4361065f1b4affee1c5910b037c078b8c18&quot;&#125; |
| 3 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e004&#46;json&quot;, &quot;id&quot;&#58; &quot;e004&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;196c0d4981b17df4ba640af2d74922d79c32efa016c6c820f4c76647fbc37c46&quot;&#125; |
| 4 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e005&#46;json&quot;, &quot;id&quot;&#58; &quot;e005&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;26bc9171d317c651faef70caabe3ae951983434cd4d80d017d9b1a6e5b9a6ff2&quot;&#125; |
| 5 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e006&#46;json&quot;, &quot;id&quot;&#58; &quot;e006&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;830570f111436073598efb964277c8ed80a74fb3ea987127bcf9b93aa42406b6&quot;&#125; |
| 6 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e007&#46;json&quot;, &quot;id&quot;&#58; &quot;e007&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;7b43c6ca1219a37a6fef1e4a08ef0e90a7a7a5d5f29e6b29bad33b5a5bb2b7e0&quot;&#125; |
| 7 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e008&#46;json&quot;, &quot;id&quot;&#58; &quot;e008&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;d0facc37c62aa219ae0db1b0b5552f793b48aef2d4ada71c5307b24315bb224d&quot;&#125; |
| 8 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e009&#46;json&quot;, &quot;id&quot;&#58; &quot;e009&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;c17051bec613fb1aab48dded3c424659cc6cc4d89980cc8ee2c0d52c08aafff1&quot;&#125; |
| 9 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e010&#46;json&quot;, &quot;id&quot;&#58; &quot;e010&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;9dcbc90005c0c9e15dfbb8699db97b5e4a077e52ea1251ccabd4e1332ed63fd3&quot;&#125; |
| 10 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e011&#46;json&quot;, &quot;id&quot;&#58; &quot;e011&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;1fa54b2ef0e725011df0aaef5475a5f9ae5460ccb3342ef3b210cc5e2bba9195&quot;&#125; |
| 11 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e012&#46;json&quot;, &quot;id&quot;&#58; &quot;e012&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;22799b542175fd72231bed570040d90bf242be61216615348642bd73a6286d05&quot;&#125; |
| 12 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e013&#46;json&quot;, &quot;id&quot;&#58; &quot;e013&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;0d9008fc1c758a0a158cd24c4254d8645211fba4fe6f5aec921619427a453eef&quot;&#125; |
| 13 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e014&#46;json&quot;, &quot;id&quot;&#58; &quot;e014&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;c7d09bb8fbeeafe2e54061e6aa740c2bdd1c53d427e9e68e6befa99aa34c347f&quot;&#125; |
| 14 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e015&#46;json&quot;, &quot;id&quot;&#58; &quot;e015&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;43f2889a5a82b36fe83c871ae749122c385c58c979305e5157e227ef07d591f1&quot;&#125; |
| 15 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e016&#46;json&quot;, &quot;id&quot;&#58; &quot;e016&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;94b487b0085396b93a649e557e794a5d1937d4e6135fb06da10216b030fbd420&quot;&#125; |
| 16 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e017&#46;json&quot;, &quot;id&quot;&#58; &quot;e017&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;0c8dfd83ddcb227eb3a089fd744f15dc411df71ec2f86a2fbaeba6112605d7e6&quot;&#125; |
| 17 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e018&#46;json&quot;, &quot;id&quot;&#58; &quot;e018&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;191daf1bdc3b786a59c254ac3f9ff94d1413e3d2d73ee64569f8115e5cb1e4b1&quot;&#125; |
| 18 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e019&#46;json&quot;, &quot;id&quot;&#58; &quot;e019&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;93a774112d1453684f1ea8433c47a00e728bb81556fa29648251e91e63e7f0a6&quot;&#125; |
| 19 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e020&#46;json&quot;, &quot;id&quot;&#58; &quot;e020&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;568d00c0b2bca437092a1d6edff1235b629a2ad090fb4012aaf6ce68d40fbba9&quot;&#125; |
| 20 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e021&#46;json&quot;, &quot;id&quot;&#58; &quot;e021&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;3432c2449505bc3f031c0860eeb3776279f5de6d95ce9dc0e4e331e1ea36e72a&quot;&#125; |
| 21 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e022&#46;json&quot;, &quot;id&quot;&#58; &quot;e022&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;d1ea97c3e585865b319d21a9026eee89b2f4af71abde656feda685432a99523d&quot;&#125; |
| 22 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e023&#46;json&quot;, &quot;id&quot;&#58; &quot;e023&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;route&#95;matrix&quot;, &quot;sha256&quot;&#58; &quot;491a3badec8a174f4e50cdf654264654c0b590e44293e9868bf3e2fcf7a86f5e&quot;&#125; |
| 23 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e024&#46;json&quot;, &quot;id&quot;&#58; &quot;e024&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;places&quot;, &quot;sha256&quot;&#58; &quot;cbc66f71129c3645b59921b6eb6baee8766b49e6eb84fa8cd93cf0914d1b2e1f&quot;&#125; |

## Errors

| Entry | Value |
| --- | --- |
| entries | [] |

## Warnings

| Entry | Value |
| --- | --- |
| 0 | Competitor coverage is sampled, at most 20 candidates and no pagination&#46; |
| 1 | The category service is broad; these candidates are not verified plumbing competitors&#46; |
| 2 | Authored synthetic fixtures, not a recording of live Geoapify calls&#46; |

## Attributions

| Entry | Value |
| --- | --- |
| 0 | &#123;&quot;source&quot;&#58; &quot;Geoapify&quot;, &quot;text&quot;&#58; &quot;API contracts and location services&#46;&quot;, &quot;url&quot;&#58; &quot;https&#58;//geoapify&#46;com&quot;&#125; |
| 1 | &#123;&quot;source&quot;&#58; &quot;OpenStreetMap&quot;, &quot;text&quot;&#58; &quot;Live map data&#58; © OpenStreetMap contributors, ODbL&#46; Synthetic fixtures contain no live map records&#46;&quot;, &quot;url&quot;&#58; &quot;https&#58;//www&#46;openstreetmap&#46;org/copyright&quot;&#125; |

## Complete field details

Every JSON field is listed independently. Null means unavailable.

| JSON path | Type | Value |
| --- | --- | --- |
| $ | object | object |
| $&#46;attributions | array | 2 entries |
| $&#46;attributions&#91;0&#93; | object | object |
| $&#46;attributions&#91;0&#93;&#46;source | string | Geoapify |
| $&#46;attributions&#91;0&#93;&#46;text | string | API contracts and location services&#46; |
| $&#46;attributions&#91;0&#93;&#46;url | string | https&#58;//geoapify&#46;com |
| $&#46;attributions&#91;1&#93; | object | object |
| $&#46;attributions&#91;1&#93;&#46;source | string | OpenStreetMap |
| $&#46;attributions&#91;1&#93;&#46;text | string | Live map data&#58; © OpenStreetMap contributors, ODbL&#46; Synthetic fixtures contain no live map records&#46; |
| $&#46;attributions&#91;1&#93;&#46;url | string | https&#58;//www&#46;openstreetmap&#46;org/copyright |
| $&#46;business | object | object |
| $&#46;business&#46;coordinates | array | 2 entries |
| $&#46;business&#46;coordinates&#91;0&#93; | number | &#45;102&#46;1 |
| $&#46;business&#46;coordinates&#91;1&#93; | number | 32&#46;0 |
| $&#46;business&#46;geocode&#95;evidence | object | object |
| $&#46;business&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;business&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;business&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;business&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;business&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;business&#46;input&#95;address | string | 90000 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;business&#46;name | string | Main Street Plumbing |
| $&#46;business&#46;resolved&#95;address | string | 90000 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;competitors | object | object |
| $&#46;competitors&#46;cap&#95;reached | boolean | false |
| $&#46;competitors&#46;category | string | service |
| $&#46;competitors&#46;coverage | string | sampled |
| $&#46;competitors&#46;duplicate&#95;count | number | 0 |
| $&#46;competitors&#46;observed&#95;in&#95;zone&#95;count | number | 1 |
| $&#46;competitors&#46;observed&#95;out&#95;of&#95;zone&#95;count | number | 1 |
| $&#46;competitors&#46;records | array | 1 entries |
| $&#46;competitors&#46;records&#91;0&#93; | object | object |
| $&#46;competitors&#46;records&#91;0&#93;&#46;address | string | Synthetic service storefront A |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories | array | 1 entries |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;0&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;0&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;12 |
| $&#46;competitors&#46;records&#91;0&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;01 |
| $&#46;competitors&#46;records&#91;0&#93;&#46;geodesic&#95;distance&#95;meters | number | 2189&#46;281 |
| $&#46;competitors&#46;records&#91;0&#93;&#46;id | string | fixture&#45;service&#45;a |
| $&#46;competitors&#46;records&#91;0&#93;&#46;name | string | Fictional repair shop A |
| $&#46;competitors&#46;records&#91;0&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;returned&#95;count | number | 2 |
| $&#46;competitors&#46;search&#95;extent | object | object |
| $&#46;competitors&#46;search&#95;extent&#46;method | string | rectangle |
| $&#46;competitors&#46;search&#95;extent&#46;parameters | object | object |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox | array | 4 entries |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox&#91;0&#93; | number | &#45;102&#46;2 |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox&#91;1&#93; | number | 31&#46;9 |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox&#91;2&#93; | number | &#45;102&#46;0 |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox&#91;3&#93; | number | 32&#46;1 |
| $&#46;competitors&#46;status | string | ok |
| $&#46;competitors&#46;unclassified&#95;count | number | 0 |
| $&#46;customers | array | 20 entries |
| $&#46;customers&#91;0&#93; | object | object |
| $&#46;customers&#91;0&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;0&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;0&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;15 |
| $&#46;customers&#91;0&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;02 |
| $&#46;customers&#91;0&#93;&#46;distance&#95;meters | number | 0&#46;0 |
| $&#46;customers&#91;0&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;0&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e003 |
| $&#46;customers&#91;0&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;0&#93;&#46;input&#95;address | string | 90001 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;0&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;0&#93;&#46;name | string | Fictional customer 01 |
| $&#46;customers&#91;0&#93;&#46;reference | string | DEMO&#45;01 |
| $&#46;customers&#91;0&#93;&#46;resolved&#95;address | string | 90001 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;0&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;0&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;0&#93;&#46;row&#95;id | number | 1 |
| $&#46;customers&#91;0&#93;&#46;time&#95;seconds | number | 0&#46;0 |
| $&#46;customers&#91;0&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;1&#93; | object | object |
| $&#46;customers&#91;1&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;1&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;1&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;14200000000001 |
| $&#46;customers&#91;1&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;02 |
| $&#46;customers&#91;1&#93;&#46;distance&#95;meters | number | 3600&#46;0 |
| $&#46;customers&#91;1&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;1&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e004 |
| $&#46;customers&#91;1&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;1&#93;&#46;input&#95;address | string | 90002 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;1&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;1&#93;&#46;name | string | Fictional customer 02 |
| $&#46;customers&#91;1&#93;&#46;reference | string | DEMO&#45;02 |
| $&#46;customers&#91;1&#93;&#46;resolved&#95;address | string | 90002 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;1&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;1&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;1&#93;&#46;row&#95;id | number | 2 |
| $&#46;customers&#91;1&#93;&#46;time&#95;seconds | number | 300&#46;0 |
| $&#46;customers&#91;1&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;2&#93; | object | object |
| $&#46;customers&#91;2&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;2&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;2&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;134 |
| $&#46;customers&#91;2&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;02 |
| $&#46;customers&#91;2&#93;&#46;distance&#95;meters | number | 5400&#46;0 |
| $&#46;customers&#91;2&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;2&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e005 |
| $&#46;customers&#91;2&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;2&#93;&#46;input&#95;address | string | 90003 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;2&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;2&#93;&#46;name | string | Fictional customer 03 |
| $&#46;customers&#91;2&#93;&#46;reference | string | DEMO&#45;03 |
| $&#46;customers&#91;2&#93;&#46;resolved&#95;address | string | 90003 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;2&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;2&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;2&#93;&#46;row&#95;id | number | 3 |
| $&#46;customers&#91;2&#93;&#46;time&#95;seconds | number | 450&#46;0 |
| $&#46;customers&#91;2&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;3&#93; | object | object |
| $&#46;customers&#91;3&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;3&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;3&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;126 |
| $&#46;customers&#91;3&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;02 |
| $&#46;customers&#91;3&#93;&#46;distance&#95;meters | number | 6000&#46;0 |
| $&#46;customers&#91;3&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;3&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e006 |
| $&#46;customers&#91;3&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;3&#93;&#46;input&#95;address | string | 90004 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;3&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;3&#93;&#46;name | string | Fictional customer 04 |
| $&#46;customers&#91;3&#93;&#46;reference | string | DEMO&#45;04 |
| $&#46;customers&#91;3&#93;&#46;resolved&#95;address | string | 90004 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;3&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;3&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;3&#93;&#46;row&#95;id | number | 4 |
| $&#46;customers&#91;3&#93;&#46;time&#95;seconds | number | 500&#46;0 |
| $&#46;customers&#91;3&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;4&#93; | object | object |
| $&#46;customers&#91;4&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;4&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;4&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;11800000000001 |
| $&#46;customers&#91;4&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;02 |
| $&#46;customers&#91;4&#93;&#46;distance&#95;meters | number | 7200&#46;0 |
| $&#46;customers&#91;4&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;4&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e007 |
| $&#46;customers&#91;4&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;4&#93;&#46;input&#95;address | string | 90005 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;4&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;4&#93;&#46;name | string | Fictional customer 05 |
| $&#46;customers&#91;4&#93;&#46;reference | string | DEMO&#45;05 |
| $&#46;customers&#91;4&#93;&#46;resolved&#95;address | string | 90005 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;4&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;4&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;4&#93;&#46;row&#95;id | number | 5 |
| $&#46;customers&#91;4&#93;&#46;time&#95;seconds | number | 600&#46;0 |
| $&#46;customers&#91;4&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;5&#93; | object | object |
| $&#46;customers&#91;5&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;5&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;5&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;11 |
| $&#46;customers&#91;5&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;02 |
| $&#46;customers&#91;5&#93;&#46;distance&#95;meters | number | 8400&#46;0 |
| $&#46;customers&#91;5&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;5&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e008 |
| $&#46;customers&#91;5&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;5&#93;&#46;input&#95;address | string | 90006 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;5&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;5&#93;&#46;name | string | Fictional customer 06 |
| $&#46;customers&#91;5&#93;&#46;reference | string | DEMO&#45;06 |
| $&#46;customers&#91;5&#93;&#46;resolved&#95;address | string | 90006 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;5&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;5&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;5&#93;&#46;row&#95;id | number | 6 |
| $&#46;customers&#91;5&#93;&#46;time&#95;seconds | number | 700&#46;0 |
| $&#46;customers&#91;5&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;6&#93; | object | object |
| $&#46;customers&#91;6&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;6&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;6&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;102 |
| $&#46;customers&#91;6&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;02 |
| $&#46;customers&#91;6&#93;&#46;distance&#95;meters | number | 9600&#46;0 |
| $&#46;customers&#91;6&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;6&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e009 |
| $&#46;customers&#91;6&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;6&#93;&#46;input&#95;address | string | 90007 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;6&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;6&#93;&#46;name | string | Fictional customer 07 |
| $&#46;customers&#91;6&#93;&#46;reference | string | DEMO&#45;07 |
| $&#46;customers&#91;6&#93;&#46;resolved&#95;address | string | 90007 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;6&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;6&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;6&#93;&#46;row&#95;id | number | 7 |
| $&#46;customers&#91;6&#93;&#46;time&#95;seconds | number | 800&#46;0 |
| $&#46;customers&#91;6&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;7&#93; | object | object |
| $&#46;customers&#91;7&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;7&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;7&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;09400000000001 |
| $&#46;customers&#91;7&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;02 |
| $&#46;customers&#91;7&#93;&#46;distance&#95;meters | number | 10800&#46;0 |
| $&#46;customers&#91;7&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;7&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e010 |
| $&#46;customers&#91;7&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;7&#93;&#46;input&#95;address | string | 90008 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;7&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;7&#93;&#46;name | string | Fictional customer 08 |
| $&#46;customers&#91;7&#93;&#46;reference | string | DEMO&#45;08 |
| $&#46;customers&#91;7&#93;&#46;resolved&#95;address | string | 90008 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;7&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;7&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;7&#93;&#46;row&#95;id | number | 8 |
| $&#46;customers&#91;7&#93;&#46;time&#95;seconds | number | 900&#46;0 |
| $&#46;customers&#91;7&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;8&#93; | object | object |
| $&#46;customers&#91;8&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;8&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;8&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;08600000000001 |
| $&#46;customers&#91;8&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;02 |
| $&#46;customers&#91;8&#93;&#46;distance&#95;meters | number | 12000&#46;0 |
| $&#46;customers&#91;8&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;8&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e011 |
| $&#46;customers&#91;8&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;8&#93;&#46;input&#95;address | string | 90009 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;8&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;8&#93;&#46;name | string | Fictional customer 09 |
| $&#46;customers&#91;8&#93;&#46;reference | string | DEMO&#45;09 |
| $&#46;customers&#91;8&#93;&#46;resolved&#95;address | string | 90009 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;8&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;8&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;8&#93;&#46;row&#95;id | number | 9 |
| $&#46;customers&#91;8&#93;&#46;time&#95;seconds | number | 1000&#46;0 |
| $&#46;customers&#91;8&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;9&#93; | object | object |
| $&#46;customers&#91;9&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;9&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;9&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;078 |
| $&#46;customers&#91;9&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;02 |
| $&#46;customers&#91;9&#93;&#46;distance&#95;meters | number | 13200&#46;0 |
| $&#46;customers&#91;9&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;9&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e012 |
| $&#46;customers&#91;9&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;9&#93;&#46;input&#95;address | string | 90010 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;9&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;9&#93;&#46;name | string | Fictional customer 10 |
| $&#46;customers&#91;9&#93;&#46;reference | string | DEMO&#45;10 |
| $&#46;customers&#91;9&#93;&#46;resolved&#95;address | string | 90010 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;9&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;9&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;9&#93;&#46;row&#95;id | number | 10 |
| $&#46;customers&#91;9&#93;&#46;time&#95;seconds | number | 1100&#46;0 |
| $&#46;customers&#91;9&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;10&#93; | object | object |
| $&#46;customers&#91;10&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;10&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;10&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;07000000000001 |
| $&#46;customers&#91;10&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;02 |
| $&#46;customers&#91;10&#93;&#46;distance&#95;meters | number | 14400&#46;0 |
| $&#46;customers&#91;10&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;10&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e013 |
| $&#46;customers&#91;10&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;10&#93;&#46;input&#95;address | string | 90011 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;10&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;10&#93;&#46;name | string | Fictional customer 11 |
| $&#46;customers&#91;10&#93;&#46;reference | string | DEMO&#45;11 |
| $&#46;customers&#91;10&#93;&#46;resolved&#95;address | string | 90011 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;10&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;10&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;10&#93;&#46;row&#95;id | number | 11 |
| $&#46;customers&#91;10&#93;&#46;time&#95;seconds | number | 1200&#46;0 |
| $&#46;customers&#91;10&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;11&#93; | object | object |
| $&#46;customers&#91;11&#93;&#46;borderline | boolean | true |
| $&#46;customers&#91;11&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;11&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;06200000000001 |
| $&#46;customers&#91;11&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;02 |
| $&#46;customers&#91;11&#93;&#46;distance&#95;meters | number | 14400&#46;000012 |
| $&#46;customers&#91;11&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;11&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e014 |
| $&#46;customers&#91;11&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;11&#93;&#46;input&#95;address | string | 90012 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;11&#93;&#46;membership&#95;route&#95;disagreement | boolean | true |
| $&#46;customers&#91;11&#93;&#46;name | string | Fictional customer 12 |
| $&#46;customers&#91;11&#93;&#46;reference | string | DEMO&#45;12 |
| $&#46;customers&#91;11&#93;&#46;resolved&#95;address | string | 90012 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;11&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;11&#93;&#46;route&#95;within&#95;budget | boolean | false |
| $&#46;customers&#91;11&#93;&#46;row&#95;id | number | 12 |
| $&#46;customers&#91;11&#93;&#46;time&#95;seconds | number | 1200&#46;000001 |
| $&#46;customers&#91;11&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;12&#93; | object | object |
| $&#46;customers&#91;12&#93;&#46;borderline | boolean | true |
| $&#46;customers&#91;12&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;12&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;2 |
| $&#46;customers&#91;12&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;0 |
| $&#46;customers&#91;12&#93;&#46;distance&#95;meters | number | 15840&#46;0 |
| $&#46;customers&#91;12&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;12&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e015 |
| $&#46;customers&#91;12&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;12&#93;&#46;input&#95;address | string | 90013 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;12&#93;&#46;membership&#95;route&#95;disagreement | boolean | true |
| $&#46;customers&#91;12&#93;&#46;name | string | Fictional customer 13 |
| $&#46;customers&#91;12&#93;&#46;reference | string | DEMO&#45;13 |
| $&#46;customers&#91;12&#93;&#46;resolved&#95;address | string | 90013 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;12&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;12&#93;&#46;route&#95;within&#95;budget | boolean | false |
| $&#46;customers&#91;12&#93;&#46;row&#95;id | number | 13 |
| $&#46;customers&#91;12&#93;&#46;time&#95;seconds | number | 1320&#46;0 |
| $&#46;customers&#91;12&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;13&#93; | object | object |
| $&#46;customers&#91;13&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;13&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;13&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;21 |
| $&#46;customers&#91;13&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;0 |
| $&#46;customers&#91;13&#93;&#46;distance&#95;meters | number | 15840&#46;000012 |
| $&#46;customers&#91;13&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;13&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e016 |
| $&#46;customers&#91;13&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;13&#93;&#46;input&#95;address | string | 90014 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;13&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;13&#93;&#46;name | string | Fictional customer 14 |
| $&#46;customers&#91;13&#93;&#46;reference | string | DEMO&#45;14 |
| $&#46;customers&#91;13&#93;&#46;resolved&#95;address | string | 90014 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;13&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;13&#93;&#46;route&#95;within&#95;budget | boolean | false |
| $&#46;customers&#91;13&#93;&#46;row&#95;id | number | 14 |
| $&#46;customers&#91;13&#93;&#46;time&#95;seconds | number | 1320&#46;000001 |
| $&#46;customers&#91;13&#93;&#46;verdict | string | out&#95;of&#95;zone |
| $&#46;customers&#91;14&#93; | object | object |
| $&#46;customers&#91;14&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;14&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;14&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;22 |
| $&#46;customers&#91;14&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;02 |
| $&#46;customers&#91;14&#93;&#46;distance&#95;meters | number | 16800&#46;0 |
| $&#46;customers&#91;14&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;14&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e017 |
| $&#46;customers&#91;14&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;14&#93;&#46;input&#95;address | string | 90015 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;14&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;14&#93;&#46;name | string | Fictional customer 15 |
| $&#46;customers&#91;14&#93;&#46;reference | string | DEMO&#45;15 |
| $&#46;customers&#91;14&#93;&#46;resolved&#95;address | string | 90015 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;14&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;14&#93;&#46;route&#95;within&#95;budget | boolean | false |
| $&#46;customers&#91;14&#93;&#46;row&#95;id | number | 15 |
| $&#46;customers&#91;14&#93;&#46;time&#95;seconds | number | 1400&#46;0 |
| $&#46;customers&#91;14&#93;&#46;verdict | string | out&#95;of&#95;zone |
| $&#46;customers&#91;15&#93; | object | object |
| $&#46;customers&#91;15&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;15&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;15&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;3 |
| $&#46;customers&#91;15&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;01 |
| $&#46;customers&#91;15&#93;&#46;distance&#95;meters | number | 19200&#46;0 |
| $&#46;customers&#91;15&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;15&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e018 |
| $&#46;customers&#91;15&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;15&#93;&#46;input&#95;address | string | 90016 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;15&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;15&#93;&#46;name | string | Fictional customer 16 |
| $&#46;customers&#91;15&#93;&#46;reference | string | DEMO&#45;16 |
| $&#46;customers&#91;15&#93;&#46;resolved&#95;address | string | 90016 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;15&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;15&#93;&#46;route&#95;within&#95;budget | boolean | false |
| $&#46;customers&#91;15&#93;&#46;row&#95;id | number | 16 |
| $&#46;customers&#91;15&#93;&#46;time&#95;seconds | number | 1600&#46;0 |
| $&#46;customers&#91;15&#93;&#46;verdict | string | out&#95;of&#95;zone |
| $&#46;customers&#91;16&#93; | object | object |
| $&#46;customers&#91;16&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;16&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;16&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;4 |
| $&#46;customers&#91;16&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;0 |
| $&#46;customers&#91;16&#93;&#46;distance&#95;meters | number | 24000&#46;0 |
| $&#46;customers&#91;16&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;16&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e019 |
| $&#46;customers&#91;16&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;16&#93;&#46;input&#95;address | string | 90017 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;16&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;16&#93;&#46;name | string | Fictional customer 17 |
| $&#46;customers&#91;16&#93;&#46;reference | string | DEMO&#45;17 |
| $&#46;customers&#91;16&#93;&#46;resolved&#95;address | string | 90017 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;16&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;16&#93;&#46;route&#95;within&#95;budget | boolean | false |
| $&#46;customers&#91;16&#93;&#46;row&#95;id | number | 17 |
| $&#46;customers&#91;16&#93;&#46;time&#95;seconds | number | 2000&#46;0 |
| $&#46;customers&#91;16&#93;&#46;verdict | string | out&#95;of&#95;zone |
| $&#46;customers&#91;17&#93; | object | object |
| $&#46;customers&#91;17&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;17&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;17&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;1 |
| $&#46;customers&#91;17&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;2 |
| $&#46;customers&#91;17&#93;&#46;distance&#95;meters | number | 27600&#46;0 |
| $&#46;customers&#91;17&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;17&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e020 |
| $&#46;customers&#91;17&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;17&#93;&#46;input&#95;address | string | 90018 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;17&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;17&#93;&#46;name | string | Fictional customer 18 |
| $&#46;customers&#91;17&#93;&#46;reference | string | DEMO&#45;18 |
| $&#46;customers&#91;17&#93;&#46;resolved&#95;address | string | 90018 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;17&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;17&#93;&#46;route&#95;within&#95;budget | boolean | false |
| $&#46;customers&#91;17&#93;&#46;row&#95;id | number | 18 |
| $&#46;customers&#91;17&#93;&#46;time&#95;seconds | number | 2300&#46;0 |
| $&#46;customers&#91;17&#93;&#46;verdict | string | out&#95;of&#95;zone |
| $&#46;customers&#91;18&#93; | object | object |
| $&#46;customers&#91;18&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;18&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;18&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;1 |
| $&#46;customers&#91;18&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;8 |
| $&#46;customers&#91;18&#93;&#46;distance&#95;meters | number | 31200&#46;0 |
| $&#46;customers&#91;18&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;18&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e021 |
| $&#46;customers&#91;18&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;18&#93;&#46;input&#95;address | string | 90019 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;18&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;18&#93;&#46;name | string | Fictional customer 19 |
| $&#46;customers&#91;18&#93;&#46;reference | string | DEMO&#45;19 |
| $&#46;customers&#91;18&#93;&#46;resolved&#95;address | string | 90019 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;18&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;18&#93;&#46;route&#95;within&#95;budget | boolean | false |
| $&#46;customers&#91;18&#93;&#46;row&#95;id | number | 19 |
| $&#46;customers&#91;18&#93;&#46;time&#95;seconds | number | 2600&#46;0 |
| $&#46;customers&#91;18&#93;&#46;verdict | string | out&#95;of&#95;zone |
| $&#46;customers&#91;19&#93; | object | object |
| $&#46;customers&#91;19&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;19&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;19&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;3 |
| $&#46;customers&#91;19&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;8 |
| $&#46;customers&#91;19&#93;&#46;distance&#95;meters | number | 31200&#46;0 |
| $&#46;customers&#91;19&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;19&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e022 |
| $&#46;customers&#91;19&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1&#46;0 |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1&#46;0 |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;19&#93;&#46;input&#95;address | string | 90020 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;19&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;19&#93;&#46;name | string | Fictional customer 20 |
| $&#46;customers&#91;19&#93;&#46;reference | string | DEMO&#45;20 |
| $&#46;customers&#91;19&#93;&#46;resolved&#95;address | string | 90020 Imaginary Fixture Lane, Midland TX &#40;fictional&#41; |
| $&#46;customers&#91;19&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;19&#93;&#46;route&#95;within&#95;budget | boolean | false |
| $&#46;customers&#91;19&#93;&#46;row&#95;id | number | 20 |
| $&#46;customers&#91;19&#93;&#46;time&#95;seconds | number | 2600&#46;0 |
| $&#46;customers&#91;19&#93;&#46;verdict | string | out&#95;of&#95;zone |
| $&#46;data&#95;mode | string | synthetic |
| $&#46;errors | array | &#91;&#93; |
| $&#46;evidence | array | 24 entries |
| $&#46;evidence&#91;0&#93; | object | object |
| $&#46;evidence&#91;0&#93;&#46;artifact | string | evidence/e001&#46;json |
| $&#46;evidence&#91;0&#93;&#46;id | string | e001 |
| $&#46;evidence&#91;0&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;0&#93;&#46;operation | string | geocode&#95;business |
| $&#46;evidence&#91;0&#93;&#46;sha256 | string | 0ab2fd5a2567113eeb4ac88c99d8a94abb660bf27ca7c5cbafd104281348913b |
| $&#46;evidence&#91;1&#93; | object | object |
| $&#46;evidence&#91;1&#93;&#46;artifact | string | evidence/e002&#46;json |
| $&#46;evidence&#91;1&#93;&#46;id | string | e002 |
| $&#46;evidence&#91;1&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;1&#93;&#46;operation | string | isoline |
| $&#46;evidence&#91;1&#93;&#46;sha256 | string | d7b7602c60bc04406df33ca616ac28c282cca1f5d2eff735d66caf4b906995ab |
| $&#46;evidence&#91;2&#93; | object | object |
| $&#46;evidence&#91;2&#93;&#46;artifact | string | evidence/e003&#46;json |
| $&#46;evidence&#91;2&#93;&#46;id | string | e003 |
| $&#46;evidence&#91;2&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;2&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;2&#93;&#46;sha256 | string | f52d5bbc2df373b6c6cc35743294d4361065f1b4affee1c5910b037c078b8c18 |
| $&#46;evidence&#91;3&#93; | object | object |
| $&#46;evidence&#91;3&#93;&#46;artifact | string | evidence/e004&#46;json |
| $&#46;evidence&#91;3&#93;&#46;id | string | e004 |
| $&#46;evidence&#91;3&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;3&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;3&#93;&#46;sha256 | string | 196c0d4981b17df4ba640af2d74922d79c32efa016c6c820f4c76647fbc37c46 |
| $&#46;evidence&#91;4&#93; | object | object |
| $&#46;evidence&#91;4&#93;&#46;artifact | string | evidence/e005&#46;json |
| $&#46;evidence&#91;4&#93;&#46;id | string | e005 |
| $&#46;evidence&#91;4&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;4&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;4&#93;&#46;sha256 | string | 26bc9171d317c651faef70caabe3ae951983434cd4d80d017d9b1a6e5b9a6ff2 |
| $&#46;evidence&#91;5&#93; | object | object |
| $&#46;evidence&#91;5&#93;&#46;artifact | string | evidence/e006&#46;json |
| $&#46;evidence&#91;5&#93;&#46;id | string | e006 |
| $&#46;evidence&#91;5&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;5&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;5&#93;&#46;sha256 | string | 830570f111436073598efb964277c8ed80a74fb3ea987127bcf9b93aa42406b6 |
| $&#46;evidence&#91;6&#93; | object | object |
| $&#46;evidence&#91;6&#93;&#46;artifact | string | evidence/e007&#46;json |
| $&#46;evidence&#91;6&#93;&#46;id | string | e007 |
| $&#46;evidence&#91;6&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;6&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;6&#93;&#46;sha256 | string | 7b43c6ca1219a37a6fef1e4a08ef0e90a7a7a5d5f29e6b29bad33b5a5bb2b7e0 |
| $&#46;evidence&#91;7&#93; | object | object |
| $&#46;evidence&#91;7&#93;&#46;artifact | string | evidence/e008&#46;json |
| $&#46;evidence&#91;7&#93;&#46;id | string | e008 |
| $&#46;evidence&#91;7&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;7&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;7&#93;&#46;sha256 | string | d0facc37c62aa219ae0db1b0b5552f793b48aef2d4ada71c5307b24315bb224d |
| $&#46;evidence&#91;8&#93; | object | object |
| $&#46;evidence&#91;8&#93;&#46;artifact | string | evidence/e009&#46;json |
| $&#46;evidence&#91;8&#93;&#46;id | string | e009 |
| $&#46;evidence&#91;8&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;8&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;8&#93;&#46;sha256 | string | c17051bec613fb1aab48dded3c424659cc6cc4d89980cc8ee2c0d52c08aafff1 |
| $&#46;evidence&#91;9&#93; | object | object |
| $&#46;evidence&#91;9&#93;&#46;artifact | string | evidence/e010&#46;json |
| $&#46;evidence&#91;9&#93;&#46;id | string | e010 |
| $&#46;evidence&#91;9&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;9&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;9&#93;&#46;sha256 | string | 9dcbc90005c0c9e15dfbb8699db97b5e4a077e52ea1251ccabd4e1332ed63fd3 |
| $&#46;evidence&#91;10&#93; | object | object |
| $&#46;evidence&#91;10&#93;&#46;artifact | string | evidence/e011&#46;json |
| $&#46;evidence&#91;10&#93;&#46;id | string | e011 |
| $&#46;evidence&#91;10&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;10&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;10&#93;&#46;sha256 | string | 1fa54b2ef0e725011df0aaef5475a5f9ae5460ccb3342ef3b210cc5e2bba9195 |
| $&#46;evidence&#91;11&#93; | object | object |
| $&#46;evidence&#91;11&#93;&#46;artifact | string | evidence/e012&#46;json |
| $&#46;evidence&#91;11&#93;&#46;id | string | e012 |
| $&#46;evidence&#91;11&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;11&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;11&#93;&#46;sha256 | string | 22799b542175fd72231bed570040d90bf242be61216615348642bd73a6286d05 |
| $&#46;evidence&#91;12&#93; | object | object |
| $&#46;evidence&#91;12&#93;&#46;artifact | string | evidence/e013&#46;json |
| $&#46;evidence&#91;12&#93;&#46;id | string | e013 |
| $&#46;evidence&#91;12&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;12&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;12&#93;&#46;sha256 | string | 0d9008fc1c758a0a158cd24c4254d8645211fba4fe6f5aec921619427a453eef |
| $&#46;evidence&#91;13&#93; | object | object |
| $&#46;evidence&#91;13&#93;&#46;artifact | string | evidence/e014&#46;json |
| $&#46;evidence&#91;13&#93;&#46;id | string | e014 |
| $&#46;evidence&#91;13&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;13&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;13&#93;&#46;sha256 | string | c7d09bb8fbeeafe2e54061e6aa740c2bdd1c53d427e9e68e6befa99aa34c347f |
| $&#46;evidence&#91;14&#93; | object | object |
| $&#46;evidence&#91;14&#93;&#46;artifact | string | evidence/e015&#46;json |
| $&#46;evidence&#91;14&#93;&#46;id | string | e015 |
| $&#46;evidence&#91;14&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;14&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;14&#93;&#46;sha256 | string | 43f2889a5a82b36fe83c871ae749122c385c58c979305e5157e227ef07d591f1 |
| $&#46;evidence&#91;15&#93; | object | object |
| $&#46;evidence&#91;15&#93;&#46;artifact | string | evidence/e016&#46;json |
| $&#46;evidence&#91;15&#93;&#46;id | string | e016 |
| $&#46;evidence&#91;15&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;15&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;15&#93;&#46;sha256 | string | 94b487b0085396b93a649e557e794a5d1937d4e6135fb06da10216b030fbd420 |
| $&#46;evidence&#91;16&#93; | object | object |
| $&#46;evidence&#91;16&#93;&#46;artifact | string | evidence/e017&#46;json |
| $&#46;evidence&#91;16&#93;&#46;id | string | e017 |
| $&#46;evidence&#91;16&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;16&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;16&#93;&#46;sha256 | string | 0c8dfd83ddcb227eb3a089fd744f15dc411df71ec2f86a2fbaeba6112605d7e6 |
| $&#46;evidence&#91;17&#93; | object | object |
| $&#46;evidence&#91;17&#93;&#46;artifact | string | evidence/e018&#46;json |
| $&#46;evidence&#91;17&#93;&#46;id | string | e018 |
| $&#46;evidence&#91;17&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;17&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;17&#93;&#46;sha256 | string | 191daf1bdc3b786a59c254ac3f9ff94d1413e3d2d73ee64569f8115e5cb1e4b1 |
| $&#46;evidence&#91;18&#93; | object | object |
| $&#46;evidence&#91;18&#93;&#46;artifact | string | evidence/e019&#46;json |
| $&#46;evidence&#91;18&#93;&#46;id | string | e019 |
| $&#46;evidence&#91;18&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;18&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;18&#93;&#46;sha256 | string | 93a774112d1453684f1ea8433c47a00e728bb81556fa29648251e91e63e7f0a6 |
| $&#46;evidence&#91;19&#93; | object | object |
| $&#46;evidence&#91;19&#93;&#46;artifact | string | evidence/e020&#46;json |
| $&#46;evidence&#91;19&#93;&#46;id | string | e020 |
| $&#46;evidence&#91;19&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;19&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;19&#93;&#46;sha256 | string | 568d00c0b2bca437092a1d6edff1235b629a2ad090fb4012aaf6ce68d40fbba9 |
| $&#46;evidence&#91;20&#93; | object | object |
| $&#46;evidence&#91;20&#93;&#46;artifact | string | evidence/e021&#46;json |
| $&#46;evidence&#91;20&#93;&#46;id | string | e021 |
| $&#46;evidence&#91;20&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;20&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;20&#93;&#46;sha256 | string | 3432c2449505bc3f031c0860eeb3776279f5de6d95ce9dc0e4e331e1ea36e72a |
| $&#46;evidence&#91;21&#93; | object | object |
| $&#46;evidence&#91;21&#93;&#46;artifact | string | evidence/e022&#46;json |
| $&#46;evidence&#91;21&#93;&#46;id | string | e022 |
| $&#46;evidence&#91;21&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;21&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;21&#93;&#46;sha256 | string | d1ea97c3e585865b319d21a9026eee89b2f4af71abde656feda685432a99523d |
| $&#46;evidence&#91;22&#93; | object | object |
| $&#46;evidence&#91;22&#93;&#46;artifact | string | evidence/e023&#46;json |
| $&#46;evidence&#91;22&#93;&#46;id | string | e023 |
| $&#46;evidence&#91;22&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;22&#93;&#46;operation | string | route&#95;matrix |
| $&#46;evidence&#91;22&#93;&#46;sha256 | string | 491a3badec8a174f4e50cdf654264654c0b590e44293e9868bf3e2fcf7a86f5e |
| $&#46;evidence&#91;23&#93; | object | object |
| $&#46;evidence&#91;23&#93;&#46;artifact | string | evidence/e024&#46;json |
| $&#46;evidence&#91;23&#93;&#46;id | string | e024 |
| $&#46;evidence&#91;23&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;23&#93;&#46;operation | string | places |
| $&#46;evidence&#91;23&#93;&#46;sha256 | string | cbc66f71129c3645b59921b6eb6baee8766b49e6eb84fa8cd93cf0914d1b2e1f |
| $&#46;path | string | cli |
| $&#46;run&#95;status | string | complete |
| $&#46;run&#95;timestamp&#95;utc | string | 2026&#45;10&#45;22T12&#58;00&#58;00Z |
| $&#46;schema&#95;version | string | 1&#46;0 |
| $&#46;settings | object | object |
| $&#46;settings&#46;boundary&#95;rule | string | All ring boundaries are in zone; segment&#45;distance tolerance 1e&#45;9 degrees&#46; |
| $&#46;settings&#46;budget&#95;seconds | number | 1200 |
| $&#46;settings&#46;direction | string | outbound |
| $&#46;settings&#46;mode | string | drive |
| $&#46;settings&#46;route&#95;type | string | balanced |
| $&#46;settings&#46;traffic | string | free&#95;flow |
| $&#46;settings&#46;units | string | metric |
| $&#46;summary | object | object |
| $&#46;summary&#46;borderline | number | 2 |
| $&#46;summary&#46;classified&#95;denominator | number | 20 |
| $&#46;summary&#46;disagreements | number | 2 |
| $&#46;summary&#46;in&#95;zone | number | 13 |
| $&#46;summary&#46;in&#95;zone&#95;percent | number | 65&#46;0 |
| $&#46;summary&#46;known&#95;routes | number | 20 |
| $&#46;summary&#46;max&#95;time&#95;row&#95;ids | array | 2 entries |
| $&#46;summary&#46;max&#95;time&#95;row&#95;ids&#91;0&#93; | number | 19 |
| $&#46;summary&#46;max&#95;time&#95;row&#95;ids&#91;1&#93; | number | 20 |
| $&#46;summary&#46;max&#95;time&#95;seconds | number | 2600&#46;0 |
| $&#46;summary&#46;median&#95;in&#95;zone&#95;seconds | number | 800&#46;0 |
| $&#46;summary&#46;missing&#95;routes | number | 0 |
| $&#46;summary&#46;out&#95;of&#95;zone | number | 7 |
| $&#46;summary&#46;out&#95;of&#95;zone&#95;percent | number | 35&#46;0 |
| $&#46;summary&#46;resolved | number | 20 |
| $&#46;summary&#46;total | number | 20 |
| $&#46;summary&#46;unknown&#95;membership | number | 0 |
| $&#46;summary&#46;unresolved | number | 0 |
| $&#46;warnings | array | 3 entries |
| $&#46;warnings&#91;0&#93; | string | Competitor coverage is sampled, at most 20 candidates and no pagination&#46; |
| $&#46;warnings&#91;1&#93; | string | The category service is broad; these candidates are not verified plumbing competitors&#46; |
| $&#46;warnings&#91;2&#93; | string | Authored synthetic fixtures, not a recording of live Geoapify calls&#46; |
| $&#46;zone | object | object |
| $&#46;zone&#46;approximation | boolean | false |
| $&#46;zone&#46;evidence&#95;refs | array | 1 entries |
| $&#46;zone&#46;evidence&#95;refs&#91;0&#93; | string | e002 |
| $&#46;zone&#46;limitations | array | 2 entries |
| $&#46;zone&#46;limitations&#91;0&#93; | string | Outbound free&#45;flow road&#45;time estimate; no live traffic, return trip or profitability model&#46; |
| $&#46;zone&#46;limitations&#91;1&#93; | string | All ring boundaries are in zone; segment&#45;distance tolerance 1e&#45;9 degrees&#46; |
| $&#46;zone&#46;method | string | geoapify&#95;isoline |
| $&#46;zone&#46;parameters | object | object |
| $&#46;zone&#46;parameters&#46;boundary&#95;tolerance&#95;degrees | number | 1e&#45;09 |
| $&#46;zone&#46;parameters&#46;range&#95;seconds | number | 1200 |
