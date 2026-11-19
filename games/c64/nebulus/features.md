# Nebulus features

| Feature | Status | Evidence or question |
|---|---|---|
| Eight towers with a timed climb and a door at each summit | traced | Eight layouts decoded and matched live at $B043. The timer and summit door are traced at $B673 and $AFA9. |
| Pogo stays near the center while the cylindrical tower turns | traced | The relative angle wraps in $9CDC. Projection and edge dispatch are in $C33E. |
| Joystick in port 2. Left and right walk, up enters doors, up and down use lifts | traced | CIA and direction outputs traced live at $AB85-$ABA7. Lift and door cell predicates traced at $AFBE and $AFA9. |
| Fire shoots from a standstill and jumps during lateral motion | confirmed | Stepped from the same tower snapshot into $917C with fire alone and $8F90 with right and fire. |
| Enemies, disappearing floors, ice, ledges and tunnels affect the climb | open | The cell predicates at $AFA9-$AFFD and object activation at $B166 trace distinct cases. The full assignment of enemy and surface names to the state handlers remains open. |
| Door at the top triggers tower destruction and a time and technique bonus | traced | Door completion path at $90BD, collapse at $943D and bonus panel at $8848. |
| Between towers the submarine shoots bubbles and collects captured fish | traced | Submarine scene initialized through $8305. Bubble and fish contacts are traced at $A769/$A7FF. |
| Title, game start and game over tunes | open | The title sequencer at $3959 and descriptor entry at $F0CA are traced. Mapping the game-start and game-over events to named tunes remains open. |
| One or two players, score and high-score table | traced | Title options and the two score buffers are traced at $89C0/$B5A1. Initials handling is at $8BD9. |

## Sources

- [Nebulus – C64-Wiki](https://www.c64-wiki.com/wiki/Nebulus), consulted 19 November 2026. Tower and underwater reference images in reference/.
- [Nebulus – Lemon64](https://www.lemon64.com/game/nebulus), consulted 19 November 2026. Release, controls and music catalogue.
