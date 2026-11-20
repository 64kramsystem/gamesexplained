# Strider II on the Commodore 64

## Image and tools

The working image is `work/Strider2.D64` from the [X-Ray release entry](https://csdb.dk/release/?id=35898). SHA-256 is `46794957efd93b8c1d958485b4a76f7f6816c4a031b7da08aa795f30155187f1`. The 174,848 bytes parse as a 35-track sector image with 683 sectors. The directory has six PRG files and the BAM reports no allocated sectors outside the directory and file chains.

VICE x64sc v3.14.0, macOS ARM64 headless release with dummy audio, emulated a PAL C64. Its assigned MCP port was 23032, with the monitor on 23033. `check-emulator` reported 56 passes and two failures. `keys-host` missed F1, so use matrix input or the KERNAL buffer. The final `no-exception` check stopped on a missing checkpoint list after a reset. A later frame capture attempt caused a disconnect at `vice_frame_advance`. The existing snapshots loaded after a restart. regenerator2000 0.9.18 answered on 23034.

## Boot and forest play

1. Autostart the image on drive 8 from a fresh machine. The first PRG is `STRIDER2+6/X-RAY` at $0801. Wait for the X-Ray intro, then hold matrix SPACE for 750 ms.
2. Wait at each trainer question and send N through the KERNAL keyboard buffer. Decline the five yes/no trainer options and leave RUN/STOP untouched. Wait for the title. Warp can shorten disk activity, then turn it off for controls.
3. Hold FIRE on joystick port 2 for 400 ms, then release. The forest scroll area and status panel appear. The captured [title](reference/title.png) and [forest playfield](reference/forest.png) are from this route. The snapshots are `work/strider-title.vsf` and `work/strider-play.vsf`. The resident analysis uses a copy of the latter.
4. In play, the vector at `$0314` reads `$EA31`, the KERNAL default. The hardware vector at `$FFFE` was `$9389`. In the captured play frame it changed to `$9680` at raster line 41 and back to `$9389` at line 112. The hardware NMI vector was `$94BA`. The frame's recorded CPU port value was `$35`, which exposes RAM at the hardware vectors.

## Stage loads and snapshots

`$0950` prepares disk I/O and calls `$CC00` with the stage value in `$FF` plus six. The loader adds `$3B` to that value to form the leading character of the PETSCII filename at `$CC20`. The second character is the wildcard. The packed bytes reach the C64 through the resident stream reader. The stage data is in RAM when `$CC1C` jumps to `$8000`.

| Selection | Disk file | Part |
|---|---|---|
| 0 | `A.CHRYSAGON/XRAY` | `forest` |
| 1 | `B.CHRYSAGON/XRAY` | `city` |
| 2 | `C.CHRYSAGON/XRAY` | `underground` |
| 3 | `D.CHRYSAGON/XRAY` | `rooftops` |
| 4 | `E.CHRYSAGON/XRAY` | `prison` |

To reproduce the hand-over snapshots, load the forest play snapshot while stopped and reattach the image to drive 8. Write the selection to `$FF` and `$8001`, set PC to `$0950`, and resume with an execution breakpoint at `$CC00`. The trace records A = 6 through 10. Remove that breakpoint and resume to a breakpoint at `$8000`. Inspect the two bytes at `$CC20` and save the entry snapshot. Delete the breakpoint and advance 80 frames for the later stages. Forest play uses the normal title-to-fire route above because the forced stage 0 entry goes through the title first.

The five `parts/<stage>/work/entry.vsf` snapshots were saved at `$8000`. Each has a corresponding `work/play.vsf` in its part. The shared resident part has the boot entry, forest play and title snapshots. Entry RAM comparisons place the stage changes between `$0B00` and `$4FFF`, apart from the loader's scratch state and selection operands. A second pass counted one store at each of `$0B00`, `$0B01`, `$4FFE`, `$4FFF` for each file. Counts at `$0AFE`, `$0AFF`, `$5000`, `$5001` were zero before the stop at `$8000`. The loader helpers and output are in ignored `work/trace-loader.py`, `work/stage-trace.txt`, `work/probe-ranges.py`, and `work/stage-writes.txt`. The hand-over routes use the game's own loader and a debugger-selected stage.

A fresh boot with an execution checkpoint at `$CDB0` stops at the trainer entry. After declining the options, the breakpoint at `$084C` catches the resident program before it reads the first stage. This is `parts/resident/work/entry.vsf`. The stage slot is still empty there. The resident listing uses `parts/resident/work/play.vsf`, with the boot snapshot for the uncounted data comparison. The code at `$85A7` and `$85C6` explains why the resident animation bytes at `$C800–$CBFF` temporarily disappear in the title snapshot.

For the two stage ranges reused as screen work space, load watches covered `$4328–$4337` and `$4738–$47FF` from each stage's `$8000` entry to the execution breakpoint at `$8561`. The count was zero in each case and RAM read back as zero after the clear. The raster display is blanked ahead of the clear and the title selects the separate VIC bank at `$C000`. The measurements are in ignored `work/buffer-watch.txt`.

The upper glyph ranges have the same values at the hand-over and in play. The `$E000–$E117` bytes also match the [Censor release](https://csdb.dk/release/?id=65036). The X-Ray intro held the complete `$FFC0–$FFF7` sequence while the disassembly range at `$8000–$C15C` was still almost entirely different. On leaving the intro, the store watch stopped after `$0819`, whose source and destination were `LDA $95EA,Y` and `STA $FF00,Y`. The 56 source bytes at `$96AA–$96E1` match the earlier intro bytes and the bytes left after the copy. The Censor release differs in all 56 bytes there. The resident ledger excludes this X-Ray bootstrap residue. The compared Censor disk, input probe and stop image stay in ignored `work/`.
