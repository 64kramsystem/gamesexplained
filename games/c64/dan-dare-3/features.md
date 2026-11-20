# Features

| Feature | Status | Evidence or question |
|---|---|---|
| Title and configurable controls | live | Title offers Y/N to redefine keys and fire to start. Defaults are O, P, Q, A and Space. |
| Escape from the cell | live | First room shows Dan beside a terminal with a rifle selected. |
| Walking and jet-pack flight | confirmed | Stopped at the rightward increment and thrust decrement, then single-stepped each. The fuel-consumption timer is traced. |
| Inventory and weapons | live | Space reached the rifle handler and incremented the charge counter. A controlled select edge started the switch to bouncing bombs at $7C8A. The bouncing and timed screen-effect item handlers are traced at $628E and $6263. |
| Terminals and resupply | live | $6382 draws the terminal menu. In a controlled purchase, the $64E4 store added ten bouncing bombs for 150 units. The affordability check rejected a balance of 149. |
| Mutants, damage and respawn | live | Entity callback type $28 reached $3B6F in a controlled dispatch. Watches identified the death countdown and life decrement. On expiry, $1F23 selects gauge reset or the title-return delay according to the remaining lives. |
| Transport tunnels | traced | $1910 chooses the destination and runs the transition at $1993. The transition samples direction and updates moving objects. The exact wall-damage conditions and natural routes remain open. |
| Escape fuel and timed chamber destruction | traced | The escape action at $642B branches to the ending only when $7C17 is five. Controlled tests exercised the four- and five-unit cases. The countdown at $1993 belongs to the transition loop. The manual’s chamber destruction trigger remains open. |
| Pause | live | A breakpoint confirmed that RUN/STOP enters the wait at $2F59 and that the released input returns at $2F6F. |
| Music and effects | live | Instruction checkpoints caught title order and pattern reads and the gameplay SID relocation. A request test caught the priority decoder setting the voice-zero queue at $9060. The captures used dummy audio. |

## Sources

- [Dro Soft manual, C64 controls on page 6](https://spa2.speccy.org/Instructions/d/DanDareIII-TheEscape%28DroSoft%29.pdf), consulted 19 November 2026.
- Emulator reference captures [title](reference/title.png) and [opening cell](reference/cell-start.png).
