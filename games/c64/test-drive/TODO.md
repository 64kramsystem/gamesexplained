# Test Drive analysis handoff

## Coverage

| Part | Explained | Tracked | Uncounted stretches | Uncounted bytes |
|---|---:|---:|---:|---:|
| title | 29310 | 29310 | 0 | 0 |
| car-select | 26842 | 26842 | 0 | 0 |
| driving | 34652 | 34652 | 0 | 0 |
| stage-1 | 1491 | 1491 | 0 | 0 |
| stage-2 | 1517 | 1517 | 0 | 0 |
| stage-3 | 1619 | 1619 | 0 | 0 |
| stage-4 | 1614 | 1614 | 0 | 0 |
| stage-5 | 1711 | 1711 | 0 | 0 |
| lamborghini | 1582 | 1582 | 0 | 0 |
| porsche | 1571 | 1571 | 0 | 0 |
| ferrari | 1582 | 1582 | 0 | 0 |
| corvette | 1161 | 1161 | 0 | 0 |
| gas-stop | 2713 | 2713 | 0 | 0 |
| high-scores | 1191 | 1191 | 0 | 0 |
| **All parts** | 108556 | 108556 | 0 | 0 |

The ledger counts the bytes assigned to the 14 captured parts. The listings have no uncounted stretches. Further executable loads identified in the media analysis may change the denominator.

## Handoff

- The exact ledgers and rebuilt listings cover the 14 captured parts. The kit’s root ledger is the sum of these part ledgers. The root has no independent image to export or list.
- The synchronized projects are `parts/title/work/resume-title-music-synced.regen2000proj`, `parts/car-select/work/resume-selector-complete-synced.regen2000proj`, `parts/driving/work/resume-driving-render-synced.regen2000proj` and `parts/corvette/work/resume-corvette-synced.regen2000proj`. The Lamborghini, Porsche and Ferrari projects are `work/resume-cockpit-synced.regen2000proj` under their part folders. The assigned live disassembler holds the earlier title project. Use the synchronized offline project for each corresponding export.
- The title owns the four side A directory pages at $2100–$24FF. Its two narrowly typed runtime symbols at $0075 and $028D prevent one-byte variables from claiming 63 bytes each. The runtime $1F00 page is excluded after store watchpoints at both ends.
- The 66 remaining open media items include raw sector runs on both sides and DOS files whose consumers have not been established. The private catalogue and address matches are in the local game work folder. The DOS-level LOAD trace caught the initial boot. The custom directory reader at $0CA6 and sector transfer at $0DDB provide separate probes for that disk path. Confirm any further executable loads before declaring the media complete.
- The unchanged DP tail at $2E00–$2E63 in the driving snapshot belongs to the selector. Side B GP and DP are documented there.
- No input recording was needed for the controlled module or routine probes. They establish dispatch, data and individual branches. They do not establish player routes to all five stages or outcomes.
- The accuracy sample found four errors in 70 comments. All four were corrected. Before a Silver declaration, a proven model should audit the listing and repeat the sample. The remaining feature questions are in `features.md`.
