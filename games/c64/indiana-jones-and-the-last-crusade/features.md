# Features

| Feature | Status | Documentation |
|---|---|---|
| Port 2 controls | confirmed | Fire starts the title screen. The panel IRQ reads the low five bits of CIA1 port A at $816F. |
| Movement and combat | live | The resident climb path at $A1B3 tests the overhead contact class and the up/down action bits. A fire-action probe stopped after the store at $9E89 with movement mode $08. The following branch uses the timer at $7A60 to choose a thrown projectile or whip. |
| Cave light | confirmed | The palette changes when the light timer carries. An instruction watch stopped just after the replacement store at $8BDD. $A6CE is the palette-restoring pickup path. |
| Cross of Coronado and escape | open | The transition at resident $8F0F sets the train subsection before advancing the main stage index. The train timer carry into $7A35 was watched at $8C64. The link between the cross graphic and its contact class remains open after tracing the pickup dispatch at $A6AD and the transition at $8EB4. |
| Catacombs | live | Six symbols and a date appear over the stage entrance. The riddle code at resident $B05F–$B0B9 selects letter glyphs by threshold and writes the decimal clue. The link from the shield and the generated clue to the correct arch remains open after reading the riddle formatter and the class-$0B pickup at $A6E5. |
| Castle wall | open | The catacombs hazard dispatcher takes the lightning path at resident $8B60. The routine advances its phase and writes bolt glyphs through the map pointer table. The link between a bolt and the player’s collision outcome remains open after following the hazard dispatcher and climb probe at $A1BA. |
| Airship | open | Class $0F dispatches to the airship map patcher at resident $A735. The patcher edits nine ten-cell strips. The links between pass graphics, individual guards and the exit remain open after reading the contact and actor dispatches at $A6AD and $B449. |
| Grail temple | open | The panel timer at resident $8C27 selects two heart patterns. The stage-three transition at $8F05 selects the third title page. The conditions connecting the Grail pickup to that transition remain open after reading the pickup and stage-transition dispatches. |

## Sources

- [Program instructions](https://idpixel.ru/games/i/indianajonesandthelastcrusade/files/indianajonesandthelastcrusademulti-lang.pdf), English C64 loading and control sections and the level descriptions, consulted 19 November 2026.
- [Lemon64](https://www.lemon64.com/game/indiana-jones-and-the-last-crusade), C64 release and screenshots, consulted 19 November 2026.
