# Documented features

Source: [Ghouls 'n Ghosts — C64-Wiki](https://www.c64-wiki.com/wiki/Ghouls_%27n_Ghosts), consulted 20 November 2026. The game’s title and first stage were also captured from the TWT disk.

| Feature | Status | Evidence or question |
| --- | --- | --- |
| Start from the title | live | Fire on joystick port 2 reaches stage 1. See `reference/title.png` and `reference/stage-1.png`. |
| Music or sound effects | confirmed | $5F17 selects MUSIC with left and SOUND FX with right. A watchpoint on $1F caught the right selection. |
| Five stage loads | confirmed | The normal transition loader was exercised for stages 2–5 using the stage-outcome flag. Each stage has two payloads. |
| Rescue ending | traced | Selector $0A takes the display path at $2A1C rather than reading another stage. The final presentation needs analysis. |
| Walking, jumping, crouching and climbing | open | The wiki lists directional combinations for these moves. |
| Directional shots | open | The wiki reports forward fire on the ground and upward and downward shots while airborne. |
| Five weapons | open | The wiki lists the spear, knife, shuriken, axe and spray torch. |
| Chests and basket-carrying enemies | open | Reported sources of weapon, bonus and magician encounters. |
| Armour, death and lives | open | The panel displays life icons. The wiki describes armour loss and a temporary animal transformation. |
| Score, weapon and timer display | live | The stage 1 panel shows all three. |
| Stage bosses and checkpoints | open | The wiki reports a continue from the last checkpoint after all lives are lost. |
| Scrolling scenery and animated enemies | open | The wiki names rain as one of the level animations. |
| Pause and abort | open | The wiki names Commodore and Q, respectively. |
| High scores | confirmed | $5589 draws ten 20-byte entries. $57B3 handles the joystick-driven grid. Disk persistence remains open. |
| Name-triggered cheats | traced | $58F6 compares the entered name with `WIGAN RLFC` and seven blanks. A match makes the extra keyboard path reachable. Its two handlers are $3090 and $3097. |
