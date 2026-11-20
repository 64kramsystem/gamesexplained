# Solomon's Key orientation

## Image and tools

The analysis uses the Scouse Cracking Group release from [CSDb](https://csdb.dk/release/?id=145188). The local input is `work/solomon.d64`. The image has the size and sector layout of a 35-track D64 and its SHA-256 is `2c3480a2a669a82428431fcb19587d7540b63b4a06518a47a5e7b01170528f21`.

Headless x64sc from vice-mcp v3.14.0 ran with the installed dummy audio wrapper on MCP port 23096. The kit check reported 56 passes. Host-key injection failed, and the final server-quirks phase stopped at `KeyError('checkpoints')`. Matrix input, joystick input, exact stops, stepping and load/store watches passed. Regenerator2000 answered on port 23098.

## Power-on to Round 1

1. Hard-reset the C64 and autostart `work/solomon.d64`. Allow about 18 seconds for the Scouse Cracking Group intro to appear. The intro screen and snapshot are `work/boot.png` and `work/crack-intro.vsf`.
2. Hold Space through the keyboard matrix for 30 frames, then release. Wait 370 more frames for the program to unpack and the title screen to appear. The route selected no trainer option.
3. On joystick port 2 hold fire for 25 frames and release for 30. The menu displays the selected player count. Apply three further presses of 25 frames with 30 released frames between presses, then run 100 frames. Confirm Round 1 with Dana and the enemies visible. This is `work/play-round1.vsf`.
4. For the handover, load `work/crack-intro.vsf`. Arm an execution stop at `$080F` while paused, hold matrix Space and resume. Release Space after about 350 ms. Save at PC `$080F` with ROMs omitted. The resulting `work/entry.vsf` is the listing source. Pass `work/play-round1.vsf` as the second snapshot for the loaded-data audit.

## Disk and handover

| Disk file | Loaded at | Result |
|---|---|---|
| `SOLOMONS KEY/SCG` | `$0801`, 25,281 payload bytes | BASIC issues `SYS 2121` into the SCG wrapper. The stack-page unpacker uses an output pointer patched into its store operands. It restores the processor port and jumps to `$080F` when unpacking ends. The packed file therefore maps to the resident image through decompression. |

The disk directory has one PRG and no allocated sectors outside that file. The first title and play transitions use the resident room loader at `$14B8` and actor loader at `$1530`, which copy indexed records directly from RAM.

## Gameplay machine state

The low three bits of the processor port are `$05`, with I/O visible and RAM selected beneath BASIC and KERNAL. The KERNAL RAM vector at `$0314` still contains `$EA31`. The RAM hardware vectors are NMI `$1388` and IRQ `$1569`, both installed by `$134F`. A store watch at `$D012` caught the four handlers writing 94, 148, 202 and 40. The one-frame capture in `work/frame.json` preserves the sprite register and pointer writes. Screen bytes start at `$4000` and the bitmap starts at `$6000`. The handover preserves authored bytes before the actor, sprite-list and display buffers are populated.
