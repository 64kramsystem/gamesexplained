# World Class Leaderboard features

| Feature | Status | Evidence or question |
|---|---|---|
| Title artwork and course list | live | Globe title and A–P list captured in reference. |
| Course selection | confirmed | Shift+Return enters the course picker. The BCT load trace changed the course descriptor to Doral Country Club. |
| One to four golfers with names and individual skill levels | live | Setup displays player count, name field, and Professional, Amateur and Kids choices. Skill effects are open. |
| 18, 36, 54 or 72 holes | live | F1, F3, F5 or F7 at setup. F1 reached hole 1 of the first round. Round progression is open. |
| Perspective course view and golfer | live | Cypress Creek hole 1 shows trees, fairway, the tee and golfer beside the status panel. |
| Status panel | live | Shows hole, par, round, player and relative score, wind, club, yards, power and snap. |
| Club selection | traced | $15C5 cycles the club index on up and down. |
| Aiming and power release | confirmed | Port 2 left and fire release reached the watched stores in the aim and swing handlers. |
| Snap | traced | $160F latches the later fire press and derives the snap value from the timing byte. |
| Ball flight, terrain, hazards, wind and putting | open | Manual describes carry, hazards and putting. |
| Scorecard and honours | traced | The engine score routines total the strokes and calculate turn order. |
| Scorecard printer | traced | PRNT load reached the printer entry at $6800 after a debugger transfer to the confirmation branch. Paper output remains open. |
| Driving range and practice putting | traced | R and G branch from the player-count prompt. |
| Demonstration | traced | The setup timeout and D key enter the demo. The DMO payload load was observed live. |
| Overhead course view | traced | The T key branch at $3E6F redraws the hole using overhead projection. |
| Course customisation and disk saving | open | The publisher manual describes custom courses. The analysed release advertises a different extended A–P course disk. |
| Effects | traced | SID setup, voice gating and filter changes appear in the engine. |
| Speech and music | open | Audio provenance across the boot and play phases remains open. |

## Sources

- Original Access Software C64 instruction manual, consulted 19 November 2026. [World Class Leader Board instruction manual](https://www.digitpress.com/library/manuals/c64/wc_leader_board.pdf)
- Screens captured from the analysed release on 19 November 2026. [Title](reference/title.png), [course list](reference/courses.png), [player count](reference/player-count.png), [first tee](reference/cypress-creek.png)
