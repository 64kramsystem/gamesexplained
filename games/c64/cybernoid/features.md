# Cybernoid features

Sources consulted on 19 November 2026

- [Cybernoid: The Fighting Machine, C64-Wiki](https://www.c64-wiki.com/wiki/Cybernoid:_The_Fighting_Machine)
- C64 title menu and the first room, captured from the Beastie Boys disk. See [menu](reference/menu.png) and [first room](reference/room-01.png).
- [Reference gameplay animation, C64-Wiki](https://www.c64-wiki.com/images/0/05/Cybernoidingame2.gif)

| Feature | Status | Evidence or question |
|---|---|---|
| Title menu and credits | live | The menu offers start, redefine keys, keyboard, joystick II, and music/sound. The title cycles through a high-score table and credit screen. |
| Start game | live | Holding `1` as the options screen appears starts the first room. |
| Move and fire | live | $48BF and $48E3 select the control mode. At the same first-room loop checkpoint, the neutral trial passed $563E zero times and the held-fire trial passed once. |
| Five auxiliary weapons | traced | $5A38 selects the five weapon records in order. Their handlers are $6448 (bombs), $63A3 (mines), $60A3 (shield), $6185 (bouncing bombs) and $60B6 (seekers). Bomb activation and stock debit were also observed by checkpoints. |
| Weapon stock | confirmed | $5B2B debits stock for a successful activation, and $6B2C refills up to the selected weapon's limit. The first-room bomb watchpoint recorded two debits, from 20 to 18. |
| Cargo and score | traced | $6B48 adds cargo and $3404–$342D applies the 1,500-point cargo test and bonus when the timer permits it. The lives award is capped at four craft. |
| Room exits and level progression | traced | $36CB wraps the coordinates and adjusts the layout index by one or the stage stride. $2DC4 selects from three stage records. $3346 runs the stage report before advancing the stage index. |
| Attacks, hazards and pickups | traced | Room setup dispatches tile markers into actor records at $3745. $3043 updates path enemies, $3A90 moves paired hazards, and $6A86 dispatches pickup effects. $6B20 and $6B7B enable rear fire and satellites. |
| Death and retry | confirmed | $704F tests room timeout and object contact. Forcing the room timer to expire took the $70C6 decrement and changed the live craft count from four to three. The respawn branch at $70D6 restored the entry coordinate and issued a new protection timer. |
| Timer and game over | confirmed | Forcing $2E9D/$2E9E to one triggered one bar advance at $725B and reloaded the divider. The level bar saturates at twenty, and $33FD uses it in the end-of-stage bonus test. The separate room timer can cost a craft. $70D3 enters game over when the craft count has reached zero. |
| Music and effects | traced | $49B0 schedules $AE06 for music or $A601 for sound effects based on $8167. The dummy sound device allowed the register-writing code to be traced. |
| Hall of Fame | traced | The title displays nine score rows. $84BA compares the six digits, shifts lower ranks and takes a name for the resulting row. The reference search for KERNAL SAVE at $FFD8 found no matching instruction. Disk persistence remains open. |
| Stale lives display | confirmed | Following a forced room timeout, $14 fell from four to three. At the end of the confirmed respawn path, the lives digit pixels had not changed and the $57F9 redraw checkpoint registered zero hits. |
| Long-session audio bug | open | Both software audio paths were identified, including the shared IRQ scheduling. The reported delayed failure requires sustained playback and its behaviour is open for this release. |
