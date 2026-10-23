# ZonePilot report

## Run and method

| Field | Value |
| --- | --- |
| schema&#95;version | 1&#46;0 |
| path | cli |
| data&#95;mode | synthetic |
| run&#95;status | complete |
| run&#95;timestamp&#95;utc | 2026&#45;01&#45;01T00&#58;00&#58;00Z |
| zone.method | geoapify&#95;isoline |
| zone.approximation | false |
| zone.parameters | &#123;&quot;boundary&#95;tolerance&#95;degrees&quot;&#58; 1e&#45;09, &quot;range&#95;seconds&quot;&#58; 1200&#125; |
| zone.limitations | &#91;&quot;Synthetic geometry is authored test evidence, not a live drive&#45;time zone&#46;&quot;, &quot;Outbound free&#45;flow driving only; return journeys and live traffic are excluded&#46;&quot;&#93; |

## Summary

| Field | Value |
| --- | --- |
| borderline | 1 |
| classified&#95;denominator | 3 |
| disagreements | 1 |
| in&#95;zone | 2 |
| in&#95;zone&#95;percent | 66&#46;67 |
| known&#95;routes | 3 |
| max&#95;time&#95;row&#95;ids | &#91;3&#93; |
| max&#95;time&#95;seconds | 1500&#46;0 |
| median&#95;in&#95;zone&#95;seconds | 1130&#46;0 |
| missing&#95;routes | 0 |
| out&#95;of&#95;zone | 1 |
| out&#95;of&#95;zone&#95;percent | 33&#46;33 |
| resolved | 3 |
| total | 3 |
| unknown&#95;membership | 0 |
| unresolved | 0 |

## Customers

| Row | Name | Supplied address | Geocode | Membership | Route | Time, seconds | Distance, metres | Within budget | Borderline | Disagreement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Synthetic customer 1 | Synthetic destination 1 | resolved | in&#95;zone | ok | 1000&#46;0 | 2000&#46;0 | true | false | false |
| 2 | Synthetic customer 2 | Synthetic destination 2 | resolved | in&#95;zone | ok | 1260&#46;0 | 2500&#46;0 | false | true | true |
| 3 | Synthetic customer 3 | Synthetic destination 3 | resolved | out&#95;of&#95;zone | ok | 1500&#46;0 | 3000&#46;0 | false | false | false |

## Competitors

Counts are observed places. Successful searches are sampled, not a market census.

| Field | Value |
| --- | --- |
| cap&#95;reached | false |
| category | service&#46;locksmith |
| coverage | sampled |
| duplicate&#95;count | 1 |
| observed&#95;in&#95;zone&#95;count | 1 |
| observed&#95;out&#95;of&#95;zone&#95;count | 1 |
| returned&#95;count | 3 |
| search&#95;extent | &#123;&quot;method&quot;&#58; &quot;rectangle&quot;, &quot;parameters&quot;&#58; &#123;&quot;bbox&quot;&#58; &#91;&#45;1, &#45;1, 1, 1&#93;&#125;&#125; |
| status | ok |
| unclassified&#95;count | 0 |

| ID | Name | Address | Categories | Coordinates, lon/lat | Membership | Geodesic distance, metres |
| --- | --- | --- | --- | --- | --- | --- |
| fixture&#45;place&#45;001 | Synthetic competitor | Synthetic competitor premises | &#91;&quot;service&#46;locksmith&quot;&#93; | &#91;0&#46;1, 0&#46;1&#93; | in&#95;zone | 15725&#46;355 |

## Evidence

