# ZonePilot report

## Run and method

| Field | Value |
| --- | --- |
| schema&#95;version | 1&#46;0 |
| path | cli |
| data&#95;mode | live |
| run&#95;status | complete |
| run&#95;timestamp&#95;utc | 2026&#45;10&#45;23T20&#58;09&#58;33Z |
| zone.method | geoapify&#95;isoline |
| zone.approximation | false |
| zone.parameters | &#123;&quot;boundary&#95;tolerance&#95;degrees&quot;&#58; 1e&#45;09, &quot;range&#95;seconds&quot;&#58; 1200&#125; |
| zone.limitations | &#91;&quot;Outbound free&#45;flow road&#45;time estimate; no live traffic, return trip or profitability model&#46;&quot;, &quot;All ring boundaries are in zone; segment&#45;distance tolerance 1e&#45;9 degrees&#46;&quot;&#93; |

## Summary

| Field | Value |
| --- | --- |
| borderline | 0 |
| classified&#95;denominator | 20 |
| disagreements | 0 |
| in&#95;zone | 20 |
| in&#95;zone&#95;percent | 100&#46;0 |
| known&#95;routes | 20 |
| max&#95;time&#95;row&#95;ids | &#91;12&#93; |
| max&#95;time&#95;seconds | 1085&#46;0 |
| median&#95;in&#95;zone&#95;seconds | 488&#46;0 |
| missing&#95;routes | 0 |
| out&#95;of&#95;zone | 0 |
| out&#95;of&#95;zone&#95;percent | 0&#46;0 |
| resolved | 20 |
| total | 20 |
| unknown&#95;membership | 0 |
| unresolved | 0 |

## Customers

| Row | Name | Supplied address | Geocode | Membership | Route | Time, seconds | Distance, metres | Within budget | Borderline | Disagreement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Fictional Customer 01 | 615 W Missouri Ave, Midland, TX 79701 | resolved | in&#95;zone | ok | 81&#46;0 | 856&#46;0 | true | false | false |
| 2 | Fictional Customer 02 | 3500 Neely Ave, Midland, TX 79707 | resolved | in&#95;zone | ok | 490&#46;0 | 6142&#46;0 | true | false | false |
| 3 | Fictional Customer 03 | 909 Bonham St, Midland, TX 79703 | resolved | in&#95;zone | ok | 449&#46;0 | 5590&#46;0 | true | false | false |
| 4 | Fictional Customer 04 | 2700 FM 1379, Midland, TX 79706 | resolved | in&#95;zone | ok | 822&#46;0 | 19262&#46;0 | true | false | false |
| 5 | Fictional Customer 05 | 900 S Raymond Rd, Midland, TX 79703 | resolved | in&#95;zone | ok | 486&#46;0 | 5968&#46;0 | true | false | false |
| 6 | Fictional Customer 06 | 5001 Preston Dr, Midland, TX 79707 | resolved | in&#95;zone | ok | 816&#46;0 | 16869&#46;0 | true | false | false |
| 7 | Fictional Customer 07 | 2800 Moss Ave, Midland, TX 79705 | resolved | in&#95;zone | ok | 607&#46;0 | 9863&#46;0 | true | false | false |
| 8 | Fictional Customer 08 | 201 W Dakota Ave, Midland, TX 79701 | resolved | in&#95;zone | ok | 156&#46;0 | 1776&#46;0 | true | false | false |
| 9 | Fictional Customer 09 | 6000 Riverfront Dr, Midland, TX 79706 | resolved | in&#95;zone | ok | 887&#46;0 | 16274&#46;0 | true | false | false |
| 10 | Fictional Customer 10 | 1400 N N St, Midland, TX 79701 | resolved | in&#95;zone | ok | 386&#46;0 | 5246&#46;0 | true | false | false |
| 11 | Fictional Customer 11 | 100 E Gist Ave, Midland, TX 79701 | resolved | in&#95;zone | ok | 247&#46;0 | 3085&#46;0 | true | false | false |
| 12 | Fictional Customer 12 | 9600 Wright Dr, Midland, TX 79706 | resolved | in&#95;zone | ok | 1085&#46;0 | 21635&#46;0 | true | false | false |
| 13 | Fictional Customer 13 | 1705 W Missouri Ave, Midland, TX 79701 | resolved | in&#95;zone | ok | 190&#46;0 | 2214&#46;0 | true | false | false |
| 14 | Fictional Customer 14 | 3800 Norwood St, Midland, TX 79707 | resolved | in&#95;zone | ok | 665&#46;0 | 12587&#46;0 | true | false | false |
| 15 | Fictional Customer 15 | 1700 E Magnolia Ave, Midland, TX 79705 | resolved | in&#95;zone | ok | 344&#46;0 | 4792&#46;0 | true | false | false |
| 16 | Fictional Customer 16 | 2601 Wedgewood St, Midland, TX 79707 | resolved | in&#95;zone | ok | 509&#46;0 | 6331&#46;0 | true | false | false |
| 17 | Fictional Customer 17 | 2400 Fannin Ave, Midland, TX 79705 | resolved | in&#95;zone | ok | 478&#46;0 | 6881&#46;0 | true | false | false |
| 18 | Fictional Customer 18 | 4800 Graceland Dr, Midland, TX 79703 | resolved | in&#95;zone | ok | 722&#46;0 | 13939&#46;0 | true | false | false |
| 19 | Fictional Customer 19 | 2503 W Loop 250 N, Midland, TX 79705 | resolved | in&#95;zone | ok | 569&#46;0 | 10820&#46;0 | true | false | false |
| 20 | Fictional Customer 20 | 301 W Missouri Ave, Midland, TX 79701 | resolved | in&#95;zone | ok | 59&#46;0 | 492&#46;0 | true | false | false |

## Competitors

Counts are observed places. Successful searches are sampled, not a market census.

| Field | Value |
| --- | --- |
| cap&#95;reached | true |
| category | service |
| coverage | sampled |
| duplicate&#95;count | 0 |
| observed&#95;in&#95;zone&#95;count | 19 |
| observed&#95;out&#95;of&#95;zone&#95;count | 1 |
| returned&#95;count | 20 |
| search&#95;extent | &#123;&quot;method&quot;&#58; &quot;rectangle&quot;, &quot;parameters&quot;&#58; &#123;&quot;bbox&quot;&#58; &#91;&#45;102&#46;332248, 31&#46;700116, &#45;101&#46;764102, 32&#46;272319&#93;&#125;&#125; |
| status | ok |
| unclassified&#95;count | 0 |

