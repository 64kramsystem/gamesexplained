# Rick Dangerous II on PAL C64

The working disk is the Alex Software release from [CSDb](https://csdb.dk/release/?id=168957). Keep `work/alex.d64` and the extracted files in `work/alex-files/`. The disk ID is `07`, and the directory name is `ASSOFT 944-34-62`. The first PRG loads at $0801 and its BASIC line runs SYS 2064.

## Boot and load Hyde Park

1. Start the installed headless VICE MCP v3.14.0 on port 23112 with dummy audio. Hard reset and autostart the first file on the disk. Wait for the Alex Software intro. In this run it appeared within 16 seconds.
2. Hold SPACE by matrix for about 250 ms and release. Wait for the trainer to finish unpacking. Answer N to each of its three Y/N prompts. Save `work/title.vsf` at PRESS FIRE TO PLAY.
3. Tap joystick 2 fire for 250 ms. Save `work/select.vsf` at SELECT LEVEL. Tap fire again on the default Hyde Park choice.
4. Wait through the colored stripes while the disk reads. Tap and release fire on each story panel until the park and the score panel appear. Save `work/play-hyde-park.vsf` without ROMs.
5. Turn warp off before sampling game timing. The gameplay snapshot has processor port $35. The RAM hardware vector at $FFFE points to $0DAE. The KERNAL's soft vector at $0314 stays $EA31. Live history reached the gameplay loop at $0549 and object processing around $16D0.

## Level overlays

From the select snapshot, down on joystick 2 moves the cursor and fire selects the highlighted level. The loader entry at $7D4B receives the selected level in A. For Headquarters, select the Mines, break at $7D4B, set A to five, and continue. This is a directed capture of the fifth overlay. The normal selection path starts with Headquarters locked.

Save each level at $7CF4, immediately after its streamed loader returns and before the resident engine restores its level-transition scratch state. The handoff snapshots are named `parts/<id>/work/entry.vsf`. The exact filename was inspected at $7CF8 at each return. It was `01.R2*` through `05.R2*` in selection order. Warp speeds up the striped loading screen.

The load switches the processor port to $36 and enters the KERNAL serial routines. CPU history in the striped screen shows $EE5A–$EE63 repeatedly sampling CIA2 port A at $DD00. The loader calls $88A7 and receives bytes through $EE13. A checkpoint at the public LOAD entry $FFD5 counted zero hits over the Hyde Park transition. No exact 16-byte windows from the packed level PRGs matched the title or the first two gameplay images. Tracing the depacker’s CPU instructions against the five disk files found the two RAM output spans $8A00–$BFFF and $D800–$EFFF. Every output byte matched the respective VICE loader-return snapshot. The additional writes to $D020, $D260 and $D3A0 are to VIC registers while I/O is visible.

The resident-engine listing uses `parts/engine/work/play-hyde-park.vsf`, compared with `parts/engine/work/entry.vsf` at $0400. To reproduce the handover, arm a stop at $8A00 before clearing the Alex intro. Once it hits, capture the relocation stub if needed, then stop again at $0400. The stub copies $9000–$93FF to $0400–$07FF and jumps to $0400. The two 1,024-byte sequences are identical in the handover snapshot. The title snapshot is saved separately because its memory still holds bytes that a level overwrites.

## Tool checks and alternate disk

The headless check passed 56 checks, including exact stops, instruction stepping, and load and store watchpoints. Host-name keys failed. Matrix keys passed. The final quirk-probe phase raised a missing checkpoint-list key and VICE was restarted on its assigned port. Regenerator2000 answered on port 23114 on the title snapshot.

The 1990 TRH/Twins/Censor disk was also tried. Direct injection of its first PRG at its BASIC SYS target ($080D) reached an intro routine at $4125 and ultimately JAM at $F0CD in CPU history. The Alex image boots through normal autostart and is the working media set.
