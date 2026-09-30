# Jet Set Willy — facts

## Scope and evidence

The complete title-state physical RAM image, including both banks of room records and the resident game. Visible I/O and KERNAL overlays are excluded from the publication.

Technical statements below are traced from the contributor’s accurate disassembly and retained evidence ledger. The validation paragraph identifies checks repeated for publication. A traced claim is not labelled as a new live test.

## Rooms

There are 60 records of 256 bytes. Rooms 0–29 occupy $B000–$CDFF; rooms 30–59 occupy $E000–$FDFF. $2E55 copies a selected record to $0840 with RAM banked in, then restores the normal mapping.

## Packed terrain

Offsets $20–$9F store 32×16 cells, four two-bit cells per byte, most-significant pair first. The extraction loop starts at $2EE5 and calls $35A7. Offsets $A0–$CF hold six eight-byte glyphs for water, earth, fire, ramp, conveyor and item. The page shows the base terrain; conveyors, ramps, items, ropes and actors are separate passes.

## Room links

Offsets $DC–$DF hold up, down, left and right destinations. $E0 selects the first guardian record, $E1 supplies its count, and $E2=$FF enables a rope. The final 29 bytes are outside the active construction fields identified in the listing.

## Items and Maria

The item table at $22C3 contains 80 four-byte records, including taken flags. Collection increments the BCD counter at $0401. At BCD $50 it sets $0400; the analysed reader uses that flag to hide Maria in room 35. Treating it as a complete victory transition is unsupported by this executable.

## Moving hazards

Sixteen arrow records begin at $2403 and 181 guardian definitions at $2443. A room supports up to seven ordinary guardians. The 172 static sprite records occupy $4000–$6AFF. The rope publication buffer at $6B00–$6BBF is rewritten during play; the rope source bank starts at $8100.

## Validation

Every physical RAM byte was compared with the supplied dump. All 60 room records and their packed terrain were decoded for the page. The source consumer at $2EE5 establishes bit-pair order. Prior capture metadata supplies the boot and machine-state evidence; no new emulator measurement is asserted.

## Import provenance

Source: `jet_set_willy_full_listing.txt`. SHA-256: `5fd2c05616422d7a5c8c257157291e1a8d658e607f06dd01213b6346c7026147`. Imported 65,536 initialized bytes. The [annotated text export](reference/annotated-listing.txt) retains original labels, references and comments for the selected game spaces. `symbols.json` is the native symbol map; `listing.json` is its searchable Source representation.

## Publication checks

The native Source rows reproduce every initialized byte of the selected physical listing. The browser pass exercised all article controls and the Source tab in Firefox 157.0, with no script errors and no horizontal overflow at a 390-pixel viewport. These checks do not establish a full-game input route.
