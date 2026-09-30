# Last Ninja Remix — facts

## Scope and evidence

Central Park, including the resident loader, retained music, scene data and gameplay engine. This is a static composition of the loaded files, not a 64 KiB stopped-machine snapshot. Later levels and the crack introductions are outside the analysed occupant.

Technical statements below are traced from the contributor’s accurate disassembly and retained evidence ledger. The validation paragraph identifies checks repeated for publication. A traced claim is not labelled as a new live test.

## Main loop

$8F55 sequences normalized input ($9418), player update ($A422), opponent state ($ADC1), action events ($AA25), projectiles ($B7B9) and rendering ($BF87). Player and enemy animation channels share the interpreter at $A802.

## Sprite compression

The 162 little-endian words at $CE54–$CF97 resolve by adding $0E54. Their records tile $CF98–$E927. Decoder $BF43 treats $68 as an escape for the next literal byte, $69–$6F as runs of one to seven zeros, and all other bytes as literals. All 162 records expand to exactly 63 bytes. The runtime continues while the output count is below 63, so exact length is a property of this corpus, not an overshoot guard.

## Actor composition

The frame pointer table at $C4C2 holds 106 entries. $BBC0 composes player slots 0–2 and opponent slots 4–6; slots 3 and 7 also carry moving components. Output is merged into fixed sprite buffers at $0C00–$0FC0. Frame descriptors choose components and placements rather than a single whole-character sprite.

## Scenery

The header at $4DE4 includes 32 area/root selections. The pointer table at $4E27 has 118 entries: 85 leaves and 33 composites. A leaf stores width and height in its first byte, then 8 bitmap bytes and two color bytes per cell, for 1+10×width×height bytes. $8A52 traverses the scene and clips it to a 30×18-cell viewport.

## Combat and persistence

Player energy is $0229; $B54A subtracts it and can latch death at $00B6. Opponent energy is $022A. $B568 records defeat, and $B5C7 restores or spawns an opponent using per-area state at $012D–$0198. Fifteen 14-byte object/trigger records start at $C0D0.

## Sound

The retained music module occupies $4000–$4DE3. Its four jump entries initialize a song ($4000), tick the player ($4003), set control state ($4006), and increment a pause/gate byte ($4009). The main interrupt handler is $1E15.

## Validation

All initialized rows are preserved and unknown workspace remains a gap. All 162 sprite streams were decoded, their lengths checked, and their encoded boundaries compared with the next pointer. The prior reconstructed scene and sprite sheet are retained as references. No new live combat or later-level verification is claimed.

## Import provenance

Source: `last_ninja_remix_full_listing.txt`. SHA-256: `0bea0daf6690509394db7e9f827a5b0ec1be478ed7ea4ac6cfac8f8d3d675a76`. Imported 61,698 initialized bytes. The [annotated text export](reference/annotated-listing.txt) retains original labels, references and comments for the selected game spaces. `symbols.json` is the native symbol map; `listing.json` is its searchable Source representation.

## Publication checks

The native Source rows reproduce every initialized byte of the selected physical listing. The browser pass exercised all article controls and the Source tab in Firefox 157.0, with no script errors and no horizontal overflow at a 390-pixel viewport. These checks do not establish a full-game input route.
