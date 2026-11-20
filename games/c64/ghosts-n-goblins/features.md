# Ghosts 'n Goblins (C64) — feature checklist

| Status | Feature | Evidence |
| --- | --- | --- |
| traced | Arthur sets out to rescue the kidnapped princess. | Stage wrap calls the ending at `$0DA1`. Its caption at `$0E0F` tells the player the princess was saved. |
| confirmed | Four playable stages: graveyard and forest, ice palace and town, clouds and fire bridge, labyrinth and castle. | `$3536` selects four starting rows and four encounter sets. The `$2F5A` instruction probes and the stage screenshots establish each opening. |
| confirmed | Walk, jump, crouch and throw with the joystick. | Port 2 input at `$2C54` produces signed steps and jump or crouch motion. Fire activates a projectile at `$2706`. |
| traced | Up and down climb a ladder when Arthur is next to a ladder tile. | `$2C8E` and `$2CED` test bit one of the tile flags through `$2653`. The ordinary-footing control probe supplied no ladder tile. |
| confirmed | Five initial lives, lance and a 2:59 stage timer. | `$087E`, `$08A5` and `$08BF` write the starting values. Live graveyard and timer checks show the timer running. The raster displays remaining reserve lives beside the active life. |
| confirmed | Contact strips the armor and starts a grace interval. | A watchpoint on `$3527` stopped after `$1168` stored `$80` and `$115F` had set the countdown. |
| traced | A later eligible hit can kill Arthur, using the midpoint as the restart if reached. | The frame base test at `$2DFB` selects death. `$0936` retries using origin and Y from `$3595–$3597`, which `$1FFB` can update. |
| traced | Stage encounters include zombies, flying enemies, plants and boss groups. Some enemies carry jars. | Encounter arrays at `$1E6E–$1FA9`, spawn table at `$1FAA` and update table at `$11BF`. The jar's parent link and fall are in `$1014` and `$1902`. |
| traced | Weapon and point bonuses emerge from landed jars. | `$1958` converts a landed jar, selecting bonus images through `$1995` or the next weapon through `$197B`. The five weapon indexes use the sprite and motion tables at `$26AC–$26BD`. |
| traced | Bosses have hit counters and can release a stage key. Key collection takes Arthur to the next stage. | `$1307` and `$1A23` count boss hits. The key starts at `$1B23`, is collected in `$144B`, and triggers the automatic movement in `$2C23`. |
| traced | Winning the final stage returns to the first. | `$091E` branches to the ending at stage index four and sets index zero afterwards. |
| confirmed | The panel shows time, score, weapon and lives. | Screenshot and raster capture. Code at `$2AEA`, `$0F28` and `$3243` writes labels, digits and sprites. |
| traced | High-score entry follows a qualifying score. The joystick selects letters, with an erase glyph and ED to finish. | Rank insertion at `$0949`, input at `$0C01`, custom keyboard at `$0B88`. |
| traced | Mark Cooksey's music and in-game sound effects use the SID. | The title credits Cooksey. `$3800` and `$3B14` choose music and `$C9B1` updates music and effects. Sound ran on VICE's dummy device. |

## Sources

- [Ghosts'n Goblins — C64-Wiki](https://www.c64-wiki.com/wiki/Ghosts%27n_Goblins), consulted 20 November 2026. Its graveyard and stage animations are in `reference/`.
- [Elite instructions in the C64Games.de manual archive](https://www.c64games.de/hugo.php?helpfiles=/g/ghosts_n_goblins_anl.zip), consulted 20 November 2026. The English sheet identifies the C64 disc command and joystick controls. The German guide specifies movement, jump, crouch, fire and high-score entry.
- The PAL disk's title and stage openings in VICE are in `reference/`.
