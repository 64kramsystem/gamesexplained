# Stormlord on the Commodore 64

The analysed image is [The Bonanza Crew's Stormlord +3](https://csdb.dk/release/?id=73842), an ordinary 174,848-byte D64 sector image. SHA-256 is `25f70bf484c32111325f53e6026033c88c7105427dd39c5fa7249109b88b5cff`. The directory has one PRG, `STORMLORD +++`, and zero allocated sectors outside the file and directory. The PRG is 38,519 bytes including its two-byte `01 08` load address. Its BASIC line runs `SYS 2051`.

## Rebuild the snapshots

1. Start the installed vice-mcp v3.14.0 macOS arm64 headless build on the assigned port with dummy audio. Hard-reset and autostart the D64. Wait for the trainer prompt. The first load took tens of seconds with the emulated disk drive.
2. Use the matrix input to press **N** for infinite lives, infinite time and removal of collisions. Release N between prompts.
3. For `work/entry.vsf`, stop at `$C000` after declining the collision trainer. This is the hand-over from the loader to the startup code. The breakpoint shows PC `$C000`, SP `$FF` and processor port `$37`. Save without ROMs. The first instructions clear memory from `$FEFA` and switch the port to `$35`.
4. Resume and decline the game's keyboard redefinition prompt with **N**. Select **2** at the title and hold joystick port 2 fire for about 25 frames, then release. Advance about 155 more frames to let the level and panel settle before saving `work/play-steady.vsf`. The comparison screenshot is `reference/play.png`.

The packed PRG starts a trainer before the final unpack. In the last unpacker at `$0193–$01F9`, the source and destination operands advance by modifying the instructions that use them. The loop tests `$71` as a marker, with commands for a literal marker, a destination change and a repeated byte. None of the extracted PRG's aligned 16-byte windows match at the corresponding load address in the hand-over. The disk file is the packed resident load. A byte-for-byte model of the final depacker consumes 48,183 bytes, beginning at $445C and wrapping to $0192. Its 63,520 writes cover $06E0–$FEFF exactly and reproduce every destination byte in the hand-over. The model and comparison are in `work/depack_evidence.py` and `work/depack-coverage.json`.

Level selection reads one of five resident map pointers at `$2DCE` and expands the selected stream to RAM. Map zero also serves the title and bonus round. The observed title and level-one sequence came from the single PRG. The four regular map streams are resident in the hand-over.

## Why the listing uses the hand-over

- `$C000–$C20A` contains startup code at the hand-over. The screen clear at `$336D` subsequently uses this address space for the screen matrix.
- `$3F35` uses the four title asset pages beneath I/O at `$DC00–$DFFF` to replace the tile preparation code at `$E000` with title character and raster data.
- `$C1EF` mirrors sprite data at `$C500–$DBFF` to `$4500–$5BFF`. Watchpoints from entry to the return at `$C20A` counted 5,888 stores and zero CPU reads in the destination. The kit counts the source set.
- The hardware NMI vector in play points to `$36B7`. The hardware IRQ vector alternates as the raster advances. A stopped gameplay snapshot showed `$2513`. Its instruction trace reached the `$D016`, `$DD00`, `$D011` and `$D019` writes, and the scheduling code at `$2612` writes the next vector at `$FFFE/$FFFF`. At the watchpoint following `DEC $FE63`, the next PC was `$2880` and the vector was `$25F8`.

The installed build passed 56 emulator checks, including instruction stops, store watchpoints and frame advance. Host-key input failed. Matrix input worked. The server-quirks phase stopped with a missing `checkpoints` key in its cleanup reply. Targeted checks used the matrix and checkpoint tools directly. Regenerator2000 answered on port 23018.
