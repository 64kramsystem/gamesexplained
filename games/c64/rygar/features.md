# Rygar features

| Feature | Status | Evidence |
| --- | --- | --- |
| Joystick in port 2 | confirmed | `$1098` reads CIA1 port A. At this instruction with right and fire held, A and the stored sample at `$6B` became `$E7`. |
| Keyboard controls | confirmed | The title lists Z left, X right, Shift jump, Space crouch and Return fire. Stops at `$111D` verified all five active-low masks. |
| Jump and raised attack | confirmed | Six-frame tests from the same Round 1 snapshot reached `$2303` with up alone and `$20B1` with up and fire. |
| Horizontal scrolling | confirmed | The Round 1 raster capture shows the playfield fine scroll. `$1262` checks direction and local ground before the shift, and the map watches confirmed reads from `$9C00` and `$B000` with right held. |
| Rounds and ending | traced | `$11D5` selects one of sixteen resident maps. `$1717` advances the round, with the terminal branch at `$173B` reaching the victory message. The ending was examined in code. |
| Enemies, weapon hits and pickups | traced | `$3580` handles object events. `$28BA` combines the latched VIC collision bits with per-object coordinate and state checks. Negative types enter the pickup path at `$2A5E`, where flags select powers, extra time and an extra life. |
| Lives and death | confirmed | A hazard-flag test stopped on the lives decrement at `$254F`. The game shows the death pose and restarts through `$21F7` when lives remain. |
| Round timer | confirmed | 50 PAL frames produced 50 timer-update hits and 100 calls to the fractional decrement routine `$0FD2`. |
| Score, bonuses and high scores | traced | `$2D67` updates the score and bonus counters, `$18BB` tallies the bonuses, and `$1B74` accepts initials into the ranked table. The full entry flow was examined in code. |
| Pause, reset and sound mode | traced | The title names F1, F3 and F5. Their handlers at `$0D75`, `$0DB5` and `$0DEF` test the corresponding matrix bits. |
| Music and effects | confirmed | `$8136` ran 50 times in the 50-frame trace. The cue and effect entry points are `$8000` and `$86D0`. Offline execution of cue 1 decoded the three distinct voice patterns. |

## Sources

- [Rygar (U.S. Gold) computer instructions](https://frameadvance.net/sources/rygar-c64-manual/), C64 inlay catalogue and scan, read 20 November 2026.
- [Rygar preservation catalogue](https://preservation64.de/index.php?title=Rygar), consulted 20 November 2026 for the C64 retail and budget releases.
- The game title, photographed in `reference/title.png`, includes the keyboard legend. `reference/round-1.png` shows the first playable round.
