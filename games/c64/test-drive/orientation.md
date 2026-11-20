# Test Drive on C64

## Image and machine

- Side A is the Decibel and Eagle Soft Incorporated D64, labelled THE LAST SCIENCE. [CSDb release](https://csdb.dk/release/?id=223076)
- Side B is the Eagle Soft Incorporated D64, labelled THE MASTER, from the separate side B upload. This disk reached the selector and the opening road with side A above. [CSDb release](https://csdb.dk/release/?id=102161)
- Each image is a 174,848-byte, 35-track sector dump. The kit reader found all 683 sectors on each side. The first side has eight directory entries and 607 used sectors outside named files. The second side has no readable PRGs in its DOS directory and 664 used sectors outside named files.
- VICE v3.14.0, macOS arm64 headless, PAL, dummy audio. The assigned MCP and monitor ports were 23120 and 23121. Regenerator2000 used 23122. The emulator check passed 56 checks and failed host-key F1 and the final server quirks phase. The latter stopped at a checkpoint-list response without the expected field. Matrix inputs worked.
- The side A hash is `a1f061698203e4f035a82c824115669b6efe266605ebdd1f8ab9ffcac315786d`. Side B is `7d58ab54cb4b0d081b2d6831329657fc440291686154347e5e07def34b2d059e`.

## Boot and driving

1. Cold reset and autostart the first PRG on `work/test-drive.d64`. Wait for the Eagle Soft and Decibel intro. Hold Space through the matrix until the loading screen appears. No trainer options were selected.
2. Wait for the Accolade logo and title key. Warp can speed up the serial transfers. Use the title image as the milestone, then press fire on port 2. Wait for the disk flip prompt.
3. Mount `work/side-b.d64` in drive 8 and press Return through the matrix. Wait for the Lotus specification screen. It can take several seconds in warp.
4. Press fire on port 2. Wait for the cockpit and road. Turn warp off for driving. `work/road.vsf` and `reference/opening-road.png` show the opening road. At the checkpoint on `$6A1B`, the relocated RD module is present and the first stage load is next. That snapshot is `work/road-entry.vsf`.

The title installs `$31DB` in the KERNAL IRQ vector at `$0314`. The selection screen uses `$33CB`, and play uses `$8AB3`. The driving handler enables I/O itself before touching VIC-II, and the saved driving snapshots can have `$01=$30` outside the interrupt. The hardware IRQ word under the KERNAL is `$16F4`. `work/probes.log` records one stop on a CIA1 port A load from the driving control routine and the native CPU history from the road renderer.

## Modules and local captures

| Snapshot or group | How it was reached |
|---|---|
| Title entry | Cold boot, dismiss the intro, stop at `$2E68`. |
| Car selector | At the disk flip prompt, attach side B and press Return. The breakpoint at `$2FB0` stopped on entry to TS, with X/Y equal to `TS`. The local entry is `work/selector-entry.vsf`. The Lotus screen was captured separately in `work/sideb2.vsf`. |
| Driving engine | Confirm Lotus and stop at `$6A1B` after the RD module has been relocated. |
| Four alternative cockpits | Restore the selector, set `$40` to 1 through 4 and enter the selector update at `$301E`. Stop at `$3057`, then press port 2 fire. Each capture reached `$6A1B` in the game's normal confirmation and loading path. |
| Stages 1–5 | Restore the RD entry at `$6A1B` and attach side B. Set `$52` to 0 through 4. Stop at `$6A2C` after the native R-file call and at `$6A37` after stage setup. The R modules occupy the same slot at `$3600` with a size stored in their four-byte headers. |
| GS and HS dispatch | From a stage-one snapshot, route the CPU to `$6D93` and `$6EE7` respectively. Watch the indirect jump at `$1AD8` and step into the module matching X/Y `GS` or `HS`. These captures establish the loaded modules and their relocation. |

## Disk to memory

The loader behind `$0800` accepts two-byte IDs in X and Y. The entry at `$081E` calls `$1A3A`, which relocates the entry word then jumps indirectly at `$1AD8`. The directory sectors on track 3 contain compact start and length records. The code at `$1987` wraps logical sectors at 16. `$19A9` and its following instructions translate logical tracks at or above `$24` through the table at `$1829`. Local `work/catalog.py` and `work/catalog.log` preserve the extraction and the mappings used in this run.

| File or ID | Evidence in RAM |
|---|---|
| TEST DRIVE!!/ESI | Initial PRG at `$0801`, BASIC SYS 2061, then cracker intro. A residue match survives elsewhere after boot. |
| DM | 5,498 of 5,794 payload bytes match the title snapshot at `$0800`. The resident jump table and its serial disk code live here. |
| DRIVE | Eleven bytes match $03F5–$03FF in the title snapshot. A CPU read watchpoint caught the resident startup flag read at $17CE. |
| CSET | 745 bytes. No distinctive 16-byte chunk matched the sampled title and selector captures. |
| Directory decoration | The differently named 74-byte entries share content. The scans found no distinctive 16-byte match for these or the 506-byte unnamed entry. Their use remains open. |
| CI, TS | Selector modules at `$2E64` and `$2FAC`. TS has a 1,811-byte executable body. |
| RD | Side B raw entry word `$6504`, relocated to `$6A04`. 13,927 of 14,465 bytes matched at `$6A00` immediately before the first stage load. |
| D1–D5 | Five cockpit modules relocated to `$2E64`. Each was found in the corresponding controlled capture. |
| R1–R5 | Each relocated to `$3600`. The entry at `$3604` installs pointers to that stage's sequence and element tables. |
| GS, HS | The controlled calls entered GS at `$B56B` and HS at `$E804`. The same HS item also has an unrelocated 1,191-byte match in the title-entry snapshot. |
| ## | All 7,546 bytes match the opening-road snapshot at `$A286–$BFFF`. The item is still being classified. |

The listings for the game are held under `parts/`, as the kit expects for programs with overlays. The root folder keeps the orientation, facts and media ledger.
