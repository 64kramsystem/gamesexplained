# Orientation

The input is `work/Who_Dares_Wins.tap`, the original Alligata cassette rip in the [GTW64 archive](https://www.gamesthatwerent.com/gtw64/who-dares-wins/). The header is `C64-TAPE-RAW`, version 1, and the pulse payload has 891,056 bytes. The companion packed PRG is retained in `work/` and the analysis uses the tape boot.

## Reproduce the snapshots

1. Start the installed VICE MCP v3.14.0 macOS arm64 headless build via the kit launcher, with the supplied dummy audio wrapper. Use PAL. The emulator check measured 56 passes and two failures. Host-named keys failed. The ancillary quirks phase failed with `KeyError('checkpoints')` after the connection check. Instruction steps, stopping checkpoints, load and store watchpoints and joystick tests passed.
2. On a fresh machine autostart the TAP with `kit/c64/vice.py`. Warp may be turned on again after VICE's autostart completes. Wait through the flashing-border loader to the title screen. Save `work/title.vsf`.
3. Hold port 2 fire for about half a second and release. The terrain and blue player replace the title. Save `work/play-round1.vsf`.
4. To reproduce `work/entry.vsf`, restart VICE through the launcher and autostart the same tape. Arm a stopping execute checkpoint at `$4000` before the loader finishes. The stop hit once with PC at `$4000` and the CPU port read `$27`. This is the listing snapshot because it preserves every payload byte, including self-modified operands and initial data changed in play.

## Loader and resident image

The KERNAL tape header carries a fast loader starting at `$0351`. The short program at `$02A7` sets up the transition to that loader. It waits for tape pulses with CIA 1 and uses CIA 2 timer B to classify them. The fast streams use 312- and 432-cycle pulses. The loader finds a `$63` pilot and `$64` marker, skips 156 bytes, reads a ten-byte header and XOR-checks the payload. It accepts two adjacent RAM payloads before transferring control to `$4000`. The other tape recording carries the same two payloads in reverse order.

| Fast header pulse | Destination, end exclusive | Entry bytes matching | Gameplay bytes matching |
|---:|---|---:|---:|
| 49,603 and 809,023 | `$A000–$C800` | 10,240 / 10,240 | 10,240 / 10,240 |
| 136,180 and 495,118 | `$0900–$A000` | 38,656 / 38,656 | 38,467 / 38,656 |

The play snapshot read `$26` at the CPU port, with BASIC ROM out and I/O and KERNAL ROM visible. At capture, the KERNAL IRQ vector `$0314/$0315` pointed at `$1ADF`. One play frame captured eight stores to the vector, yielding `$152F`, `$14FA`, `$154E` and `$1ADF` in sequence. The frame and paired snapshots are in `work/`.
