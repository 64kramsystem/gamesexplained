# Features

| Feature | Status | Evidence or question |
|---|---|---|
| Title and high-score table | live | The title screen displays seven entries and prompts for fire. |
| Start with joystick fire | live | Port 2 fire enters the first round. |
| Side-scrolling stages and bosses | traced | The four loads use local section counters. Load A’s $3358 processes the large enemy’s hits and defeat. |
| Walk and jump | confirmed | The engine checks left and right before testing the wall cells. Port-2 Up reached the jump branch at $190B and stepping the store set vertical velocity to $FD. |
| Crouch | open | The C64 joystick diagram assigns Down to crouch with fire released. The shared movement routine tests Up, Left and Right, and the sword routine uses Down to select an attack. A separate crouch path in the stage overlays remains open. |
| Aim with the joystick while holding fire | traced | $19BD looks up attack direction from the active-low joystick bits and jumps to the selected weapon routine. |
| Sword, shuriken, bombs and blade on a rope | traced | Four callback lists at $1521, $216E and $2176 drive weapon action, tiles and hits. |
| Space selects weapon and P toggles pause | confirmed | Space reached the matrix comparison, and stepping the store changed the weapon index at $25D2. A matrix P hold reached the pause comparison at $1039 with A=$FD. |
| Shadow doubles | traced | Pickup handler $1407 allocates up to two copies. $14F4 and $153E replay earlier player states. |
| Lives, score, high score and timer | confirmed | HUD routines draw the indicators. The timer probe took 2:00 to 1:59 and sent 0:00 to the death path. $0FB0 updates the packed decimal score and $0899 handles insertion into the high-score table. |
| Enemy contact costs a life | traced | $1474 detects an overlap and enters $1219. Load A’s $28C7 handles respawn and life expenditure. |
| SID music and effects | traced | $A287 and $A543 advance effects and music from the HUD interrupt. The tune and note tables are in the engine listing. |

## Sources

Read on 19 November 2026.

- [Ninja Spirit – C64-Wiki](https://c64-spielefuehrer.c64-wiki.de/wiki/Ninja_Spirit)
- [Activision instruction booklet, including C64 controls](https://www.gamesdatabase.org/Media/SYSTEM/Sinclair_ZX_Spectrum/manual/Formated/Ninja_Spirit_-_1990_-_Activision.pdf)
- [Title](reference/title.png) and [Round 1](reference/round-1.png), captured from the DCS disk release.
