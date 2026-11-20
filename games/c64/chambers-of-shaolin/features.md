# Features

The printed guide describes three platforms. The disk load calls and media ledger identify which of its features this C64 release contains.

| Feature | Status | Evidence |
| --- | --- | --- |
| Stick | differs | The manual describes a training chamber with the master’s stick. The numbered disk loads and fixed LOAD names lead through Balance, Speed and Strength before Combat. |
| Agility | differs | The documented Agility chamber has no file or transition in the disk route. The Balance overlay has its own moving hazards and pickup markers. |
| Balance | live | The first overlay shows four poles and the time and sign counters. The pickup check at $0EC3 counts successful matches. A controlled result test reached the training flag and four award stores. |
| Speed | live | The second overlay shows the suspended ball and the rising water. Instruction traces show the ball’s recenter and reversal branches and both water painters. VICE checkpoints caught the four result award stores and the flag boundary between 49 and 50 percent. |
| Strength | live | The third overlay shows the board chamber and its gauges. The code at $0D8C uses time between joystick direction changes, and $0F7C takes the strike path once the strength gauge finishes. Execution checkpoints covered partial progress and full success in the result handler. |
| Fire | differs | The manual describes a burning-basket bridge. The counted disk files lead directly from Strength to Combat. |
| Combat | live | The fourth overlay draws two fighters and four scene sources. Both motion interpreters read the training unlock flags for moves four, six and seven. The starting bar and timer calculations and the contact-score routines read training values carried from the numbered overlays. |
| End sequence | differs | The disk uses an interlude followed by HIGH. A one-apprentice win in scene index 3 sets the exit flag and selects interlude 1. Two-apprentice completion selects interlude 6 and takes the same score exit. |
| Character storage | differs | The code and media search accounts for the fixed load names, including the relocated Speed loader. The save call at $C44E in HIGH writes the score file H. The two names and training values pass between overlays in resident RAM. |
| Score table | live | The score screen requested H at $FFD5 and displayed five records. Fire led to LOAD for LABLE. The score-save call uses the replacement name @:H. |
| Music and sound effects | traced | Title, Balance, Speed, Combat and High Scores use SID music drivers. Speed has two traced tune selectors. Six Strength effect streams drive its own SID player. |

## Sources

- [Chambers of Shaolin printed manual](https://db.hfsplay.fr/files/2018/10/06/cefaf35f-cfde-419b-a20d-cf990ade2c95.pdf), consulted 20 November 2026. The English training and combat instructions are on pp. 6–15.
- [Overdrive release record](https://csdb.dk/release/?id=241287), consulted 20 November 2026.
- [Chambers of Shaolin – C64-Wiki](https://www.c64-wiki.de/wiki/Chambers_of_Shaolin), consulted 20 November 2026.
