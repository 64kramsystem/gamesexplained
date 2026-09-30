# Jet Set Willy — checked facts

- **Boot (live):** CMM disk boots from hard reset to CMMO intro. Port 1 fire dismisses it; three `N` answers disable trainers. Return at the title reaches THE BATHROOM. Fresh captures are `reference/title.png` and `reference/play.png`.
- **Intro input (live trace):** `$2AF7` reads `$DC01`, compares with `$EF`, and jumps through `$2C23` when fire alone is held. Stepping observed A=$EF and the taken exit branch. This is boot provenance, not gameplay logic.
- **Code image (byte comparison):** boot title and play each match every imported code-typed byte (6,777) and word-typed byte (514). Title/play code agrees completely. Sprite storage `$4000–$6AFF` is unchanged. Room ranges differ at 16 and 24 bytes respectively; these are not assumed immutable.
- **Initialized gameplay (live):** IRQ vector changes from `$A801` at title to `$33E1` in play. Play processor port `$36`, DDR `$2F`; CIA2 port `$96` selects VIC bank `$4000`. The observed `$D018=$FF` selects screen `$7C00` and characters `$7800` in that bank.

## Verification work

The imported room format, collection logic, collisions, guardians, arrows, ropes and winning route remain verification leads. The source export’s own tests do not verify these claims here. The interactive draft stays private until normal coverage/verification confirms it.

## Annotation checks

The 60 room records carry individual descriptions naming their captured room title and four exit ids. The sprite bank has 172 individual 64-byte records, each described as 21 three-byte rows plus alignment; sprite pointer arithmetic follows the C64 platform reference. Ghidra operand labels retain their actual offcut addresses. Post-row data descriptions were moved back to the row they describe; duplicate comments on the following row were removed. Runtime guardian work arrays, copied room glyphs and the indirect vector page are excluded from the authored-data ledger.
