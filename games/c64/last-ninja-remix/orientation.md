# Last Ninja Remix — orientation

## Build and scope

Ikari & Talent disk release; resident kernel plus Central Park active occupant. Central Park, including the resident loader, retained music, scene data and gameplay engine. This is a static composition of the loaded files, not a 64 KiB stopped-machine snapshot. Later levels and the crack introductions are outside the analysed occupant.

## Route and capture

The prior evidence records this route: boot the first disk, use control-port-1 fire at the TSM presentation, Space at the Ikari & Talent presentation, select the first level with F7, and acknowledge the Central Park title. The listing models the resulting loaded occupant. Its volatile workspace is deliberately uninitialized, so its bytes must not be launched as a snapshot. The reference scene is the prior analysis reconstruction, not a new emulator screenshot.

## Machine state

Initialized: $0000–$0001 and $0E00–$FEFF, 61,698 bytes. Uninitialized: $0002–$0DFF and $FF00–$FFFF. Stored port bytes $F7/$FF are file provenance and do not establish runtime banking.

## Reproduction

Keep the supplied image and any recovered snapshots under `work/`. Import `last_ninja_remix_full_listing.txt` with `kit/c64/import_ghidra.py` (introduced by the Castle Master contribution). Use `--verify-ram` with the supplied 65,536-byte dump when one exists. The Source tab is built from the text export directly; no synthetic snapshot is created. 61,698 initialized bytes are represented; uninitialized ranges remain gaps.

Original listing SHA-256: `0bea0daf6690509394db7e9f827a5b0ec1be478ed7ea4ac6cfac8f8d3d675a76`. Binary media and emulator state are not published.
