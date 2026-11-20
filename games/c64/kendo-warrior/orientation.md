# Orientation

## Image and tools

Hokuto Force's 2004 release of the Byte Back game. The [CSDb release](https://csdb.dk/release/?id=13317) archive contains a 174,848-byte D64 with a standard 35-track sector layout. Its directory contains one PRG, `KENDOWAR+15PD/HF`, loading at `$0801`. The archive also contains a map image outside the disk.

VICE-MCP v3.14.0 macOS arm64 headless, C64SC in PAL mode with dummy audio. The emulator check passed 56 checks. Host-name F1 delivery failed, so the route uses matrix inputs. The server-quirk phase stopped when the checkpoint-list response lacked its `checkpoints` field. Stopping checkpoints worked during the boot route.

## Boot route

1. Extract the PRG with the kit disk reader. Hard-reset and wait for BASIC. Inject the extracted PRG with `vice.inject` and then type `SYS 2051` through BASIC.
2. Enable warp for the packed release's startup. Hold SPACE on the Hokuto Force intro. At the document viewer, press RUN/STOP (matrix row 7, column 7). At the illustrated loading picture, press SPACE.
3. Answer N to each trainer prompt, holding and releasing it until the menu advances. A checkpoint at `$0880` after the last answer catches the first instruction of the engine proper. The bytes there begin `78 A9 17`. Save this state as `work/entry.vsf`.
4. Release that checkpoint, wait for the Byte Back title, and turn warp off. Save the title separately. Hold port 2 fire for about 120 PAL frames and release it on the first corridor. Save `work/play-round1.vsf` with ROMs omitted.

The packer's intro, viewer, loading picture and trainer all precede the engine at `$0880`. The packed PRG is the disk source of the game image. Compare the unpacked entry and play snapshots when classifying changed memory.

In play the CPU port reads `$35`. The processor vectors under the KERNAL read NMI `$09F1` and IRQ `$08FF`. The KERNAL RAM IRQ indirection at `$0314` still reads `$EA31`. The game runs from RAM under the KERNAL and supplies the processor's IRQ entry directly.

## Analysis image

`listing.json` uses `work/entry.vsf`, with `work/play-round1.vsf` as its comparison image. The handover preserves startup operands and the original tile byte at `$A000` before the new-game routine changes it.

The game's packed file does not retain a fixed-offset match to the unpacked image. Its mapped output includes the engine from `$0880`, sprite and character data in the VIC bank and reserve sheets, room data at `$A000–$B9FF`, and the music driver and streams from `$BBFF`. The one file and the empty list of stray disk sectors are recorded in `media.json`. Gameplay room changes take their maps and sprites from those resident directories, so this release uses a single analysis image.

The independent comparisons are the [DCS disk](https://csdb.dk/release/?id=83774) and the [Byte Back tape](https://www.c64games.de/phpseiten/spieledetail.php?filnummer=3717), each stopped at `$0880`. They are reference inputs under `work/`. Their files do not contribute additional parts to the disk listing.
