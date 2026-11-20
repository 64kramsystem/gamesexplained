# Test Drive analysis handoff

## Coverage

| Part | Explained | Tracked | Uncounted stretches | Uncounted bytes |
|---|---:|---:|---:|---:|
| title | 4709 | 10603 | 10 | 3603 |
| car-select | 1561 | 2761 | 1 | 4096 |
| driving | 25602 | 34592 | 3 | 1219 |
| stage-1 | 1491 | 1491 | 0 | 0 |
| stage-2 | 1517 | 1517 | 0 | 0 |
| stage-3 | 1619 | 1619 | 0 | 0 |
| stage-4 | 1614 | 1614 | 0 | 0 |
| stage-5 | 1711 | 1711 | 0 | 0 |
| lamborghini | 1010 | 1582 | 0 | 0 |
| porsche | 1010 | 1571 | 0 | 0 |
| ferrari | 1010 | 1582 | 0 | 0 |
| corvette | 258 | 1161 | 0 | 0 |
| gas-stop | 2229 | 2713 | 0 | 0 |
| high-scores | 1191 | 1191 | 0 | 0 |
| **All parts** | 46532 | 65708 | 14 | 8918 |

The ledger counts the bytes assigned to the 14 captured parts. The uncounted stretches are outside its denominator. Any further executable loads identified in the media analysis may change the denominator.

## Open analysis

- Resolve the title and selector RAM that the listings report outside the ledger. The selector entry at $2FB0 and the steady-state Lotus snapshot are both available.
- Finish the routine and data queue in the title, car selection, common driving engine, car-specific overlays and gas-stop module. Use the listings’ uncounted ranges and the per-part coverage commands to locate remaining bytes.
- Follow the resident directory and unpacker for the disk items the game loads by ID. The private directory extraction and address matches are available in the root work folder. The DOS-level LOAD trace caught the initial boot but did not enumerate private disk reads.
- Resolve the 69 open media items. The listings and loader note account for 2 of the 71 items enumerated by the kit.
- Re-run exact game and part ledgers before starting formal verification. The instruction traces and watchpoints recorded during analysis can be rerun from the saved snapshots. The remaining feature claims and any workflow-required recordings follow the coverage gate.
- Record the independent listing accuracy sample only after the coverage gate passes. The kit marks gpt-6.2-sol as unproven for a Silver tier declaration.
