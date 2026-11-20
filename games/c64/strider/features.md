# Strider features

| Feature | Status | Evidence |
|---|---|---|
| Front-end options and start | confirmed | Port 2 fire on START GAME opens stage 1. The front-end joystick routine at resident $B303 distinguishes up, down and fire, and sets the selected audio mode or starts the game. |
| Status display | confirmed | $8B0E draws the timer, score and lives. $896D writes the segmented health bar. The timer's decimal borrow was stepped in VICE. |
| Horizontal movement and level scrolling | confirmed | Right advanced the low X byte by $0C from the grounded probe. $94A2 updates position, $950C follows X and $A038 expands the view into a screen matrix. |
| Jump and sword | confirmed | Grounded up entered action 1 and hit the jump displacement instruction. Fire from the same snapshot hit the sword initiation path at $9BB5. |
| Edge movement and slopes | traced | $8C6C chooses diagonal motion from terrain properties 3 and 5. $8E0B probes each side and selects a different edge action. The live controls probe exercised the first grounded room. |
| Enemy encounters and five stage loads | confirmed | Each stage was reached through its loader selector and observed with its own playfield. The stage-specific camera and object checks are in $B823 and $A6FD. |
| Failure, retry and high scores | traced | $89BB spends a life and $8A7F resets the current area or returns to the title with the score. $B71D inserts a qualifying score and $B213 draws the score screen. |
| Ending | traced | The final completion case at $A2DE prints the ending text from $CE59. |
| Music and sound effects | confirmed | The title offers both modes. The live gameplay raster probe reached $6C12 and counted SID writes. The effect entry at $7FE0 installs an effect when the audio setting allows it. |

## Sources

- The emulator captures include the [loading picture](reference/loading.png), [title screen](reference/title.png) and [stage 1](reference/stage1.png).
- [Commodore 64 Longplay [330] Strider (EU)](https://www.youtube.com/watch?v=r9UtEAv3Ep0), consulted 20 November 2026.