| Entry | Value |
| --- | --- |
| 0 | &#123;&quot;artifact&quot;&#58; &quot;evidence/complete&#46;json&quot;, &quot;id&quot;&#58; &quot;origin&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;forward&#95;geocoding&quot;, &quot;sha256&quot;&#58; &quot;b0194770bbd0f45e3056fe1e86ef88729437cac84fdbf22eb1e844a2f9569b99&quot;&#125; |
| 1 | &#123;&quot;artifact&quot;&#58; &quot;evidence/complete&#46;json&quot;, &quot;id&quot;&#58; &quot;zone&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;isoline&quot;, &quot;sha256&quot;&#58; &quot;b0194770bbd0f45e3056fe1e86ef88729437cac84fdbf22eb1e844a2f9569b99&quot;&#125; |
| 2 | &#123;&quot;artifact&quot;&#58; &quot;evidence/complete&#46;json&quot;, &quot;id&quot;&#58; &quot;customers&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;forward&#95;geocoding&quot;, &quot;sha256&quot;&#58; &quot;b0194770bbd0f45e3056fe1e86ef88729437cac84fdbf22eb1e844a2f9569b99&quot;&#125; |
| 3 | &#123;&quot;artifact&quot;&#58; &quot;evidence/complete&#46;json&quot;, &quot;id&quot;&#58; &quot;routes&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;route&#95;matrix&quot;, &quot;sha256&quot;&#58; &quot;b0194770bbd0f45e3056fe1e86ef88729437cac84fdbf22eb1e844a2f9569b99&quot;&#125; |
| 4 | &#123;&quot;artifact&quot;&#58; &quot;evidence/complete&#46;json&quot;, &quot;id&quot;&#58; &quot;places&quot;, &quot;kind&quot;&#58; &quot;synthetic&quot;, &quot;operation&quot;&#58; &quot;places&quot;, &quot;sha256&quot;&#58; &quot;b0194770bbd0f45e3056fe1e86ef88729437cac84fdbf22eb1e844a2f9569b99&quot;&#125; |

## Errors

| Entry | Value |
| --- | --- |
| entries | [] |

## Warnings

| Entry | Value |
| --- | --- |
| 0 | Competitor results are sampled observations, not a complete market census&#46; |

## Attributions

| Entry | Value |
| --- | --- |
| 0 | &#123;&quot;source&quot;&#58; &quot;ZonePilot synthetic fixtures&quot;, &quot;text&quot;&#58; &quot;Authored synthetic data; no API calls or real premises&#46;&quot;, &quot;url&quot;&#58; &quot;https&#58;//geoapify&#46;com&quot;&#125; |

## Complete field details

Every JSON field is listed independently. Null means unavailable.

