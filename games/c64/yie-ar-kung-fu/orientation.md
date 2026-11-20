# Yie Ar Kung-Fu · C64 PAL tape

`work/euro.tap` is the Euro image from the C64Games tape archive. It is 644,177 bytes, begins with `C64-TAPE-RAW` and reports TAP version 1. SHA-256 `0f278e4efedc8af2051a696edd98bbfc88f3719b46c4b2feb706321c6085d423`. [C64Games game entry](https://www.c64games.de/phpseiten/spieledetail.php?filnummer=206)

## Rebuild the snapshots

1. Start the kit's headless vice-mcp 3.14.0 in PAL with dummy audio. Before autostart, set `Drive8Type` through `Drive11Type`, `Drive8TrueEmulation`, `Printer4` and `Printer5` to zero with the monitor's `resourceset`. Cold reset the C64. These settings apply to the running emulator.
2. Arm an execute checkpoint at `$4276` and autostart the TAP. Enable warp until the hand-over. The loader reports the program as YIE-AR KUNG-FU and displays the instruction to remove printers and disks. No trainer menu or manual key press is required.
3. At `$4276`, delete the breakpoint and single-step the RTS. It reaches `$0400` with I set. Save `work/entry.vsf` with no ROMs. The clean boot reference is also in `work/entry-nodrive.vsf`. The two snapshots' main RAM agrees at all authored payload addresses. The differences are the underlying processor port byte at `$0001` and five stack bytes.
4. Turn off warp. From the title, hold joystick port 2 fire for 15 frames. Release for 15 frames at the player menu. Hold fire for 15 frames again. Release and allow 270 frames for the introductory display to give way to the fight. Save `work/play-round1.vsf` with no ROMs. The fight is identified by Oolong and Buchu opposite one another on the waterfall floor without the opponent preview cards.
5. In the fight, the hardware IRQ vector at `$FFFE/$FFFF` reads `$C3A7` and the RAM KERNAL IRQ vector at `$0314/$0315` still reads `$EA31`. The processor port selects RAM instead of the BASIC and KERNAL ROMs, with I/O visible (`$C39C` writes `$35`). A frame capture confirms stores from the IRQ phase routines associated with `$C3BC/$C3BD`.

The installed emulator passed 56 health checks. The host F1 test failed, while matrix F1 and both joystick ports passed. The server quirks phase aborted with a missing `checkpoints` field. The first-fight capture and instruction trace used the kit VICE client on the assigned ports.

## Loader and memory image

The KERNAL-format bootstrap loads at `$0316`, relocates a loader into `$4000` and reads Ocean–Imagine pulse blocks. The loader plays a tune from `$A000` while loading. Its final sequence at `$4223` disables the loader's sound and CIA1 timer, copies 16 pages from under I/O at `$D000` to `$A000`, restores I/O mapping and transfers to `$0400` via the stacked return address.

| Tape item | Load address | Match against hand-over |
|---|---|---|
| KERNAL bootstrap | `$0316` | Source partly overwritten. Its relocated loader runs in `$4000–$4276`. |
| Turbo 1 | `$A000` | Music player used by the loader, then superseded by turbo 8. |
| Turbo 2 | `$CC00` | 1,024 of 1,024 bytes. Bitmap screen color attributes. |
| Turbo 3 | `$C800` | 1,024 of 1,024 bytes. Source for the title's color RAM. |
| Turbo 4 | `$D800` | Exact duplicate of turbo 3 at `$C800`. The later block 8 overwrites underlying RAM in this region. |
| Turbo 5 | `$E000` | 8,191 of 8,192 bytes. Title bitmap and tail containing vectors. |
| Turbo 6 | `$0400` | 15,360 of 15,360 bytes. Front end, screen streams, pose tables and graphics. |
| Turbo 7 | `$4400` | 23,552 of 23,552 bytes. Sprite components, character sets and game sound data and code. |
| Turbo 8 | `$D000` | 4,096 of 4,096 bytes at both `$D000` and the copied destination `$A000`. |
| Turbo 9 | `$B000` | 8,192 of 8,192 bytes. Fight engine, raster code, tables and the same title color pages as blocks 2 and 3. |

The hand-over image supplies the listing because it preserves authored data before initialization writes to its buffers and relocates sprite pieces. The observed path from title to active play uses the resident tape load throughout. The arena decoder reads resident streams and the sprite bank exchange works on already loaded RAM.
