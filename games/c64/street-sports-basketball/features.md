# Street Sports Basketball features

| Feature | Status | Evidence or question |
| --- | --- | --- |
| Four courts | live | The court menu offers School, Alley, Suburbs and City, with a preview. The manual calls City a parking lot. |
| Court hazards | open | The manual mentions the alley oil slick and the suburban curb. Find the associated coordinate tests and their effects. |
| Human or computer opponent | live | The opponent menu shows Human and Computer. |
| Three computer skill levels | open | The manual lists Easy, Intermediate and Tough. Locate the differences in computer decisions. |
| Green and blue teams with editable names | live | A controller claims green. Both name prompts accept the default with fire and show instructions for typing a replacement. |
| Coin flip and alternating draft | live | The winner gets first pick. After each selection the menu hands the turn over, and each side fills three slots. |
| Ten distinct players | live | The draft shows names, portraits and descriptions. Any differences in the actual shot, speed and handling parameters remain open. |
| Play or restart the selection | live | The completed draft offers Play Game and Start Over. |
| Choose the target score | confirmed | A right press reached the BCD store at $164C and changed 20 to 22. |
| Move the controlled player | open | The manual describes movement in joystick directions and a lighter uniform for the selected player. |
| Change selected teammate without possession | open | The manual describes holding fire. |
| Jump to interrupt a shot or pass | open | The manual describes tapping fire on defense. |
| Steal by approaching the dribbler head-on | open | The manual describes a collision that depends on facing. |
| Dribble, pass, jump shot, hook and dunk | open | The manual describes movement with possession and firing while facing a teammate or basket. Find how the game chooses between these actions. |
| Two points per basket and a running score | traced | The score routine adds two in decimal mode at $558F. The forced award-phase check reached the store at $55B0. The shot-to-award path remains open. |
| End at the target or use RUN/STOP plus RESTORE | open | The manual documents both ways to end play. |
| Rematch with the same teams or start again | open | The manual describes a Yes/No prompt. |
| Music and sound cues | open | Identify drivers and their callers. |

## Sources

- [Epyx instruction manual](https://evercade.info/wp-content/uploads/2023/02/Street_Sports_Basketball_-_1987_-_Epyx_Inc..pdf), read on 20 November 2026.
- [REG-Vault C64 screenshots](https://regvault.org/game/c64/street-sports-basketball), consulted on 20 November 2026.
- Court selection and the draft were observed on the XPB disk in VICE. The emulator captures are in [reference](reference/).
