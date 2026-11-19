# Mission A.D. on the Commodore 64

## Media and hardware

The analysis image is [CSDb release 210100](https://csdb.dk/release/?id=210100), saved locally as `work/MissionAD.d64`. Its length of 174,848 bytes and 683 readable sectors identify a standard 35-track D64. The directory holds a single PRG, `MISSION A.D.`, with a two-byte load address of `$0801` followed by 46,202 payload bytes. The disk reader found no allocated stray sectors. See [media.json](media.json).

Use PAL C64SC. The installed headless vice-mcp v3.14.0 build ran with dummy audio and MCP port 23000. The tool check reported 56 passes and two failures. Host-key input failed, while keyboard matrix input passed. The final quirks phase raised a missing `checkpoints` key after reset. Instruction stops, watchpoints and snapshot loads worked in the game. The disassembler answered on port 23002.

## Reproduce the snapshots

1. Start from a fresh power-on and autostart the first PRG on the disk. VICE loads it from device 8 and runs the BASIC stub. The stub issues `SYS 2088` and the packer starts at `$0828`.
2. For `work/entry.vsf`, arm an execute checkpoint at `$0828` before autostart. When it fires, replace it with a checkpoint at `$0100` and resume. Repeat at `$0812`, `$C16F`, `$003E` and `$0153`. At `$0153`, remove the checkpoint while paused and step the one `RTI`. Save with ROMs excluded when PC reads `$AF2E`.
3. Run to the [title](reference/title.png). There is no trainer prompt along this path. With the title showing joystick mode, stop and hold port 1 fire for 20 PAL frames. Release and advance at least 50 frames to the [briefing](reference/briefing.png). The briefing waits for a separate press.
4. Hold port 1 fire for 18 frames, release and advance 12 more. Save `work/play-round1.vsf` with ROMs excluded in the [first room](reference/first-room.png). IRQ vector reads differ by raster phase. The CPU port in play reads `$35`. The ROMs are banked out and the I/O chips are visible.

## Loader and game boundary

The PRG's packed bytes do not map to a continuous range at their disk load address after boot. The first relocation and decrunch run from `$0100` into a second boot stub at `$0812`. That stub jumps to the copier at `$C16F`. It moves the next loader to low RAM and starts it at `$05AB`. The loader restores RAM and chip state, then the decoder starting at `$003E` copies saved zero-page and vector data out of the staging area below I/O. The last restore code runs from the stack page and reaches `RTI` at `$0153`. The instruction consumed the saved stack frame and transferred control to `$AF2E`, inside the title loop. This is a frozen game image.

The [original tape from Ultimate Tape Archive](https://uta.pokefinder.org/Ultimate_Tape_Archive/Mission_A.D._(1986_Odin_Computer_Graphics)_%5B7025%5D/) also reached the title in the same headless emulator. It serves as a comparison copy. The disk hand-over and title dumps differ at 15 bytes. Comparing the tape and disk title dumps shows differences concentrated in the shadow behind I/O, high RAM work areas, zero page and the stack, with smaller differences elsewhere. For example, the entire `$63D9-$7A30` room layout area matches. The disk's hand-over image retains its freezer staging in `$D004-$D203`. In that disk image `$D204-$DFFF` exactly matches the emulator's address-dependent RAM fill.

The first gameplay frame is in bank 0. CIA2 port A read `$97` and `$D018` read `$19`. The bitmap is at `$2000`, the screen matrix is at `$0400` and sprite pointers are at `$07F8-$07FF`. The RAM vectors at `$FFFA/$FFFC` point to `$57CC`. The frame captured in `work/first-room-frame.json` observed the IRQ vector alternating between `$5818` and `$5895` at raster lines 132 and 226, including the latter write after the handler entered at raster 204. The updates at raster 132 replace sprite Y values for the lower half. The updates following raster 204 prepare sprite positions for the upper half of the next frame.

The first room uses resident graphics and placement lists. A single game image is the working scope. Later disk or tape reads remain an open check.
