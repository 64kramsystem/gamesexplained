# World Class Leaderboard on the C64

The two D64 sides are from the Nostalgia release hosted by [C64 Online](https://c64online.com/c64-games/world-class-leaderboard/). The hashes and directory entries are in [media.json](media.json). Side 1 contains the boot program, the separate documentation program and the packed GAME file. Side 2 contains the demo, practice data and files for the advertised A–P course selection.

1. Hard-reset the PAL C64 and autostart the first file on side 1 in drive 8.
2. At the Nostalgia screen, hold port 1 fire for 20 frames and release. Wait for the globe title, then press port 1 fire again.
3. At TURN THE DISK, attach side 2 in drive 8. Press port 1 fire. Wait for the player count prompt on the Cypress Creek scoreboard.
4. Enter 1, wait for the name prompt, enter SAM followed by Return, then enter K for Kids. At the round-length prompt, press F1 (keyboard matrix row 0, column 4) for 18 holes.
5. Wait for the first tee to finish drawing. Pause before swinging. The snapshot is `parts/engine/work/play.vsf`, saved without ROM or disk images.

At the tee the CPU was at $0E72. The play display is a multicolour bitmap in VIC bank $4000, with screen matrix at $6000 and bitmap at $4000. The loader and the gameplay program use different addresses. The boot intro hands off on port 1 fire, and the game asks for the swap to the course disk before setup.

## Part snapshots

- **Engine.** `parts/engine/work/entry.vsf` is the course-list prompt before the side swap. `parts/engine/work/play.vsf` is the first-tee snapshot used for the engine listing. The resident entry and the packed sprite source matched between these captures.
- **Printer.** Starting from the first-tee snapshot, leave side 2 attached and set PC to $BA56, the branch that handles confirmation of the print prompt. Set an execution checkpoint at $6800 and resume until it fires. Save `parts/print-scorecard/work/entry.vsf`. Step three instructions to $6810 and save `parts/print-scorecard/work/print.vsf`, the listing snapshot. This isolates the loader and printer entry. It bypasses the end-of-round gameplay route.
