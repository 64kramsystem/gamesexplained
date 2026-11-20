# Who Dares Wins features

| Feature | Status | Evidence |
|---|---|---|
| Title, author credit and score panel | confirmed | `$1613` prints the credits and `$4DF5` draws the HUD. See [title](reference/title.png) and [play](reference/play.png). |
| Joystick movement and start | confirmed | Port 2 fire starts the game from `$1653`. The direction path reads the same port at `$1939` and indexes signed movement tables. |
| Tap to fire, hold to throw | confirmed | Instruction probes distinguish the edge at `$1C16` from the held-fire threshold at `$1D52`. The stock store at `$1D6B` spent one grenade. |
| Ammunition boxes | traced | `$4287` spawns the box and `$422F` adds a timer-derived amount on contact. Initial stock is six at `$15C2`. |
| Eight fields and garrisons | confirmed | The resident map at `$5000` contains eight garrison row commands. An isolated row probe traced the `$FF` command through the patched jump and the threshold store at `$4B3C`. Garrison clearance is traced at `$174D–$175E`. |
| Return to the first field | traced | The area-eight branch at `$17B3` resets the map pointer and draws the victory message. The shared transition raises three spawn and reserve settings up to a cap. |
| Troops, obstacles and vehicles | traced | The map dispatcher at `$1AB1` reaches the gunner, launcher, vehicle, bike and captive routines. Terrain flags at `$1F00` drive movement, priority and sinking. |
| Catalogue of named scenery | open | The `$3800` glyph render and `$5000` map identify terrain codes and recurring silhouettes. The inlay's names for every bridge, trench, mountain and sandbag variant have no full cross-reference. |
| Prisoners and bonus points | traced | `$480E` grants 750 for freeing the captive and its paired guard has a separate 50-point value. The score tables and hit paths account for the garrison controller's 1,250 rifle award and 250 blast award. The inlay's wording for the 250-point hill award remains open. |
| Three lives and extra men | traced | `$1675` sets three initial lives, `$4681` spends one, and `$42D0` implements the extra-life threshold. |
| Music and effects | confirmed | The two title music pointers and a music-command read were traced live. `$13A7` updates the SID voices for the tune and gameplay effects. |

## Sources

- [Alligata cassette inlay](https://www.gamesthatwerent.com/wp-content/uploads/gtw64/w/who-dares-wins/WDW-improved-cover.jpg), read 20 November 2026.
- [GTW64 preservation entry](https://www.gamesthatwerent.com/gtw64/who-dares-wins/), read 20 November 2026. The [gallery screenshot](reference/gtw64-screenshot.jpg) comes from this entry.
