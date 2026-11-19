# Orientation

## Image and emulator

Ocean's PAL cassette from [C64Games.de](https://www.c64games.de/phpseiten/spieledetail.php?filnummer=74). The file in the local work directory is `Hunchback_(Ocean).tap`. The first 20 bytes identify a version 1 `C64-TAPE-RAW` image for the PAL C64. SHA-256 is `ea97257e717222bc574966b753403b9496dca0f69666c1bb8bc0741b3ef640bb`.

VICE-MCP v3.14.0 macOS arm64 headless ran with dummy audio. The kit's emulator check reported 56 passes and two failures. `keys-host` failed to deliver F1, so use the matrix tool. `no-exception` was a `KeyError('checkpoints')` in the final quirks phase. The emulator check restarted its instance and the later Hunchback execute and store checkpoints both stopped successfully.

## Rebuild the local snapshots

1. Hard reset, arm an execute checkpoint at `$4000`, and autostart the TAP. The first tape file is the BASIC bootstrap. Following its own delay, it loads the next file with secondary address 1. BASIC runs from the top again after the load and calls `SYS 16384`. Enable warp during this second tape load to shorten the wait.
2. The checkpoint stops at PC `$4000` before the first instruction. Turn off warp and save this state without ROMs as `work/entry.vsf`. Continue execution to see the title. The two disk or tape options offered by the download site are different releases. The run used the Ocean tape exclusively.
3. Hold SPACE via the keyboard matrix for 30 frames and release. Choose J via the matrix, hold it for 30 frames and release. The game shows the port 2 prompt before drawing the wall and displaying GET READY. Allow about 20 seconds of emulated time for the wall reveal and ready delay. A stopping execute checkpoint at `$4920` catches the first input poll. Save this state without ROMs as `work/play-round1.vsf`.

## Memory at the hand-over and in play

| Tape file | Loaded range, inclusive | Comparison |
| --- | --- | --- |
| HUNCHBACK | `$0801-$087B` | The 123-byte tokenized bootstrap contains the loading message, delay, cassette LOAD and SYS. |
| HCODE | `$3C00-$8000` | The full 17,409 bytes match `entry.vsf` at their tape addresses. |

At entry the processor port reads `$0000=$2F`, `$0001=$27`. BASIC and KERNAL ROM and I/O are visible. The RAM vectors at `$0314-$0319` are `$EA31`, `$FE66` and `$FE47`. At the first gameplay input poll the IRQ vector reads `$4BF1`, while BRK and NMI are unchanged. The code at `$4BE4` installs `$4BF1`. Other handlers selected by state include `$46AD` for title input, `$4580` for the attract walker, `$4B74` for the wall transition and `$3C73` for the colour flash. Running wait loops leave the KERNAL IRQ selected in some transitions.

The VIC configuration at start selects bank `$4000`, screen `$7400` and character memory `$7800`. The screen is redrawn in play and the five score records are copied to RAM at `$8100`. Regenerator2000 was started on `work/entry.vsf` on the assigned port. Use the entry snapshot for the listing because it preserves the complete tape payload before screen writes and character animation. The tape contains a bootstrap and one gameplay image. The wall renderer dispatches to in-memory routines and buffers.
