# Stormlord features

| Feature | Status | Detail |
| --- | --- | --- |
| Fairy rescue | traced | The pickup callback increments the rescued count at $0D26. The round compares it with the level target at $073C. |
| Four levels | traced | Four map streams are resident. The level initializer at `$2CA2` replaces level 5 with level 1. |
| Movement | traced | Walk left or right, jump and duck. Title screen offers keyboard or joystick in port 2. |
| Weapons | confirmed | Live checkpoints on the two release paths at `$3E3B` and `$3EEB` distinguish the short shot from the sword after nine held reads. |
| Carried item | open | The icon routine at $0E03 reads the equipment ID. The pickup path was inspected for equipment handling, and the swap rules for all item types remain open. |
| Key and gates | traced | The gate handler at $0C35 tests for equipment ID $6A and overlap, then removes the key and gate. |
| Umbrella | open | The falling-hazard setup compares held item $74 and clears $1573 on a match. The complete damage path remains open. |
| Honey pot | open | The handler at $0CD9 uses the associated map-object state. The sequence from dropping the pot to the insect response remains open. |
| Boots | traced | Equipment ID $5C raises the grounded up-input hold limit from $14 to $2C at $16DF. |
| Timer and lives | traced | The lower panel shows the clock, lives, score, carried item and fairy counts. The phase test at $3074 sets the end flag at $21. |
| Bonus round | confirmed | Instruction steps through $11D8 show the tenth catch awards a life when the life counter is below nine. |
| Abort | traced | The NMI at `$36B7` writes the abort flag read by the play loop. |
| Presentation | confirmed | Horizontal scrolling, a lower status panel and music during play. |
| Redefine controls | confirmed | The opening prompt names O, P, Q, A and Space. The code at `$7A60` handles accepting or changing those bindings. |

## Sources

- [Stormlord – C64-Wiki](https://www.c64-wiki.com/wiki/Stormlord), consulted 19 November 2026.
- [Stormlord instructions, Hewson](https://www.gamesdatabase.org/Media/SYSTEM/Amstrad_CPC/Manual/formated/Stormlord_-_1989_-_Hewson_Consultants.pdf), cross-platform manual.
