# Shinobi (C64) features

## Sources

- [Shinobi manual](https://www.cpc-power.com/extra_lire_fichier.php?extra=notice&fiche=1926&part=B&slot=1&type=.pdf), English pages 2–3, consulted on 20 November 2026.
- [Lemon64 game entry](https://www.lemon64.com/game/shinobi), consulted on 20 November 2026, for release credits, port and player count.
- `reference/attract.png` and `reference/mission1.png` show the fire prompt and the first playable street in the X-Large release.

| Feature | Status | Evidence or question |
|---|---|---|
| Five missions, with multiple stages and a boss in each | traced | The resident loader builds the file name using the mission number. Controlled stage entry showed all five first stages in play. Later stage transitions and boss rules are open. |
| One or two players | live | The attract prompt shows one player, and the HUD has both score positions. The mode selection and handoff rules are open. |
| Movement | open | The manual describes a turn followed by walking, crouching and jumping. |
| Weapons and close attacks | traced | The active-low fire bit feeds the two-slot projectile launcher at `$2413` and the close-range test at `$B862`. A store watch confirmed the left-facing launch offset. The conditions for each weapon form remain open. |
| Platform changes | open | The manual describes combining fire with up or down to change height. |
| Ninja magic | open | The manual assigns magic to Space and states a one-use limit per level. |
| Pause and player colour | open | The manual assigns pause to P and colour change during pause to C. |
| Rescues and upgrades | open | The manual describes passing children to rescue them, points for each rescue and upgraded weapons after enough rescues. |
| Timer and remaining-time bonus | confirmed | The HUD countdown matches the BCD timer and its 50-call divider. The points conversion remains open. |
| Bonus scene | traced | The main loop and target sprite renderer dispatch through separate tables. Execution stops confirmed one patched call from each table. The complete entry and reward rules remain open. |
| Ending and credits | traced | Mission 5 uses the split pointers at `$F87E/$F8A6` and column table at `$F8CE`. A store watch caught the first character of the ending narrative. |
| Life loss, retry and game over | open | Which counters and rescue flags survive a retry is open. |
| Music and sound | traced | Effect playback uses the entry at `$BD1B` and an updater at `$BD72`. The ending credits name Tiny Williams for loading music. Music playback and the game events that trigger individual sounds remain open. |

The message templates add entries for practice or demo, perfect and special bonus results, stage clear, and a prompt to retain Mission 1. Their entry conditions remain open. The attract handler traces left/right to one/two players and fire to the game setup. The keyboard loop traces separate colour changes while paused.
