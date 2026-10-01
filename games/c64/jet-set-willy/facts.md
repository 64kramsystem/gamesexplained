# Jet Set Willy — checked facts

- **Boot (live):** CMM disk boots from hard reset to CMMO intro. Port 1 fire dismisses it; three `N` answers disable trainers. Return at the title reaches THE BATHROOM. Fresh captures are `reference/title.png` and `reference/play.png`.
- **Intro input (live trace):** `$2AF7` reads `$DC01`, compares with `$EF`, and jumps through `$2C23` when fire alone is held. Stepping observed A=$EF and the taken exit branch. This is boot provenance, not gameplay logic.
- **Code image (byte comparison):** boot title and play each match every imported code-typed byte (6,777) and word-typed byte (514). Title/play code agrees completely. Sprite storage `$4000–$6AFF` is unchanged. Room ranges differ at 16 and 24 bytes respectively; these are not assumed immutable.
- **Initialized gameplay (live):** IRQ vector changes from `$A801` at title to `$33E1` in play. Play processor port `$36`, DDR `$2F`; CIA2 port `$96` selects VIC bank `$4000`. The observed `$D018=$FF` selects screen `$7C00` and characters `$7800` in that bank.

## Verification work

Collection logic, collisions, guardians, arrows, ropes and winning route remain verification leads. The source export’s own tests do not verify these claims here. The interactive draft stays private until normal coverage/verification confirms it.

## Annotation checks

The 60 room records carry individual descriptions naming their captured room title and four exit ids. The sprite bank has 172 individual 64-byte records, each described as 21 three-byte rows plus alignment; sprite pointer arithmetic follows the C64 platform reference. Ghidra operand labels retain their actual offcut addresses. Post-row data descriptions were moved back to the row they describe; duplicate comments on the following row were removed. Runtime guardian work arrays, copied room glyphs and the indirect vector page are excluded from the authored-data ledger.

## Checked room and rope transfers

- **Room copy (live, controlled entry):** entering `$2E55` with each room id 0–59 copied exactly 256 bytes into `$0840–$093F`, stopping at `$2E7C`. Rooms 0–29 use `$B000 + id*256`; rooms 30–59 use `$C200 + id*256`. Each test compared the destination with the live source immediately before the call, because animated glyphs can change room records. All 60 cases restored processor port `$36`.
- **Rope staging (live, controlled entry):** the 34 words at `$1856` are `$8100 + position*192`. For each position 0–33, forcing the room rope flag and staging divider then entering `$16A2` copied the selected 192 bytes to `$0500–$05BF`; the check stopped at `$16E8` before coordinate processing. This verifies graphics staging, not player attachment or reachability.
- **Retained bootstrap (live, controlled entry):** `$D002` relocates 37 bytes from `$D015–$D039` to `$0334–$0358`. The relocated loop copies 8,192 bytes from `$D100–$F0FF` to `$E000–$FFFF` in descending pages, then restores `$01=$36`, enables interrupts and jumps to `$3C23`. All destination bytes matched the source captured before the test. This was a controlled execution of the retained routine, not an observed cold-boot hand-over.
- **Hidden room templates (traced):** `$D100–$DFFF` holds initialization source copies of rooms 30–44. They are distinct from the later playable records at `$E000–$EEFF`, whose glyph bytes can change. CPU references to `$DAAC`, `$DAF8`, `$DB70`, `$DB71`, `$DB98` and `$DB99` made with I/O visible write color RAM; those stores are not physical reads of the hidden templates.
- **Snapshot scope (live):** `work/entry.vsf` stops at `$2000` after Return leaves the healthy title snapshot, before the gameplay initializer. It does not capture the earlier crack/decompression hand-over.

- **Packed terrain (live, controlled entry):** the renderer at `$2E9C` was run for every captured room record, stopping at `$2F0F`. All 30,720 screen cells and color-RAM low nibbles matched an independent decoder: four two-bit cells per source byte, most-significant pair first. Tile codes come from `$222C`; colors come from record offsets `$D7-$DA`. The `$2F11` glyph-copy loop separately matched all 48 bytes from `$08E0-$090F` to `$7908-$7937`. The browser shows this base terrain only, before conveyor/ramp/object/sprite overlays.
- **Title music (live, controlled native loop):** after `$A0CD`, repeated calls to `$A139` ended with pointers `$7246`, `$7350`, `$7518`, end flag `$FE=$FF` and SID volume zero. Voice 1 supplies 803 note/duration pairs and the terminal `$FF,$FF`; voice 2 consumes 132 pairs and voice 3 consumes 228 pairs.

- **Frame reconstruction (live capture):** `C64.renderFrame` matched all 104,448 pixels of one initialized gameplay frame. The trimmed renderer input contains 1,409 RAM bytes in 17 runs, plus color memory and display-register state. The page's sprite toggle changes the sprite-enable register in a copy of this capture. This is a rendering check, not a timing or collision test.

## Retained copyright and restart behavior

The retained loading-complete/copyright code spans `$3A02-$3CD2`. Its four-color checker at `$3C23` first treats any entered byte with bit 7 set as incomplete, then compares all four bytes with `$3A81-$3A84`. A controlled correct code reached `$3C3A`; changing each individual digit reached `$3C4E`; one `$FF` slot reached `$3C00`. The success routine copied all nine bytes of its cartridge header from `$3C62` to `$8000`. The captured expected-color base word is `$2C57`; its origin is open and no unpatched protection-sheet layout is inferred.

**RESTORE versus reset (live):** both reach the success header's entry stub `$0FA0`. RESTORE preserves DDR `$2F` and port `$36`, and the jump to `$A000` fetches the RAM title's `JMP $A744`. A CPU reset, checked with a positive checkpoint at KERNAL reset entry `$FCE2`, reaches the stub with DDR `$00` and port readback `$17`. Clearing bit 0 in the port latch cannot drive the banking pins while the direction register is zero. At the subsequent `$A000` jump, CPU-visible bytes are BASIC ROM `94 E3 7B`, while physical RAM contains `4C 44 A7`. The stub never initializes the direction register. This finding applies to the captured CMM disk image.

The third trainer answer led through the retained decompressor: a store checkpoint stopped with PC `$011E` after writing `$22` to the gap byte `$3CDE`, matching the later title/play capture. This identifies its producer, not the purpose of the surrounding gap. A packed-data relocation also wrote `$AEBD`; that byte changed again to its final captured value during unpacking. These observations do not establish an active gameplay consumer.
