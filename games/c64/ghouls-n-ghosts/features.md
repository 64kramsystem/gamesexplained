# Documented features

Source: [Ghouls 'n Ghosts — C64-Wiki](https://www.c64-wiki.com/wiki/Ghouls_%27n_Ghosts), consulted 20 November 2026. The game’s title and first stage were also captured from the TWT disk.

| Feature | Status | Evidence or question |
| --- | --- | --- |
| Start from the title | live | Fire on joystick port 2 reaches stage 1. See `reference/title.png` and `reference/stage-1.png`. |
| Music or sound effects | confirmed | $5F17 selects MUSIC with left and SOUND FX with right. A watchpoint on $1F caught the right selection. |
| Five stage loads | confirmed | The normal transition loader was exercised for stages 2–5 using the stage-outcome flag. Each stage has two payloads. |
| Rescue ending | live | A forced outcome in the stage-five snapshot took selector $0A to the resident ending at $2A1C, then reached its text and song calls. |
| Walking, jumping, crouching and climbing | traced | The resident movement routine at $41AD dispatches by terrain and direction. The climb path is at $442D and the jump-direction decoder is at $44EB. Individual control combinations have not been exercised. |
| Directional shots | traced | The resident launcher at $47AE combines facing and attack pose before choosing X and Y from $481F and $4833. The set of legal airborne firing poses remains open. |
| Five weapons | traced | The resident launcher at $47AE indexes weapon limits and actor types at $480B and $4811. The engine has six entries including a charged-weapon mode. Mapping every slot to the wiki names remains open. |
| Chests and basket-carrying enemies | traced | The resident search at $2C30 checks chest coordinates and used flags, then spawns type $0C. The pickup path at $40A6 handles type $12. The basket-specific reward cases remain open. |
| Armour, death and lives | traced | The resident path at $4193 changes the costume and flash timer. $48EA sets the death result and $2A2E decrements the lives counter. The animal transformation conditions remain open. |
| Score, weapon and timer display | live | The stage 1 panel shows all three. |
| Stage bosses and checkpoints | traced | The resident continue prompt uses $2A93 and resumes the current section through $29A2. Stage actor lists and their handlers are in the part listings. A complete boss-to-transition play route was outside this analysis. |
| Scrolling scenery and animated enemies | traced | Resident scrolling is driven through $5163. Stage one builds extra moving sprites through $9374 and $939B. Stage two exchanges ten terrain glyphs at $8F41. |
| Pause and abort | live | The resident keyboard scan took Commodore to $3064 and Q to $3051. Store watches caught the pause indicator colour and the score clear. |
| High scores | confirmed | $5589 draws ten 20-byte entries. $57B3 handles the joystick-driven grid and $562B inserts the score into the RAM table. The disk reader census covers the named files and numbered loads. Disk persistence was not exercised. |
| Name-triggered cheats | traced | $58F6 compares the entered name with `WIGAN RLFC` and seven blanks. A match makes the extra keyboard path reachable. Its two handlers are $3090 and $3097. |
