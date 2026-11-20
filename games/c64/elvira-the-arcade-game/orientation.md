# Elvira: The Arcade Game on C64

## Media and machine

The input is `work/Elvira_-_The_Arcade_Game_(L).d64` from the [C64Games disk archive](https://www.c64games.de/phpseiten/spieledetail.php?filnummer=697). SHA-256 is `4d80492d57be3b80dffbc1fd288d0e05cce7a5feb6296ba8775e39cc74859776`. The reader found 174,848 bytes in 683 sectors with a 1541 directory and no allocated, unowned sectors. This is a plain D64 sector image.

The machine was PAL x64sc, VICE MCP v3.14.0 for macOS arm64, headless with the dummy sound device. The emulator check reported 56 passes. Host key names and the optional quirks probe failed. Matrix keys, frame stepping, execution checkpoints and read/write watchpoints passed. The server and Regenerator2000 answered on ports 23016 and 23018 respectively.

## Boot and world routes

1. Autostart the disk. Wait for the Sharks intro and press Space. Advance through both Legend screens with Space once each. The wait for the first unpack can be several seconds. On the green Fletch and Doc trainer both unlimited options read NO. Press F7 without changing the two settings.
2. At the language screen press 1 for English. Wait through the opening screens until the globes show FIRE TO START. Press fire on control port 2. The saved title and pointer states are `work/opening.vsf` and `work/selection.vsf`.
3. For Fire, move the pointer left and down until the caption says ENTER THE FIRE LEVEL. For Ice move right and down until it says ENTER THE ICE LEVEL. From the saved pointer state, 73 frames of left and 28 of down reached the Fire hotspot. The Ice hotspot was reached with 40 frames of right and 28 of down.
4. Press joystick fire to open the difficulty line, then key 1. Wait for the world illustration. Press fire again and wait for PRESS SPACE TO START QUEST. Hold Space for 12 frames and advance a further 35 frames to capture play. The loading waits vary by world and can take thousands of emulated frames. Warp speeds up the waits.
5. To capture Castle, restore `work/play-ice.vsf` on the same disk, set `$094F=$FF`, `$094E=$01`, and `$07FF=$01`, then run the normal game loop. The `CL` interlude appears. Advance it with joystick fire and the following quest prompt with Space as above. This is a debugger route that reaches the game’s own load path.
6. From `work/play-castle.vsf`, set `$094F=$FF`, `$094E=$0A`, and `$07FF=$01`. Run the main loop until the congratulatory picture appears. This is a debugger route to the WIN load.

## Captures and disk mapping

| Part | File or files | Capture in the part’s `work/` |
|---|---|---|
| Language and title | `ELVIRA+2    /NEI`, autostart | `entry.vsf` at $12ED and `language.vsf` at language selection |
| Opening | `OPEN` | `entry.vsf` at $0840 and `selection.vsf`, globe pointer active |
| Fire interlude | `HL` | `entry.vsf` at $1800 and `interlude.vsf` |
| Fire | `G1B`, `G1A` | `entry.vsf` at $0812, `quest.vsf` at the prompt and `play.vsf` |
| Ice interlude | `IL` | `entry.vsf` at $1800 and `interlude.vsf` |
| Ice | `G2B`, `G2A` | `entry.vsf` at $0812, `quest.vsf` at the prompt and `play.vsf` |
| Castle interlude | `CL` | `entry.vsf` at $1800 and `interlude.vsf` |
| Castle | `G3B`, `G3A` | `entry.vsf` at $0812, `quest.vsf` at the prompt and `play.vsf` |
| Ending | `WIN` | `entry.vsf` at $12ED and `ending.vsf`, congratulatory picture |

Searching the nine captures with aligned 16-byte blocks from each extracted file found no sustained match for the interludes, quest pairs, opening or ending. The boot file had seven windows at the strongest candidate offset, with only 324 of 24,196 bytes matching there. The matching output and extracted files are local in `work/`. The table uses the runtime requests and entry points for the packed loads. The separately runnable BASIC release note and the directory entries that point to the BAM are described in `media.json`.

The boot depacks before the language selector. The selected globe requests a picture interlude. That interlude runs its own interrupt and requests the B file through the call at $0825, moves loaded pages upward, and jumps to LOAD at $0875 for the A file with a synthetic stack return to $0812. Execution stops at $FFD5 showed each pair of world filenames in that order. The engine can re-enter the loader to play a further interlude, return to OPEN, or load WIN.

In play the hardware IRQ vector under the KERNAL at $FFFE contains $13D5. The Fire snapshot held $1C0E at the software IRQ vector $0314 and $3B49 at the hardware reset vector. The raster IRQ banks I/O in for register access and restores the saved processor port on exit. A store watch on $D011 stopped at $1489 immediately after the HUD split wrote $7F. The three quest entries were captured before their own setup ran. The three interludes, opening and ending also have hand-over captures. After F7 at the trainer, the loader copy runs at $7D03. Single-stepping its jump at $7D1E entered the language setup at $12ED. The earlier $1669 capture remains in `work/early.vsf`. The per-part ledgers record the authored ranges and explain exclusions using the hand-over captures, load writes and targeted instruction traces.
