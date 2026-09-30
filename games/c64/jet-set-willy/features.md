# Jet Set Willy — features

Sources: [game documentation](https://www.c64-wiki.com/wiki/Jet_Set_Willy) and the contributor’s annotated listing, consulted 30 September 2026. The documentation supplies the feature inventory; technical status comes from the listing.

| Feature | Status | Evidence or open work |
|---|---|---|
| Explore connected rooms | traced | $2E55 room copy and offsets $DC–$DF |
| Jumping and platform collision | traced | Player and collision routines preserved in Source; no new live replay |
| Collect objects | traced | $22C3 item records and $0401 BCD counter |
| Guardians, arrows and ropes | traced | $2443, $2403 and $8100 |
| Return to bed after collection | open | $0400 changes Maria visibility; complete winning input route is not demonstrated |

“Traced” means supported by the imported analysis. It does not imply a fresh live replay in this publication pass. Scope exclusions are described in `orientation.md`.
