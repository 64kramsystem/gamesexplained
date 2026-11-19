# Features

| Feature | Status | Evidence or question |
|---|---|---|
| Score and Naughtyometer | confirmed | $CF47 renders score and $CF9D renders the meter. A live test at meter four wrote four filled cells. $ADFE starts the ending path on player contact at exactly ten. |
| Movement | confirmed | Port 2 left, right and neutral branches were observed at $9108, $9121 and $9198. Jump and climb paths are traced at $908B and $92C4. |
| Nappy parachute | differs | $9851 checks port 2 fire during the falling window. Live instruction stops showed that fire alone activated it at counts 30 and 49. The preceding early-fire latch can block it. |
| Items | traced | $CD4C searches and exchanges the item records in crouch mode. $C810 dispatches the selected item through $C7AE. The wiki lists grease, rope, pineapple, mouse, onion, honey, toffees and termites. Individual item routes remain open. |
| Weapons | traced | $C7DA reads port 2 fire and $C829 starts an effect through sprite one. The wiki lists coconuts, blowtube, dynamite and shield. Individual item routes remain open. |
| Hazards and retries | traced | $989F sets the late-fall flag. $C3AC dispatches the scripted actions, $BCFC saves restart state and $8C23 reloads it. $C344 handles the game-over display. |
| Pause, resume and quit | confirmed | A live Commodore press reached $8BAB, fire reached $8BC1 and RUN/STOP while paused reached $8015. |
| Sound | confirmed | The live title capture reached $E003 thirty times in thirty frames and wrote SID registers. |
| CTRL music toggle | open | The manual documents CTRL. The CIA1 access census and the direct keyboard loops at $8B9F and $8BAB did not resolve its path. |

## Sources

- Gremlin Graphics instructions, consulted 19 November 2026. [Instruction sheet](https://uta.pokefinder.org/Ultimate_Tape_Archive/Jack_the_Nipper_II_in_Coconut_Capers_%281987_Gremlin_Graphics%29_%5B1308%5D/Extras/Instructions.pdf)
- C64-Wiki, consulted 19 November 2026. [Jack the Nipper II – Coconut Capers](https://www.c64-wiki.com/wiki/Jack_The_Nipper_2)
