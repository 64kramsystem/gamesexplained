# Analysis history

- Reused the installed PAL VICE 3.14.0 headless build and Regenerator2000 0.9.18 on the assigned ports, 17428 and 17430. Dummy audio was set before startup. The emulator check passed 55 of 57 tests.
- Captured the trainer exit at `$082A` and a separate steady-state snapshot in Area 1, Round 1. The disk's only program loses its packed representation when it depacks.
- Seeded the disassembler with the observed execution map and followed the actor, SID, floor and sprite dispatch tables. Exported the annotations to the symbol map and rebuilt the listing from the local snapshots.
- Recovered the server after its first failed frame capture and collected targeted instruction and store-watch evidence. A paced retry of the full capture reproduced the disconnect. Kept the queue and open ownership questions in TODO.md.
