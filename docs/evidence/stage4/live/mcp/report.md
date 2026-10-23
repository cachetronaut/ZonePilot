# ZonePilot report

## Run and method

| Field | Value |
| --- | --- |
| schema&#95;version | 1&#46;0 |
| path | mcp |
| data&#95;mode | live |
| run&#95;status | complete |
| run&#95;timestamp&#95;utc | 2026&#45;10&#45;23T19&#58;58&#58;09Z |
| zone.method | route&#95;time&#95;at&#95;points |
| zone.approximation | true |
| zone.parameters | &#123;&quot;budget&#95;seconds&quot;&#58; 1200&#125; |
| zone.limitations | &#91;&quot;Route&#45;time classification only at measured points; no continuous zone&#46;&quot;&#93; |

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
| observed&#95;in&#95;zone&#95;count | 20 |
| observed&#95;out&#95;of&#95;zone&#95;count | 0 |
| returned&#95;count | 20 |
| search&#95;extent | &#123;&quot;method&quot;&#58; &quot;circle&quot;, &quot;parameters&quot;&#58; &#123;&quot;center&quot;&#58; &#91;&#45;102&#46;075567, 31&#46;9997&#93;, &quot;radius&#95;meters&quot;&#58; 20000&#125;&#125; |
| status | ok |
| unclassified&#95;count | 0 |

| ID | Name | Address | Categories | Coordinates, lon/lat | Membership | Geodesic distance, metres |
| --- | --- | --- | --- | --- | --- | --- |
| 51098a62c5358559c0597d0cdbbb86004040f00102f90109ec1d18000000009203194d7920436f6d6d756e6974792043726564697420556e696f6e | My Community Credit Union | My Community Credit Union, 600 West Louisiana Avenue, Midland, TX 79701, United States of America | &#91;&quot;building&quot;, &quot;building&#46;commercial&quot;, &quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;0814069, 32&#46;0041118&#93; | in&#95;zone | 737&#46;504 |
| 51166a4df30e8559c059bd70491f5f014040f00103f9016ded12de0200000092031349726f6e20507265737320436c65616e657273 | Iron Press Cleaners | Iron Press Cleaners, 1309 North Big Spring Street, Midland, TX 79701, United States of America | &#91;&quot;commercial&quot;, &quot;service&quot;, &quot;service&#46;cleaning&quot;, &quot;service&#46;cleaning&#46;dry&#95;cleaning&quot;&#93; | &#91;&#45;102&#46;0790375, 32&#46;0107154&#93; | in&#95;zone | 1267&#46;82 |
| 511b5fd247dd8459c059f75a7dd069004040f00101f9018df55d000000000092032a4c6f7261696e652043656e746572202f204d69646c616e6420506f6c696365204465706172746d656e74 | Loraine Center / Midland Police Department | Loraine Center / Midland Police Department, 601 North Loraine Street, Midland, TX 79701, United States of America | &#91;&quot;building&quot;, &quot;building&#46;facility&quot;, &quot;service&quot;, &quot;service&#46;police&quot;&#93; | &#91;&#45;102&#46;0760059, 32&#46;0032292&#93; | in&#95;zone | 394&#46;606 |
| 511b71b7daf98459c05938c67d5072fe3f40f00103f9014f9e238702000000 | unavailable | South Big Spring Street, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;advertising&quot;, &quot;service&#46;advertising&#46;billboard&quot;&#93; | &#91;&#45;102&#46;07790468045857, 31&#46;993926663726327&#93; | in&#95;zone | 678&#46;762 |
| 511c339aa6198559c0596d5771aa6bff3f40f00103f90135c79ef6000000009203054368617365 | Chase | Chase, West Wall Street, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;0796906, 31&#46;9977366&#93; | in&#95;zone | 445&#46;951 |
| 513a9b4473d38459c0599baa4f8369fe3f40f00103f9018b6287f20000000092031f4d69646c616e6420436f756e747920446574656e74696f6e2043656e746572 | Midland County Detention Center | Midland County Detention Center, West Washington Avenue, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;police&quot;&#93; | &#91;&#45;102&#46;0754059, 31&#46;9937975&#93; | in&#95;zone | 656&#46;505 |
| 5143c879ff1f8559c059a60ccd2b43ff3f40f00103f9018f6b9cf40000000092030f50726f737065726974792042616e6b | Prosperity Bank | Prosperity Bank, West Wall Street, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;080078, 31&#46;9971187&#93; | in&#95;zone | 513&#46;168 |
| 516e3b7eb9e08459c059ea84ef5822004040f00103f9015f6b9cf40000000092030f42616e6b206f6620416d6572696361 | Bank of America | Bank of America, West Ohio Avenue, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;0762161, 32&#46;0010482&#93; | in&#95;zone | 161&#46;928 |
| 517174f0a7218559c0592983d15169ff3f40f00103f9017c01cbf10000000092030a46726f73742042616e6b | Frost Bank | Frost Bank, West Wall Street, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;0801792, 31&#46;9977008&#93; | in&#95;zone | 488&#46;449 |
| 51962a0769fc8459c0597f4db68196004040f00103f9016f599cf40000000092030442422654 | BB&amp;T | BB&amp;T, West Kansas Avenue, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;0779059, 32&#46;0045931&#93; | in&#95;zone | 587&#46;09 |
| 519800570d1d8559c059ca15f549a4ff3f40f00103f9011344ef6c0000000092030b57656c6c7320466172676f | Wells Fargo | Wells Fargo, West Texas Avenue, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;0798982, 31&#46;9986006&#93; | in&#95;zone | 426&#46;333 |
| 519f0bd92f0e8559c0595ab835e96cff3f40f00103f9018c6b9cf40000000092030a46726f73742042616e6b | Frost Bank | Frost Bank, North Marienfeld Street, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;0789909, 31&#46;9977556&#93; | in&#95;zone | 388&#46;579 |
| 51a210b7f9358559c059e9c97fedbbff3f40f00103f901916b9cf40000000092030b57656c6c7320466172676f | Wells Fargo | Wells Fargo, North Carrizo Street, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;0814194, 31&#46;9989613&#93; | in&#95;zone | 557&#46;957 |
| 51a3474211418459c059e6fd7c5b66fd3f40f00102f901b456eb17000000009203224d69646c616e642046697265204465706172746d656e742053746174696f6e202332 | Midland Fire Department Station &#35;2 | Midland Fire Department Station &#35;2, South Mineola Street, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;fire&#95;station&quot;&#93; | &#91;&#45;102&#46;0664714, 31&#46;9898431&#93; | in&#95;zone | 1391&#46;776 |
| 51ae6a1cb7b78459c05920f86e4e36ff3f40f00102f9013e6bc10d00000000920319556e697465642053746174657320506f7374204f6666696365 | United States Post Office | United States Post Office, 100 East Wall Street, Midland, TX 79701, United States of America | &#91;&quot;building&quot;, &quot;building&#46;facility&quot;, &quot;service&quot;, &quot;service&#46;post&quot;, &quot;service&#46;post&#46;office&quot;&#93; | &#91;&#45;102&#46;0737131, 31&#46;9969224&#93; | in&#95;zone | 354&#46;901 |
| 51bcfec984048559c059011c812e86ff3f40f00103f901737c9cf400000000920317436f6d6d756e697479204e6174696f6e616c2042616e6b | Community National Bank | Community National Bank, North Big Spring Street, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;0784008, 31&#46;9981412&#93; | in&#95;zone | 318&#46;518 |
| 51ce16105a0f8559c059fa4a83ec61004040f00103f901fb469cf40000000092030d53656375726974792042616e6b | Security Bank | Security Bank, West Michigan Avenue, Midland, TX 79703, United States of America | &#91;&quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;079062, 32&#46;0029884&#93; | in&#95;zone | 492&#46;259 |
| 51e3a7cc28f18459c059a60ccd2b43ff3f40f00103f901170def6c0000000092030f42616e6b206f6620416d6572696361 | Bank of America | Bank of America, 303 West Wall Street, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;0772192, 31&#46;9971187&#93; | in&#95;zone | 326&#46;588 |
| 51e6f0a4e0048559c059a1fa62a5eeff3f40f00103f90119a0a6a502000000920311436974792042616e6b204d69646c616e64 | City Bank Midland | City Bank Midland, 400 West Illinois Avenue, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;financial&quot;, &quot;service&#46;financial&#46;bank&quot;&#93; | &#91;&#45;102&#46;0784227, 31&#46;9997352&#93; | in&#95;zone | 269&#46;318 |
| 51fda36fd2348459c059781b3d2311004040f00103f901329f238702000000 | unavailable | East Front Street, Midland, TX 79701, United States of America | &#91;&quot;service&quot;, &quot;service&#46;advertising&quot;, &quot;service&#46;advertising&#46;billboard&quot;&#93; | &#91;&#45;102&#46;0656298029267, 32&#46;00034157158431&#93; | in&#95;zone | 939&#46;777 |

