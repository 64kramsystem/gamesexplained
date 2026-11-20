# Features

| Feature | Status | Evidence |
|---|---|---|
| Title screen, animated characters and fire prompt | live | Title screenshot. |
| Select Hyde Park, the Ice Caverns of Freezia, the Forests of Vegetablia, or the Atomic Mud Mines | live | Level selection screen and initial gameplay snapshots. |
| The Fat Guy's headquarters | traced | Fresh menu shows the locked entry in blue. $0A66 enables it, and $14AD writes that flag on the campaign continuation path after the Mines. The fifth overlay was captured with a directed loader argument. |
| Story panels entered between disk load and Hyde Park gameplay | live | Fire advanced the panels one at a time. |
| Score, ammunition and lives displayed below the playfield | live | The Hyde Park screenshot shows a six-digit display and three icon groups. The exact assignment of the groups awaits code evidence. |
| Movement, climbing, jumping and ducking | open | Joystick controls described in the manual. |
| Shoot and use a charge | confirmed | Fire plus up and fire plus down hit separate ammunition-store instructions in Hyde Park. Exact traces are in facts.md. |
| Slide a charge and attack at close range | open | Manual. |
| Enemies, traps, extra ammunition and bonus areas | open | Manual and C64 reference guide. |
| Death, retry, game over and high-score initials or name entry | open | Game-over and name-entry text found at $056D and $0663 in the title image. |
| Attract demonstration | traced | DEMO MODE at $5155. At $343D the engine reads virtual joystick and duration pairs when demo mode is active. |

## Sources

- MicroProse's 1990 multiplatform [Rick Dangerous II manual](https://www.retrogames.cz/manualy/DOS/Rick_Dangerous_2_-_DOS_-_Manual.pdf).
- [C64-Wiki game guide](https://www.c64-wiki.de/wiki/Rick_Dangerous_II).
- PAL screenshots taken in VICE. See `reference/`.
