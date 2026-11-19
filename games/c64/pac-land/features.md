# Pac-Land features

| Feature | Status | Evidence or question |
| --- | --- | --- |
| Title and credit counter | live | The title shows both players' scores, the high score and credits. F1 adds a credit. |
| Start one player and show the ready screen | live | F3 starts Trip 1 after a credit. |
| Two-player mode and pause | traced | $074C spends two credits for F5. $0CD7 chooses the other player if they have lives and restores that player’s score and round. $7FAD handles F7. |
| Left, right and jump | confirmed | Steps through the CIA reads confirmed O, P, CTRL and joystick port 2. The zero key is neutral in the gameplay sampler. |
| Double-press to run | open | The manual says a second press in the same direction reaches top speed. |
| Scroll through town, forest and other terrain | live | Round 1 begins outside Pac's house with a separate lower panel. The reference gallery shows other settings. |
| Terrain obstacles | open | The manual lists hydrants, ravines, logs, moving platforms and clouds. |
| Vehicle ghosts and collisions | open | The manual describes ghosts driving cars and flying aircraft. |
| Power pills and ghost regeneration | traced | The contact path at $2851 sets $23 and requests tune 9. The $09B0 contact code uses that flag to switch from life loss to a capture effect. The colour and returning-eye behavior is open. |
| Fruit, bonuses and extra lives | open | The manual describes airborne fruit and bonuses for jumping onto objects. The wiki lists trip-specific fruit and scores. |
| Energy and pursuit | traced | $EA80 initializes the gauge, $EAB4 ticks it and $EB2B marks exhaustion. The $09B0 chase sequence tests the exhaustion and powered states. |
| Springboard and repeated input in mid-air | open | The manual describes alternating directions. The wiki describes repeated presses in the intended direction. |
| Fairyland, shoes and return home | traced | $0DCD dispatches different exit sequences by the round number modulo four. The shoe award and exact movement rules on the homeward leg remain open. |
| Four trips and sixteen rounds | confirmed | The data contains sixteen recipes and $0C6D wraps the map index to 1 while advancing the displayed round. The boundary instruction trace measured both values. |
| Music, sound effects and attract mode | traced | $B069 updates the SID, $B214 selects tunes and $B1DC starts effects. The title timeout calls the motion loop with the alternate control handler at $F306. |
| Q suicide and S/T/G speed input | open | Both are reported on the wiki. Establish whether they apply to this disk. |

## Sources

- [Pac-Land – C64-Wiki](https://www.c64-wiki.com/wiki/Pac-Land), read 19 November 2026.
- [Pac-Land instructions for the C64 disk release](https://www.lemon64.com/doc/pac-land/434), Project 64 transcription at Lemon64, read 19 November 2026.
- [Pac-Land history and reception](https://frameadvance.net/claims/pac-land-history/), including the contemporary Zzap!64 review and cassette instruction sheet, read 19 November 2026.
- [Commodore 64 screenshots](https://www.mobygames.com/game/13801/pac-land/screenshots/c64/), consulted 19 November 2026.
- Screens from the analysed disk are in `reference/title.png` and `reference/round-01.png`. [Round 5 image](https://www.c64-wiki.com/images/9/93/Pacland_1.JPG) is saved as `reference/wiki-round-05.jpg`.
