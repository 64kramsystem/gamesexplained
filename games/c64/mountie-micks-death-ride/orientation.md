# Mountie Mick's Death Ride orientation

The [CSDb disk build](https://csdb.dk/release/?id=246550) contains one sequentially loaded PRG, `DEATH RIDE /MEGA`, starting at $0801. The local image is `work/Death_Ride.d64`. It has 174,848 bytes, the size of a 35-track D64 without an error map. The disk reader found 683 sectors, one 150-block file and zero allocated sectors outside the file. The directory label is DIGITAL DUNGEON. The release attribution to The Mega Team is tentative.

## Boot to Train 1

1. Start the installed macOS arm64 VICE v3.14.0 headless build with dummy audio. Use the worktree's MCP port 17444 and monitor port 17445. Autostart the first file on the disk. It loads and RUN executes the BASIC stub's SYS 2064.
2. Wait for the crack intro. Its coloured bars show on a black screen. Hold Space through the keyboard matrix at row 7, column 4 for about two seconds, then release. No training options were selected.
3. Wait for the illustrated Reaktör loading picture. Joystick fire on port 2 takes the loading-picture loop's exit at $C7D8. Release fire and wait for the title and score table. The staging snapshot is `work/loading-screen.vsf`.
4. Hold joystick fire on either port to start Train 1, then release. The listing uses `work/play-train1.vsf`, with Mick visible atop the first display of the train. The loading and title pictures and train screens are in `reference/`. To reproduce the session's exact breakpoint sequence, use the ignored `work/entry-trace.py` from this worktree.
5. For the handover, arm a stopping execute breakpoint covering $1000 through $107F at the loading-picture exit, then resume. The first engine stop is $1000 with CPU port $37, A=$37 and SP=$FF. Save it without ROMs as `work/entry.vsf`. Startup changes the two 256-byte tables at $1CC4 and $9000. The play snapshot preserves their adjusted values and the code used during the race.

## Memory and interrupts

The engine's play snapshot had CPU port $15, with I/O visible and BASIC and KERNAL out. It uses the hardware IRQ vector $FFFE-$FFFF, rather than the KERNAL vector at $0314. During play the hardware vectors in RAM point to $107F for NMI and reset and $1220 for IRQ. Title code at $8CCD instead installs $8525. The VIC uses the bank at $4000, with two screen bases ($4000 and $4400), graphics starting at $4800 and split-dependent character selection. Regenerator2000 answered on its assigned port 17446 with the full 64 KiB play image.

## Loader and parts

The loader expands the crack intro and moves through the illustrated loading picture. The second mover copies packed bytes up through RAM with $01=$34 and a descending page loop at $082F-$0840. The unpacker runs from $0100 and writes to an ascending pointer at $AE/$AF. Its final jump at $012B reaches $1000 with the output pointer at $AC10. Store watchpoints at $BB00, $D100, $E100 and $F900 stopped in the mover at $0839 after its store. Store watchpoints at $1000, $A700 and $A800 also caught the unpacker's literal copy at $0166. The runtime image therefore ends at $AC0F, with packed residue above it until startup installs the hardware vectors.

The only directory file contains both loader and engine payload. Comparison of 16-byte pieces finds no full placed copy in either engine snapshot. The nine train script pointers reference resident data at $922C-$94EB. There is one analysis part for this disk build.

## Emulator preflight

The preflight recorded 56 passes and two failures. Host-key F1 produced no input. The final server-quirks check ended with a `KeyError('checkpoints')`. Cold-boot orientation used matrix input. Execute breakpoints, store watchpoints, stepping, frame advance and snapshot restore passed their preflight checks.