| ID | Name | Address | Categories | Coordinates, lon/lat | Membership | Geodesic distance, metres |
| --- | --- | --- | --- | --- | --- | --- |
| 51098a62c5358559c0597d0cdbbb86004040f00102f90109ec1d18000000009203194d7920436f6d6d756e6974792043726564697420556e696f6e | My Community Credit Union | My Community Credit Union, 600 West Louisiana Avenue, Midland, TX 79701, United States of America | &#91;&quot;building&quot;, &quot;building&#46;commercial&quot;, &quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;08140692351311, 32&#46;004111749608434&#93; | in&#95;zone | 737&#46;502 |
| 511c339aa6198559c0596d5771aa6bff3f40f00103f90135c79ef6000000009203054368617365 | Chase | Chase, West Wall Street, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;07969059999999, 31&#46;997736599608675&#93; | in&#95;zone | 445&#46;951 |
| 512cea44f3868759c05982908d519eff3f40f00102f9013e19c42b000000009203194d7920436f6d6d756e6974792043726564697420556e696f6e | My Community Credit Union | My Community Credit Union, 912 North Midkiff Road, Midland, TX 79701, United States of America | &#91;&quot;building&quot;, &quot;building&#46;commercial&quot;, &quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;11761171083407, 31&#46;99850949960865&#93; | in&#95;zone | 3967&#46;013 |
| 512da97fb50f8a59c0592b2934b56c014040f00103f901be7671cb0000000092030b53706f727420436c697073 | Sport Clips | Sport Clips, 3208 North Loop 250 West, Midland, TX 79707, United States of America | &#91;&quot;commercial&quot;, &quot;service&quot;, &quot;service&#46;beauty&quot;, &quot;service&#46;beauty&#46;hairdresser&quot;&#93; | &#91;&#45;102&#46;15720879999999, 32&#46;01112999960818&#93; | in&#95;zone | 7802&#46;477 |
| 5136ee169e578859c0592c31946e81044040f00102f901727b75200000000092031656616c766f6c696e6520457870726573732043617265 | Valvoline Express Care | Valvoline Express Care, 4705 North Midkiff Road, Midland, TX 79705, United States of America | &#91;&quot;building&quot;, &quot;building&#46;commercial&quot;, &quot;commercial&quot;, &quot;service&quot;, &quot;service&#46;vehicle&quot;, &quot;service&#46;vehicle&#46;repair&quot;, &quot;service&#46;vehicle&#46;repair&#46;car&quot;&#93; | &#91;&#45;102&#46;13034775008495, 32&#46;03519994960729&#93; | in&#95;zone | 6500&#46;54 |
| 516d167ccc0a8959c059b45e5caa2d024040f00102f901e2b8ac2400000000920318466972737420426173696e2043726564697420556e696f6e | First Basin Credit Union | First Basin Credit Union, 3316 North Midland Drive, Midland, TX 79707, United States of America | &#91;&quot;building&quot;, &quot;building&#46;commercial&quot;, &quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;14128410451822, 32&#46;01701859960795&#93; | in&#95;zone | 6488&#46;823 |
| 518218fad9a38959c059fd36990299fd3f40f00102f9017cbc8926000000009203134c6f6e6573746172204175746f6d6f74697665 | Lonestar Automotive | Lonestar Automotive, 900 North Loop 250 West, Midland, TX 79703, United States of America | &#91;&quot;building&quot;, &quot;building&#46;commercial&quot;, &quot;commercial&quot;, &quot;service&quot;, &quot;service&#46;vehicle&quot;, &quot;service&#46;vehicle&#46;repair&quot;, &quot;service&#46;vehicle&#46;repair&#46;car&quot;&#93; | &#91;&#45;102&#46;15062570022022, 31&#46;990615999608952&#93; | in&#95;zone | 7150&#46;026 |
| 51961128ac1e8859c05949fc33de0c044040f00103f9010f09ead2010000009203054368617365 | Chase | Chase, Courtyard Drive, Midland, TX 79705, United States of America | &#91;&quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;12687209999999, 32&#46;03164269960741&#93; | in&#95;zone | 6001&#46;175 |
| 519655d80c708659c059d079a0ba14fe3f40f00103f9015eb220810100000092031d446973636f756e74204d7566666c65722026204175746f6d6f74697665 | Discount Muffler &amp; Automotive | Discount Muffler &amp; Automotive, 2324 West Wall Street, Midland, TX 79701, United States of America | &#91;&quot;commercial&quot;, &quot;service&quot;, &quot;service&#46;vehicle&quot;, &quot;service&#46;vehicle&#46;repair&quot;, &quot;service&#46;vehicle&#46;repair&#46;car&quot;&#93; | &#91;&#45;102&#46;10058899999999, 31&#46;99250379960887&#93; | in&#95;zone | 2491&#46;628 |
| 51a68b2243ae8559c0599893090918fd3f40f00102f901d28950570000000092031a4c6f6f702032353020436f6c6c6973696f6e2045787072657373 | Loop 250 Collision Express | Loop 250 Collision Express, 1608 West Front Street, Midland, TX 79701, United States of America | &#91;&quot;building&quot;, &quot;building&#46;commercial&quot;, &quot;commercial&quot;, &quot;service&quot;, &quot;service&#46;vehicle&quot;, &quot;service&#46;vehicle&#46;repair&quot;, &quot;service&#46;vehicle&#46;repair&#46;car&quot;&#93; | &#91;&#45;102&#46;0887611234053, 31&#46;988647999609015&#93; | in&#95;zone | 1748&#46;848 |
| 51a84236fe668459c0596f0b868494014040f00102f901942fdc51000000009203114c6172612773204175746f6d6f74697665 | Lara&&#35;x27;s Automotive | Lara&&#35;x27;s Automotive, 1302 North Lamesa Road, Midland, TX 79701, United States of America | &#91;&quot;building&quot;, &quot;building&#46;commercial&quot;, &quot;commercial&quot;, &quot;service&quot;, &quot;service&#46;vehicle&quot;, &quot;service&#46;vehicle&#46;repair&quot;, &quot;service&#46;vehicle&#46;repair&#46;car&quot;&#93; | &#91;&#45;102&#46;0687861947905, 32&#46;01234489960813&#93; | in&#95;zone | 1544&#46;599 |
| 51b754a51b818659c059c0398cee7bfd3f40f00102f9017020784e0000000092031543617272696c6c6f2773204175746f6d6f74697665 | Carrillo&&#35;x27;s Automotive | Carrillo&&#35;x27;s Automotive, 2501 West Wall Street, Midland, TX 79701, United States of America | &#91;&quot;building&quot;, &quot;building&#46;commercial&quot;, &quot;commercial&quot;, &quot;service&quot;, &quot;service&#46;vehicle&quot;, &quot;service&#46;vehicle&#46;repair&quot;, &quot;service&#46;vehicle&#46;repair&#46;car&quot;&#93; | &#91;&#45;102&#46;1016301264343, 31&#46;990172299608957&#93; | in&#95;zone | 2676&#46;464 |
| 51c229a8dcf58859c0593814223b25024040f00102f901604e89430000000092031644727920436c65616e2053757065722043656e746572 | Dry Clean Super Center | Dry Clean Super Center, 4218 West Wadley Avenue, Midland, TX 79707, United States of America | &#91;&quot;building&quot;, &quot;building&#46;commercial&quot;, &quot;commercial&quot;, &quot;service&quot;, &quot;service&#46;cleaning&quot;, &quot;service&#46;cleaning&#46;dry&#95;cleaning&quot;&#93; | &#91;&#45;102&#46;14000622198276, 32&#46;01676119960797&#93; | in&#95;zone | 6365&#46;279 |
| 51c7c0936c828359c059b644a396f7fc3f40f00102f901c1217f4e0000000092030d434d432052656379636c696e67 | CMC Recycling | CMC Recycling, 1605 Garden City Highway, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;recycling&quot;, &quot;service&#46;recycling&#46;centre&quot;&#93; | &#91;&#45;102&#46;05483545712478, 31&#46;98815289960904&#93; | in&#95;zone | 2339&#46;012 |
| 51c978ef036b8859c059986630fcf1034040f00103f901d096c5040200000092030b556c746120426561757479 | Ulta Beauty | Ulta Beauty, 4511 North Midkiff Road, Midland, TX 79705, United States of America | &#91;&quot;commercial&quot;, &quot;commercial&#46;health&#95;and&#95;beauty&quot;, &quot;service&quot;, &quot;service&#46;beauty&quot;, &quot;service&#46;beauty&#46;spa&quot;&#93; | &#91;&#45;102&#46;1315317, 32&#46;03082229960745&#93; | in&#95;zone | 6310&#46;133 |
| 51d82b720f748659c0592ac3affdbffd3f40f00102f9016f20784e000000009203174d69646c616e64204672616d6520616e6420576865656c | Midland Frame and Wheel | Midland Frame and Wheel, 2407 West Wall Street, Midland, TX 79701, United States of America | &#91;&quot;building&quot;, &quot;building&#46;commercial&quot;, &quot;commercial&quot;, &quot;service&quot;, &quot;service&#46;vehicle&quot;, &quot;service&#46;vehicle&#46;repair&quot;, &quot;service&#46;vehicle&#46;repair&#46;car&quot;&#93; | &#91;&#45;102&#46;10083376073396, 31&#46;99121079960893&#93; | in&#95;zone | 2562&#46;912 |
| 51e513ff54ff8859c0596474c93821024040f00102f9015d4e894300000000920312536f66742053756473204175746f20537061 | Soft Suds Auto Spa | Soft Suds Auto Spa, 4300 West Wadley Avenue, Midland, TX 79707, United States of America | &#91;&quot;building&quot;, &quot;building&#46;commercial&quot;, &quot;service&quot;, &quot;service&#46;vehicle&quot;, &quot;service&#46;vehicle&#46;car&#95;wash&quot;&#93; | &#91;&#45;102&#46;14058422956403, 32&#46;01663884960797&#93; | in&#95;zone | 6413&#46;318 |
| 51e85212c81b8959c05905aa52c40e024040f00102f901614e89430000000092031154616b652035204f696c204368616e6765 | Take 5 Oil Change | Take 5 Oil Change, 4404 West Wadley Avenue, Midland, TX 79707, United States of America | &#91;&quot;building&quot;, &quot;building&#46;commercial&quot;, &quot;commercial&quot;, &quot;service&quot;, &quot;service&#46;vehicle&quot;, &quot;service&#46;vehicle&#46;repair&quot;, &quot;service&#46;vehicle&#46;repair&#46;car&quot;&#93; | &#91;&#45;102&#46;14232064999999, 32&#46;01607564960799&#93; | in&#95;zone | 6552&#46;341 |
| 51eb38cb3d8c8559c059c4650ddeb2044040f00102f9019588920a000000009203194d7920436f6d6d756e6974792043726564697420556e696f6e | My Community Credit Union | My Community Credit Union, 4001 North Big Spring Street, Midland, TX 79705, United States of America | &#91;&quot;building&quot;, &quot;building&#46;commercial&quot;, &quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;08668465467387, 32&#46;03670859960724&#93; | in&#95;zone | 4246&#46;566 |

## Evidence

| Entry | Value |
| --- | --- |
| 0 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e001&#46;json&quot;, &quot;id&quot;&#58; &quot;e001&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;business&quot;, &quot;sha256&quot;&#58; &quot;e644ac3a0ba8255675dbdf4b29bd2fa56fc776d07a8bed1a8ed2d83718a93613&quot;&#125; |
| 1 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e002&#46;json&quot;, &quot;id&quot;&#58; &quot;e002&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;isoline&quot;, &quot;sha256&quot;&#58; &quot;29a17d2ab0ffbe562082d23dcf27a18f33e03d2eee1d7e76ff2970bdb5a97b95&quot;&#125; |
| 2 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e003&#46;json&quot;, &quot;id&quot;&#58; &quot;e003&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;faf7a7e83da4c669c715ad3cad4596370ef40856af672274649cde296ceed8cb&quot;&#125; |
| 3 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e004&#46;json&quot;, &quot;id&quot;&#58; &quot;e004&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;bca98f620ae0534fbe29b8ea800522c4da242eda35cb7e31ca9b26caacd1c78e&quot;&#125; |
| 4 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e005&#46;json&quot;, &quot;id&quot;&#58; &quot;e005&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;90456d5246060ca64b6e03a3d6344c4219d71ccd782ddf9c26740c65a5b53c2b&quot;&#125; |
| 5 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e006&#46;json&quot;, &quot;id&quot;&#58; &quot;e006&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;b67fba8ab7a0a46f83796fe23cb3af40420be8f1827eb97febd03363fb3b3552&quot;&#125; |
| 6 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e007&#46;json&quot;, &quot;id&quot;&#58; &quot;e007&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;bf52c3065cd042e406f5a809dd08aa55f9056c6a1eff789acbe10f53730759db&quot;&#125; |
| 7 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e008&#46;json&quot;, &quot;id&quot;&#58; &quot;e008&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;039ea9e88358c2bed1ed7cb9a7e1a28c42d7812dc4bf790363ad6ef5a8b58bbe&quot;&#125; |
| 8 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e009&#46;json&quot;, &quot;id&quot;&#58; &quot;e009&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;848379d22a2858782d240fed52cb52411baad5cea2e10ce19f1a9ac12e00ccfe&quot;&#125; |
| 9 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e010&#46;json&quot;, &quot;id&quot;&#58; &quot;e010&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;7236b9ebed089b83a59de26d5462a5327c66449c6f4712740670756610d4ffa1&quot;&#125; |
| 10 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e011&#46;json&quot;, &quot;id&quot;&#58; &quot;e011&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;a2b15edd04ac655ac3777d2ac1ca291a50a3ffaf14c5846ecc064c1c2b44f84e&quot;&#125; |
| 11 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e012&#46;json&quot;, &quot;id&quot;&#58; &quot;e012&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;2ea3bbc54a40153c2e8698cb2880f96f5eb4ad3091cc96f42ce27dd943674c70&quot;&#125; |
| 12 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e013&#46;json&quot;, &quot;id&quot;&#58; &quot;e013&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;640e1c61819a7228c2bf32920b78d275e11cd713b72b698c4f4abe60e4914586&quot;&#125; |
| 13 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e014&#46;json&quot;, &quot;id&quot;&#58; &quot;e014&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;7a8ec7f2b031901a091f4722d592e8e8c30b95c3aa4ae940e22f86fc68bce9b2&quot;&#125; |
| 14 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e015&#46;json&quot;, &quot;id&quot;&#58; &quot;e015&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;9bdcdcfca0a85a55f744c906439ce7b48411b1af3e91dbf7b1d4898f616bd82e&quot;&#125; |
| 15 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e016&#46;json&quot;, &quot;id&quot;&#58; &quot;e016&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;0f8a84dabd7abc44d9a8f5b27a077e3e36415b63316cf1efce3d105ab1903a50&quot;&#125; |
| 16 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e017&#46;json&quot;, &quot;id&quot;&#58; &quot;e017&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;7311dbbc592ff4d5757e6eb2dc0e2a54aa8d4242eeaea024263a372077803d37&quot;&#125; |
| 17 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e018&#46;json&quot;, &quot;id&quot;&#58; &quot;e018&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;bcaf578e1180c2136616827c8777d3471fa3257aae6859ad081b21ac8d6f5582&quot;&#125; |
| 18 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e019&#46;json&quot;, &quot;id&quot;&#58; &quot;e019&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;8a70a83837d8369afe929b7388a1fb64542e317c37396525867ea6687e0d5db5&quot;&#125; |
| 19 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e020&#46;json&quot;, &quot;id&quot;&#58; &quot;e020&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;fb01e21876cedf9e2e5be9c6bdfcaa17660919ad45836ad26e7a9ae4359f8937&quot;&#125; |
| 20 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e021&#46;json&quot;, &quot;id&quot;&#58; &quot;e021&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;61a41b2fe9156bc4453dd66caebeb38e9e71ee959ac915fe3219c4c525f106d5&quot;&#125; |
| 21 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e022&#46;json&quot;, &quot;id&quot;&#58; &quot;e022&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;09d9c58d35b4b2870cab063fde88738e8377621d114edea399ee7f8f2126acd0&quot;&#125; |
| 22 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e023&#46;json&quot;, &quot;id&quot;&#58; &quot;e023&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;route&#95;matrix&quot;, &quot;sha256&quot;&#58; &quot;ff1525e77f4380e58b5094b7805205811d6cd1d55a4b1e9d339401cdd3d78c33&quot;&#125; |
| 23 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e024&#46;json&quot;, &quot;id&quot;&#58; &quot;e024&quot;, &quot;kind&quot;&#58; &quot;rest&quot;, &quot;operation&quot;&#58; &quot;places&quot;, &quot;sha256&quot;&#58; &quot;a4135d82fe51394df8d34608e48499e1c91808cc93dd430cc4729af994193d86&quot;&#125; |

