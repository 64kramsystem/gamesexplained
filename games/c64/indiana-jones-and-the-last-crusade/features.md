# Features

| Feature | Status | Documentation |
|---|---|---|
| Port 2 controls | confirmed | Fire starts the title screen. The panel IRQ reads the low five bits of CIA1 port A at $816F. |
| Movement and combat | open | Movement and attacks remain to be followed from the decoded action at $7A3F. |
| Cave light | confirmed | The palette changes when the light timer carries. An instruction watch stopped just after the replacement store at $8BDD. $A6CE is the palette-restoring pickup path. |
| Cross of Coronado and escape | open | Recover the cross, then escape over the train. |
| Catacombs | live | Six symbols and a date appear over the stage entrance. The instructions say to recover the Crusader's shield and use the date shown above the arches to choose the correct arch. |
| Castle wall | open | Climb the wall while avoiding lightning. |
| Airship | open | Collect passes to get past guards and reach the exit. |
| Grail temple | open | Reach the Grail to save Henry Jones. |

## Sources

- [Program instructions](https://idpixel.ru/games/i/indianajonesandthelastcrusade/files/indianajonesandthelastcrusademulti-lang.pdf), English C64 loading and control sections and the level descriptions, consulted 19 November 2026.
- [Lemon64](https://www.lemon64.com/game/indiana-jones-and-the-last-crusade), C64 release and screenshots, consulted 19 November 2026.
