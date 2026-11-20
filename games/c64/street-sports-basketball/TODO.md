# Remaining analysis

Step 50 is incomplete. These figures come from the rebuilt listings and the kit ledger.

| Part | Explained bytes | Tracked bytes | Uncounted stretches | Bytes in those stretches |
| --- | ---: | ---: | ---: | ---: |
| Menu | 56,188 | 57,775 | 10 | 4,983 |
| Match | 17,519 | 57,759 | 7 | 1,344 |
| Combined | 73,707 | 115,534 | 17 | 6,327 |

Each part's listing was built from its own ignored `work/entry.vsf`. Run `coverage.py` on each part and the game for the remaining work queue. The game-level ignored `work/` has the load traces, watchpoint logs, court hand-overs and repeatable scripts.

- Selection. Identify provenance of packed RAM outside the proven menu assets, especially the pockets at $4CDE, $5001, $ACAC and $BB1F and the hidden RAM after $D400. The retail downloads returned HTTP 401, the LCX boot stayed on a striped border and the TBF M file is identical. Keep those stretches open until a clean hand-over or CPU evidence resolves them.
- Match. Finish movement, ball handling, computer decisions, pose states and sound. Classify the rest of A's art and tables, the disk transition workspace and RAM at $D700. In the match hand-over, $D000–$D6FF is a byte-for-byte copy of the parked menu pages at $0800–$0EFF. It is counted on the menu side where applicable.
- Media. Finish A's placements and determine the purpose of file L and the deleted entry.
- The verification and recording steps depend on completing the coverage gate. The kit does not list gpt-6.2-sol as proven, so the recorded tier is Bronze.
