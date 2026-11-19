# Blood Money analysis handoff

Step 50 is incomplete. The exported symbol maps and rebuilt listings give these exact ledger figures.

| Part | Explained bytes | Tracked bytes | Bare bytes |
|---|---:|---:|---:|
| Resident engine | 10,904 | 33,873 | 22,969 |
| Level 1 | 14,723 | 21,469 | 6,746 |
| Level 2 | 14,724 | 21,469 | 6,745 |
| Level 3 | 13,373 | 21,470 | 8,097 |
| Level 4 | 14,401 | 21,469 | 7,068 |
| Total | 68,125 | 119,750 | 51,625 |

The largest engine gaps include the graphics around `$6F43`, the sound code around `$E44B`, and the routines and tables at `$2765` and `$38E0`. In the overlays, the remaining LEVEL bytes include commands and data after the event terminator and bytes after the sprite pointer tables. The DATA tails past the last indexed sprite record also remain bare. A file's disk load proves where its bytes go. Additional consumers must be traced before assigning meanings or excluding any tail.

The Syntax disk supplied the complete fourth-level load. Its separate boot PRG and picture remain open in `media.json`. The Accept disk and the two level 4 routes are documented in [orientation.md](orientation.md). The exact code and data work queues are reproducible with `coverage.py` on each part folder.

The analysis stopped at Step 50. Step 60 verification and the independent listing sample remain pending. The handoff has written reproduction routes and no replay recording. The model gate requires a proven-model check before any Silver designation.
