# Ghouls 'n Ghosts on the C64

## Disk and emulator

Use The Wonderful Team disk from [its CSDb release](https://csdb.dk/release/?id=166613), saved locally as `work/ghouls.d64`. It is a 174,848-byte, 35-track sector image with SHA-256 `93559cea6c2e52f258646a7dbaf69321ec72aa60b55c177e4b6e1a9ecf1f6b47`. The first directory program is `GHOULS'N'G. /TWT`. The second is `LOADER`, which the bootstrap loads at $C000. The three DEL directory decorations point to the same BAM and directory sectors.

Use PAL with VICE MCP 3.14.0 macOS arm64 headless and the installed dummy audio launcher. The emulator self-check passed 56 checks. `keys-host` failed, so use joystick or direct keyboard matrix input. `no-exception` stopped the last quirks probe at a checkpoint-list reply that lacked the `checkpoints` field. Exact instruction stops, load and store watches, frame advance and snapshot save/load passed. SID behavior under dummy audio was outside this check.

## Cold boot and handover

1. Stop and start VICE through the kit launcher to get a fresh machine. Set `Drive8Type=1541`, `Drive8TrueEmulation=1` and `TrapDevice8=0` in its local `vicerc` under `[C64SC]`. Autostart the disk and wait for the TWT introduction. One successful run waited 20 seconds from the autostart call.
2. Enable warp, wait about four seconds and hold Space through the keyboard matrix for about 300 ms. There is a loading picture before the game's title. No trainer options were selected. The serial handshake at $C2AD/$C2B0 reads CIA2 port A and requires the drive to respond. One reset-and-autostart attempt stalled there, while restarting the VICE process with the 1541 settings and starting fresh reached the title.
3. For the listing snapshot, arm an execution stop at $8A00 before pressing Space. The bootstrap at $02C9 jumps there with the CPU port set to $35. Save `parts/resident/work/entry.vsf`. $8A00 installs the disk service and jumps to the game's initialization at $1700, which is later reused as the visible tile buffer. A second checkpoint at $2993 captures the first title/game loop entry as `parts/resident/work/first-frame-entry.vsf`.
4. Continue to the title with the fire prompt. Release all inputs and turn off warp. Hold fire on joystick port 2 for one second and release it. Allow the stage to appear. If the high-score screen is up, wait for the title and press fire there. `reference/stage-1.png` shows the resulting play state, saved as `work/play-round1.vsf`. The active port read is $35. With the ROM banked out, the IRQ vector at $FFFE/$FFFF points to $5C31. An execution watch there counted four hits in four frames. CIA2 NMI changes the vector at $FFFA/$FFFB during play, so a single read can give $5D88 instead of the initially installed $5D44.

## Stage loads

The gameplay request at $5AF6 passes an even selector to the disk wrapper at $0300 and then passes the following odd selector. The call sites are $5B5C (destination $86E9) and $5B67 (destination $C800). Stage 1 is loaded while preparing the title. Stages 2–5 replace both windows. The resident engine, title font and raster code stay in RAM.

The repeatable debugger route starts from `work/play-round1.vsf`. Stop at $29FE, set $9C to $80 and continue through the transition. Catch the next execution of $5B6A after both requests. Save the RAM as `entry.vsf` in the stage's own `work/` directory. Disable warp, continue to $29FE, and advance six frames to reproduce `play.vsf`. Repeat from that state for each following stage. The `steady.vsf` snapshots advance another 145 frames with no held controls to show the playfield. The corresponding images are in `reference/`. This route drives the game's loader using its stage-outcome flag. It does not require a gameplay recording.

| Loader ID | Starting track/sector | Destination | Decoded contents |
| --- | --- | --- | --- |
| $00 | 19/1 | $86E9–$BFFF | Stage 1 code, terrain and tables, including title assets |
| $01 | 21/2 | $C800–$F7FF | Stage 1 sprites and terrain glyphs |
| $02 | 23/1 | $86E9–$BFFF | Stage 2 code, terrain and tables |
| $03 | 11/2 | $C800–$F7FF | Stage 2 sprites and terrain glyphs |
| $04 | 25/0 | $86E9–$BFFF | Stage 3 code, terrain and tables |
| $05 | 9/0 | $C800–$F7FF | Stage 3 sprites and terrain glyphs |
| $06 | 27/5 | $86E9–$BFFF | Stage 4 code, terrain and tables |
| $07 | 7/0 | $C800–$F7FF | Stage 4 sprites and terrain glyphs |
| $08 | 6/17 | $86E9–$BFFF | Stage 5 code, terrain and tables |
| $09 | 30/0 | $C800–$F7FF | Stage 5 sprites and terrain glyphs |
| $0A | 32/3 | $4000–$67FF | Loading bitmap, screen and colour planes |
| $0B | 17/2 | $0400–$8BFF | Resident engine and bootstrap, with the high end replaced by stage data |
| $0C | 19/0 | $F800–$FFBF | Title and panel font data |

The disk sector chains follow the link bytes starting at the track and sector selected by the six-byte entry at $C30A + 6 × ID. For the packed payload, skip the 4-byte first-sector header and the 2-byte links on following sectors. The third table byte counts the final sector's payload bytes. Convert the stored bits to decoded bits 0 through 7 in the order 7, 5, 6, 4, 3, 1, 2, 0 and complement them. The fourth table byte is the run-length escape. A zero count emits the escape itself, while a nonzero count repeats the next byte. The ten stage payloads and both resident payloads match their entry snapshots byte for byte. The first program and `LOADER` have no complete 16-byte-aligned file match in play. Part of the first program's payload appears inside the resident program, and the $C000 loader gets replaced by screen RAM.

## Listings

The kit uses a separate export for each part and aggregates coverage at the game folder. Build the resident listing from its `work/entry.vsf`, stage 1 from its `work/pre-play.vsf` and stages 2–5 from their `work/entry.vsf`. Short live execution maps and tracing scripts are available under the game's ignored `work/` folder. Regenerator2000 answered on the assigned disassembler port.