## Evidence

| Entry | Value |
| --- | --- |
| 0 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e001&#46;json&quot;, &quot;id&quot;&#58; &quot;e001&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;business&quot;, &quot;sha256&quot;&#58; &quot;acb085a9e0b5effee747f5d76e858da28722881b6b38c195f4cc13720679b76b&quot;&#125; |
| 1 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e002&#46;json&quot;, &quot;id&quot;&#58; &quot;e002&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;57a6da5f93d26eb4b987061a77d76b18064ef7df0a8041a7cfdb541c3053fe49&quot;&#125; |
| 2 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e003&#46;json&quot;, &quot;id&quot;&#58; &quot;e003&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;d564a8e56f8e9c3f477af2e798f3fef0c35337e057164a35332ed85173c99169&quot;&#125; |
| 3 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e004&#46;json&quot;, &quot;id&quot;&#58; &quot;e004&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;75f25ea802f952f292643fdf4c84688654112f289c588cbf2f595f61c37dacde&quot;&#125; |
| 4 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e005&#46;json&quot;, &quot;id&quot;&#58; &quot;e005&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;1c30173b96907a045d9d4e51bfc3026d10bdf6047c8c19e28196664e649cb92d&quot;&#125; |
| 5 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e006&#46;json&quot;, &quot;id&quot;&#58; &quot;e006&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;545bbe810385770e44db733e1bafc0f5425f57da8aeb064d89c3c4fc5754c8fd&quot;&#125; |
| 6 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e007&#46;json&quot;, &quot;id&quot;&#58; &quot;e007&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;e2f19950291ada02262e83569fc2f1435f7b2a860ea19979927db69381807235&quot;&#125; |
| 7 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e008&#46;json&quot;, &quot;id&quot;&#58; &quot;e008&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;460d4788e02db9d77604c8142835ed58859261e9ced86110b463e0758bc38a40&quot;&#125; |
| 8 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e009&#46;json&quot;, &quot;id&quot;&#58; &quot;e009&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;4afb4364677d78336b60ebc1c6a20b6ffb91cdc3b091437318b8da633002eef1&quot;&#125; |
| 9 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e010&#46;json&quot;, &quot;id&quot;&#58; &quot;e010&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;75e84ed92ebcabcd9fa3dc229589a0ed242acc43e3e18ce0e452daa7b96d97f3&quot;&#125; |
| 10 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e011&#46;json&quot;, &quot;id&quot;&#58; &quot;e011&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;6f845791a51f10c49a7c8ec0b0480c756f53db705516c43043ee2384cbfc2b01&quot;&#125; |
| 11 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e012&#46;json&quot;, &quot;id&quot;&#58; &quot;e012&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;f8552ac23ba88cfdf32b59661fc1d153a5d9049894100ea036ca0ef4a1520a9e&quot;&#125; |
| 12 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e013&#46;json&quot;, &quot;id&quot;&#58; &quot;e013&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;61ac5a7f3799cc97ab554639a08a4e0417ba41f0c13b3a9678d926fcb60eb063&quot;&#125; |
| 13 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e014&#46;json&quot;, &quot;id&quot;&#58; &quot;e014&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;46cff00e2fdf02bdc6c9c9c3ba7fd6b50fbc91fc101dc58a1fc0bc74bc3cca9d&quot;&#125; |
| 14 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e015&#46;json&quot;, &quot;id&quot;&#58; &quot;e015&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;bcf394a470742487cbafcb3ab231d161a25fd3dd768ac3717b129307fd353669&quot;&#125; |
| 15 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e016&#46;json&quot;, &quot;id&quot;&#58; &quot;e016&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;ed711523e31b1ca25226aafbabecbff1f7965e04678aa21ad8db44abf0aed81c&quot;&#125; |
| 16 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e017&#46;json&quot;, &quot;id&quot;&#58; &quot;e017&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;5a13748ba54a7bd9941f90ab692335d299cdb3dc5715eda5af1975b03112d5c7&quot;&#125; |
| 17 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e018&#46;json&quot;, &quot;id&quot;&#58; &quot;e018&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;385e927200e18c5dde9678bde956266df4b0a6f61c90b0802221e691ae8a037a&quot;&#125; |
| 18 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e019&#46;json&quot;, &quot;id&quot;&#58; &quot;e019&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;d894624dfaeca14c1549ae30403223d876bf7be528fabfea4709fc6ef524508f&quot;&#125; |
| 19 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e020&#46;json&quot;, &quot;id&quot;&#58; &quot;e020&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;396300acdc837f378a1a5b3bb815dfe3e9d29dd1367aab8e24b0cbbf1d96e99b&quot;&#125; |
| 20 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e021&#46;json&quot;, &quot;id&quot;&#58; &quot;e021&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;geocode&#95;customer&quot;, &quot;sha256&quot;&#58; &quot;130e910d9eaa5e6618f636ef7529c3599be83cf16ae8dbee10379a8fa3dea603&quot;&#125; |
| 21 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e022&#46;json&quot;, &quot;id&quot;&#58; &quot;e022&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;calculate&#95;route&#95;matrix&#95;customers&quot;, &quot;sha256&quot;&#58; &quot;c354e620f1f50889a60f623f21ee4234e903be06901c13a729a15f074340a08b&quot;&#125; |
| 22 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e023&#46;json&quot;, &quot;id&quot;&#58; &quot;e023&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;search&#95;places&quot;, &quot;sha256&quot;&#58; &quot;258f96a1b187b5b90a74cbf92f133374196f1d95ea501e738a1748a568e1639f&quot;&#125; |
| 23 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e024&#46;json&quot;, &quot;id&quot;&#58; &quot;e024&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;calculate&#95;route&#95;matrix&#95;competitors&quot;, &quot;sha256&quot;&#58; &quot;4e20d0235fbebb802d8c3c6c37d8220957c6de29e1a1bd04ca538d27befb05f5&quot;&#125; |
| 24 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e025&#46;json&quot;, &quot;id&quot;&#58; &quot;e025&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;mcp&#95;competitor&#95;classification&quot;, &quot;sha256&quot;&#58; &quot;91e4b5262f4602f3bb0bd001cde52412cbe51b882fd048858cafac6c296807d8&quot;&#125; |
| 25 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e026&#46;json&quot;, &quot;id&quot;&#58; &quot;e026&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;reverse&#95;geocode&#95;coordinates&quot;, &quot;sha256&quot;&#58; &quot;061bb864041a8e956f4cc5d248e4f0e0ebe4d6defc1e76f70743baeb11b56bbf&quot;&#125; |
| 26 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e027&#46;json&quot;, &quot;id&quot;&#58; &quot;e027&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;list&#95;place&#95;categories&quot;, &quot;sha256&quot;&#58; &quot;4445bf3616f6447811189c247f9d934dfa155e91a0986eea2b1553d6f83abadf&quot;&#125; |
| 27 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e028&#46;json&quot;, &quot;id&quot;&#58; &quot;e028&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;transform&#95;geometry&quot;, &quot;sha256&quot;&#58; &quot;82cc2327e5f4291cd472387f51f6f8cda2896e41c4d56f2d7a645c3d17a29ff0&quot;&#125; |
| 28 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e029&#46;json&quot;, &quot;id&quot;&#58; &quot;e029&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;evaluate&#95;spatial&#95;relation&quot;, &quot;sha256&quot;&#58; &quot;8b20bd04e672ecd488cfba5d195a638cbaad65f727b8c9603068d88db9034ab0&quot;&#125; |
| 29 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e030&#46;json&quot;, &quot;id&quot;&#58; &quot;e030&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;evaluate&#95;spatial&#95;relation&quot;, &quot;sha256&quot;&#58; &quot;cff90bd2859220a52d26b458843172e5d95b4b1ab794189203d0891c3a8452cc&quot;&#125; |
| 30 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e031&#46;json&quot;, &quot;id&quot;&#58; &quot;e031&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;measure&#95;geometry&quot;, &quot;sha256&quot;&#58; &quot;afb8267cbc65ae4b78acb12d5086d926e0fd1d30b827640aa1e8f60641580d69&quot;&#125; |
| 31 | &#123;&quot;artifact&quot;&#58; &quot;evidence/e032&#46;json&quot;, &quot;id&quot;&#58; &quot;e032&quot;, &quot;kind&quot;&#58; &quot;mcp&quot;, &quot;operation&quot;&#58; &quot;calculate&#95;route&quot;, &quot;sha256&quot;&#58; &quot;8a37a1b65c2a6e32d603daca5f6ba67195be0142843407920579c5903e9835f1&quot;&#125; |

