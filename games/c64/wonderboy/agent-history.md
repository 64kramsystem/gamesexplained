# Analysis history

- Reused the installed PAL VICE 3.14.0 headless build and Regenerator2000 0.9.18 on the assigned ports, 17428 and 17430. Dummy audio was set before startup. The emulator check passed 55 of 57 tests.
- Captured the trainer exit at `$082A` and a separate steady-state snapshot in Area 1, Round 1. The disk's only program loses its packed representation when it depacks.
- Seeded the disassembler with the observed execution map and followed the actor, SID, floor and sprite dispatch tables. Exported the annotations to the symbol map and rebuilt the listing from the local snapshots.
- Recovered the server after its first failed frame capture and collected targeted instruction and store-watch evidence. A paced retry of the full capture reproduced the disconnect. Kept the queue and open ownership questions in TODO.md.
- Resumed the live analysis on the existing branch and reproduced the previous
  listing from the saved play snapshot before editing. Bounded the screen
  clear, round-start opcode rewrite, four character-tail streams and selector
  $19 score reads with targeted traces. Re-exported the symbols and rebuilt
  the listing. The coverage ledger reached 53,133 of 53,596 tracked bytes,
  with five ranges still uncounted.
- Closed 463 bare bytes, then accounted for all five retained stretches.
  Depacker store watches established provenance, and CPU traces established
  the badge and event-list read limits. The exact ledger reached 54,703
  explained of 54,703 tracked bytes with no uncounted stretches.
- Checked round advancement, checkpoint selection, boss setup and the
  raster sprite writes. The independent sample found 15 errors in 65
  comments. Corrected the findings and the related array annotations.
  No verification required a recorded input route.
