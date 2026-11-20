# The Real Ghostbusters features

| Feature | Status | Evidence |
| --- | --- | --- |
| One- or two-player start | live | The title shows “PRESS 1 or 2”. One player starts the Stage 1 loading prompt. |
| Stage transitions | live | Selecting one player leads to “Press any key to continue”. The first stage loads from disk after that prompt. |
| Stage HUD | live | The first stage displays a ghost count, score, time and stage number. |
| Joystick input and fire hold | live | The stage polls the two ports separately. A stopping checkpoint at `$1C96` recorded the five-poll hold threshold for player zero on port 2. |
| Ending screen | live | Loading LEVELK through the stage selector displayed the congratulatory picture. |
| Short and held fire | live | Breakpoints at `$1FAC` and `$1F65` distinguish the two resident actor types. See the input sampling section of [facts.md](facts.md). |
| Animated map tiles | live | Store watchpoints in LEVELA through LEVELI confirmed writes to the playfield character set from each stage’s animated glyph data. |
| Music and sound effects | live | The title selects a three-voice pattern sequence. The initial fire press in Stage 1 loads effect preset three into voice three. |
| Ghost counter and capture | traced | The resident overlap path at `$24AD` increments the selected player’s ghost count at `$85`. The update first selects the player from the other actor’s parent field, then tests the overlap at `$23D6`. |
| End-of-stage bonus | live | The interlude at `$3CCB` runs the meter update at `$3A6B`. In a controlled exchange at `$3B96`, the watchpoints caught the fiftieth ghost adding a life and clearing the credited count. |
| Stage actors | live | Each overlay installs its own actors and callbacks. Controlled checks confirmed the linked actor initialization in LEVELB and a fixed-slot initializer write in LEVELE. |
| Two-player state | traced | The title’s keyboard test enables the second player at `$29BE`. The resident selectors set the actor slot and persistent-state offsets to zero and zero, or one and `$11`. Fire and movement read separate joystick values. |

The publisher and program credits are from the game's C64 title screen. The disk edition is archived as [Activision release cracked by OUG](https://archive.org/details/Real_Ghostbusters_The_1989_Activision_cr_OUG_t_2_OUG).
