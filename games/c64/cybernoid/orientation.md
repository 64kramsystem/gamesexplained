# Cybernoid orientation

## Image and tools

The analysed image is [Hewson's Cybernoid with the Beastie Boys intro](https://archive.org/details/Cybernoid_The_Fighting_Machine_1988_Hewson_cr_Beastie_Boys). Its 174,848-byte D64 contains one 42,940-byte PRG, including its two-byte load address. The disk reader reports 683 sectors, no error-table entries and no allocated sectors outside the file. See [media.json](media.json).

| File | Load address | Where it appears |
|---|---|---|
| `CYBERNOID/BB` | `$0801` | A BASIC line calls `SYS 2064`. The packed program is replaced in RAM in two phases. The final depacker emits `$0800–$CFFF` and calls the game at `$0824`. |

VICE MCP v3.14.0 for macOS arm64 ran headless with the dummy sound device. The assigned MCP and monitor ports were 23020 and 23021. Regenerator2000 answered on 23022 with the entry snapshot loaded. The emulator check observed failures in host key input, determinism across restart, and a frame-advance crash during the stepping phase. Matrix input, joystick II, direct execution stops, snapshots and non-stopping execution and store watchpoints worked in the game. The full frame recorder also hit the frame-advance failure. The IRQ trace below uses checkpoints instead.

## Reproduce the snapshots

1. Start a fresh PAL C64 with `python3 kit/scripts/tools.py vice`. Wait for BASIC to initialize. On this image the MCP autostart attempt left the program area unfilled, so use the extracted PRG. Extract it with `python3 kit/c64/disk.py extract games/c64/cybernoid/work/Cybernoid.d64 games/c64/cybernoid/work/extracted`.
2. Call `vice_execution_pause` directly through `kit/c64/vice.py`, then use its `inject(rpc, path, 2064)` helper on the extracted file `CYBERNOID$2FBB`. With warp enabled while unpacking, the first stopping execution checkpoint at `$1900` reached the Beastie Boys intro. The check also confirmed PC `$1900`. The local snapshot is `work/intro-entry.vsf`.
3. Delete that checkpoint and run. Turn warp off. Hold Space through the matrix until the intro accepts it. The intro's `$1991` jumps to `$1800`, which restores system display state, copies a short relocator to `$03B7` and executes it. The relocator copies the next PRG from `$3000` to `$0801` and calls its unpacker at `$0810`. Arm a stopping execution checkpoint at `$0824` before pressing Space, then save `work/entry.vsf` without ROMs when the PC stops there. This is the listing image.
4. Remove the checkpoint and release Space before resuming. The options screen cycles with the credits and high-score table. Hold `1` while the options screen is active, starting after its key-release gate. A stopping checkpoint at `$8054` catches the active menu and `$2D0B` catches the accepted start command. Release `1`, remove the start checkpoint and resume for about a second. Capture `work/room1.vsf` without ROMs. See [room 1](reference/room-01.png).

The optional Zenith disk was downloaded for a crack comparison. Its bootstrap entered a jam in this setup, so it supplies no evidence about differences in the original game. The analysed disk needed no trainer choices.

## Banking and execution

The CPU port reads `$37` at `$0824` and `$35` during play. Initialization temporarily writes `$34` to copy data beneath the I/O registers. In play the KERNAL is banked out, so the hardware vectors are authoritative. NMI points to `$55F8`. The IRQ vector cycles through `$49B0`, `$4A66` and `$4A71`. A short first-room trace counted 16, 15 and 15 executions respectively, and 92 writes to `$FFFE–$FFFF`. The main loop at `$2D39` ran 16 times in that interval. Raw checkpoint output is in `work/raster-checkpoints.txt`.

The entry capture preserves the source sprite bank at `$C000–$C3FF`, which startup copies beneath I/O before the screen matrix occupies that address. The game initializes one resident image. Stages select initialization records at `$2E7B`, and room transitions select pointers at `$0830` in the same image. The disk has no separate stage files.

Rebuild the listing with `python3 kit/scripts/listing.py games/c64/cybernoid games/c64/cybernoid/work/entry.vsf`.
