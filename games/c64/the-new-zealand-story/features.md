# Features

| Feature | Status | Evidence or question |
|---|---|---|
| Title and setup | live | The title offers Start Game, music, joystick or keyboard control, and credits. Port 2 fire starts a game with the default selections. |
| Rescue | traced | Resident $0A5A places the captive when its coordinates fall within the screen window. $96AB steers the player on contact. $0A00 and $0A09 handle progression. Direct loader routes exercised the five disk worlds. |
| Movement and combat | confirmed | Compared identical Auckland snapshots with no input, up, and fire. Port 2 reads at $50CA reached $1613/$1651 for a jump and $1675 for a shot. $16D9 selects a trajectory from the equipped weapon. |
| Flying | traced | $14EE checks overlap from above or below and attaches a rideable object. $1562 identifies its kind, and the rider enters the controls at $0EC0. The mounted path was read in the listing. |
| Swimming | traced | $0ABA switches motion state using the terrain probe. It calls the six-character status updates at $9E4A. The relevant tile and state tests are in the resident listing. |
| Pickups | traced | $2AC1 chooses a letter, $2ACA advances the collected-letter counter, and $978A updates colors and grants a life. The score update entry is $8793. |
| Enemies and traps | traced | $41BE expands the world object lists. $2C08 animates portal activation. $36D8 selects hostile shot trajectories, and $4ADA selects four of the world boss attack routines. |
| Status panel | live | The first round shows score, high score, credits, life icons, a timer and an empty inset. |
| Failure and retries | traced | $0BDD runs the falling death display and tests the life state. $0864 and $5B61 return the engine to the first world when the title needs to be restored. |
| Music and effects | confirmed | $6E5E selects three voice-order streams. $6EF9 ran on 96 of 96 tracked Auckland frames. The title toggles audio type at $9014. The complete tune and effect inventory is open. |
| Hidden lives cheat | confirmed | The sequential title checker at $9078 enables $0628 after 25 keys. The final-key VICE trace confirmed the flag and border change. $0C8A tests the flag before subtracting a life. The different chord reported by C64-Wiki remains open after searching the flag writes and the title matrix checker. |

## Sources

- [The Newzealand Story, C64-Wiki](https://www.c64-wiki.com/wiki/The_Newzealand_Story), accessed 20 November 2026.
- [The Newzealand Story, Lemon64](https://www.lemon64.com/game/newzealand-story), accessed 20 November 2026. Documents joystick port 2 and the collection disk.
- [The Newzealand Story, C64Games.de](https://www.c64games.de/phpseiten/spieledetail.php?filnummer=120), external screenshot.
- The title and round 1-1 screenshots in `reference/` come from the Rainbow Collection G64 in PAL VICE.
