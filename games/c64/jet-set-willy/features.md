# Jet Set Willy — features

Sources: [game documentation](https://www.c64-wiki.com/wiki/Jet_Set_Willy) and the contributor’s annotated listing, consulted 30 September 2026. The documentation supplies the feature inventory; the annotations supply leads for verification.

| Feature | Status | Evidence or open work |
|---|---|---|
| Explore connected rooms | partly live | $2E55 copies all 60 records exactly; $2EE5 expansion matched all 30,720 cells. Exit-transition behavior remains open |
| Jumping and platform collision | open | Player and collision routines preserved in Source; no new live replay |
| Collect objects | open | $22C3 item records and $0401 BCD counter |
| Guardians, arrows and ropes | partly live | Rope staging at $16DE matches all 34 positions. Guardian/arrow collision and rope attachment remain open |
| Return to bed after collection | open | $0400 changes Maria visibility; complete winning input route is not demonstrated |

Imported annotations are leads until traced or exercised in this run. The boot itself is observed live.

| Character and sprite display | live | Complete recorded frame matches all 104,448 emulator pixels |
| Title music | live | Native playback ends at decoded stream pointers; the end flag and zero volume match |
