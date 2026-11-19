# Features

| Feature | Status | Evidence or question |
|---|---|---|
| Title and configurable controls | live | Title offers Y/N to redefine keys and fire to start. Defaults are O, P, Q, A and Space. |
| Escape from the cell | live | First room shows Dan beside a terminal with a rifle selected. |
| Walking and jet-pack flight | confirmed | Stopped at the rightward increment and thrust decrement, then single-stepped each. The fuel-consumption timer is traced. |
| Inventory and weapons | confirmed | The rifle handler was reached with Space, and a watchpoint caught its charge counter increment. Equipment selection and rifle stock are traced. Other weapons remain open. |
| Terminals and resupply | traced | The menu code at $6382 prints the terminal stream at $65E6. The manual specifies a store terminal for bombs. Individual purchases remain open. |
| Mutants, damage and respawn | open | Manual describes energy loss on mutant contact and a return to the start after energy loss. |
| Transport tunnels | open | Manual describes steering through tunnels and energy loss on touching their walls. |
| Escape fuel and timed chamber destruction | open | Manual warns that leaving a chamber without collecting the fuel can strand Dan. |
| Pause | open | The C64 section of the manual specifies RUN/STOP. |
| Music and effects | traced | $2307 switches between two audio entry points and $9041 selects a requested effect by channel and priority. Tune inventory remains open. |

## Sources

- [Dro Soft manual, C64 controls on page 6](https://spa2.speccy.org/Instructions/d/DanDareIII-TheEscape%28DroSoft%29.pdf), consulted 19 November 2026.
- Emulator reference captures [title](reference/title.png) and [opening cell](reference/cell-start.png).
