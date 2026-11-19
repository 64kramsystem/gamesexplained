# Flimbo's Quest orientation

The analysis uses the PAL C64 version of System 3's 1990 game in the Soldiers import of the Illusion/ATC +6/Fix release. [Release record and disk download](https://csdb.dk/release/?id=177655). The disk stays in `work/flimbos-quest.d64`. Its 174,848-byte length, disk directory and BAM identify a 35-track D64 with 683 sectors. Disk name `FLIMBOSQUEST`, ID `SD`, SHA-256 `608b70625926f865dad395e8d649fdeabbc8a40c258c3d664467a0a182056d3a`.

## Boot and capture

1. Start the installed headless VICE through the kit launcher with dummy audio. This worktree used MCP port 17404, monitor port 17405 and regenerator2000 port 17406. The emulator check passed 56 checks. Host-key delivery failed and the final server-quirks group stopped with a missing `checkpoints` key. Matrix input, instruction stepping, checkpoints, watchpoints and snapshot capture passed.
2. Hard reset, then autostart directory entry 1. At the Soldiers intro hold fire, then release. At the Illusion/ATC intro hold port-1 fire for about a second, then release. Answer N at each trainer option using matrix input. Wait for the loading picture and the first payload. Warp can shorten the serial load. Return to normal speed for play.
3. Wait for the title with the MUSIC and SNDFX indicators. Press and release port-2 fire. Wait for GET READY to clear and pause in the stage. `parts/engine/work/play.vsf` is the resident listing snapshot. `work/title.vsf` is the loading-picture phase, with the resident code installed and before payload one. `work/menu.vsf` is the interactive title.
4. At play the CPU port pair reads `$2F/$35`. The RAM IRQ vector at `$FFFE` points into a changing frame chain while the KERNAL IRQ indirection at `$0314` still holds `$ED2E`. Instruction checkpoints at `$791D` showed the repeating next-vector sequence `$19AD` at line `$82`, `$1A89` at line `$C2`, and `$16AD` at line zero. `$19AD` itself also inserts the `$1A59` IRQ at `$B2`.

The boot PRG contains BASIC startup, the cracker introductions and trainer, and a packed program. Its loading-picture path reaches the resident program through the jump at `$AD0C` to `$7900`. The game selects numbered disk files through its own serial depacker at `$76D4`. It reads and unpacks each stream with the ROM visible for serial calls and RAM visible for writes. The eight payloads replace high RAM while the engine below `$9080` remains resident. The media inventory accounts for the boot program, the two manually launched documents, and the eight payloads.

## Part capture routes

Every numbered part's `work/entry.vsf` stops at `$215D`, immediately after the loader returns. From the stage-one play snapshot, stop the CPU, set `$02A7` to the wanted file number minus one, set PC to `$215A`, then continue to the `$215D` checkpoint. The code at `$7737` selects that file and increments `$02A7`. This route calls the real loader and decodes the disk image in VICE. The watch chain and byte snapshots put the play overlays at `$9080–$BFFF` and `$CA00–$FFF7`. The ending's second span ends at `$ED7F`. The data under I/O is included as RAM.

For the playable captures of stages 2–7, start from stage one and set `$02A7` as above. Set `$15` to 1 to enter the shop and break at `$1FF8`. Set PC to `$20FE` and let the game run its stage-completion transition. Break at `$14A1` after the next file loads, resume for 145 frames and apply right and fire on port 2 for 20 frames before capturing. The stage screenshots use this route, which can carry a bonus score into the next HUD. For the ending use payload eight and resume from `$215D` through the call to `$9080`. The ending reference shows the first rendered laboratory scene.

The recorded routes are debugger recipes for capturing the loaded states. An input replay is unnecessary for these captures.
