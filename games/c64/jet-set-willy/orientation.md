# Jet Set Willy — orientation

## Build and scope

CMM disk release; physical RAM at the title after trainer answers N, N, N. The complete title-state physical RAM image, including both banks of room records and the resident game. Visible I/O and KERNAL overlays are excluded from the publication.

## Route and capture

The contributor capture records the CMM disk boot followed by three N answers to the trainer. The title is the stable capture point. Return or joystick-port-2 fire proceeds through $2000 to game setup at $2C57. The recorded PC is inside the title loop and is not a standalone load address. This contribution imports that prior capture and analysis; it does not claim a new emulator playthrough.

## Machine state

PC $A8A4; A $02, X $30, Y $00, SP $90, P $21; CPU port $36, direction $2F. The raw bytes at $0000/$0001 are underlying RAM, not those port registers.

## Reproduction

Keep the supplied image and any recovered snapshots under `work/`. Import `jet_set_willy_full_listing.txt` with `kit/c64/import_ghidra.py` (introduced by the Castle Master contribution). Use `--verify-ram` with the supplied 65,536-byte dump when one exists. The Source tab is built from the text export directly; no synthetic snapshot is created. 65,536 initialized bytes are represented; uninitialized ranges remain gaps.

Original listing SHA-256: `5fd2c05616422d7a5c8c257157291e1a8d658e607f06dd01213b6346c7026147`. Binary media and emulator state are not published.
