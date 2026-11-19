# Nebulus on C64

The analysis uses the European Nebulus release with the Danish Gold trainer. The source is [CSDb release 141983](https://csdb.dk/release/?id=141983). The downloaded file is a 174,848-byte sector image with 683 sectors and no error-byte trailer. Its SHA-256 is `b4432f75db9337d76bbe7ae0f9de162ee448bd7e862e3911b6271171d7b865a7`.

## Boot and snapshots

1. Start VICE v3.14.0 (macOS arm64 headless build, dummy audio). The assigned MCP and monitor ports are 17424 and 17425. The disassembler uses 17426.
2. Autostart `work/nebulus.d64` from a fresh machine. VICE loads the first file and runs it. Wait for the Danish Gold intro.
3. Hold joystick port 2 fire for 12 PAL frames, then release. Wait for the menu showing **LIMETED LIVES**. Keep that setting and hold Space via the keyboard matrix for 10 frames.
4. A breakpoint at `$8017` catches the trainer entering the unpacked game. `work/entry.vsf` was saved there, with A=$36, X=$FF, Y=$00, SP=$F6 and I set. Clear the breakpoint, release Space and let the title appear.
5. From the title, hold port 2 fire for 10 frames, release it and advance 225 frames. `work/play-tower1.vsf` shows Pogo beside the submarine in Tower of Eyes. The sampled PC is `$AA99`, waiting for the raster tick. This is the listing snapshot. `work/game-title.vsf` shows the title menu.

The active CPU port during play reads `$35` (DDR `$2F`), exposing RAM under BASIC and KERNAL and I/O at `$D000`. The live NMI vector is `$B88A`. The sampled IRQ vector is `$B88B`. The IRQ handlers themselves write the next addresses into `$FFFE-$FFFF`: see `$B820`, `$B875`, `$B8C3`, `$B8E5` and `$B96F`. The foreground waits at `$AA93` for the tick increment at `$B859`. The title and tower share the resident program. Comparing the two snapshots shows changed display buffers and runtime values. The disk directory has one game program and a standalone documentation program. A later overlay is an open question.

## Disk contents

| File | Bytes with load word | Load | Where it appears |
|---|---:|---|---|
| `NEBULUS+     /DG` | 27,688 | `$0801` | Packed game and trainer. The trainer enters `$8017`. At the strongest exact 16-byte chunk alignment only 12 chunks match, so a direct copy of the PRG does not account for resident RAM. |
| `NEBULA DOCS  /DG` | 5,602 | `$0801` | Standalone Hades Nebula documentation, identified by its screen when autostarted as file 2. No nontrivial aligned 16-byte chunks matched entry or play. |

The emulator check failed host-key F1 and ended its quirk probe with `KeyError('checkpoints')`. Keyboard matrix, joystick port 2, stop and step, watchpoints, and snapshot determinism passed the corresponding checks. The full check log is in `work/emulator-check.log`. The frame recorder lost its MCP connection while stepping, so the IRQ chain is documented from the vector writes in the handlers. The saved play snapshot subsequently restored at the same PC.