| JSON path | Type | Value |
| --- | --- | --- |
| $ | object | object |
| $&#46;attributions | array | 1 entries |
| $&#46;attributions&#91;0&#93; | object | object |
| $&#46;attributions&#91;0&#93;&#46;source | string | ZonePilot synthetic fixtures |
| $&#46;attributions&#91;0&#93;&#46;text | string | Authored synthetic data; no API calls or real premises&#46; |
| $&#46;attributions&#91;0&#93;&#46;url | string | https&#58;//geoapify&#46;com |
| $&#46;business | object | object |
| $&#46;business&#46;coordinates | array | 2 entries |
| $&#46;business&#46;coordinates&#91;0&#93; | number | 0 |
| $&#46;business&#46;coordinates&#91;1&#93; | number | 0 |
| $&#46;business&#46;geocode&#95;evidence | object | object |
| $&#46;business&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;business&#46;geocode&#95;evidence&#46;confidence | number | 0&#46;99 |
| $&#46;business&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 0&#46;99 |
| $&#46;business&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;business&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;business&#46;input&#95;address | string | Synthetic origin A |
| $&#46;business&#46;name | string | Synthetic service business |
| $&#46;business&#46;resolved&#95;address | string | Synthetic business premises A |
| $&#46;competitors | object | object |
| $&#46;competitors&#46;cap&#95;reached | boolean | false |
| $&#46;competitors&#46;category | string | service&#46;locksmith |
| $&#46;competitors&#46;coverage | string | sampled |
| $&#46;competitors&#46;duplicate&#95;count | number | 1 |
| $&#46;competitors&#46;observed&#95;in&#95;zone&#95;count | number | 1 |
| $&#46;competitors&#46;observed&#95;out&#95;of&#95;zone&#95;count | number | 1 |
| $&#46;competitors&#46;records | array | 1 entries |
| $&#46;competitors&#46;records&#91;0&#93; | object | object |
| $&#46;competitors&#46;records&#91;0&#93;&#46;address | string | Synthetic competitor premises |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories | array | 1 entries |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories&#91;0&#93; | string | service&#46;locksmith |
| $&#46;competitors&#46;records&#91;0&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;0&#93;&#46;coordinates&#91;0&#93; | number | 0&#46;1 |
| $&#46;competitors&#46;records&#91;0&#93;&#46;coordinates&#91;1&#93; | number | 0&#46;1 |
| $&#46;competitors&#46;records&#91;0&#93;&#46;geodesic&#95;distance&#95;meters | number | 15725&#46;355 |
| $&#46;competitors&#46;records&#91;0&#93;&#46;id | string | fixture&#45;place&#45;001 |
| $&#46;competitors&#46;records&#91;0&#93;&#46;name | string | Synthetic competitor |
| $&#46;competitors&#46;records&#91;0&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;returned&#95;count | number | 3 |
| $&#46;competitors&#46;search&#95;extent | object | object |
| $&#46;competitors&#46;search&#95;extent&#46;method | string | rectangle |
| $&#46;competitors&#46;search&#95;extent&#46;parameters | object | object |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox | array | 4 entries |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox&#91;0&#93; | number | &#45;1 |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox&#91;1&#93; | number | &#45;1 |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox&#91;2&#93; | number | 1 |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox&#91;3&#93; | number | 1 |
| $&#46;competitors&#46;status | string | ok |
| $&#46;competitors&#46;unclassified&#95;count | number | 0 |
| $&#46;customers | array | 3 entries |
| $&#46;customers&#91;0&#93; | object | object |
| $&#46;customers&#91;0&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;0&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;0&#93;&#46;coordinates&#91;0&#93; | number | 0&#46;2 |
| $&#46;customers&#91;0&#93;&#46;coordinates&#91;1&#93; | number | 0&#46;3 |
| $&#46;customers&#91;0&#93;&#46;distance&#95;meters | number | 2000&#46;0 |
| $&#46;customers&#91;0&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;0&#93;&#46;evidence&#95;refs&#91;0&#93; | string | customers |
| $&#46;customers&#91;0&#93;&#46;evidence&#95;refs&#91;1&#93; | string | routes |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;confidence | number | 0&#46;99 |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 0&#46;99 |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;0&#93;&#46;input&#95;address | string | Synthetic destination 1 |
| $&#46;customers&#91;0&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;0&#93;&#46;name | string | Synthetic customer 1 |
| $&#46;customers&#91;0&#93;&#46;reference | null | unavailable |
| $&#46;customers&#91;0&#93;&#46;resolved&#95;address | string | Synthetic premises 1 |
| $&#46;customers&#91;0&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;0&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;0&#93;&#46;row&#95;id | number | 1 |
| $&#46;customers&#91;0&#93;&#46;time&#95;seconds | number | 1000&#46;0 |
| $&#46;customers&#91;0&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;1&#93; | object | object |
| $&#46;customers&#91;1&#93;&#46;borderline | boolean | true |
| $&#46;customers&#91;1&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;1&#93;&#46;coordinates&#91;0&#93; | number | 0&#46;4 |
| $&#46;customers&#91;1&#93;&#46;coordinates&#91;1&#93; | number | 0&#46;5 |
| $&#46;customers&#91;1&#93;&#46;distance&#95;meters | number | 2500&#46;0 |
| $&#46;customers&#91;1&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;1&#93;&#46;evidence&#95;refs&#91;0&#93; | string | customers |
| $&#46;customers&#91;1&#93;&#46;evidence&#95;refs&#91;1&#93; | string | routes |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;confidence | number | 0&#46;99 |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 0&#46;99 |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;1&#93;&#46;input&#95;address | string | Synthetic destination 2 |
| $&#46;customers&#91;1&#93;&#46;membership&#95;route&#95;disagreement | boolean | true |
| $&#46;customers&#91;1&#93;&#46;name | string | Synthetic customer 2 |
| $&#46;customers&#91;1&#93;&#46;reference | null | unavailable |
| $&#46;customers&#91;1&#93;&#46;resolved&#95;address | string | Synthetic premises 2 |
| $&#46;customers&#91;1&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;1&#93;&#46;route&#95;within&#95;budget | boolean | false |
| $&#46;customers&#91;1&#93;&#46;row&#95;id | number | 2 |
| $&#46;customers&#91;1&#93;&#46;time&#95;seconds | number | 1260&#46;0 |
| $&#46;customers&#91;1&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;2&#93; | object | object |
| $&#46;customers&#91;2&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;2&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;2&#93;&#46;coordinates&#91;0&#93; | number | 2 |
| $&#46;customers&#91;2&#93;&#46;coordinates&#91;1&#93; | number | 2 |
| $&#46;customers&#91;2&#93;&#46;distance&#95;meters | number | 3000&#46;0 |
| $&#46;customers&#91;2&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;2&#93;&#46;evidence&#95;refs&#91;0&#93; | string | customers |
| $&#46;customers&#91;2&#93;&#46;evidence&#95;refs&#91;1&#93; | string | routes |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;confidence | number | 0&#46;99 |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 0&#46;99 |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;2&#93;&#46;input&#95;address | string | Synthetic destination 3 |
| $&#46;customers&#91;2&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;2&#93;&#46;name | string | Synthetic customer 3 |
| $&#46;customers&#91;2&#93;&#46;reference | null | unavailable |
| $&#46;customers&#91;2&#93;&#46;resolved&#95;address | string | Synthetic premises 3 |
| $&#46;customers&#91;2&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;2&#93;&#46;route&#95;within&#95;budget | boolean | false |
| $&#46;customers&#91;2&#93;&#46;row&#95;id | number | 3 |
| $&#46;customers&#91;2&#93;&#46;time&#95;seconds | number | 1500&#46;0 |
| $&#46;customers&#91;2&#93;&#46;verdict | string | out&#95;of&#95;zone |
| $&#46;data&#95;mode | string | synthetic |
| $&#46;errors | array | &#91;&#93; |
| $&#46;evidence | array | 5 entries |
| $&#46;evidence&#91;0&#93; | object | object |
| $&#46;evidence&#91;0&#93;&#46;artifact | string | evidence/complete&#46;json |
| $&#46;evidence&#91;0&#93;&#46;id | string | origin |
| $&#46;evidence&#91;0&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;0&#93;&#46;operation | string | forward&#95;geocoding |
| $&#46;evidence&#91;0&#93;&#46;sha256 | string | b0194770bbd0f45e3056fe1e86ef88729437cac84fdbf22eb1e844a2f9569b99 |
| $&#46;evidence&#91;1&#93; | object | object |
| $&#46;evidence&#91;1&#93;&#46;artifact | string | evidence/complete&#46;json |
| $&#46;evidence&#91;1&#93;&#46;id | string | zone |
| $&#46;evidence&#91;1&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;1&#93;&#46;operation | string | isoline |
| $&#46;evidence&#91;1&#93;&#46;sha256 | string | b0194770bbd0f45e3056fe1e86ef88729437cac84fdbf22eb1e844a2f9569b99 |
| $&#46;evidence&#91;2&#93; | object | object |
| $&#46;evidence&#91;2&#93;&#46;artifact | string | evidence/complete&#46;json |
| $&#46;evidence&#91;2&#93;&#46;id | string | customers |
| $&#46;evidence&#91;2&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;2&#93;&#46;operation | string | forward&#95;geocoding |
| $&#46;evidence&#91;2&#93;&#46;sha256 | string | b0194770bbd0f45e3056fe1e86ef88729437cac84fdbf22eb1e844a2f9569b99 |
| $&#46;evidence&#91;3&#93; | object | object |
| $&#46;evidence&#91;3&#93;&#46;artifact | string | evidence/complete&#46;json |
| $&#46;evidence&#91;3&#93;&#46;id | string | routes |
| $&#46;evidence&#91;3&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;3&#93;&#46;operation | string | route&#95;matrix |
| $&#46;evidence&#91;3&#93;&#46;sha256 | string | b0194770bbd0f45e3056fe1e86ef88729437cac84fdbf22eb1e844a2f9569b99 |
| $&#46;evidence&#91;4&#93; | object | object |
| $&#46;evidence&#91;4&#93;&#46;artifact | string | evidence/complete&#46;json |
| $&#46;evidence&#91;4&#93;&#46;id | string | places |
| $&#46;evidence&#91;4&#93;&#46;kind | string | synthetic |
| $&#46;evidence&#91;4&#93;&#46;operation | string | places |
| $&#46;evidence&#91;4&#93;&#46;sha256 | string | b0194770bbd0f45e3056fe1e86ef88729437cac84fdbf22eb1e844a2f9569b99 |
| $&#46;path | string | cli |
| $&#46;run&#95;status | string | complete |
| $&#46;run&#95;timestamp&#95;utc | string | 2026&#45;01&#45;01T00&#58;00&#58;00Z |
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
| $&#46;summary&#46;borderline | number | 1 |
| $&#46;summary&#46;classified&#95;denominator | number | 3 |
| $&#46;summary&#46;disagreements | number | 1 |
| $&#46;summary&#46;in&#95;zone | number | 2 |
| $&#46;summary&#46;in&#95;zone&#95;percent | number | 66&#46;67 |
| $&#46;summary&#46;known&#95;routes | number | 3 |
| $&#46;summary&#46;max&#95;time&#95;row&#95;ids | array | 1 entries |
| $&#46;summary&#46;max&#95;time&#95;row&#95;ids&#91;0&#93; | number | 3 |
| $&#46;summary&#46;max&#95;time&#95;seconds | number | 1500&#46;0 |
| $&#46;summary&#46;median&#95;in&#95;zone&#95;seconds | number | 1130&#46;0 |
| $&#46;summary&#46;missing&#95;routes | number | 0 |
| $&#46;summary&#46;out&#95;of&#95;zone | number | 1 |
| $&#46;summary&#46;out&#95;of&#95;zone&#95;percent | number | 33&#46;33 |
| $&#46;summary&#46;resolved | number | 3 |
| $&#46;summary&#46;total | number | 3 |
| $&#46;summary&#46;unknown&#95;membership | number | 0 |
| $&#46;summary&#46;unresolved | number | 0 |
| $&#46;warnings | array | 1 entries |
| $&#46;warnings&#91;0&#93; | string | Competitor results are sampled observations, not a complete market census&#46; |
| $&#46;zone | object | object |
| $&#46;zone&#46;approximation | boolean | false |
| $&#46;zone&#46;evidence&#95;refs | array | 1 entries |
| $&#46;zone&#46;evidence&#95;refs&#91;0&#93; | string | zone |
| $&#46;zone&#46;limitations | array | 2 entries |
| $&#46;zone&#46;limitations&#91;0&#93; | string | Synthetic geometry is authored test evidence, not a live drive&#45;time zone&#46; |
| $&#46;zone&#46;limitations&#91;1&#93; | string | Outbound free&#45;flow driving only; return journeys and live traffic are excluded&#46; |
| $&#46;zone&#46;method | string | geoapify&#95;isoline |
| $&#46;zone&#46;parameters | object | object |
| $&#46;zone&#46;parameters&#46;boundary&#95;tolerance&#95;degrees | number | 1e&#45;09 |
| $&#46;zone&#46;parameters&#46;range&#95;seconds | number | 1200 |
