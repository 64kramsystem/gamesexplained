# Blood Money features

Sources consulted on 19 November 2026 include the Accept disk's title and options screens, the [C64 review at Lemon64](https://www.lemon64.com/review/blood-money/348), and the [C64 catalog at Games Database](https://www.gamesdatabase.org/game/commodore-64/blood-money).

| Feature | Status | Evidence or question |
|---|---|---|
| Animated title and credits | live | Title screen in the Accept disk. |
| Title theme and in-game sound | traced | Title setup calls $E000 with command 2 at $1D82. The driver reads pattern pointers and writes voice frequency and pulse width. The level 1 SID write probes are in the resident engine facts. |
| One- and two-player modes | live | Menu key 1 reached one-player gameplay. Matrix key 2 hit the $C399 store of the two-player flag. The two-player input loop reads both mapped ports at $23D7 and $23F6. |
| Options for faster text and viewing high scores | live | Matrix key 4 hit the text-speed toggle at $C3EA. The high-score path at $3E0E renders the records and searches the ten RAM entries at $1BD3 through $CE50. Score persistence remains open. |
| Four missions with side-view scrolling | live | Four level loads reached play. The loader selects files with the digit set at $C8BF. Direction bytes at $8004 are consumed at $CC6A and $9E28. |
| Shooting enemies releases money | traced | The projectile overlap path calls $3509. The hit and replacement paths can install coin properties in the defeated object’s slot. A forced replacement of the level 1 record at $8EC7 installed class 1 from $8F9A. The class 2 record at $8FA7 pays more. |
| Dropped money falls out of reach | traced | The level 1 replacement loop at $8E0D adds five to Y. Its properties set the boundary-cull flag handled by $D473. Player collision at $3410 credits class 1 and 2 drops and releases the collected slot. |
| Shops sell upgrades | live | A controlled purchase at $2713 reached the rising-shot upgrade store at $2767. The eight action pointers use $02F1 and $0340, and the currency checks use $0349 and $0352. |
| Contact with walls or enemies drains energy | live | The terrain hull check is at $CA26. Class 5 sprite overlap calls $31B9. A forced call at its damage threshold hit the decimal life-count store at $3204. |
| Some enemies take money | live | A forced class 4 overlap at $3410 hit the $3283 store, which reduced the packed decimal balance from $30 to $25. Class 5 uses the separate damage path. |
