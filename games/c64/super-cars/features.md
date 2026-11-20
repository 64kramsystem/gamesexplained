# Features

| Feature | Status | Evidence or question |
|---|---|---|
| Top-down scrolling races against other cars | confirmed | The Track 1 race and HUD are visible in reference/race-steady.png. $0B22 follows the player and $21E2 positions the car sprites. |
| Courses, lap targets and increasing opposition | confirmed | $9C40 and $7F8D each hold nine pointers. Track 1 starts with four cars and a displayed five-lap target. $1642 and $1667 raise car and lap counts on class selection. |
| Joystick steering and acceleration | confirmed | $054B samples port 2. Controlled stops at $0553 distinguish all five inputs. Held fire reaches the player acceleration store at $26B9. |
| Front and rear missiles | traced | $2388 and $23A7 test the bought-item flags and space in the missile slot. The direction offset is zero or eight. |
| Space pauses and Q leaves the race | confirmed | Verified at $1C94, $1CA6 and $1E19. Q reaches the results transition at $1C78. |
| Track hazards, tunnels and arches | traced | $3D0E applies covered-area flags and $397F distinguishes surface types five and six. The material names for those values remain open. |
| Garage service and performance parts | traced | $180A–$1889 handles purchases, $1ACE assembles prices and $1F72 reads the steering, turbo and speed upgrade flags. The sprite sheet shows the item labels. |
| Sales office, car choices, prices and trade-in | confirmed | The office and balance appear in reference/menu.png. $1316 computes the trade-in and $127C tests the adjusted price. Seven variant records span $7384–$7471. |
| Starting balance | differs | £20,000 in the analysed Airwolf build with the default trainer selection. The wiki describes £5,000. |
| Price negotiation | differs | The office text at $7532 says negotiation is unavailable in this version. The traced purchase path computes a fixed amount from the variant and trade-in. |
| Name entry and class codes | confirmed | Name input through the CIA keyboard matrix reaches the sales office. The special-name comparisons are at $15DB–$1608 and the code text starts at $772F. |
| Persistent score table | open | The documented name screen precedes the sale menu. The string sweep and searches of the resident results path and KERNAL disk entry points found no corresponding persistent score table. |
| Music and race sound | traced | $EC7F services the resident sequence player. With trainer race music off, $FE02 services race audio requests and the player-speed engine parameter. |

## Sources

- [Super Cars – C64-Wiki](https://www.c64-wiki.de/wiki/Super_Cars), read 20 November 2026. Its overview may incorporate mechanics from other platforms.
- [Super Cars – Lemon64](https://www.lemon64.com/game/super-cars), read 20 November 2026 for release, credits and controller port.
