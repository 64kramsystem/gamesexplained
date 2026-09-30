# The NeverEnding Story — orientation

## Build and scope

Ocean disk release; resident adventure engine and captured PART1. The resident engine and captured PART1 content at $0000–$CFFF. The I/O/ROM window is uninitialized in the analysis. PART2 and PART3 are separate loads and are not represented by reusing the captured graphics addresses.

## Route and capture

The preserved VICE snapshot and CPU-view dump describe the same Part 1 session, paused while waiting for Space through KERNAL keyboard scanning. The prior capture records part number 0, room 1, and picture 4. Snapshot physical RAM agrees with the dump at $0002–$CFFF; port bytes and the banked I/O/ROM window have different meanings. The C64MEM RAM offset in this snapshot is 177. This publication uses the existing stopped-state evidence, without claiming a new complete adventure replay.

## Machine state

CPU port $36, direction $2F; CURRENT_PART_NO at $2940 is 0, CURRENT_ROOM at $293F is 1, CURRENT_ROOM_GRAPHIC_ID at $2942 is 4. The picture split at $A7E3 selects screen $CC00, bitmap $E000 and black background.

## Reproduction

Keep the supplied image and any recovered snapshots under `work/`. Import `neverending_story_full_listing.txt` with `kit/c64/import_ghidra.py` (introduced by the Castle Master contribution). Use `--verify-ram` with the supplied 65,536-byte dump when one exists. The Source tab is built from the text export directly; no synthetic snapshot is created. 53,248 initialized bytes are represented; uninitialized ranges remain gaps.

Original listing SHA-256: `ef4cadfc4fb0bbe410a3a0881d8ca9da6c877c19ef9579ce2f07147c66f90e12`. Binary media and emulator state are not published.
