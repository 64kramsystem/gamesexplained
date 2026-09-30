# The NeverEnding Story — facts

## Scope and evidence

The resident engine and captured PART1 content at $0000–$CFFF. The I/O/ROM window is uninitialized in the analysis. PART2 and PART3 are separate loads and are not represented by reusing the captured graphics addresses.

Technical statements below are traced from the contributor’s accurate disassembly and retained evidence ledger. The validation paragraph identifies checks repeated for publication. A traced claim is not labelled as a new live test.

## Picture records

$0BF9–$0D4E contains 57 six-byte descriptors: destination row, destination column, source pointer, height and width. Only descriptors 0–20 belong to the captured picture payload. Descriptor 0 points to $A100; 1–20 tile $4300–$93E5.

## Picture rows

$05BF draws a descriptor and $0676 copies its component rows. Each character row stores 8×width bitmap bytes, width screen bytes, and width color bytes. In multicolor mode the pairs 00, 01, 10, 11 select black, screen high nibble, screen low nibble and color-RAM low nibble. The page reconstructs these records directly.

## Adventure rules

The command parser entry is $122F. Actions and conditions use separate dispatch tables: 33 action words at $0DE3 and 10 condition words at $1193. Calls at $1641 and $1699 are rewritten to their selected handlers. Those tables and their consumers are preserved in the Source tab.

## Overlay boundary

Descriptors 21–56 are valid resident metadata for replacement picture occupants. Their payload is absent from this capture. PART_ROOM_BASE_IDS at $0DCC stores room-number bases, not picture indexes. The loader remains in scope while later-part narrative and graphics remain open.

## Object artwork

Object image slots start at $A560 at a stride of 160 bytes. Some slots have been reused by active code or retain excluded introduction bytes. The listing distinguishes those occupants, so treating the whole span as intact icons would decode code as artwork.

## Validation

Every initialized byte below $D000 was compared with the contributor dump. All 21 captured picture descriptors were checked for bounds, and descriptors 1–20 form an exact contiguous chain ending at $93E6. The row format and color selection were cross-checked against the retained illustration note and source consumers.

## Import provenance

Source: `neverending_story_full_listing.txt`. SHA-256: `ef4cadfc4fb0bbe410a3a0881d8ca9da6c877c19ef9579ce2f07147c66f90e12`. Imported 53,248 initialized bytes. The [annotated text export](reference/annotated-listing.txt) retains original labels, references and comments for the selected game spaces. `symbols.json` is the native symbol map; `listing.json` is its searchable Source representation.

## Publication checks

The native Source rows reproduce every initialized byte of the selected physical listing. The browser pass exercised all article controls and the Source tab in Firefox 157.0, with no script errors and no horizontal overflow at a 390-pixel viewport. These checks do not establish a full-game input route.
