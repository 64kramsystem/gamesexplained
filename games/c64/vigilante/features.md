# Vigilante — features

| Feature | Status | Evidence |
|---|---|---|
| One-player scrolling brawler, controlled with joystick port 2 | live | Port 2 fire dismissed the Hall of Fame and started the first stage. |
| The Skinheads take Madonna hostage | live | The opening story screen names both. |
| Player and enemy health, timer, score, high score and lives | live | First-stage panel shows two bars, TIME, SCORE, HI-SCORE and three player figures. |
| Hall of Fame and fire prompt | live | The attract screen shows five entries. |
| Horizontal input and fire-based actions | traced | Targeted instruction and store checkpoints at `$16EF`, `$124C`, and `$16ED`. |
| Up jumps. Down selects a separate stance. | confirmed | `$124C` selected headers `$2114` and `$2119`. The write to player Y moved up for the first case. Up-diagonal and stance details remain open. |
| Up+fire and horizontal+fire select separate attacks | traced | Live dispatch selected `$2132` and `$2141`. The first moved the player upward. The strike names from the C64-Wiki guide remain open. |
| Down diagonals with and without fire select separate actions | traced | Right+down used `$2128`. With fire it used `$2137`. The exact strike names remain open. |
| Enemies can grab the player. Rapid left and right breaks free. | open | C64-Wiki description. The actor proximity routine at `$3061` and stick dispatch at `$11CA` were traced. The escape path was not isolated. |
| Pick up and use a chain | open | C64-Wiki description. Traced damage and proximity paths at `$34F3` and `$3061`. References to the stage-change flag `$0D18` showed the tile update and resets, with pickup still unlocated. |
| RUN/STOP pauses and resumes | confirmed | Stepped through `$10F4–$10FB` for released and pressed matrix inputs, then hit the timer-enable instruction at `$1101`. |
| Five stages loaded over the resident engine | confirmed | Each stage file group matches a snapshot at the reload exit. |
| Stage-end opponent behaviour | traced | Five stage callbacks are selected via `$2C8A`. Exact action selection remains open. |
| Music and effects during play | traced | Music at `$380F` gates two pulse voices in this disk build. Hit effects at `$388B` and text sound at `$3A80` use the third voice. |

## Sources

- [Vigilante at C64-Wiki (German)](https://www.c64-wiki.de/wiki/Vigilante), consulted 19 November 2026.
- [Vigilante at Lemon64](https://www.lemon64.com/game/vigilante), consulted 19 November 2026. Covers the U.S. Gold release.
- [Zzap!64 issue 55, page 18](https://www.zzap64.co.uk/magazine/zzap64/55/18), November 1989, consulted 19 November 2026.
- Data East disk build in VICE. See `reference/` for the Hall of Fame, story and first stage.
