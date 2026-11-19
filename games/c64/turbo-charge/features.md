# Turbo Charge — feature checklist

| Feature | Status | Evidence or question |
|---|---|---|
| Start a single-player chase | live | Port 2 fire at the title loads the first driving scene. |
| Recover the stolen weapons | open | The manual sets the pursuit in Operation Underdog. |
| Steering, braking and acceleration | confirmed | Checkpoints at `$6E9A/$6ED5` distinguish left and right. `$6F73` and `$6F80` are the accelerate and brake calls. |
| Handgun and missiles | confirmed | A hold hits the initial press branch once, changes the sight, then spends one missile on release. See [driving facts](facts.md). |
| Turbo boost | confirmed | Space hits the countdown setup at `$6FAB`. The active path spends fuel and advances speed. |
| Pause and abort | open | The manual lists RUN/STOP and tentatively lists RESTORE. |
| Damage, fuel and pickups | open | The panel displays damage and fuel. The documentation describes fuel canisters and failure when fuel runs out or damage is excessive. |
| Traffic, hills, bends and forks | open | The documented routes include climbs and forks. The first-round view also has trackside scenery and a central sight. |
| Border countdown and scoring | live | The first-round panel displays score and distance to the border. Deadline and score rules remain open. |
| Multi-load stages and transitions | confirmed | Ten driving images form five chapters. The finish cards alternate border-smash and villain-capture scenes. The last capture card says Game complete. |
| Music and effects | open | Sean Connolly reports six tunes shared with Marc François, plus sound effects. Locate the player and selectors. |
| Title and high scores | live | The title cycles through a scores display. The score-entry and disk-saving paths remain open. |

## Sources

Consulted 19 November 2026.

- [System 3 instruction manual](https://archive.org/details/Turbo_Charge_1991_System_3_M3/page/n1/mode/2up)
- [Turbo Charge gameplay summary](https://en.wikipedia.org/wiki/Turbo_Charge)
- [Sean Connolly interview](https://www.c64.com/gt_display_interview.php?interview=44)
- [Nostalgia disk release](https://csdb.dk/release/?id=230212&show=notes)
- VICE title and first-round observations. See `reference/` and `orientation.md`.
