# Supertrux — features

| Feature | Status | Evidence or question |
|---|---|---|
| One driver, joystick in port 2 | live | Fire in port 2 starts play from the title map. |
| F1 quits, F3 pauses | traced | F1 follows the restart path at $14C6. The F3 store at $14DC was single-stepped in VICE and set the pause latch to $01. |
| Race between European cities against a clock | traced | The route uses six-character labels at $1639 and sets the stage clock with opcode 8 at $2993. |
| Road signs and alternate routes | traced | $28E8 installs the stored routes and signs, and $2891 selects a branch using truck X. |
| Narrow lanes, bends and roadworks | traced | Elite describes these hazards. The course stream per-distance opcode classes stage obstacle groups at $2944 and change the edge tables at $285B and $28E8. |
| Rival trucks and contact | traced | $215F chooses and projects a rival. $1E7B tests proximity to the player. |
| Air horn | open | Elite invites the driver to sound it. The controller latch references and the three direct calls to $F3CE show movement, menus and collision/light effects. A C64 horn trigger remains open. |
| Stage scenery and in-race display | confirmed | The descriptor table at $7C00 selects scenery and roadworks graphics. The HUD, gantry and road are visible in the London start capture. |
| Title music | confirmed | $F410 initializes the three pattern streams. A hardware watchpoint counted 951 SID register stores over 50 title frames. |
| Accelerate and brake with Up and Down | traced | $1D1C adds the speed-band step when Up is held and its store was single-stepped in VICE. $1D39 subtracts the braking step for Down. |

## Sources

- [Supertrux, Lemon64](https://www.lemon64.com/game/supertrux), consulted 20 November 2026.
- [Elite Systems catalogue description, Retro Isle](https://www.retroisle.com/general/publishers/Elite%20Systems/softography.php), consulted 20 November 2026. This describes all three home computer releases.
- [Power Play 5/89](https://acpc.me/ACME/LITTERATURE/REVUES/%5BGER%5DGERMAN/%5BGER%5D%5BMULTI%5DPOWER_PLAY/POWER_PLAY_1989_05.pdf), consulted 20 November 2026.

## Reference frames

- [Elite loading picture](reference/loading.png)
- [Title map and control legend](reference/title.png)
- [London start and HUD](reference/london-start.png)
