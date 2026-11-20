# Rainbow Islands on the C64

## Disk images

The boot disk is the Powers of Pain release, with disk name
`****G-FORCE****`. Its file is `work/rainbow-islands.d64`, a plain
35-track, 683-sector D64 of 174,848 bytes. SHA-256
`bdae877583b862a2b918b2ba260f52a12fd5e4ac5ad520bda4ecb31528edfcb4`.
The disk supplies the first file `RAINBOW ISLANDS` and all of the
numbered files except `11` and `21`. [Powers of Pain release](https://csdb.dk/release/?id=144564)

The supplement is the Saigon disk, also a plain 35-track D64, stored as
`work/saigon.d64`. SHA-256
`4cb9c270545b4efeee7dd15c0e5b4a64522a543d9aa7383be0eb81ed9535a70b`.
All thirteen numbered files present on both disks are byte-identical,
including their two-byte load addresses. The two missing files on the
boot disk are present on the supplement. The run used the supplement
as drive 8 media after capturing the boot disk's game in play.
[Saigon release](https://csdb.dk/release/?id=24350)

The emulator was the prepared VICE v3.14.0 macOS arm64 headless release,
with dummy audio and PAL video. The health check recorded 56 passes.
Host-key F1 delivery failed, and the final quirk probe raised a
checkpoint-list exception. The matrix key calls, snapshots, exact
instruction stops, and memory watchpoints passed. Regenerator 2000
0.9.20 opened the gameplay image and reported a C64 65,536-byte address
space.

## Boot and handover

1. Start VICE on the assigned port through the kit launcher. From a
   fresh machine, autostart the Powers of Pain disk on unit 8. The first
   file loads at $0801, its BASIC stub calls SYS 2061 and the crack
   displays a black screen reading NO PAIN, NO GAIN. The disk transfer
   took tens of seconds even with autostart warp enabled.
2. Once the intro IRQ at $1043 is running, hold port 1 fire for about a
   second. The read at $1105 compares CIA 1 port B with $EF and
   branches to the intro exit at $1270. The exit calls KERNAL setup
   before handing over to the packed game. The fire release leaves the
   game's attract screens running. No trainer options were selected.
3. Hold F7 through the keyboard matrix for 0.5 seconds, release it,
   wait 0.25 seconds, then hold F1 for 0.5 seconds and release it. The
   next round display proceeds to playable Round 1. Turn warp off
   before taking timing measurements.
4. The Round 1 workspace snapshot is `work/play-round1.vsf`, also
   copied into the resident engine part. $00 read $2F and $01 read
   $35, so the hardware vectors in RAM were active. $FFFE pointed to
   $53BD and $FFFA to $5419 at the saved instant. In a separate
   checkpoint window, both addresses recorded 21 executions in
   roughly 0.4 seconds. The NMI handlers patch $FFFA/$FFFB to alternate
   $5419 and $5464 during play.
5. The early engine snapshot `work/entry.vsf` was taken at $4020,
   inside the first startup delay. To reproduce that capture, keep the
   disk attached, hard reset, wait for BASIC, inject the extracted
   boot PRG at its load address and start at its SYS target $080D.
   Break at $1270 after port 1 fire, then arm $4020 and continue.
   `work/intro-trace.txt` records the instructions stepped after the
   $1270 stop. The entry snapshot precedes the display and simulation
   setup and retains more of the initial file staging data than the
   play snapshot.

## Parts and disk mapping

The boot PRG contains the crack's intro and packed resident program.
The engine owns the code and tables shared by the islands. Its listing
uses `parts/engine/work/play-round1.vsf` alongside its early engine
snapshot. The island listings use their post-loader snapshots so the
packed data is still present before round setup reuses the staging
window. Later captures use the engine's normal setup and drive routines
with an explicit saved player record, as described below.

| Part | Files | Installed data and entry |
|---|---|---|
| Island 1 | 01 and 02 | $1B00 and $9800, stopped at $7EEA |
| Island 2 | 11 and 12 | $1B00 and $9800, stopped at $7EEA |
| Island 3 | 21 and 22 | $1B00 and $9800, stopped at $7EEA |
| Island 4 | 31 and 32 | $1B00 and $9800, stopped at $7EEA |
| Island 5 | 41 and 42 | $1B00 and $9800, stopped at $7EEA |
| Island 6 | 51 and 52 | $1B00 and $9800, stopped at $7EEA |
| Island 7 | 61 and 62 | $1B00 and $9800, stopped at $7EEA |
| Ending | 71 | Packed entry at $0801, depacked handover at $0810 |

The first suffix is loaded to $9800 then copied for 32 pages to $1B00.
The second suffix replaces the beginning of the $9800 window. $0F57
copies its first six pages into $C800, copies the attribute page and
then expands or copies 64 sprite slots to $E800. Round setup later
decodes map data using the staging pages again. Bytes beyond the
recorded first file's size can be carried from earlier uses of the
staging area by the fixed-length page copy.

For each island entry, load the saved Round 1 state and attach the
supplement to drive 8. Write the zero-based island index at $1165, four
times that index at $1166, and $FF at $A9 to make the resident engine
treat the island as changed. Set the program counter to $4037 to go
through player restoration and the normal round startup. Stop at
$7EEA just after the two files have loaded and save
`parts/island-N/work/entry.vsf`. Remove the breakpoint and advance
frames for the companion play snapshot. The first file's complete
payload was found at $1B00, and the second's at $9800, in these
post-load images. `work/load-island.py` and `work/round-loads.log`
record the route and breakpoint stops.

For the ending, use the same play state and attached disk, set $A8 to
seven and enter $7F07. This preserves the active player fields and runs
the ending's load path. Stop at $7F39 after the file read, then continue
to $0810 after the depacker's jump at $CE48. Save the entry snapshot at
that point. The ending's companion snapshot shows the congratulations
display after continuing from the handover.
