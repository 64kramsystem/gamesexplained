# Kendo Warrior features

| Feature | Status | Evidence |
| --- | --- | --- |
| Title, credits and demo actor | confirmed | The Byte Back logo and title appear before play. `$0DA9` draws the title and `$0E3A` scripts the actor. See [title](reference/title.png). |
| New operative | confirmed | Play opens on an industrial corridor with an initial operative count of four. `$3A31` initializes the count and `$3C12` displays it. See [play](reference/play.png). |
| Movement | confirmed | The C64 dispatch selects walking, a jump, a somersault, crouching or a roll from the direction bits. Checkpoints at `$2780` observed the five action IDs with fire released. |
| Combat | confirmed | Fire with right, up-right, down-right or down selects action IDs six, seven, eight and nine at `$2780`. The action tables supply the animation and `$2CE5` handles player attack contact. The complete series of opposition attacks is traced at `$37F5`. |
| Exploration | traced | `$20DA` draws forty tiles per room and `$24BD` consults the four-way room graph at `$25BE`. The entry room is observed. The entire room graph was read from the table. |
| Inventory and tools | confirmed | The I-key branch at `$2730` changes on a live matrix read. Item placement and interactions are traced at `$10B6` and `$1596`. |
| Coloured barriers | confirmed | The controlled tests at `$1182` consumed one matching shield and selected the crossing action. With zero matching shields the same test selected the hit action. |
| Coded safe | traced | At `$1616` the code starts the manual or sequencer attempt. `$141C` handles progress, lockout and document acquisition. No route to the safe was required for these checks. |
| Helicopter extraction | traced | `$197F` checks roof room `$3F` and the documents flag before the encounter and pickup sequence. No completion route was required for these checks. |
| Health and defeat | confirmed | Four boundary values passed the live test of the sixteen-cell energy bar at `$3C42`. Hit handling, the operative decrement and game over are traced at `$3C65`, `$3B0B` and `$3B94`. |
| Music and effects | traced | The raster driver at `$BBFF` reads tune and effect requests. It uses four tune descriptors and eight effect streams. VICE used dummy audio for this run. |

## Sources

- [C64 documentation hosted by Lemon64](https://www.lemon64.com/doc/kendo-warrior/1024), consulted 20 November 2026.
- [Byte Back instructions, Spanish edition](https://spa2.speccy.org/Instructions/k/KendoWarrior%28MCM%29.pdf), consulted 20 November 2026. The joystick chart supplies leads for C64 checks.
- [MobyGames objective and item summary](https://www.mobygames.com/game/61469/kendo-warrior/), consulted 20 November 2026.
- [AL82 C64 longplay](https://www.youtube.com/watch?v=tMutzwGZcEY), description consulted 20 November 2026.
