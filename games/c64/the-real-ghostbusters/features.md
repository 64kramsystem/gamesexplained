# The Real Ghostbusters features

| Feature | Status | Evidence |
| --- | --- | --- |
| One- or two-player start | live | The title shows “PRESS 1 or 2”. One player starts the Stage 1 loading prompt. |
| Stage transitions | live | Selecting one player leads to “Press any key to continue”. The first stage loads from disk after that prompt. |
| Stage HUD | live | The first stage displays a ghost count, score, time and stage number. |
| Joystick input and fire hold | confirmed | The stage polls the two ports separately. A stopping checkpoint at `$1C96` recorded the five-poll hold threshold for player zero on port 2. |
| Ending screen | live | Loading LEVELK through the stage selector displayed the congratulatory picture. |
| Ghost capture, weapons, bonuses, enemy behavior and multiplayer rules | open | The stage HUD establishes a ghost counter. The rules that update the counter and the other mechanics still need tracing. |

The publisher and program credits are from the game's C64 title screen. The disk edition is archived as [Activision release cracked by OUG](https://archive.org/details/Real_Ghostbusters_The_1989_Activision_cr_OUG_t_2_OUG).