## Errors

| Entry | Value |
| --- | --- |
| entries | [] |

## Warnings

| Entry | Value |
| --- | --- |
| 0 | Fictional business/customer identities at real public demo locations; no affiliation or actual customer relationship&#46; |
| 1 | Hosted acquisition spans captured sessions; final twenty&#45;target matrix supersedes the preliminary nineteen&#45;target matrix&#46; |
| 2 | Competitor coverage is sampled, at most 20 candidates and no pagination&#46; |
| 3 | The category service is broad; these candidates are not verified plumbing competitors&#46; |
| 4 | Claude projects hosted structured results as JSON text; normalization validates typed results and captured arguments&#46; |

## Attributions

| Entry | Value |
| --- | --- |
| 0 | &#123;&quot;source&quot;&#58; &quot;Geoapify&quot;, &quot;text&quot;&#58; &quot;Live hosted MCP location services&#46;&quot;, &quot;url&quot;&#58; &quot;https&#58;//geoapify&#46;com&quot;&#125; |
| 1 | &#123;&quot;source&quot;&#58; &quot;OpenStreetMap&quot;, &quot;text&quot;&#58; &quot;Live map data&#58; © OpenStreetMap contributors, ODbL&#46;&quot;, &quot;url&quot;&#58; &quot;https&#58;//www&#46;openstreetmap&#46;org/copyright&quot;&#125; |

## Complete field details

Every JSON field is listed independently. Null means unavailable.

