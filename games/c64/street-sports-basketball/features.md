# Street Sports Basketball features

| Feature | Status | Evidence or question |
| --- | --- | --- |
| Four courts | live | The court menu offers School, Alley, Suburbs and City, with a preview. The manual calls City a parking lot. |
| Court hazards | open | The file G–J maps feed the ball and actor contact dispatchers at $3C63 and $411D. The oil-slick and curb names have not been matched to individual map cells and handlers. |
| Human or computer opponent | live | The opponent menu shows Human and Computer. |
| Three computer skill levels | live | Menu $1616 writes the selected option. Match $121D reads it and indexes the threshold values at $139C. Index two also remaps the opposing roster parameters at $1D12. |
| Green and blue teams with editable names | live | A controller claims green. Both name prompts accept the default with fire and show instructions for typing a replacement. |
| Coin flip and alternating draft | live | The winner gets first pick. After each selection the menu hands the turn over, and each side fills three slots. |
| Ten distinct players | live | The draft shows ten portraits and biographies. Controlled reads at $2069, $205A, $5184 and $6640 confirm separate roster-indexed movement, ball-carrier speed, velocity variation and vertical launch fields. |
| Play or restart the selection | live | The completed draft offers Play Game and Start Over. |
| Choose the target score | confirmed | A right press reached the BCD store at $164C and changed 20 to 22. |
| Move the controlled player | live | The port paths at $1FC6 and $1FDC feed the direction nibble to $1FF2. In a controlled entry, right reached $2086 and wrote the high X velocity byte for slot one. |
| Change selected teammate without possession | live | The counter at $222D invokes the slot cycle on the third fire detection while the controlled actor lacks possession. A controlled entry selected slot three from slot one and latched the counter at $80. |
| Jump to interrupt a shot or pass | open | The pose dispatcher and launch velocity table are traced. The precise defensive tap-to-jump and interception conditions were not matched to one observed input path. |
| Steal by approaching the dribbler head-on | open | The close-pair test at $45FA and the loose-ball recovery heading matrix at $4B1F are distinct paths. The manual’s facing condition for stealing has not been isolated. |
| Dribble, pass, jump shot, hook and dunk | open | The pose dispatcher at $5B94 chooses placement and release handlers, and $508E derives a ball velocity for the chosen target. Controlled calls checked pose dispatch and follow-through choices. Mapping every manual move name to its complete input and state condition remains open. |
| Two points per basket and a running score | traced | The score routine adds two in decimal mode at $558F. The forced award-phase check reached the store at $55B0. The shot-to-award path remains open. |
| End at the target or use RUN/STOP plus RESTORE | traced | $1694 compares both BCD scores with the target and enters the winner path. Match setup points the NMI vector at $0E85. The RUN/STOP plus RESTORE sequence itself was left open after tracing the match vectors and return stub. |
| Rematch with the same teams or start again | traced | The Yes/No path at $174A tests $07AE at $17AD. It jumps to match initialization for Yes and the reload stub for No. The latter reached KERNAL LOAD with the wildcard M name. |
| Music and sound cues | live | The selection IRQ enters the three-voice player at $E000. A controlled title check stepped a note-frequency load. The match IRQ dispatches the effects at $270E and $288B, with voice 1 frequency stores checked at $27F4 and $2811. |

## Sources

- [Epyx instruction manual](https://evercade.info/wp-content/uploads/2023/02/Street_Sports_Basketball_-_1987_-_Epyx_Inc..pdf), read on 20 November 2026.
- [REG-Vault C64 screenshots](https://regvault.org/game/c64/street-sports-basketball), consulted on 20 November 2026.
- Court selection and the draft were observed on the XPB disk in VICE. The emulator captures are in [reference](reference/).
