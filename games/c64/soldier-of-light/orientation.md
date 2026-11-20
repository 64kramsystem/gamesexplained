# Soldier of Light on the C64

## Image and tools

The analysis uses the [F.S.N. disk](https://csdb.dk/release/?id=215946). The image is local as `work/soldier-fsn.d64`. It has 174,848 bytes, no GCR-1541 header and a readable 683-sector directory. Its SHA-256 is `9d2594de55a03f857a5e72688a0b85693fbb4944def8c912d10c1fe27e56cca3`.

VICE MCP v3.14.0 macOS arm64 headless ran with the dummy sound device on the assigned MCP port 23108 and monitor port 23109. The emulator check recorded 56 passes and two failures. Host-key injection missed F1, and the final quirk phase stopped with a `KeyError('checkpoints')`; the GUI-independent joystick and checkpoint tests passed. Regenerator2000 answered through the stdio bridge on port 23110.

## Boot and handover

1. Hard-reset VICE and autostart the first PRG, `SOLDIER OF LIGHT`, from unit 8 with `kit/c64/vice.py`. The two-byte load address is `$0801`. BASIC runs `SYS 2064`, reaching `$0810`.
2. Wait for the title with the three planets and the start prompt. The intervening blue screen has an F.S.N. marker. The image proceeds to the title by itself, without a trainer selection.
3. To reproduce the loader handover, set a stopping checkpoint on `$080D` before the boot. Remove it at the stop, resume to `$008E` and then break on execution in `$0200–$FFFF`. The next stop is `$0291`, a restore stub. Resume to the `RTI` at `$01EF` and step once. The captured PC is `$3F93`, within the title raster handler. This is `work/game-handover.vsf`, copied to `work/entry.vsf` for the listing comparison.
4. Use `$3F00` as the title setup entry when exercising game code from the restored state. Setting the PC there with SP equal to `$FF` in the handover snapshot and running produced the title screen again. The setup rebuilds the display matrix from `$0A00` and `$F400–$F6FF`.

The loader restores a running machine. The second unpacking stage transfers control to the stub at `$0291`, which restores CIA state and copies saved zero-page bytes from `$0394`. The tail at `$01DF` clears its temporary routine, restores the processor port and registers, then uses the saved return PC on the stack to resume the title interrupt.

## Reaching play

At the title, save `work/title.vsf` with the stick released. From a paused emulator, hold joystick port 2 fire for six frames, release it and advance 30 frames to the selector. Save that state as `work/play-first.vsf`.

The stick moves the ship in pixels. From the selector capture, hold left 35 frames, left and up 50, right 17 and down 17 to position it on Cleemalt. Hold fire six frames, release, and advance until Get Ready. The capture used a total of 215 released frames after selection. Hold fire another 15 frames, release, and advance 55 frames to the ground display. The listing snapshot is `work/cleemalt-play.vsf` and the verified gameplay image is `reference/cleemalt.png`.

From the same selector state, Lagto used right 100 frames and down 9. Cleedos used left 17 frames and down 85. Fire six frames, wait about 145 frames with the stick released, then fire 15 frames and advance 45 released frames to each ground display. The corresponding local snapshots are `work/lagto-play.vsf` and `work/cleedos-ground.vsf`.

## Interrupts and memory

At the title, the KERNAL RAM IRQ vector at `$0314` names `$3F52`. The handler selects low bytes from `$8C00` for its three phases. In ground play the vector names `$190F`. Its dispatch table at `$19AD` selects `$1A00`, `$1A30` and `$1A60`. A captured frame records both character-bank choices and the writes to `$03FF`; the ground frame does not need to rewrite the IRQ vector to change phase. The port reads `$36` in the sampled title and ground states. The game also uses `$35` for RAM under KERNAL and `$34` for access to RAM under I/O.

| Disk item | Comparison with snapshots | Role |
|---|---|---|
| `SOLDIER OF LIGHT` | 34,041 payload bytes at `$0801`. The best fixed alignment left fewer than 800 equal bytes in either handover or play, so the payload does not map intact. The loader trace reaches the title IRQ after expanding it. | Packed resident game. |
| Track 17 sectors outside the file chain | Their on-disk links reconstruct a separate 4,172-byte BASIC program beginning at track 17 sector 0. Its own text identifies a human/computer token-removal game. | Remnants of a different program. |

The title, selector and three planet snapshots retain a common engine and source data. The planet setup expands a map into `$4000–$7FFF` at `$1C00`, copies glyphs to `$B800–$BFFF` at `$1BA0`, and writes the display matrix at `$8400`. Store checkpoints at `$4000`, `$5800`, `$7000` and `$B800` stop on those generating routines. These are resident-source buffers. The space transition uses resident code too. Starting at the game’s transition entry `$0C63` from the ground snapshot hit the checkpoint at `$E800`. Advancing 70 frames produced the space display. The simultaneous execution watch at `$9CB0` counted zero hits.

A resident disk helper at `$9CD1` asks for P, 3, 4 and V, which the F.S.N. disk does not contain. No direct call or jump to this entry was found in the captured image. Its reachability outside the captured starts and space transition is open.