## Errors

| Entry | Value |
| --- | --- |
| entries | [] |

## Warnings

| Entry | Value |
| --- | --- |
| 0 | Competitor coverage is sampled, at most 20 candidates and no pagination&#46; |
| 1 | The category service is broad; these candidates are not verified plumbing competitors&#46; |
| 2 | HTTP attempts&#58; 24; isoline polls&#58; 0; billed credits unavailable&#46; |

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
| $&#46;business&#46;coordinates&#91;0&#93; | number | &#45;102&#46;075567 |
| $&#46;business&#46;coordinates&#91;1&#93; | number | 31&#46;9997 |
| $&#46;business&#46;geocode&#95;evidence | object | object |
| $&#46;business&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;business&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;business&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;business&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;business&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;business&#46;input&#95;address | string | 300 N Loraine St, Midland, TX 79701 |
| $&#46;business&#46;name | string | Main Street Plumbing |
| $&#46;business&#46;resolved&#95;address | string | 300 North Loraine Street, Downtown Midland Management District, Midland, TX 79701, United States of America |
| $&#46;competitors | object | object |
| $&#46;competitors&#46;cap&#95;reached | boolean | true |
| $&#46;competitors&#46;category | string | service |
| $&#46;competitors&#46;coverage | string | sampled |
| $&#46;competitors&#46;duplicate&#95;count | number | 0 |
| $&#46;competitors&#46;observed&#95;in&#95;zone&#95;count | number | 19 |
| $&#46;competitors&#46;observed&#95;out&#95;of&#95;zone&#95;count | number | 1 |
| $&#46;competitors&#46;records | array | 19 entries |
| $&#46;competitors&#46;records&#91;0&#93; | object | object |
| $&#46;competitors&#46;records&#91;0&#93;&#46;address | string | My Community Credit Union, 600 West Louisiana Avenue, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories | array | 5 entries |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories&#91;1&#93; | string | building&#46;commercial |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories&#91;2&#93; | string | service |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories&#91;3&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories&#91;4&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;0&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;0&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;08140692351311 |
| $&#46;competitors&#46;records&#91;0&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;004111749608434 |
| $&#46;competitors&#46;records&#91;0&#93;&#46;geodesic&#95;distance&#95;meters | number | 737&#46;502 |
| $&#46;competitors&#46;records&#91;0&#93;&#46;id | string | 51098a62c5358559c0597d0cdbbb86004040f00102f90109ec1d18000000009203194d7920436f6d6d756e6974792043726564697420556e696f6e |
| $&#46;competitors&#46;records&#91;0&#93;&#46;name | string | My Community Credit Union |
| $&#46;competitors&#46;records&#91;0&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;1&#93; | object | object |
| $&#46;competitors&#46;records&#91;1&#93;&#46;address | string | Chase, West Wall Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;1&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;1&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;1&#93;&#46;categories&#91;1&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;1&#93;&#46;categories&#91;2&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;1&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;1&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;07969059999999 |
| $&#46;competitors&#46;records&#91;1&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;997736599608675 |
| $&#46;competitors&#46;records&#91;1&#93;&#46;geodesic&#95;distance&#95;meters | number | 445&#46;951 |
| $&#46;competitors&#46;records&#91;1&#93;&#46;id | string | 511c339aa6198559c0596d5771aa6bff3f40f00103f90135c79ef6000000009203054368617365 |
| $&#46;competitors&#46;records&#91;1&#93;&#46;name | string | Chase |
| $&#46;competitors&#46;records&#91;1&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;2&#93; | object | object |
| $&#46;competitors&#46;records&#91;2&#93;&#46;address | string | My Community Credit Union, 912 North Midkiff Road, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;2&#93;&#46;categories | array | 5 entries |
| $&#46;competitors&#46;records&#91;2&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;2&#93;&#46;categories&#91;1&#93; | string | building&#46;commercial |
| $&#46;competitors&#46;records&#91;2&#93;&#46;categories&#91;2&#93; | string | service |
| $&#46;competitors&#46;records&#91;2&#93;&#46;categories&#91;3&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;2&#93;&#46;categories&#91;4&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;2&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;2&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;11761171083407 |
| $&#46;competitors&#46;records&#91;2&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;99850949960865 |
| $&#46;competitors&#46;records&#91;2&#93;&#46;geodesic&#95;distance&#95;meters | number | 3967&#46;013 |
| $&#46;competitors&#46;records&#91;2&#93;&#46;id | string | 512cea44f3868759c05982908d519eff3f40f00102f9013e19c42b000000009203194d7920436f6d6d756e6974792043726564697420556e696f6e |
| $&#46;competitors&#46;records&#91;2&#93;&#46;name | string | My Community Credit Union |
| $&#46;competitors&#46;records&#91;2&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;3&#93; | object | object |
| $&#46;competitors&#46;records&#91;3&#93;&#46;address | string | Sport Clips, 3208 North Loop 250 West, Midland, TX 79707, United States of America |
| $&#46;competitors&#46;records&#91;3&#93;&#46;categories | array | 4 entries |
| $&#46;competitors&#46;records&#91;3&#93;&#46;categories&#91;0&#93; | string | commercial |
| $&#46;competitors&#46;records&#91;3&#93;&#46;categories&#91;1&#93; | string | service |
| $&#46;competitors&#46;records&#91;3&#93;&#46;categories&#91;2&#93; | string | service&#46;beauty |
| $&#46;competitors&#46;records&#91;3&#93;&#46;categories&#91;3&#93; | string | service&#46;beauty&#46;hairdresser |
| $&#46;competitors&#46;records&#91;3&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;3&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;15720879999999 |
| $&#46;competitors&#46;records&#91;3&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;01112999960818 |
| $&#46;competitors&#46;records&#91;3&#93;&#46;geodesic&#95;distance&#95;meters | number | 7802&#46;477 |
| $&#46;competitors&#46;records&#91;3&#93;&#46;id | string | 512da97fb50f8a59c0592b2934b56c014040f00103f901be7671cb0000000092030b53706f727420436c697073 |
| $&#46;competitors&#46;records&#91;3&#93;&#46;name | string | Sport Clips |
| $&#46;competitors&#46;records&#91;3&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;4&#93; | object | object |
| $&#46;competitors&#46;records&#91;4&#93;&#46;address | string | Valvoline Express Care, 4705 North Midkiff Road, Midland, TX 79705, United States of America |
| $&#46;competitors&#46;records&#91;4&#93;&#46;categories | array | 7 entries |
| $&#46;competitors&#46;records&#91;4&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;4&#93;&#46;categories&#91;1&#93; | string | building&#46;commercial |
| $&#46;competitors&#46;records&#91;4&#93;&#46;categories&#91;2&#93; | string | commercial |
| $&#46;competitors&#46;records&#91;4&#93;&#46;categories&#91;3&#93; | string | service |
| $&#46;competitors&#46;records&#91;4&#93;&#46;categories&#91;4&#93; | string | service&#46;vehicle |
| $&#46;competitors&#46;records&#91;4&#93;&#46;categories&#91;5&#93; | string | service&#46;vehicle&#46;repair |
| $&#46;competitors&#46;records&#91;4&#93;&#46;categories&#91;6&#93; | string | service&#46;vehicle&#46;repair&#46;car |
| $&#46;competitors&#46;records&#91;4&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;4&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;13034775008495 |
| $&#46;competitors&#46;records&#91;4&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;03519994960729 |
| $&#46;competitors&#46;records&#91;4&#93;&#46;geodesic&#95;distance&#95;meters | number | 6500&#46;54 |
| $&#46;competitors&#46;records&#91;4&#93;&#46;id | string | 5136ee169e578859c0592c31946e81044040f00102f901727b75200000000092031656616c766f6c696e6520457870726573732043617265 |
| $&#46;competitors&#46;records&#91;4&#93;&#46;name | string | Valvoline Express Care |
| $&#46;competitors&#46;records&#91;4&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;5&#93; | object | object |
| $&#46;competitors&#46;records&#91;5&#93;&#46;address | string | First Basin Credit Union, 3316 North Midland Drive, Midland, TX 79707, United States of America |
| $&#46;competitors&#46;records&#91;5&#93;&#46;categories | array | 5 entries |
| $&#46;competitors&#46;records&#91;5&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;5&#93;&#46;categories&#91;1&#93; | string | building&#46;commercial |
| $&#46;competitors&#46;records&#91;5&#93;&#46;categories&#91;2&#93; | string | service |
| $&#46;competitors&#46;records&#91;5&#93;&#46;categories&#91;3&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;5&#93;&#46;categories&#91;4&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;5&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;5&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;14128410451822 |
| $&#46;competitors&#46;records&#91;5&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;01701859960795 |
| $&#46;competitors&#46;records&#91;5&#93;&#46;geodesic&#95;distance&#95;meters | number | 6488&#46;823 |
| $&#46;competitors&#46;records&#91;5&#93;&#46;id | string | 516d167ccc0a8959c059b45e5caa2d024040f00102f901e2b8ac2400000000920318466972737420426173696e2043726564697420556e696f6e |
| $&#46;competitors&#46;records&#91;5&#93;&#46;name | string | First Basin Credit Union |
| $&#46;competitors&#46;records&#91;5&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;6&#93; | object | object |
| $&#46;competitors&#46;records&#91;6&#93;&#46;address | string | Lonestar Automotive, 900 North Loop 250 West, Midland, TX 79703, United States of America |
| $&#46;competitors&#46;records&#91;6&#93;&#46;categories | array | 7 entries |
| $&#46;competitors&#46;records&#91;6&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;6&#93;&#46;categories&#91;1&#93; | string | building&#46;commercial |
| $&#46;competitors&#46;records&#91;6&#93;&#46;categories&#91;2&#93; | string | commercial |
| $&#46;competitors&#46;records&#91;6&#93;&#46;categories&#91;3&#93; | string | service |
| $&#46;competitors&#46;records&#91;6&#93;&#46;categories&#91;4&#93; | string | service&#46;vehicle |
| $&#46;competitors&#46;records&#91;6&#93;&#46;categories&#91;5&#93; | string | service&#46;vehicle&#46;repair |
| $&#46;competitors&#46;records&#91;6&#93;&#46;categories&#91;6&#93; | string | service&#46;vehicle&#46;repair&#46;car |
| $&#46;competitors&#46;records&#91;6&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;6&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;15062570022022 |
| $&#46;competitors&#46;records&#91;6&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;990615999608952 |
| $&#46;competitors&#46;records&#91;6&#93;&#46;geodesic&#95;distance&#95;meters | number | 7150&#46;026 |
| $&#46;competitors&#46;records&#91;6&#93;&#46;id | string | 518218fad9a38959c059fd36990299fd3f40f00102f9017cbc8926000000009203134c6f6e6573746172204175746f6d6f74697665 |
| $&#46;competitors&#46;records&#91;6&#93;&#46;name | string | Lonestar Automotive |
| $&#46;competitors&#46;records&#91;6&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;7&#93; | object | object |
| $&#46;competitors&#46;records&#91;7&#93;&#46;address | string | Chase, Courtyard Drive, Midland, TX 79705, United States of America |
| $&#46;competitors&#46;records&#91;7&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;7&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;7&#93;&#46;categories&#91;1&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;7&#93;&#46;categories&#91;2&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;7&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;7&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;12687209999999 |
| $&#46;competitors&#46;records&#91;7&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;03164269960741 |
| $&#46;competitors&#46;records&#91;7&#93;&#46;geodesic&#95;distance&#95;meters | number | 6001&#46;175 |
| $&#46;competitors&#46;records&#91;7&#93;&#46;id | string | 51961128ac1e8859c05949fc33de0c044040f00103f9010f09ead2010000009203054368617365 |
| $&#46;competitors&#46;records&#91;7&#93;&#46;name | string | Chase |
| $&#46;competitors&#46;records&#91;7&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;8&#93; | object | object |
| $&#46;competitors&#46;records&#91;8&#93;&#46;address | string | Discount Muffler &amp; Automotive, 2324 West Wall Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;8&#93;&#46;categories | array | 5 entries |
| $&#46;competitors&#46;records&#91;8&#93;&#46;categories&#91;0&#93; | string | commercial |
| $&#46;competitors&#46;records&#91;8&#93;&#46;categories&#91;1&#93; | string | service |
| $&#46;competitors&#46;records&#91;8&#93;&#46;categories&#91;2&#93; | string | service&#46;vehicle |
| $&#46;competitors&#46;records&#91;8&#93;&#46;categories&#91;3&#93; | string | service&#46;vehicle&#46;repair |
| $&#46;competitors&#46;records&#91;8&#93;&#46;categories&#91;4&#93; | string | service&#46;vehicle&#46;repair&#46;car |
| $&#46;competitors&#46;records&#91;8&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;8&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;10058899999999 |
| $&#46;competitors&#46;records&#91;8&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;99250379960887 |
| $&#46;competitors&#46;records&#91;8&#93;&#46;geodesic&#95;distance&#95;meters | number | 2491&#46;628 |
| $&#46;competitors&#46;records&#91;8&#93;&#46;id | string | 519655d80c708659c059d079a0ba14fe3f40f00103f9015eb220810100000092031d446973636f756e74204d7566666c65722026204175746f6d6f74697665 |
| $&#46;competitors&#46;records&#91;8&#93;&#46;name | string | Discount Muffler &amp; Automotive |
| $&#46;competitors&#46;records&#91;8&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;9&#93; | object | object |
| $&#46;competitors&#46;records&#91;9&#93;&#46;address | string | Loop 250 Collision Express, 1608 West Front Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;9&#93;&#46;categories | array | 7 entries |
| $&#46;competitors&#46;records&#91;9&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;9&#93;&#46;categories&#91;1&#93; | string | building&#46;commercial |
| $&#46;competitors&#46;records&#91;9&#93;&#46;categories&#91;2&#93; | string | commercial |
| $&#46;competitors&#46;records&#91;9&#93;&#46;categories&#91;3&#93; | string | service |
| $&#46;competitors&#46;records&#91;9&#93;&#46;categories&#91;4&#93; | string | service&#46;vehicle |
| $&#46;competitors&#46;records&#91;9&#93;&#46;categories&#91;5&#93; | string | service&#46;vehicle&#46;repair |
| $&#46;competitors&#46;records&#91;9&#93;&#46;categories&#91;6&#93; | string | service&#46;vehicle&#46;repair&#46;car |
| $&#46;competitors&#46;records&#91;9&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;9&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0887611234053 |
| $&#46;competitors&#46;records&#91;9&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;988647999609015 |
| $&#46;competitors&#46;records&#91;9&#93;&#46;geodesic&#95;distance&#95;meters | number | 1748&#46;848 |
| $&#46;competitors&#46;records&#91;9&#93;&#46;id | string | 51a68b2243ae8559c0599893090918fd3f40f00102f901d28950570000000092031a4c6f6f702032353020436f6c6c6973696f6e2045787072657373 |
| $&#46;competitors&#46;records&#91;9&#93;&#46;name | string | Loop 250 Collision Express |
| $&#46;competitors&#46;records&#91;9&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;10&#93; | object | object |
| $&#46;competitors&#46;records&#91;10&#93;&#46;address | string | Lara&&#35;x27;s Automotive, 1302 North Lamesa Road, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;10&#93;&#46;categories | array | 7 entries |
| $&#46;competitors&#46;records&#91;10&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;10&#93;&#46;categories&#91;1&#93; | string | building&#46;commercial |
| $&#46;competitors&#46;records&#91;10&#93;&#46;categories&#91;2&#93; | string | commercial |
| $&#46;competitors&#46;records&#91;10&#93;&#46;categories&#91;3&#93; | string | service |
| $&#46;competitors&#46;records&#91;10&#93;&#46;categories&#91;4&#93; | string | service&#46;vehicle |
| $&#46;competitors&#46;records&#91;10&#93;&#46;categories&#91;5&#93; | string | service&#46;vehicle&#46;repair |
| $&#46;competitors&#46;records&#91;10&#93;&#46;categories&#91;6&#93; | string | service&#46;vehicle&#46;repair&#46;car |
| $&#46;competitors&#46;records&#91;10&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;10&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0687861947905 |
| $&#46;competitors&#46;records&#91;10&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;01234489960813 |
| $&#46;competitors&#46;records&#91;10&#93;&#46;geodesic&#95;distance&#95;meters | number | 1544&#46;599 |
| $&#46;competitors&#46;records&#91;10&#93;&#46;id | string | 51a84236fe668459c0596f0b868494014040f00102f901942fdc51000000009203114c6172612773204175746f6d6f74697665 |
| $&#46;competitors&#46;records&#91;10&#93;&#46;name | string | Lara&&#35;x27;s Automotive |
| $&#46;competitors&#46;records&#91;10&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;11&#93; | object | object |
| $&#46;competitors&#46;records&#91;11&#93;&#46;address | string | Carrillo&&#35;x27;s Automotive, 2501 West Wall Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;11&#93;&#46;categories | array | 7 entries |
| $&#46;competitors&#46;records&#91;11&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;11&#93;&#46;categories&#91;1&#93; | string | building&#46;commercial |
| $&#46;competitors&#46;records&#91;11&#93;&#46;categories&#91;2&#93; | string | commercial |
| $&#46;competitors&#46;records&#91;11&#93;&#46;categories&#91;3&#93; | string | service |
| $&#46;competitors&#46;records&#91;11&#93;&#46;categories&#91;4&#93; | string | service&#46;vehicle |
| $&#46;competitors&#46;records&#91;11&#93;&#46;categories&#91;5&#93; | string | service&#46;vehicle&#46;repair |
| $&#46;competitors&#46;records&#91;11&#93;&#46;categories&#91;6&#93; | string | service&#46;vehicle&#46;repair&#46;car |
| $&#46;competitors&#46;records&#91;11&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;11&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;1016301264343 |
| $&#46;competitors&#46;records&#91;11&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;990172299608957 |
| $&#46;competitors&#46;records&#91;11&#93;&#46;geodesic&#95;distance&#95;meters | number | 2676&#46;464 |
| $&#46;competitors&#46;records&#91;11&#93;&#46;id | string | 51b754a51b818659c059c0398cee7bfd3f40f00102f9017020784e0000000092031543617272696c6c6f2773204175746f6d6f74697665 |
| $&#46;competitors&#46;records&#91;11&#93;&#46;name | string | Carrillo&&#35;x27;s Automotive |
| $&#46;competitors&#46;records&#91;11&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;12&#93; | object | object |
| $&#46;competitors&#46;records&#91;12&#93;&#46;address | string | Dry Clean Super Center, 4218 West Wadley Avenue, Midland, TX 79707, United States of America |
| $&#46;competitors&#46;records&#91;12&#93;&#46;categories | array | 6 entries |
| $&#46;competitors&#46;records&#91;12&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;12&#93;&#46;categories&#91;1&#93; | string | building&#46;commercial |
| $&#46;competitors&#46;records&#91;12&#93;&#46;categories&#91;2&#93; | string | commercial |
| $&#46;competitors&#46;records&#91;12&#93;&#46;categories&#91;3&#93; | string | service |
| $&#46;competitors&#46;records&#91;12&#93;&#46;categories&#91;4&#93; | string | service&#46;cleaning |
| $&#46;competitors&#46;records&#91;12&#93;&#46;categories&#91;5&#93; | string | service&#46;cleaning&#46;dry&#95;cleaning |
| $&#46;competitors&#46;records&#91;12&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;12&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;14000622198276 |
| $&#46;competitors&#46;records&#91;12&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;01676119960797 |
| $&#46;competitors&#46;records&#91;12&#93;&#46;geodesic&#95;distance&#95;meters | number | 6365&#46;279 |
| $&#46;competitors&#46;records&#91;12&#93;&#46;id | string | 51c229a8dcf58859c0593814223b25024040f00102f901604e89430000000092031644727920436c65616e2053757065722043656e746572 |
| $&#46;competitors&#46;records&#91;12&#93;&#46;name | string | Dry Clean Super Center |
| $&#46;competitors&#46;records&#91;12&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;13&#93; | object | object |
| $&#46;competitors&#46;records&#91;13&#93;&#46;address | string | CMC Recycling, 1605 Garden City Highway, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;13&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;13&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;13&#93;&#46;categories&#91;1&#93; | string | service&#46;recycling |
| $&#46;competitors&#46;records&#91;13&#93;&#46;categories&#91;2&#93; | string | service&#46;recycling&#46;centre |
| $&#46;competitors&#46;records&#91;13&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;13&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;05483545712478 |
| $&#46;competitors&#46;records&#91;13&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;98815289960904 |
| $&#46;competitors&#46;records&#91;13&#93;&#46;geodesic&#95;distance&#95;meters | number | 2339&#46;012 |
| $&#46;competitors&#46;records&#91;13&#93;&#46;id | string | 51c7c0936c828359c059b644a396f7fc3f40f00102f901c1217f4e0000000092030d434d432052656379636c696e67 |
| $&#46;competitors&#46;records&#91;13&#93;&#46;name | string | CMC Recycling |
| $&#46;competitors&#46;records&#91;13&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;14&#93; | object | object |
| $&#46;competitors&#46;records&#91;14&#93;&#46;address | string | Ulta Beauty, 4511 North Midkiff Road, Midland, TX 79705, United States of America |
| $&#46;competitors&#46;records&#91;14&#93;&#46;categories | array | 5 entries |
| $&#46;competitors&#46;records&#91;14&#93;&#46;categories&#91;0&#93; | string | commercial |
| $&#46;competitors&#46;records&#91;14&#93;&#46;categories&#91;1&#93; | string | commercial&#46;health&#95;and&#95;beauty |
| $&#46;competitors&#46;records&#91;14&#93;&#46;categories&#91;2&#93; | string | service |
| $&#46;competitors&#46;records&#91;14&#93;&#46;categories&#91;3&#93; | string | service&#46;beauty |
| $&#46;competitors&#46;records&#91;14&#93;&#46;categories&#91;4&#93; | string | service&#46;beauty&#46;spa |
| $&#46;competitors&#46;records&#91;14&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;14&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;1315317 |
| $&#46;competitors&#46;records&#91;14&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;03082229960745 |
| $&#46;competitors&#46;records&#91;14&#93;&#46;geodesic&#95;distance&#95;meters | number | 6310&#46;133 |
| $&#46;competitors&#46;records&#91;14&#93;&#46;id | string | 51c978ef036b8859c059986630fcf1034040f00103f901d096c5040200000092030b556c746120426561757479 |
| $&#46;competitors&#46;records&#91;14&#93;&#46;name | string | Ulta Beauty |
| $&#46;competitors&#46;records&#91;14&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;15&#93; | object | object |
| $&#46;competitors&#46;records&#91;15&#93;&#46;address | string | Midland Frame and Wheel, 2407 West Wall Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;15&#93;&#46;categories | array | 7 entries |
| $&#46;competitors&#46;records&#91;15&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;15&#93;&#46;categories&#91;1&#93; | string | building&#46;commercial |
| $&#46;competitors&#46;records&#91;15&#93;&#46;categories&#91;2&#93; | string | commercial |
| $&#46;competitors&#46;records&#91;15&#93;&#46;categories&#91;3&#93; | string | service |
| $&#46;competitors&#46;records&#91;15&#93;&#46;categories&#91;4&#93; | string | service&#46;vehicle |
| $&#46;competitors&#46;records&#91;15&#93;&#46;categories&#91;5&#93; | string | service&#46;vehicle&#46;repair |
| $&#46;competitors&#46;records&#91;15&#93;&#46;categories&#91;6&#93; | string | service&#46;vehicle&#46;repair&#46;car |
| $&#46;competitors&#46;records&#91;15&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;15&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;10083376073396 |
| $&#46;competitors&#46;records&#91;15&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;99121079960893 |
| $&#46;competitors&#46;records&#91;15&#93;&#46;geodesic&#95;distance&#95;meters | number | 2562&#46;912 |
| $&#46;competitors&#46;records&#91;15&#93;&#46;id | string | 51d82b720f748659c0592ac3affdbffd3f40f00102f9016f20784e000000009203174d69646c616e64204672616d6520616e6420576865656c |
| $&#46;competitors&#46;records&#91;15&#93;&#46;name | string | Midland Frame and Wheel |
| $&#46;competitors&#46;records&#91;15&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;16&#93; | object | object |
| $&#46;competitors&#46;records&#91;16&#93;&#46;address | string | Soft Suds Auto Spa, 4300 West Wadley Avenue, Midland, TX 79707, United States of America |
| $&#46;competitors&#46;records&#91;16&#93;&#46;categories | array | 5 entries |
| $&#46;competitors&#46;records&#91;16&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;16&#93;&#46;categories&#91;1&#93; | string | building&#46;commercial |
| $&#46;competitors&#46;records&#91;16&#93;&#46;categories&#91;2&#93; | string | service |
| $&#46;competitors&#46;records&#91;16&#93;&#46;categories&#91;3&#93; | string | service&#46;vehicle |
| $&#46;competitors&#46;records&#91;16&#93;&#46;categories&#91;4&#93; | string | service&#46;vehicle&#46;car&#95;wash |
| $&#46;competitors&#46;records&#91;16&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;16&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;14058422956403 |
| $&#46;competitors&#46;records&#91;16&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;01663884960797 |
| $&#46;competitors&#46;records&#91;16&#93;&#46;geodesic&#95;distance&#95;meters | number | 6413&#46;318 |
| $&#46;competitors&#46;records&#91;16&#93;&#46;id | string | 51e513ff54ff8859c0596474c93821024040f00102f9015d4e894300000000920312536f66742053756473204175746f20537061 |
| $&#46;competitors&#46;records&#91;16&#93;&#46;name | string | Soft Suds Auto Spa |
| $&#46;competitors&#46;records&#91;16&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;17&#93; | object | object |
| $&#46;competitors&#46;records&#91;17&#93;&#46;address | string | Take 5 Oil Change, 4404 West Wadley Avenue, Midland, TX 79707, United States of America |
| $&#46;competitors&#46;records&#91;17&#93;&#46;categories | array | 7 entries |
| $&#46;competitors&#46;records&#91;17&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;17&#93;&#46;categories&#91;1&#93; | string | building&#46;commercial |
| $&#46;competitors&#46;records&#91;17&#93;&#46;categories&#91;2&#93; | string | commercial |
| $&#46;competitors&#46;records&#91;17&#93;&#46;categories&#91;3&#93; | string | service |
| $&#46;competitors&#46;records&#91;17&#93;&#46;categories&#91;4&#93; | string | service&#46;vehicle |
| $&#46;competitors&#46;records&#91;17&#93;&#46;categories&#91;5&#93; | string | service&#46;vehicle&#46;repair |
| $&#46;competitors&#46;records&#91;17&#93;&#46;categories&#91;6&#93; | string | service&#46;vehicle&#46;repair&#46;car |
| $&#46;competitors&#46;records&#91;17&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;17&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;14232064999999 |
| $&#46;competitors&#46;records&#91;17&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;01607564960799 |
| $&#46;competitors&#46;records&#91;17&#93;&#46;geodesic&#95;distance&#95;meters | number | 6552&#46;341 |
| $&#46;competitors&#46;records&#91;17&#93;&#46;id | string | 51e85212c81b8959c05905aa52c40e024040f00102f901614e89430000000092031154616b652035204f696c204368616e6765 |
| $&#46;competitors&#46;records&#91;17&#93;&#46;name | string | Take 5 Oil Change |
| $&#46;competitors&#46;records&#91;17&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;18&#93; | object | object |
| $&#46;competitors&#46;records&#91;18&#93;&#46;address | string | My Community Credit Union, 4001 North Big Spring Street, Midland, TX 79705, United States of America |
| $&#46;competitors&#46;records&#91;18&#93;&#46;categories | array | 5 entries |
| $&#46;competitors&#46;records&#91;18&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;18&#93;&#46;categories&#91;1&#93; | string | building&#46;commercial |
| $&#46;competitors&#46;records&#91;18&#93;&#46;categories&#91;2&#93; | string | service |
| $&#46;competitors&#46;records&#91;18&#93;&#46;categories&#91;3&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;18&#93;&#46;categories&#91;4&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;18&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;18&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;08668465467387 |
| $&#46;competitors&#46;records&#91;18&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;03670859960724 |
| $&#46;competitors&#46;records&#91;18&#93;&#46;geodesic&#95;distance&#95;meters | number | 4246&#46;566 |
| $&#46;competitors&#46;records&#91;18&#93;&#46;id | string | 51eb38cb3d8c8559c059c4650ddeb2044040f00102f9019588920a000000009203194d7920436f6d6d756e6974792043726564697420556e696f6e |
| $&#46;competitors&#46;records&#91;18&#93;&#46;name | string | My Community Credit Union |
| $&#46;competitors&#46;records&#91;18&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;returned&#95;count | number | 20 |
| $&#46;competitors&#46;search&#95;extent | object | object |
| $&#46;competitors&#46;search&#95;extent&#46;method | string | rectangle |
| $&#46;competitors&#46;search&#95;extent&#46;parameters | object | object |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox | array | 4 entries |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox&#91;0&#93; | number | &#45;102&#46;332248 |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox&#91;1&#93; | number | 31&#46;700116 |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox&#91;2&#93; | number | &#45;101&#46;764102 |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;bbox&#91;3&#93; | number | 32&#46;272319 |
| $&#46;competitors&#46;status | string | ok |
| $&#46;competitors&#46;unclassified&#95;count | number | 0 |
| $&#46;customers | array | 20 entries |
| $&#46;customers&#91;0&#93; | object | object |
| $&#46;customers&#91;0&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;0&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;0&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;08075785714286 |
| $&#46;customers&#91;0&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;99625142857143 |
| $&#46;customers&#91;0&#93;&#46;distance&#95;meters | number | 856&#46;0 |
| $&#46;customers&#91;0&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;0&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e003 |
| $&#46;customers&#91;0&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;0&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;0&#93;&#46;input&#95;address | string | 615 W Missouri Ave, Midland, TX 79701 |
| $&#46;customers&#91;0&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;0&#93;&#46;name | string | Fictional Customer 01 |
| $&#46;customers&#91;0&#93;&#46;reference | string | DEMO&#45;01 |
| $&#46;customers&#91;0&#93;&#46;resolved&#95;address | string | 615 West Missouri Avenue, Downtown Midland Management District, Midland, TX 79701, United States of America |
| $&#46;customers&#91;0&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;0&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;0&#93;&#46;row&#95;id | number | 1 |
| $&#46;customers&#91;0&#93;&#46;time&#95;seconds | number | 81&#46;0 |
| $&#46;customers&#91;0&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;1&#93; | object | object |
| $&#46;customers&#91;1&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;1&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;1&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;12886042723052 |
| $&#46;customers&#91;1&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;011364317804045 |
| $&#46;customers&#91;1&#93;&#46;distance&#95;meters | number | 6142&#46;0 |
| $&#46;customers&#91;1&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;1&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e004 |
| $&#46;customers&#91;1&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 2 |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;1&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;1&#93;&#46;input&#95;address | string | 3500 Neely Ave, Midland, TX 79707 |
| $&#46;customers&#91;1&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;1&#93;&#46;name | string | Fictional Customer 02 |
| $&#46;customers&#91;1&#93;&#46;reference | string | DEMO&#45;02 |
| $&#46;customers&#91;1&#93;&#46;resolved&#95;address | string | 3500 Neely Avenue, Midland, TX 79707, United States of America |
| $&#46;customers&#91;1&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;1&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;1&#93;&#46;row&#95;id | number | 2 |
| $&#46;customers&#91;1&#93;&#46;time&#95;seconds | number | 490&#46;0 |
| $&#46;customers&#91;1&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;2&#93; | object | object |
| $&#46;customers&#91;2&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;2&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;2&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;12813177220578 |
| $&#46;customers&#91;2&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;995025705553658 |
| $&#46;customers&#91;2&#93;&#46;distance&#95;meters | number | 5590&#46;0 |
| $&#46;customers&#91;2&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;2&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e005 |
| $&#46;customers&#91;2&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;2&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;2&#93;&#46;input&#95;address | string | 909 Bonham St, Midland, TX 79703 |
| $&#46;customers&#91;2&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;2&#93;&#46;name | string | Fictional Customer 03 |
| $&#46;customers&#91;2&#93;&#46;reference | string | DEMO&#45;03 |
| $&#46;customers&#91;2&#93;&#46;resolved&#95;address | string | 909 Bonham Street, Midland, TX 79703, United States of America |
| $&#46;customers&#91;2&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;2&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;2&#93;&#46;row&#95;id | number | 3 |
| $&#46;customers&#91;2&#93;&#46;time&#95;seconds | number | 449&#46;0 |
| $&#46;customers&#91;2&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;3&#93; | object | object |
| $&#46;customers&#91;3&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;3&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;3&#93;&#46;coordinates&#91;0&#93; | number | &#45;101&#46;895762 |
| $&#46;customers&#91;3&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;027595 |
| $&#46;customers&#91;3&#93;&#46;distance&#95;meters | number | 19262&#46;0 |
| $&#46;customers&#91;3&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;3&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e006 |
| $&#46;customers&#91;3&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;3&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;3&#93;&#46;input&#95;address | string | 2700 FM 1379, Midland, TX 79706 |
| $&#46;customers&#91;3&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;3&#93;&#46;name | string | Fictional Customer 04 |
| $&#46;customers&#91;3&#93;&#46;reference | string | DEMO&#45;04 |
| $&#46;customers&#91;3&#93;&#46;resolved&#95;address | string | 2700 FM 1379, Greenwood, TX 79706, United States of America |
| $&#46;customers&#91;3&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;3&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;3&#93;&#46;row&#95;id | number | 4 |
| $&#46;customers&#91;3&#93;&#46;time&#95;seconds | number | 822&#46;0 |
| $&#46;customers&#91;3&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;4&#93; | object | object |
| $&#46;customers&#91;4&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;4&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;4&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;1234 |
| $&#46;customers&#91;4&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;977861 |
| $&#46;customers&#91;4&#93;&#46;distance&#95;meters | number | 5968&#46;0 |
| $&#46;customers&#91;4&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;4&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e007 |
| $&#46;customers&#91;4&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;4&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;4&#93;&#46;input&#95;address | string | 900 S Raymond Rd, Midland, TX 79703 |
| $&#46;customers&#91;4&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;4&#93;&#46;name | string | Fictional Customer 05 |
| $&#46;customers&#91;4&#93;&#46;reference | string | DEMO&#45;05 |
| $&#46;customers&#91;4&#93;&#46;resolved&#95;address | string | 900 South Raymond Road, Midland, TX 79703, United States of America |
| $&#46;customers&#91;4&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;4&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;4&#93;&#46;row&#95;id | number | 5 |
| $&#46;customers&#91;4&#93;&#46;time&#95;seconds | number | 486&#46;0 |
| $&#46;customers&#91;4&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;5&#93; | object | object |
| $&#46;customers&#91;5&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;5&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;5&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;152163 |
| $&#46;customers&#91;5&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;009876 |
| $&#46;customers&#91;5&#93;&#46;distance&#95;meters | number | 16869&#46;0 |
| $&#46;customers&#91;5&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;5&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e008 |
| $&#46;customers&#91;5&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;5&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;5&#93;&#46;input&#95;address | string | 5001 Preston Dr, Midland, TX 79707 |
| $&#46;customers&#91;5&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;5&#93;&#46;name | string | Fictional Customer 06 |
| $&#46;customers&#91;5&#93;&#46;reference | string | DEMO&#45;06 |
| $&#46;customers&#91;5&#93;&#46;resolved&#95;address | string | 5001 Preston Drive, Midland, TX 79707, United States of America |
| $&#46;customers&#91;5&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;5&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;5&#93;&#46;row&#95;id | number | 6 |
| $&#46;customers&#91;5&#93;&#46;time&#95;seconds | number | 816&#46;0 |
| $&#46;customers&#91;5&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;6&#93; | object | object |
| $&#46;customers&#91;6&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;6&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;6&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;119297 |
| $&#46;customers&#91;6&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;029558 |
| $&#46;customers&#91;6&#93;&#46;distance&#95;meters | number | 9863&#46;0 |
| $&#46;customers&#91;6&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;6&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e009 |
| $&#46;customers&#91;6&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;6&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;6&#93;&#46;input&#95;address | string | 2800 Moss Ave, Midland, TX 79705 |
| $&#46;customers&#91;6&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;6&#93;&#46;name | string | Fictional Customer 07 |
| $&#46;customers&#91;6&#93;&#46;reference | string | DEMO&#45;07 |
| $&#46;customers&#91;6&#93;&#46;resolved&#95;address | string | 2800 Moss Avenue, Midland, TX 79705, United States of America |
| $&#46;customers&#91;6&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;6&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;6&#93;&#46;row&#95;id | number | 7 |
| $&#46;customers&#91;6&#93;&#46;time&#95;seconds | number | 607&#46;0 |
| $&#46;customers&#91;6&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;7&#93; | object | object |
| $&#46;customers&#91;7&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;7&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;7&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;07548065306122 |
| $&#46;customers&#91;7&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;988152836734695 |
| $&#46;customers&#91;7&#93;&#46;distance&#95;meters | number | 1776&#46;0 |
| $&#46;customers&#91;7&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;7&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e010 |
| $&#46;customers&#91;7&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;7&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;7&#93;&#46;input&#95;address | string | 201 W Dakota Ave, Midland, TX 79701 |
| $&#46;customers&#91;7&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;7&#93;&#46;name | string | Fictional Customer 08 |
| $&#46;customers&#91;7&#93;&#46;reference | string | DEMO&#45;08 |
| $&#46;customers&#91;7&#93;&#46;resolved&#95;address | string | 201 West Dakota Avenue, Midland Heights, Midland, TX 79701, United States of America |
| $&#46;customers&#91;7&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;7&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;7&#93;&#46;row&#95;id | number | 8 |
| $&#46;customers&#91;7&#93;&#46;time&#95;seconds | number | 156&#46;0 |
| $&#46;customers&#91;7&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;8&#93; | object | object |
| $&#46;customers&#91;8&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;8&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;8&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;163169 |
| $&#46;customers&#91;8&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;983509 |
| $&#46;customers&#91;8&#93;&#46;distance&#95;meters | number | 16274&#46;0 |
| $&#46;customers&#91;8&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;8&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e011 |
| $&#46;customers&#91;8&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;8&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;8&#93;&#46;input&#95;address | string | 6000 Riverfront Dr, Midland, TX 79706 |
| $&#46;customers&#91;8&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;8&#93;&#46;name | string | Fictional Customer 09 |
| $&#46;customers&#91;8&#93;&#46;reference | string | DEMO&#45;09 |
| $&#46;customers&#91;8&#93;&#46;resolved&#95;address | string | 6000 Riverfront Drive, Midland, TX 79706, United States of America |
| $&#46;customers&#91;8&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;8&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;8&#93;&#46;row&#95;id | number | 9 |
| $&#46;customers&#91;8&#93;&#46;time&#95;seconds | number | 887&#46;0 |
| $&#46;customers&#91;8&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;9&#93; | object | object |
| $&#46;customers&#91;9&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;9&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;9&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;10162 |
| $&#46;customers&#91;9&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;008075 |
| $&#46;customers&#91;9&#93;&#46;distance&#95;meters | number | 5246&#46;0 |
| $&#46;customers&#91;9&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;9&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e012 |
| $&#46;customers&#91;9&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;9&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;9&#93;&#46;input&#95;address | string | 1400 N N St, Midland, TX 79701 |
| $&#46;customers&#91;9&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;9&#93;&#46;name | string | Fictional Customer 10 |
| $&#46;customers&#91;9&#93;&#46;reference | string | DEMO&#45;10 |
| $&#46;customers&#91;9&#93;&#46;resolved&#95;address | string | 1400 North N Street, Midland, TX 79701, United States of America |
| $&#46;customers&#91;9&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;9&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;9&#93;&#46;row&#95;id | number | 10 |
| $&#46;customers&#91;9&#93;&#46;time&#95;seconds | number | 386&#46;0 |
| $&#46;customers&#91;9&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;10&#93; | object | object |
| $&#46;customers&#91;10&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;10&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;10&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;071072 |
| $&#46;customers&#91;10&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;980342 |
| $&#46;customers&#91;10&#93;&#46;distance&#95;meters | number | 3085&#46;0 |
| $&#46;customers&#91;10&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;10&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e013 |
| $&#46;customers&#91;10&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;10&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;10&#93;&#46;input&#95;address | string | 100 E Gist Ave, Midland, TX 79701 |
| $&#46;customers&#91;10&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;10&#93;&#46;name | string | Fictional Customer 11 |
| $&#46;customers&#91;10&#93;&#46;reference | string | DEMO&#45;11 |
| $&#46;customers&#91;10&#93;&#46;resolved&#95;address | string | 100 East Gist Avenue, Midland, TX 79701, United States of America |
| $&#46;customers&#91;10&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;10&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;10&#93;&#46;row&#95;id | number | 11 |
| $&#46;customers&#91;10&#93;&#46;time&#95;seconds | number | 247&#46;0 |
| $&#46;customers&#91;10&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;11&#93; | object | object |
| $&#46;customers&#91;11&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;11&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;11&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;214435 |
| $&#46;customers&#91;11&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;940028 |
| $&#46;customers&#91;11&#93;&#46;distance&#95;meters | number | 21635&#46;0 |
| $&#46;customers&#91;11&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;11&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e014 |
| $&#46;customers&#91;11&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;11&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;11&#93;&#46;input&#95;address | string | 9600 Wright Dr, Midland, TX 79706 |
| $&#46;customers&#91;11&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;11&#93;&#46;name | string | Fictional Customer 12 |
| $&#46;customers&#91;11&#93;&#46;reference | string | DEMO&#45;12 |
| $&#46;customers&#91;11&#93;&#46;resolved&#95;address | string | 9600 Wright Drive, Midland, TX 79706, United States of America |
| $&#46;customers&#91;11&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;11&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;11&#93;&#46;row&#95;id | number | 12 |
| $&#46;customers&#91;11&#93;&#46;time&#95;seconds | number | 1085&#46;0 |
| $&#46;customers&#91;11&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;12&#93; | object | object |
| $&#46;customers&#91;12&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;12&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;12&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;092478 |
| $&#46;customers&#91;12&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;993315 |
| $&#46;customers&#91;12&#93;&#46;distance&#95;meters | number | 2214&#46;0 |
| $&#46;customers&#91;12&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;12&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e015 |
| $&#46;customers&#91;12&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 5 |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;12&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;12&#93;&#46;input&#95;address | string | 1705 W Missouri Ave, Midland, TX 79701 |
| $&#46;customers&#91;12&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;12&#93;&#46;name | string | Fictional Customer 13 |
| $&#46;customers&#91;12&#93;&#46;reference | string | DEMO&#45;13 |
| $&#46;customers&#91;12&#93;&#46;resolved&#95;address | string | 1705 West Missouri Avenue, Midland, TX 79701, United States of America |
| $&#46;customers&#91;12&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;12&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;12&#93;&#46;row&#95;id | number | 13 |
| $&#46;customers&#91;12&#93;&#46;time&#95;seconds | number | 190&#46;0 |
| $&#46;customers&#91;12&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;13&#93; | object | object |
| $&#46;customers&#91;13&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;13&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;13&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;140165 |
| $&#46;customers&#91;13&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;022708 |
| $&#46;customers&#91;13&#93;&#46;distance&#95;meters | number | 12587&#46;0 |
| $&#46;customers&#91;13&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;13&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e016 |
| $&#46;customers&#91;13&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;13&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;13&#93;&#46;input&#95;address | string | 3800 Norwood St, Midland, TX 79707 |
| $&#46;customers&#91;13&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;13&#93;&#46;name | string | Fictional Customer 14 |
| $&#46;customers&#91;13&#93;&#46;reference | string | DEMO&#45;14 |
| $&#46;customers&#91;13&#93;&#46;resolved&#95;address | string | 3800 Norwood Street, Midland, TX 79707, United States of America |
| $&#46;customers&#91;13&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;13&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;13&#93;&#46;row&#95;id | number | 14 |
| $&#46;customers&#91;13&#93;&#46;time&#95;seconds | number | 665&#46;0 |
| $&#46;customers&#91;13&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;14&#93; | object | object |
| $&#46;customers&#91;14&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;14&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;14&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;061321 |
| $&#46;customers&#91;14&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;025087 |
| $&#46;customers&#91;14&#93;&#46;distance&#95;meters | number | 4792&#46;0 |
| $&#46;customers&#91;14&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;14&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e017 |
| $&#46;customers&#91;14&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;14&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;14&#93;&#46;input&#95;address | string | 1700 E Magnolia Ave, Midland, TX 79705 |
| $&#46;customers&#91;14&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;14&#93;&#46;name | string | Fictional Customer 15 |
| $&#46;customers&#91;14&#93;&#46;reference | string | DEMO&#45;15 |
| $&#46;customers&#91;14&#93;&#46;resolved&#95;address | string | 1700 East Magnolia Avenue, Midland, TX 79705, United States of America |
| $&#46;customers&#91;14&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;14&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;14&#93;&#46;row&#95;id | number | 15 |
| $&#46;customers&#91;14&#93;&#46;time&#95;seconds | number | 344&#46;0 |
| $&#46;customers&#91;14&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;15&#93; | object | object |
| $&#46;customers&#91;15&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;15&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;15&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;133052 |
| $&#46;customers&#91;15&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;01044 |
| $&#46;customers&#91;15&#93;&#46;distance&#95;meters | number | 6331&#46;0 |
| $&#46;customers&#91;15&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;15&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e018 |
| $&#46;customers&#91;15&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;15&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;15&#93;&#46;input&#95;address | string | 2601 Wedgewood St, Midland, TX 79707 |
| $&#46;customers&#91;15&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;15&#93;&#46;name | string | Fictional Customer 16 |
| $&#46;customers&#91;15&#93;&#46;reference | string | DEMO&#45;16 |
| $&#46;customers&#91;15&#93;&#46;resolved&#95;address | string | 2601 Wedgewood Street, Midland, TX 79707, United States of America |
| $&#46;customers&#91;15&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;15&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;15&#93;&#46;row&#95;id | number | 16 |
| $&#46;customers&#91;15&#93;&#46;time&#95;seconds | number | 509&#46;0 |
| $&#46;customers&#91;15&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;16&#93; | object | object |
| $&#46;customers&#91;16&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;16&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;16&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;108976 |
| $&#46;customers&#91;16&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;018071 |
| $&#46;customers&#91;16&#93;&#46;distance&#95;meters | number | 6881&#46;0 |
| $&#46;customers&#91;16&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;16&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e019 |
| $&#46;customers&#91;16&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;16&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;16&#93;&#46;input&#95;address | string | 2400 Fannin Ave, Midland, TX 79705 |
| $&#46;customers&#91;16&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;16&#93;&#46;name | string | Fictional Customer 17 |
| $&#46;customers&#91;16&#93;&#46;reference | string | DEMO&#45;17 |
| $&#46;customers&#91;16&#93;&#46;resolved&#95;address | string | 2400 Fannin Avenue, Midland, TX 79705, United States of America |
| $&#46;customers&#91;16&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;16&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;16&#93;&#46;row&#95;id | number | 17 |
| $&#46;customers&#91;16&#93;&#46;time&#95;seconds | number | 478&#46;0 |
| $&#46;customers&#91;16&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;17&#93; | object | object |
| $&#46;customers&#91;17&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;17&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;17&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;139277 |
| $&#46;customers&#91;17&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;975557 |
| $&#46;customers&#91;17&#93;&#46;distance&#95;meters | number | 13939&#46;0 |
| $&#46;customers&#91;17&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;17&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e020 |
| $&#46;customers&#91;17&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;17&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;17&#93;&#46;input&#95;address | string | 4800 Graceland Dr, Midland, TX 79703 |
| $&#46;customers&#91;17&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;17&#93;&#46;name | string | Fictional Customer 18 |
| $&#46;customers&#91;17&#93;&#46;reference | string | DEMO&#45;18 |
| $&#46;customers&#91;17&#93;&#46;resolved&#95;address | string | 4800 Graceland Drive, Midland, TX 79703, United States of America |
| $&#46;customers&#91;17&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;17&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;17&#93;&#46;row&#95;id | number | 18 |
| $&#46;customers&#91;17&#93;&#46;time&#95;seconds | number | 722&#46;0 |
| $&#46;customers&#91;17&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;18&#93; | object | object |
| $&#46;customers&#91;18&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;18&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;18&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;11804277580553 |
| $&#46;customers&#91;18&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;036252252035105 |
| $&#46;customers&#91;18&#93;&#46;distance&#95;meters | number | 10820&#46;0 |
| $&#46;customers&#91;18&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;18&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e021 |
| $&#46;customers&#91;18&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;18&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;18&#93;&#46;input&#95;address | string | 2503 W Loop 250 N, Midland, TX 79705 |
| $&#46;customers&#91;18&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;18&#93;&#46;name | string | Fictional Customer 19 |
| $&#46;customers&#91;18&#93;&#46;reference | string | DEMO&#45;19 |
| $&#46;customers&#91;18&#93;&#46;resolved&#95;address | string | 2503 West Loop 250 North, Midland, TX 79705, United States of America |
| $&#46;customers&#91;18&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;18&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;18&#93;&#46;row&#95;id | number | 19 |
| $&#46;customers&#91;18&#93;&#46;time&#95;seconds | number | 569&#46;0 |
| $&#46;customers&#91;18&#93;&#46;verdict | string | in&#95;zone |
| $&#46;customers&#91;19&#93; | object | object |
| $&#46;customers&#91;19&#93;&#46;borderline | boolean | false |
| $&#46;customers&#91;19&#93;&#46;coordinates | array | 2 entries |
| $&#46;customers&#91;19&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;07694 |
| $&#46;customers&#91;19&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;996331 |
| $&#46;customers&#91;19&#93;&#46;distance&#95;meters | number | 492&#46;0 |
| $&#46;customers&#91;19&#93;&#46;evidence&#95;refs | array | 2 entries |
| $&#46;customers&#91;19&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e022 |
| $&#46;customers&#91;19&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e023 |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;evidence | object | object |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;evidence&#46;candidate&#95;count | number | 1 |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;evidence&#46;confidence | number | 1 |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;evidence&#46;confidence&#95;building&#95;level | number | 1 |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;evidence&#46;match&#95;type | string | full&#95;match |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;evidence&#46;result&#95;type | string | building |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;reason | null | unavailable |
| $&#46;customers&#91;19&#93;&#46;geocode&#95;status | string | resolved |
| $&#46;customers&#91;19&#93;&#46;input&#95;address | string | 301 W Missouri Ave, Midland, TX 79701 |
| $&#46;customers&#91;19&#93;&#46;membership&#95;route&#95;disagreement | boolean | false |
| $&#46;customers&#91;19&#93;&#46;name | string | Fictional Customer 20 |
| $&#46;customers&#91;19&#93;&#46;reference | string | DEMO&#45;20 |
| $&#46;customers&#91;19&#93;&#46;resolved&#95;address | string | 301 West Missouri Avenue, Downtown Midland Management District, Midland, TX 79701, United States of America |
| $&#46;customers&#91;19&#93;&#46;route&#95;status | string | ok |
| $&#46;customers&#91;19&#93;&#46;route&#95;within&#95;budget | boolean | true |
| $&#46;customers&#91;19&#93;&#46;row&#95;id | number | 20 |
| $&#46;customers&#91;19&#93;&#46;time&#95;seconds | number | 59&#46;0 |
| $&#46;customers&#91;19&#93;&#46;verdict | string | in&#95;zone |
| $&#46;data&#95;mode | string | live |
| $&#46;errors | array | &#91;&#93; |
| $&#46;evidence | array | 24 entries |
| $&#46;evidence&#91;0&#93; | object | object |
| $&#46;evidence&#91;0&#93;&#46;artifact | string | evidence/e001&#46;json |
| $&#46;evidence&#91;0&#93;&#46;id | string | e001 |
| $&#46;evidence&#91;0&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;0&#93;&#46;operation | string | geocode&#95;business |
| $&#46;evidence&#91;0&#93;&#46;sha256 | string | e644ac3a0ba8255675dbdf4b29bd2fa56fc776d07a8bed1a8ed2d83718a93613 |
| $&#46;evidence&#91;1&#93; | object | object |
| $&#46;evidence&#91;1&#93;&#46;artifact | string | evidence/e002&#46;json |
| $&#46;evidence&#91;1&#93;&#46;id | string | e002 |
| $&#46;evidence&#91;1&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;1&#93;&#46;operation | string | isoline |
| $&#46;evidence&#91;1&#93;&#46;sha256 | string | 29a17d2ab0ffbe562082d23dcf27a18f33e03d2eee1d7e76ff2970bdb5a97b95 |
| $&#46;evidence&#91;2&#93; | object | object |
| $&#46;evidence&#91;2&#93;&#46;artifact | string | evidence/e003&#46;json |
| $&#46;evidence&#91;2&#93;&#46;id | string | e003 |
| $&#46;evidence&#91;2&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;2&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;2&#93;&#46;sha256 | string | faf7a7e83da4c669c715ad3cad4596370ef40856af672274649cde296ceed8cb |
| $&#46;evidence&#91;3&#93; | object | object |
| $&#46;evidence&#91;3&#93;&#46;artifact | string | evidence/e004&#46;json |
| $&#46;evidence&#91;3&#93;&#46;id | string | e004 |
| $&#46;evidence&#91;3&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;3&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;3&#93;&#46;sha256 | string | bca98f620ae0534fbe29b8ea800522c4da242eda35cb7e31ca9b26caacd1c78e |
| $&#46;evidence&#91;4&#93; | object | object |
| $&#46;evidence&#91;4&#93;&#46;artifact | string | evidence/e005&#46;json |
| $&#46;evidence&#91;4&#93;&#46;id | string | e005 |
| $&#46;evidence&#91;4&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;4&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;4&#93;&#46;sha256 | string | 90456d5246060ca64b6e03a3d6344c4219d71ccd782ddf9c26740c65a5b53c2b |
| $&#46;evidence&#91;5&#93; | object | object |
| $&#46;evidence&#91;5&#93;&#46;artifact | string | evidence/e006&#46;json |
| $&#46;evidence&#91;5&#93;&#46;id | string | e006 |
| $&#46;evidence&#91;5&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;5&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;5&#93;&#46;sha256 | string | b67fba8ab7a0a46f83796fe23cb3af40420be8f1827eb97febd03363fb3b3552 |
| $&#46;evidence&#91;6&#93; | object | object |
| $&#46;evidence&#91;6&#93;&#46;artifact | string | evidence/e007&#46;json |
| $&#46;evidence&#91;6&#93;&#46;id | string | e007 |
| $&#46;evidence&#91;6&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;6&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;6&#93;&#46;sha256 | string | bf52c3065cd042e406f5a809dd08aa55f9056c6a1eff789acbe10f53730759db |
| $&#46;evidence&#91;7&#93; | object | object |
| $&#46;evidence&#91;7&#93;&#46;artifact | string | evidence/e008&#46;json |
| $&#46;evidence&#91;7&#93;&#46;id | string | e008 |
| $&#46;evidence&#91;7&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;7&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;7&#93;&#46;sha256 | string | 039ea9e88358c2bed1ed7cb9a7e1a28c42d7812dc4bf790363ad6ef5a8b58bbe |
| $&#46;evidence&#91;8&#93; | object | object |
| $&#46;evidence&#91;8&#93;&#46;artifact | string | evidence/e009&#46;json |
| $&#46;evidence&#91;8&#93;&#46;id | string | e009 |
| $&#46;evidence&#91;8&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;8&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;8&#93;&#46;sha256 | string | 848379d22a2858782d240fed52cb52411baad5cea2e10ce19f1a9ac12e00ccfe |
| $&#46;evidence&#91;9&#93; | object | object |
| $&#46;evidence&#91;9&#93;&#46;artifact | string | evidence/e010&#46;json |
| $&#46;evidence&#91;9&#93;&#46;id | string | e010 |
| $&#46;evidence&#91;9&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;9&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;9&#93;&#46;sha256 | string | 7236b9ebed089b83a59de26d5462a5327c66449c6f4712740670756610d4ffa1 |
| $&#46;evidence&#91;10&#93; | object | object |
| $&#46;evidence&#91;10&#93;&#46;artifact | string | evidence/e011&#46;json |
| $&#46;evidence&#91;10&#93;&#46;id | string | e011 |
| $&#46;evidence&#91;10&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;10&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;10&#93;&#46;sha256 | string | a2b15edd04ac655ac3777d2ac1ca291a50a3ffaf14c5846ecc064c1c2b44f84e |
| $&#46;evidence&#91;11&#93; | object | object |
| $&#46;evidence&#91;11&#93;&#46;artifact | string | evidence/e012&#46;json |
| $&#46;evidence&#91;11&#93;&#46;id | string | e012 |
| $&#46;evidence&#91;11&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;11&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;11&#93;&#46;sha256 | string | 2ea3bbc54a40153c2e8698cb2880f96f5eb4ad3091cc96f42ce27dd943674c70 |
| $&#46;evidence&#91;12&#93; | object | object |
| $&#46;evidence&#91;12&#93;&#46;artifact | string | evidence/e013&#46;json |
| $&#46;evidence&#91;12&#93;&#46;id | string | e013 |
| $&#46;evidence&#91;12&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;12&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;12&#93;&#46;sha256 | string | 640e1c61819a7228c2bf32920b78d275e11cd713b72b698c4f4abe60e4914586 |
| $&#46;evidence&#91;13&#93; | object | object |
| $&#46;evidence&#91;13&#93;&#46;artifact | string | evidence/e014&#46;json |
| $&#46;evidence&#91;13&#93;&#46;id | string | e014 |
| $&#46;evidence&#91;13&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;13&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;13&#93;&#46;sha256 | string | 7a8ec7f2b031901a091f4722d592e8e8c30b95c3aa4ae940e22f86fc68bce9b2 |
| $&#46;evidence&#91;14&#93; | object | object |
| $&#46;evidence&#91;14&#93;&#46;artifact | string | evidence/e015&#46;json |
| $&#46;evidence&#91;14&#93;&#46;id | string | e015 |
| $&#46;evidence&#91;14&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;14&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;14&#93;&#46;sha256 | string | 9bdcdcfca0a85a55f744c906439ce7b48411b1af3e91dbf7b1d4898f616bd82e |
| $&#46;evidence&#91;15&#93; | object | object |
| $&#46;evidence&#91;15&#93;&#46;artifact | string | evidence/e016&#46;json |
| $&#46;evidence&#91;15&#93;&#46;id | string | e016 |
| $&#46;evidence&#91;15&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;15&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;15&#93;&#46;sha256 | string | 0f8a84dabd7abc44d9a8f5b27a077e3e36415b63316cf1efce3d105ab1903a50 |
| $&#46;evidence&#91;16&#93; | object | object |
| $&#46;evidence&#91;16&#93;&#46;artifact | string | evidence/e017&#46;json |
| $&#46;evidence&#91;16&#93;&#46;id | string | e017 |
| $&#46;evidence&#91;16&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;16&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;16&#93;&#46;sha256 | string | 7311dbbc592ff4d5757e6eb2dc0e2a54aa8d4242eeaea024263a372077803d37 |
| $&#46;evidence&#91;17&#93; | object | object |
| $&#46;evidence&#91;17&#93;&#46;artifact | string | evidence/e018&#46;json |
| $&#46;evidence&#91;17&#93;&#46;id | string | e018 |
| $&#46;evidence&#91;17&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;17&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;17&#93;&#46;sha256 | string | bcaf578e1180c2136616827c8777d3471fa3257aae6859ad081b21ac8d6f5582 |
| $&#46;evidence&#91;18&#93; | object | object |
| $&#46;evidence&#91;18&#93;&#46;artifact | string | evidence/e019&#46;json |
| $&#46;evidence&#91;18&#93;&#46;id | string | e019 |
| $&#46;evidence&#91;18&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;18&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;18&#93;&#46;sha256 | string | 8a70a83837d8369afe929b7388a1fb64542e317c37396525867ea6687e0d5db5 |
| $&#46;evidence&#91;19&#93; | object | object |
| $&#46;evidence&#91;19&#93;&#46;artifact | string | evidence/e020&#46;json |
| $&#46;evidence&#91;19&#93;&#46;id | string | e020 |
| $&#46;evidence&#91;19&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;19&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;19&#93;&#46;sha256 | string | fb01e21876cedf9e2e5be9c6bdfcaa17660919ad45836ad26e7a9ae4359f8937 |
| $&#46;evidence&#91;20&#93; | object | object |
| $&#46;evidence&#91;20&#93;&#46;artifact | string | evidence/e021&#46;json |
| $&#46;evidence&#91;20&#93;&#46;id | string | e021 |
| $&#46;evidence&#91;20&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;20&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;20&#93;&#46;sha256 | string | 61a41b2fe9156bc4453dd66caebeb38e9e71ee959ac915fe3219c4c525f106d5 |
| $&#46;evidence&#91;21&#93; | object | object |
| $&#46;evidence&#91;21&#93;&#46;artifact | string | evidence/e022&#46;json |
| $&#46;evidence&#91;21&#93;&#46;id | string | e022 |
| $&#46;evidence&#91;21&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;21&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;21&#93;&#46;sha256 | string | 09d9c58d35b4b2870cab063fde88738e8377621d114edea399ee7f8f2126acd0 |
| $&#46;evidence&#91;22&#93; | object | object |
| $&#46;evidence&#91;22&#93;&#46;artifact | string | evidence/e023&#46;json |
| $&#46;evidence&#91;22&#93;&#46;id | string | e023 |
| $&#46;evidence&#91;22&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;22&#93;&#46;operation | string | route&#95;matrix |
| $&#46;evidence&#91;22&#93;&#46;sha256 | string | ff1525e77f4380e58b5094b7805205811d6cd1d55a4b1e9d339401cdd3d78c33 |
| $&#46;evidence&#91;23&#93; | object | object |
| $&#46;evidence&#91;23&#93;&#46;artifact | string | evidence/e024&#46;json |
| $&#46;evidence&#91;23&#93;&#46;id | string | e024 |
| $&#46;evidence&#91;23&#93;&#46;kind | string | rest |
| $&#46;evidence&#91;23&#93;&#46;operation | string | places |
| $&#46;evidence&#91;23&#93;&#46;sha256 | string | a4135d82fe51394df8d34608e48499e1c91808cc93dd430cc4729af994193d86 |
| $&#46;path | string | cli |
| $&#46;run&#95;status | string | complete |
| $&#46;run&#95;timestamp&#95;utc | string | 2026&#45;10&#45;23T20&#58;09&#58;33Z |
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
| $&#46;summary&#46;borderline | number | 0 |
| $&#46;summary&#46;classified&#95;denominator | number | 20 |
| $&#46;summary&#46;disagreements | number | 0 |
| $&#46;summary&#46;in&#95;zone | number | 20 |
| $&#46;summary&#46;in&#95;zone&#95;percent | number | 100&#46;0 |
| $&#46;summary&#46;known&#95;routes | number | 20 |
| $&#46;summary&#46;max&#95;time&#95;row&#95;ids | array | 1 entries |
| $&#46;summary&#46;max&#95;time&#95;row&#95;ids&#91;0&#93; | number | 12 |
| $&#46;summary&#46;max&#95;time&#95;seconds | number | 1085&#46;0 |
| $&#46;summary&#46;median&#95;in&#95;zone&#95;seconds | number | 488&#46;0 |
| $&#46;summary&#46;missing&#95;routes | number | 0 |
| $&#46;summary&#46;out&#95;of&#95;zone | number | 0 |
| $&#46;summary&#46;out&#95;of&#95;zone&#95;percent | number | 0&#46;0 |
| $&#46;summary&#46;resolved | number | 20 |
| $&#46;summary&#46;total | number | 20 |
| $&#46;summary&#46;unknown&#95;membership | number | 0 |
| $&#46;summary&#46;unresolved | number | 0 |
| $&#46;warnings | array | 3 entries |
| $&#46;warnings&#91;0&#93; | string | Competitor coverage is sampled, at most 20 candidates and no pagination&#46; |
| $&#46;warnings&#91;1&#93; | string | The category service is broad; these candidates are not verified plumbing competitors&#46; |
| $&#46;warnings&#91;2&#93; | string | HTTP attempts&#58; 24; isoline polls&#58; 0; billed credits unavailable&#46; |
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
