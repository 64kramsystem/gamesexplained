# Orientation

## Input and tools

RCS/HCC Terramex disk, dated 24 February 1988 on the intro. The private image is `work/terramex.d64`, a 174,848-byte 35-track sector image with 683 readable sectors. The directory on track 18 has two closed PRGs and the allocation map has zero unowned used sectors. SHA-256 `f7a7bc7308b443ecfcb5bc2e97e63cdda365fe5b3cf60597c0fa42844745cbbf`. [CSDb release](https://csdb.dk/release/?id=171769)

The installed macOS arm64 headless v3.14.0 x64sc ran with the dummy sound device on PAL. VICE MCP uses port 17440, the remote monitor uses 17441, and Regenerator 2000 v0.9.18 uses 17442. The emulator check reported 56 passes and two failures. Host-key F1 failed, so use the C64 keyboard matrix. The final quirks phase raised a KeyError when the checkpoint reply lacked its expected property, with the same result after a clean start. Exact stops, direct key matrix, joystick pins, watchpoints and snapshot determinism passed in the test program.

## From power-on to the listings

1. Start VICE through `kit/scripts/tools.py vice`, hard-reset, and autostart the first PRG of `work/terramex.d64`. The RCS intro scrolls below the HCC logo. Hold fire on port 1 for about 0.7 seconds. When the second HCC intro appears, hold Space on the C64 matrix for about 0.5 seconds.
2. To save the selector handoff, arm an execute checkpoint at `$59AA` before dismissing the intros. Save `parts/selection/work/entry.vsf` on that stop. Continue to the five portraits. Save `parts/selection/work/selection.vsf` here for its listing. The entry and living selector agree on the code at `$59AA–$5D62` apart from the two coordinate bytes, and on the five explorer blocks. The cursor sprite slot and hardware vectors are populated during initialization.
3. From the untouched initial cursor, hold up on port 2 for about 0.5 seconds. The hand should be over Fortisque-Smithe, and the selector's hit ID at `$0300` should be zero. Tap fire and allow time for the disk load. Use warp while loading if desired and turn it off before measuring timing.
4. To save the expedition listing image, set a checkpoint on `$FFD5` before fire. The selector jumps to `$FFD5` from `$5872` with name `MAIN`, device 8, secondary address 8 and A=0. It pushes `$080F` as the return word. Stop at `$0810` as the load returns into the freshly loaded program. Continue with a new checkpoint at `$8049`. At that stop, save `parts/main/work/entry.vsf`. This is the expedition's listing image. The unpacked stub at `$0400` leads through `$7FF8` to it.
5. Continue to the credit and controls screen and save `parts/main/work/title.vsf` if needed. A tap of fire on port 2 starts the desert scene. Save `parts/main/work/play-start.vsf` after the HUD and main playfield appear. The entry image preserves the engine's initial operands and authored HUD template. The play image contains expanded map buffers and initialized video state.

Use snapshots without ROMs or disks. The title and play snapshots already contain the selected explorer blob. When restoring a snapshot for a disk load, verify unit 8 still has the image attached.

| File | Disk load | Mapping observed |
|---|---|---|
| BY RCS 2100/HCC | `$0801`, 28,161 payload bytes | BASIC starts the cracker wrapper. The final selector enters at `$59AA`, portrait data appears at `$4800` and `$5400`, and five frame blocks appear at `$6840–$B6FF`. The packed-file window scan found pieces across multiple offsets. Most dominant offsets for 16-byte packed windows were near `-$1B49` and are loader residues. |
| MAIN | `$0800`, 32,065 payload bytes | Disk return at `$0810`. The bootstrap copies parts of itself to the stack and low-memory scratch space, then expands the expedition and transfers to `$8049`. The sparse direct matches to `MAIN` are consistent with a packed file. |

The transfer at selector `$5B0C` copies 4,032 bytes to `$F036–$FFF5`. For Fortisque-Smithe the source starts at `$6840`. All 4,032 bytes match the entry and play snapshots. The payload survives the `MAIN` depack, which ends below `$EF00`. This is a transition between game loads. The title and the expedition playfield within `MAIN` share one part.

The selector installs IRQ `$5C45` and NMI `$5D62` in the RAM hardware vectors. The expedition installs IRQ `$8796` and NMI `$872F`. Each handler switches the 6510 port temporarily to expose I/O. The underlying RAM bytes at `$0000–$0001` differ from the live port registers. In the two steady states normal gameplay code uses the low banking bits `%100`, with the IRQ switching them to `%101`. The one-frame expedition capture logged `$D018=$0E` at line 182, cycle 62 and `$D018=$02` at line 257, cycle 32, without a change of hardware IRQ vector. The fixed vector dispatches several phases inside the handler.

## Reference captures

- `reference/explorer-selection.png` shows the five portraits.
- `reference/title.png` shows the title controls and music setting.
- `reference/expedition.png` shows the opening desert and HUD.