| JSON path | Type | Value |
| --- | --- | --- |
| $ | object | object |
| $&#46;attributions | array | 2 entries |
| $&#46;attributions&#91;0&#93; | object | object |
| $&#46;attributions&#91;0&#93;&#46;source | string | Geoapify |
| $&#46;attributions&#91;0&#93;&#46;text | string | Live hosted MCP location services&#46; |
| $&#46;attributions&#91;0&#93;&#46;url | string | https&#58;//geoapify&#46;com |
| $&#46;attributions&#91;1&#93; | object | object |
| $&#46;attributions&#91;1&#93;&#46;source | string | OpenStreetMap |
| $&#46;attributions&#91;1&#93;&#46;text | string | Live map data&#58; © OpenStreetMap contributors, ODbL&#46; |
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
| $&#46;competitors&#46;observed&#95;in&#95;zone&#95;count | number | 20 |
| $&#46;competitors&#46;observed&#95;out&#95;of&#95;zone&#95;count | number | 0 |
| $&#46;competitors&#46;records | array | 20 entries |
| $&#46;competitors&#46;records&#91;0&#93; | object | object |
| $&#46;competitors&#46;records&#91;0&#93;&#46;address | string | My Community Credit Union, 600 West Louisiana Avenue, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories | array | 5 entries |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories&#91;1&#93; | string | building&#46;commercial |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories&#91;2&#93; | string | service |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories&#91;3&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;0&#93;&#46;categories&#91;4&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;0&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;0&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0814069 |
| $&#46;competitors&#46;records&#91;0&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;0041118 |
| $&#46;competitors&#46;records&#91;0&#93;&#46;geodesic&#95;distance&#95;meters | number | 737&#46;504 |
| $&#46;competitors&#46;records&#91;0&#93;&#46;id | string | 51098a62c5358559c0597d0cdbbb86004040f00102f90109ec1d18000000009203194d7920436f6d6d756e6974792043726564697420556e696f6e |
| $&#46;competitors&#46;records&#91;0&#93;&#46;name | string | My Community Credit Union |
| $&#46;competitors&#46;records&#91;0&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;1&#93; | object | object |
| $&#46;competitors&#46;records&#91;1&#93;&#46;address | string | Iron Press Cleaners, 1309 North Big Spring Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;1&#93;&#46;categories | array | 4 entries |
| $&#46;competitors&#46;records&#91;1&#93;&#46;categories&#91;0&#93; | string | commercial |
| $&#46;competitors&#46;records&#91;1&#93;&#46;categories&#91;1&#93; | string | service |
| $&#46;competitors&#46;records&#91;1&#93;&#46;categories&#91;2&#93; | string | service&#46;cleaning |
| $&#46;competitors&#46;records&#91;1&#93;&#46;categories&#91;3&#93; | string | service&#46;cleaning&#46;dry&#95;cleaning |
| $&#46;competitors&#46;records&#91;1&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;1&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0790375 |
| $&#46;competitors&#46;records&#91;1&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;0107154 |
| $&#46;competitors&#46;records&#91;1&#93;&#46;geodesic&#95;distance&#95;meters | number | 1267&#46;82 |
| $&#46;competitors&#46;records&#91;1&#93;&#46;id | string | 51166a4df30e8559c059bd70491f5f014040f00103f9016ded12de0200000092031349726f6e20507265737320436c65616e657273 |
| $&#46;competitors&#46;records&#91;1&#93;&#46;name | string | Iron Press Cleaners |
| $&#46;competitors&#46;records&#91;1&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;2&#93; | object | object |
| $&#46;competitors&#46;records&#91;2&#93;&#46;address | string | Loraine Center / Midland Police Department, 601 North Loraine Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;2&#93;&#46;categories | array | 4 entries |
| $&#46;competitors&#46;records&#91;2&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;2&#93;&#46;categories&#91;1&#93; | string | building&#46;facility |
| $&#46;competitors&#46;records&#91;2&#93;&#46;categories&#91;2&#93; | string | service |
| $&#46;competitors&#46;records&#91;2&#93;&#46;categories&#91;3&#93; | string | service&#46;police |
| $&#46;competitors&#46;records&#91;2&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;2&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0760059 |
| $&#46;competitors&#46;records&#91;2&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;0032292 |
| $&#46;competitors&#46;records&#91;2&#93;&#46;geodesic&#95;distance&#95;meters | number | 394&#46;606 |
| $&#46;competitors&#46;records&#91;2&#93;&#46;id | string | 511b5fd247dd8459c059f75a7dd069004040f00101f9018df55d000000000092032a4c6f7261696e652043656e746572202f204d69646c616e6420506f6c696365204465706172746d656e74 |
| $&#46;competitors&#46;records&#91;2&#93;&#46;name | string | Loraine Center / Midland Police Department |
| $&#46;competitors&#46;records&#91;2&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;3&#93; | object | object |
| $&#46;competitors&#46;records&#91;3&#93;&#46;address | string | South Big Spring Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;3&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;3&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;3&#93;&#46;categories&#91;1&#93; | string | service&#46;advertising |
| $&#46;competitors&#46;records&#91;3&#93;&#46;categories&#91;2&#93; | string | service&#46;advertising&#46;billboard |
| $&#46;competitors&#46;records&#91;3&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;3&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;07790468045857 |
| $&#46;competitors&#46;records&#91;3&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;993926663726327 |
| $&#46;competitors&#46;records&#91;3&#93;&#46;geodesic&#95;distance&#95;meters | number | 678&#46;762 |
| $&#46;competitors&#46;records&#91;3&#93;&#46;id | string | 511b71b7daf98459c05938c67d5072fe3f40f00103f9014f9e238702000000 |
| $&#46;competitors&#46;records&#91;3&#93;&#46;name | null | unavailable |
| $&#46;competitors&#46;records&#91;3&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;4&#93; | object | object |
| $&#46;competitors&#46;records&#91;4&#93;&#46;address | string | Chase, West Wall Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;4&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;4&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;4&#93;&#46;categories&#91;1&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;4&#93;&#46;categories&#91;2&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;4&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;4&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0796906 |
| $&#46;competitors&#46;records&#91;4&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;9977366 |
| $&#46;competitors&#46;records&#91;4&#93;&#46;geodesic&#95;distance&#95;meters | number | 445&#46;951 |
| $&#46;competitors&#46;records&#91;4&#93;&#46;id | string | 511c339aa6198559c0596d5771aa6bff3f40f00103f90135c79ef6000000009203054368617365 |
| $&#46;competitors&#46;records&#91;4&#93;&#46;name | string | Chase |
| $&#46;competitors&#46;records&#91;4&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;5&#93; | object | object |
| $&#46;competitors&#46;records&#91;5&#93;&#46;address | string | Midland County Detention Center, West Washington Avenue, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;5&#93;&#46;categories | array | 2 entries |
| $&#46;competitors&#46;records&#91;5&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;5&#93;&#46;categories&#91;1&#93; | string | service&#46;police |
| $&#46;competitors&#46;records&#91;5&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;5&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0754059 |
| $&#46;competitors&#46;records&#91;5&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;9937975 |
| $&#46;competitors&#46;records&#91;5&#93;&#46;geodesic&#95;distance&#95;meters | number | 656&#46;505 |
| $&#46;competitors&#46;records&#91;5&#93;&#46;id | string | 513a9b4473d38459c0599baa4f8369fe3f40f00103f9018b6287f20000000092031f4d69646c616e6420436f756e747920446574656e74696f6e2043656e746572 |
| $&#46;competitors&#46;records&#91;5&#93;&#46;name | string | Midland County Detention Center |
| $&#46;competitors&#46;records&#91;5&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;6&#93; | object | object |
| $&#46;competitors&#46;records&#91;6&#93;&#46;address | string | Prosperity Bank, West Wall Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;6&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;6&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;6&#93;&#46;categories&#91;1&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;6&#93;&#46;categories&#91;2&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;6&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;6&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;080078 |
| $&#46;competitors&#46;records&#91;6&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;9971187 |
| $&#46;competitors&#46;records&#91;6&#93;&#46;geodesic&#95;distance&#95;meters | number | 513&#46;168 |
| $&#46;competitors&#46;records&#91;6&#93;&#46;id | string | 5143c879ff1f8559c059a60ccd2b43ff3f40f00103f9018f6b9cf40000000092030f50726f737065726974792042616e6b |
| $&#46;competitors&#46;records&#91;6&#93;&#46;name | string | Prosperity Bank |
| $&#46;competitors&#46;records&#91;6&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;7&#93; | object | object |
| $&#46;competitors&#46;records&#91;7&#93;&#46;address | string | Bank of America, West Ohio Avenue, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;7&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;7&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;7&#93;&#46;categories&#91;1&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;7&#93;&#46;categories&#91;2&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;7&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;7&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0762161 |
| $&#46;competitors&#46;records&#91;7&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;0010482 |
| $&#46;competitors&#46;records&#91;7&#93;&#46;geodesic&#95;distance&#95;meters | number | 161&#46;928 |
| $&#46;competitors&#46;records&#91;7&#93;&#46;id | string | 516e3b7eb9e08459c059ea84ef5822004040f00103f9015f6b9cf40000000092030f42616e6b206f6620416d6572696361 |
| $&#46;competitors&#46;records&#91;7&#93;&#46;name | string | Bank of America |
| $&#46;competitors&#46;records&#91;7&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;8&#93; | object | object |
| $&#46;competitors&#46;records&#91;8&#93;&#46;address | string | Frost Bank, West Wall Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;8&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;8&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;8&#93;&#46;categories&#91;1&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;8&#93;&#46;categories&#91;2&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;8&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;8&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0801792 |
| $&#46;competitors&#46;records&#91;8&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;9977008 |
| $&#46;competitors&#46;records&#91;8&#93;&#46;geodesic&#95;distance&#95;meters | number | 488&#46;449 |
| $&#46;competitors&#46;records&#91;8&#93;&#46;id | string | 517174f0a7218559c0592983d15169ff3f40f00103f9017c01cbf10000000092030a46726f73742042616e6b |
| $&#46;competitors&#46;records&#91;8&#93;&#46;name | string | Frost Bank |
| $&#46;competitors&#46;records&#91;8&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;9&#93; | object | object |
| $&#46;competitors&#46;records&#91;9&#93;&#46;address | string | BB&amp;T, West Kansas Avenue, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;9&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;9&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;9&#93;&#46;categories&#91;1&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;9&#93;&#46;categories&#91;2&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;9&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;9&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0779059 |
| $&#46;competitors&#46;records&#91;9&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;0045931 |
| $&#46;competitors&#46;records&#91;9&#93;&#46;geodesic&#95;distance&#95;meters | number | 587&#46;09 |
| $&#46;competitors&#46;records&#91;9&#93;&#46;id | string | 51962a0769fc8459c0597f4db68196004040f00103f9016f599cf40000000092030442422654 |
| $&#46;competitors&#46;records&#91;9&#93;&#46;name | string | BB&amp;T |
| $&#46;competitors&#46;records&#91;9&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;10&#93; | object | object |
| $&#46;competitors&#46;records&#91;10&#93;&#46;address | string | Wells Fargo, West Texas Avenue, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;10&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;10&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;10&#93;&#46;categories&#91;1&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;10&#93;&#46;categories&#91;2&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;10&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;10&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0798982 |
| $&#46;competitors&#46;records&#91;10&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;9986006 |
| $&#46;competitors&#46;records&#91;10&#93;&#46;geodesic&#95;distance&#95;meters | number | 426&#46;333 |
| $&#46;competitors&#46;records&#91;10&#93;&#46;id | string | 519800570d1d8559c059ca15f549a4ff3f40f00103f9011344ef6c0000000092030b57656c6c7320466172676f |
| $&#46;competitors&#46;records&#91;10&#93;&#46;name | string | Wells Fargo |
| $&#46;competitors&#46;records&#91;10&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;11&#93; | object | object |
| $&#46;competitors&#46;records&#91;11&#93;&#46;address | string | Frost Bank, North Marienfeld Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;11&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;11&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;11&#93;&#46;categories&#91;1&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;11&#93;&#46;categories&#91;2&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;11&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;11&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0789909 |
| $&#46;competitors&#46;records&#91;11&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;9977556 |
| $&#46;competitors&#46;records&#91;11&#93;&#46;geodesic&#95;distance&#95;meters | number | 388&#46;579 |
| $&#46;competitors&#46;records&#91;11&#93;&#46;id | string | 519f0bd92f0e8559c0595ab835e96cff3f40f00103f9018c6b9cf40000000092030a46726f73742042616e6b |
| $&#46;competitors&#46;records&#91;11&#93;&#46;name | string | Frost Bank |
| $&#46;competitors&#46;records&#91;11&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;12&#93; | object | object |
| $&#46;competitors&#46;records&#91;12&#93;&#46;address | string | Wells Fargo, North Carrizo Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;12&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;12&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;12&#93;&#46;categories&#91;1&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;12&#93;&#46;categories&#91;2&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;12&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;12&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0814194 |
| $&#46;competitors&#46;records&#91;12&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;9989613 |
| $&#46;competitors&#46;records&#91;12&#93;&#46;geodesic&#95;distance&#95;meters | number | 557&#46;957 |
| $&#46;competitors&#46;records&#91;12&#93;&#46;id | string | 51a210b7f9358559c059e9c97fedbbff3f40f00103f901916b9cf40000000092030b57656c6c7320466172676f |
| $&#46;competitors&#46;records&#91;12&#93;&#46;name | string | Wells Fargo |
| $&#46;competitors&#46;records&#91;12&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;13&#93; | object | object |
| $&#46;competitors&#46;records&#91;13&#93;&#46;address | string | Midland Fire Department Station &#35;2, South Mineola Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;13&#93;&#46;categories | array | 2 entries |
| $&#46;competitors&#46;records&#91;13&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;13&#93;&#46;categories&#91;1&#93; | string | service&#46;fire&#95;station |
| $&#46;competitors&#46;records&#91;13&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;13&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0664714 |
| $&#46;competitors&#46;records&#91;13&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;9898431 |
| $&#46;competitors&#46;records&#91;13&#93;&#46;geodesic&#95;distance&#95;meters | number | 1391&#46;776 |
| $&#46;competitors&#46;records&#91;13&#93;&#46;id | string | 51a3474211418459c059e6fd7c5b66fd3f40f00102f901b456eb17000000009203224d69646c616e642046697265204465706172746d656e742053746174696f6e202332 |
| $&#46;competitors&#46;records&#91;13&#93;&#46;name | string | Midland Fire Department Station &#35;2 |
| $&#46;competitors&#46;records&#91;13&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;14&#93; | object | object |
| $&#46;competitors&#46;records&#91;14&#93;&#46;address | string | United States Post Office, 100 East Wall Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;14&#93;&#46;categories | array | 5 entries |
| $&#46;competitors&#46;records&#91;14&#93;&#46;categories&#91;0&#93; | string | building |
| $&#46;competitors&#46;records&#91;14&#93;&#46;categories&#91;1&#93; | string | building&#46;facility |
| $&#46;competitors&#46;records&#91;14&#93;&#46;categories&#91;2&#93; | string | service |
| $&#46;competitors&#46;records&#91;14&#93;&#46;categories&#91;3&#93; | string | service&#46;post |
| $&#46;competitors&#46;records&#91;14&#93;&#46;categories&#91;4&#93; | string | service&#46;post&#46;office |
| $&#46;competitors&#46;records&#91;14&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;14&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0737131 |
| $&#46;competitors&#46;records&#91;14&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;9969224 |
| $&#46;competitors&#46;records&#91;14&#93;&#46;geodesic&#95;distance&#95;meters | number | 354&#46;901 |
| $&#46;competitors&#46;records&#91;14&#93;&#46;id | string | 51ae6a1cb7b78459c05920f86e4e36ff3f40f00102f9013e6bc10d00000000920319556e697465642053746174657320506f7374204f6666696365 |
| $&#46;competitors&#46;records&#91;14&#93;&#46;name | string | United States Post Office |
| $&#46;competitors&#46;records&#91;14&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;15&#93; | object | object |
| $&#46;competitors&#46;records&#91;15&#93;&#46;address | string | Community National Bank, North Big Spring Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;15&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;15&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;15&#93;&#46;categories&#91;1&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;15&#93;&#46;categories&#91;2&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;15&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;15&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0784008 |
| $&#46;competitors&#46;records&#91;15&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;9981412 |
| $&#46;competitors&#46;records&#91;15&#93;&#46;geodesic&#95;distance&#95;meters | number | 318&#46;518 |
| $&#46;competitors&#46;records&#91;15&#93;&#46;id | string | 51bcfec984048559c059011c812e86ff3f40f00103f901737c9cf400000000920317436f6d6d756e697479204e6174696f6e616c2042616e6b |
| $&#46;competitors&#46;records&#91;15&#93;&#46;name | string | Community National Bank |
| $&#46;competitors&#46;records&#91;15&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;16&#93; | object | object |
| $&#46;competitors&#46;records&#91;16&#93;&#46;address | string | Security Bank, West Michigan Avenue, Midland, TX 79703, United States of America |
| $&#46;competitors&#46;records&#91;16&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;16&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;16&#93;&#46;categories&#91;1&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;16&#93;&#46;categories&#91;2&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;16&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;16&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;079062 |
| $&#46;competitors&#46;records&#91;16&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;0029884 |
| $&#46;competitors&#46;records&#91;16&#93;&#46;geodesic&#95;distance&#95;meters | number | 492&#46;259 |
| $&#46;competitors&#46;records&#91;16&#93;&#46;id | string | 51ce16105a0f8559c059fa4a83ec61004040f00103f901fb469cf40000000092030d53656375726974792042616e6b |
| $&#46;competitors&#46;records&#91;16&#93;&#46;name | string | Security Bank |
| $&#46;competitors&#46;records&#91;16&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;17&#93; | object | object |
| $&#46;competitors&#46;records&#91;17&#93;&#46;address | string | Bank of America, 303 West Wall Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;17&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;17&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;17&#93;&#46;categories&#91;1&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;17&#93;&#46;categories&#91;2&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;17&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;17&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0772192 |
| $&#46;competitors&#46;records&#91;17&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;9971187 |
| $&#46;competitors&#46;records&#91;17&#93;&#46;geodesic&#95;distance&#95;meters | number | 326&#46;588 |
| $&#46;competitors&#46;records&#91;17&#93;&#46;id | string | 51e3a7cc28f18459c059a60ccd2b43ff3f40f00103f901170def6c0000000092030f42616e6b206f6620416d6572696361 |
| $&#46;competitors&#46;records&#91;17&#93;&#46;name | string | Bank of America |
| $&#46;competitors&#46;records&#91;17&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;18&#93; | object | object |
| $&#46;competitors&#46;records&#91;18&#93;&#46;address | string | City Bank Midland, 400 West Illinois Avenue, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;18&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;18&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;18&#93;&#46;categories&#91;1&#93; | string | service&#46;financial |
| $&#46;competitors&#46;records&#91;18&#93;&#46;categories&#91;2&#93; | string | service&#46;financial&#46;bank |
| $&#46;competitors&#46;records&#91;18&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;18&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0784227 |
| $&#46;competitors&#46;records&#91;18&#93;&#46;coordinates&#91;1&#93; | number | 31&#46;9997352 |
| $&#46;competitors&#46;records&#91;18&#93;&#46;geodesic&#95;distance&#95;meters | number | 269&#46;318 |
| $&#46;competitors&#46;records&#91;18&#93;&#46;id | string | 51e6f0a4e0048559c059a1fa62a5eeff3f40f00103f90119a0a6a502000000920311436974792042616e6b204d69646c616e64 |
| $&#46;competitors&#46;records&#91;18&#93;&#46;name | string | City Bank Midland |
| $&#46;competitors&#46;records&#91;18&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;records&#91;19&#93; | object | object |
| $&#46;competitors&#46;records&#91;19&#93;&#46;address | string | East Front Street, Midland, TX 79701, United States of America |
| $&#46;competitors&#46;records&#91;19&#93;&#46;categories | array | 3 entries |
| $&#46;competitors&#46;records&#91;19&#93;&#46;categories&#91;0&#93; | string | service |
| $&#46;competitors&#46;records&#91;19&#93;&#46;categories&#91;1&#93; | string | service&#46;advertising |
| $&#46;competitors&#46;records&#91;19&#93;&#46;categories&#91;2&#93; | string | service&#46;advertising&#46;billboard |
| $&#46;competitors&#46;records&#91;19&#93;&#46;coordinates | array | 2 entries |
| $&#46;competitors&#46;records&#91;19&#93;&#46;coordinates&#91;0&#93; | number | &#45;102&#46;0656298029267 |
| $&#46;competitors&#46;records&#91;19&#93;&#46;coordinates&#91;1&#93; | number | 32&#46;00034157158431 |
| $&#46;competitors&#46;records&#91;19&#93;&#46;geodesic&#95;distance&#95;meters | number | 939&#46;777 |
| $&#46;competitors&#46;records&#91;19&#93;&#46;id | string | 51fda36fd2348459c059781b3d2311004040f00103f901329f238702000000 |
| $&#46;competitors&#46;records&#91;19&#93;&#46;name | null | unavailable |
| $&#46;competitors&#46;records&#91;19&#93;&#46;verdict | string | in&#95;zone |
| $&#46;competitors&#46;returned&#95;count | number | 20 |
| $&#46;competitors&#46;search&#95;extent | object | object |
| $&#46;competitors&#46;search&#95;extent&#46;method | string | circle |
| $&#46;competitors&#46;search&#95;extent&#46;parameters | object | object |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;center | array | 2 entries |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;center&#91;0&#93; | number | &#45;102&#46;075567 |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;center&#91;1&#93; | number | 31&#46;9997 |
| $&#46;competitors&#46;search&#95;extent&#46;parameters&#46;radius&#95;meters | number | 20000 |
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
| $&#46;customers&#91;0&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e002 |
| $&#46;customers&#91;0&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;1&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e003 |
| $&#46;customers&#91;1&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;2&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e004 |
| $&#46;customers&#91;2&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;3&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e005 |
| $&#46;customers&#91;3&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;4&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e006 |
| $&#46;customers&#91;4&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;5&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e007 |
| $&#46;customers&#91;5&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;6&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e008 |
| $&#46;customers&#91;6&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;7&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e009 |
| $&#46;customers&#91;7&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;8&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e010 |
| $&#46;customers&#91;8&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;9&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e011 |
| $&#46;customers&#91;9&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;10&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e012 |
| $&#46;customers&#91;10&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;11&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e013 |
| $&#46;customers&#91;11&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;12&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e014 |
| $&#46;customers&#91;12&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;13&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e015 |
| $&#46;customers&#91;13&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;14&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e016 |
| $&#46;customers&#91;14&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;15&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e017 |
| $&#46;customers&#91;15&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;16&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e018 |
| $&#46;customers&#91;16&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;17&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e019 |
| $&#46;customers&#91;17&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;18&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e020 |
| $&#46;customers&#91;18&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;customers&#91;19&#93;&#46;evidence&#95;refs&#91;0&#93; | string | e021 |
| $&#46;customers&#91;19&#93;&#46;evidence&#95;refs&#91;1&#93; | string | e022 |
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
| $&#46;evidence | array | 32 entries |
| $&#46;evidence&#91;0&#93; | object | object |
| $&#46;evidence&#91;0&#93;&#46;artifact | string | evidence/e001&#46;json |
| $&#46;evidence&#91;0&#93;&#46;id | string | e001 |
| $&#46;evidence&#91;0&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;0&#93;&#46;operation | string | geocode&#95;business |
| $&#46;evidence&#91;0&#93;&#46;sha256 | string | acb085a9e0b5effee747f5d76e858da28722881b6b38c195f4cc13720679b76b |
| $&#46;evidence&#91;1&#93; | object | object |
| $&#46;evidence&#91;1&#93;&#46;artifact | string | evidence/e002&#46;json |
| $&#46;evidence&#91;1&#93;&#46;id | string | e002 |
| $&#46;evidence&#91;1&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;1&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;1&#93;&#46;sha256 | string | 57a6da5f93d26eb4b987061a77d76b18064ef7df0a8041a7cfdb541c3053fe49 |
| $&#46;evidence&#91;2&#93; | object | object |
| $&#46;evidence&#91;2&#93;&#46;artifact | string | evidence/e003&#46;json |
| $&#46;evidence&#91;2&#93;&#46;id | string | e003 |
| $&#46;evidence&#91;2&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;2&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;2&#93;&#46;sha256 | string | d564a8e56f8e9c3f477af2e798f3fef0c35337e057164a35332ed85173c99169 |
| $&#46;evidence&#91;3&#93; | object | object |
| $&#46;evidence&#91;3&#93;&#46;artifact | string | evidence/e004&#46;json |
| $&#46;evidence&#91;3&#93;&#46;id | string | e004 |
| $&#46;evidence&#91;3&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;3&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;3&#93;&#46;sha256 | string | 75f25ea802f952f292643fdf4c84688654112f289c588cbf2f595f61c37dacde |
| $&#46;evidence&#91;4&#93; | object | object |
| $&#46;evidence&#91;4&#93;&#46;artifact | string | evidence/e005&#46;json |
| $&#46;evidence&#91;4&#93;&#46;id | string | e005 |
| $&#46;evidence&#91;4&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;4&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;4&#93;&#46;sha256 | string | 1c30173b96907a045d9d4e51bfc3026d10bdf6047c8c19e28196664e649cb92d |
| $&#46;evidence&#91;5&#93; | object | object |
| $&#46;evidence&#91;5&#93;&#46;artifact | string | evidence/e006&#46;json |
| $&#46;evidence&#91;5&#93;&#46;id | string | e006 |
| $&#46;evidence&#91;5&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;5&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;5&#93;&#46;sha256 | string | 545bbe810385770e44db733e1bafc0f5425f57da8aeb064d89c3c4fc5754c8fd |
| $&#46;evidence&#91;6&#93; | object | object |
| $&#46;evidence&#91;6&#93;&#46;artifact | string | evidence/e007&#46;json |
| $&#46;evidence&#91;6&#93;&#46;id | string | e007 |
| $&#46;evidence&#91;6&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;6&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;6&#93;&#46;sha256 | string | e2f19950291ada02262e83569fc2f1435f7b2a860ea19979927db69381807235 |
| $&#46;evidence&#91;7&#93; | object | object |
| $&#46;evidence&#91;7&#93;&#46;artifact | string | evidence/e008&#46;json |
| $&#46;evidence&#91;7&#93;&#46;id | string | e008 |
| $&#46;evidence&#91;7&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;7&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;7&#93;&#46;sha256 | string | 460d4788e02db9d77604c8142835ed58859261e9ced86110b463e0758bc38a40 |
| $&#46;evidence&#91;8&#93; | object | object |
| $&#46;evidence&#91;8&#93;&#46;artifact | string | evidence/e009&#46;json |
| $&#46;evidence&#91;8&#93;&#46;id | string | e009 |
| $&#46;evidence&#91;8&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;8&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;8&#93;&#46;sha256 | string | 4afb4364677d78336b60ebc1c6a20b6ffb91cdc3b091437318b8da633002eef1 |
| $&#46;evidence&#91;9&#93; | object | object |
| $&#46;evidence&#91;9&#93;&#46;artifact | string | evidence/e010&#46;json |
| $&#46;evidence&#91;9&#93;&#46;id | string | e010 |
| $&#46;evidence&#91;9&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;9&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;9&#93;&#46;sha256 | string | 75e84ed92ebcabcd9fa3dc229589a0ed242acc43e3e18ce0e452daa7b96d97f3 |
| $&#46;evidence&#91;10&#93; | object | object |
| $&#46;evidence&#91;10&#93;&#46;artifact | string | evidence/e011&#46;json |
| $&#46;evidence&#91;10&#93;&#46;id | string | e011 |
| $&#46;evidence&#91;10&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;10&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;10&#93;&#46;sha256 | string | 6f845791a51f10c49a7c8ec0b0480c756f53db705516c43043ee2384cbfc2b01 |
| $&#46;evidence&#91;11&#93; | object | object |
| $&#46;evidence&#91;11&#93;&#46;artifact | string | evidence/e012&#46;json |
| $&#46;evidence&#91;11&#93;&#46;id | string | e012 |
| $&#46;evidence&#91;11&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;11&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;11&#93;&#46;sha256 | string | f8552ac23ba88cfdf32b59661fc1d153a5d9049894100ea036ca0ef4a1520a9e |
| $&#46;evidence&#91;12&#93; | object | object |
| $&#46;evidence&#91;12&#93;&#46;artifact | string | evidence/e013&#46;json |
| $&#46;evidence&#91;12&#93;&#46;id | string | e013 |
| $&#46;evidence&#91;12&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;12&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;12&#93;&#46;sha256 | string | 61ac5a7f3799cc97ab554639a08a4e0417ba41f0c13b3a9678d926fcb60eb063 |
| $&#46;evidence&#91;13&#93; | object | object |
| $&#46;evidence&#91;13&#93;&#46;artifact | string | evidence/e014&#46;json |
| $&#46;evidence&#91;13&#93;&#46;id | string | e014 |
| $&#46;evidence&#91;13&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;13&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;13&#93;&#46;sha256 | string | 46cff00e2fdf02bdc6c9c9c3ba7fd6b50fbc91fc101dc58a1fc0bc74bc3cca9d |
| $&#46;evidence&#91;14&#93; | object | object |
| $&#46;evidence&#91;14&#93;&#46;artifact | string | evidence/e015&#46;json |
| $&#46;evidence&#91;14&#93;&#46;id | string | e015 |
| $&#46;evidence&#91;14&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;14&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;14&#93;&#46;sha256 | string | bcf394a470742487cbafcb3ab231d161a25fd3dd768ac3717b129307fd353669 |
| $&#46;evidence&#91;15&#93; | object | object |
| $&#46;evidence&#91;15&#93;&#46;artifact | string | evidence/e016&#46;json |
| $&#46;evidence&#91;15&#93;&#46;id | string | e016 |
| $&#46;evidence&#91;15&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;15&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;15&#93;&#46;sha256 | string | ed711523e31b1ca25226aafbabecbff1f7965e04678aa21ad8db44abf0aed81c |
| $&#46;evidence&#91;16&#93; | object | object |
| $&#46;evidence&#91;16&#93;&#46;artifact | string | evidence/e017&#46;json |
| $&#46;evidence&#91;16&#93;&#46;id | string | e017 |
| $&#46;evidence&#91;16&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;16&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;16&#93;&#46;sha256 | string | 5a13748ba54a7bd9941f90ab692335d299cdb3dc5715eda5af1975b03112d5c7 |
| $&#46;evidence&#91;17&#93; | object | object |
| $&#46;evidence&#91;17&#93;&#46;artifact | string | evidence/e018&#46;json |
| $&#46;evidence&#91;17&#93;&#46;id | string | e018 |
| $&#46;evidence&#91;17&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;17&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;17&#93;&#46;sha256 | string | 385e927200e18c5dde9678bde956266df4b0a6f61c90b0802221e691ae8a037a |
| $&#46;evidence&#91;18&#93; | object | object |
| $&#46;evidence&#91;18&#93;&#46;artifact | string | evidence/e019&#46;json |
| $&#46;evidence&#91;18&#93;&#46;id | string | e019 |
| $&#46;evidence&#91;18&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;18&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;18&#93;&#46;sha256 | string | d894624dfaeca14c1549ae30403223d876bf7be528fabfea4709fc6ef524508f |
| $&#46;evidence&#91;19&#93; | object | object |
| $&#46;evidence&#91;19&#93;&#46;artifact | string | evidence/e020&#46;json |
| $&#46;evidence&#91;19&#93;&#46;id | string | e020 |
| $&#46;evidence&#91;19&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;19&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;19&#93;&#46;sha256 | string | 396300acdc837f378a1a5b3bb815dfe3e9d29dd1367aab8e24b0cbbf1d96e99b |
| $&#46;evidence&#91;20&#93; | object | object |
| $&#46;evidence&#91;20&#93;&#46;artifact | string | evidence/e021&#46;json |
| $&#46;evidence&#91;20&#93;&#46;id | string | e021 |
| $&#46;evidence&#91;20&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;20&#93;&#46;operation | string | geocode&#95;customer |
| $&#46;evidence&#91;20&#93;&#46;sha256 | string | 130e910d9eaa5e6618f636ef7529c3599be83cf16ae8dbee10379a8fa3dea603 |
| $&#46;evidence&#91;21&#93; | object | object |
| $&#46;evidence&#91;21&#93;&#46;artifact | string | evidence/e022&#46;json |
| $&#46;evidence&#91;21&#93;&#46;id | string | e022 |
| $&#46;evidence&#91;21&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;21&#93;&#46;operation | string | calculate&#95;route&#95;matrix&#95;customers |
| $&#46;evidence&#91;21&#93;&#46;sha256 | string | c354e620f1f50889a60f623f21ee4234e903be06901c13a729a15f074340a08b |
| $&#46;evidence&#91;22&#93; | object | object |
| $&#46;evidence&#91;22&#93;&#46;artifact | string | evidence/e023&#46;json |
| $&#46;evidence&#91;22&#93;&#46;id | string | e023 |
| $&#46;evidence&#91;22&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;22&#93;&#46;operation | string | search&#95;places |
| $&#46;evidence&#91;22&#93;&#46;sha256 | string | 258f96a1b187b5b90a74cbf92f133374196f1d95ea501e738a1748a568e1639f |
| $&#46;evidence&#91;23&#93; | object | object |
| $&#46;evidence&#91;23&#93;&#46;artifact | string | evidence/e024&#46;json |
| $&#46;evidence&#91;23&#93;&#46;id | string | e024 |
| $&#46;evidence&#91;23&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;23&#93;&#46;operation | string | calculate&#95;route&#95;matrix&#95;competitors |
| $&#46;evidence&#91;23&#93;&#46;sha256 | string | 4e20d0235fbebb802d8c3c6c37d8220957c6de29e1a1bd04ca538d27befb05f5 |
| $&#46;evidence&#91;24&#93; | object | object |
| $&#46;evidence&#91;24&#93;&#46;artifact | string | evidence/e025&#46;json |
| $&#46;evidence&#91;24&#93;&#46;id | string | e025 |
| $&#46;evidence&#91;24&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;24&#93;&#46;operation | string | mcp&#95;competitor&#95;classification |
| $&#46;evidence&#91;24&#93;&#46;sha256 | string | 91e4b5262f4602f3bb0bd001cde52412cbe51b882fd048858cafac6c296807d8 |
| $&#46;evidence&#91;25&#93; | object | object |
| $&#46;evidence&#91;25&#93;&#46;artifact | string | evidence/e026&#46;json |
| $&#46;evidence&#91;25&#93;&#46;id | string | e026 |
| $&#46;evidence&#91;25&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;25&#93;&#46;operation | string | reverse&#95;geocode&#95;coordinates |
| $&#46;evidence&#91;25&#93;&#46;sha256 | string | 061bb864041a8e956f4cc5d248e4f0e0ebe4d6defc1e76f70743baeb11b56bbf |
| $&#46;evidence&#91;26&#93; | object | object |
| $&#46;evidence&#91;26&#93;&#46;artifact | string | evidence/e027&#46;json |
| $&#46;evidence&#91;26&#93;&#46;id | string | e027 |
| $&#46;evidence&#91;26&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;26&#93;&#46;operation | string | list&#95;place&#95;categories |
| $&#46;evidence&#91;26&#93;&#46;sha256 | string | 4445bf3616f6447811189c247f9d934dfa155e91a0986eea2b1553d6f83abadf |
| $&#46;evidence&#91;27&#93; | object | object |
| $&#46;evidence&#91;27&#93;&#46;artifact | string | evidence/e028&#46;json |
| $&#46;evidence&#91;27&#93;&#46;id | string | e028 |
| $&#46;evidence&#91;27&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;27&#93;&#46;operation | string | transform&#95;geometry |
| $&#46;evidence&#91;27&#93;&#46;sha256 | string | 82cc2327e5f4291cd472387f51f6f8cda2896e41c4d56f2d7a645c3d17a29ff0 |
| $&#46;evidence&#91;28&#93; | object | object |
| $&#46;evidence&#91;28&#93;&#46;artifact | string | evidence/e029&#46;json |
| $&#46;evidence&#91;28&#93;&#46;id | string | e029 |
| $&#46;evidence&#91;28&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;28&#93;&#46;operation | string | evaluate&#95;spatial&#95;relation |
| $&#46;evidence&#91;28&#93;&#46;sha256 | string | 8b20bd04e672ecd488cfba5d195a638cbaad65f727b8c9603068d88db9034ab0 |
| $&#46;evidence&#91;29&#93; | object | object |
| $&#46;evidence&#91;29&#93;&#46;artifact | string | evidence/e030&#46;json |
| $&#46;evidence&#91;29&#93;&#46;id | string | e030 |
| $&#46;evidence&#91;29&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;29&#93;&#46;operation | string | evaluate&#95;spatial&#95;relation |
| $&#46;evidence&#91;29&#93;&#46;sha256 | string | cff90bd2859220a52d26b458843172e5d95b4b1ab794189203d0891c3a8452cc |
| $&#46;evidence&#91;30&#93; | object | object |
| $&#46;evidence&#91;30&#93;&#46;artifact | string | evidence/e031&#46;json |
| $&#46;evidence&#91;30&#93;&#46;id | string | e031 |
| $&#46;evidence&#91;30&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;30&#93;&#46;operation | string | measure&#95;geometry |
| $&#46;evidence&#91;30&#93;&#46;sha256 | string | afb8267cbc65ae4b78acb12d5086d926e0fd1d30b827640aa1e8f60641580d69 |
| $&#46;evidence&#91;31&#93; | object | object |
| $&#46;evidence&#91;31&#93;&#46;artifact | string | evidence/e032&#46;json |
| $&#46;evidence&#91;31&#93;&#46;id | string | e032 |
| $&#46;evidence&#91;31&#93;&#46;kind | string | mcp |
| $&#46;evidence&#91;31&#93;&#46;operation | string | calculate&#95;route |
| $&#46;evidence&#91;31&#93;&#46;sha256 | string | 8a37a1b65c2a6e32d603daca5f6ba67195be0142843407920579c5903e9835f1 |
| $&#46;path | string | mcp |
| $&#46;run&#95;status | string | complete |
| $&#46;run&#95;timestamp&#95;utc | string | 2026&#45;10&#45;23T19&#58;58&#58;09Z |
| $&#46;schema&#95;version | string | 1&#46;0 |
| $&#46;settings | object | object |
| $&#46;settings&#46;boundary&#95;rule | string | Known outbound time at or below budget is in zone; no continuous boundary&#46; |
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
| $&#46;warnings | array | 5 entries |
| $&#46;warnings&#91;0&#93; | string | Fictional business/customer identities at real public demo locations; no affiliation or actual customer relationship&#46; |
| $&#46;warnings&#91;1&#93; | string | Hosted acquisition spans captured sessions; final twenty&#45;target matrix supersedes the preliminary nineteen&#45;target matrix&#46; |
| $&#46;warnings&#91;2&#93; | string | Competitor coverage is sampled, at most 20 candidates and no pagination&#46; |
| $&#46;warnings&#91;3&#93; | string | The category service is broad; these candidates are not verified plumbing competitors&#46; |
| $&#46;warnings&#91;4&#93; | string | Claude projects hosted structured results as JSON text; normalization validates typed results and captured arguments&#46; |
| $&#46;zone | object | object |
| $&#46;zone&#46;approximation | boolean | true |
| $&#46;zone&#46;evidence&#95;refs | array | 1 entries |
| $&#46;zone&#46;evidence&#95;refs&#91;0&#93; | string | e022 |
| $&#46;zone&#46;limitations | array | 1 entries |
| $&#46;zone&#46;limitations&#91;0&#93; | string | Route&#45;time classification only at measured points; no continuous zone&#46; |
| $&#46;zone&#46;method | string | route&#95;time&#95;at&#95;points |
| $&#46;zone&#46;parameters | object | object |
| $&#46;zone&#46;parameters&#46;budget&#95;seconds | number | 1200 |
