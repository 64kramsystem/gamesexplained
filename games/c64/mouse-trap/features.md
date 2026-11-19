# Mouse Trap features

| Feature | Status | Evidence |
|---|---|---|
| Single-player, fixed-screen platforming with joystick in port 2 | live | The first room follows the title after fire. Lemon64 and GameBase64 identify the same control port. |
| Title illustration and theme | live | `reference/title.png` shows the illustrated title. GameBase64 credits Dirk Haserman for music. |
| Platforms, gaps, cheese-shaped objects, and moving hazards | live | `reference/play.png` shows the first room and the right-hand panel. |
| Jump, collect objects, and unlock the exit | confirmed | Checkpointed VICE calls verified jump setup at $12DD, the collectible clear at $17B3 and the exit tile write at $17FA. |
| Advance through rooms | traced | The room ladder is at $18CF. All 22 directory entries loaded in controlled VICE calls. |
| Lives, the timer strip, and score | traced | The HUD painters are $1A3A, $1BB5 and $1A7B. Normal mode starts with five lives. |
| Trainer choices before the title | live | The supplied build offers Normal, 9 Lives, and Trainer. Normal was selected. |

## Sources

- [Mouse Trap, GameBase64](https://gb64.com/game.php?id=5031), consulted 19 November 2026.
- [Mouse Trap, Lemon64](https://www.lemon64.com/game/mouse-trap), consulted 19 November 2026.
- [Squeal, Edicola 8 Bit](https://www.edicola8bit.com/gioco?id=2364), consulted 19 November 2026. The program used here was the download listed under the original title.
