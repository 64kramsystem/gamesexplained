# Vigilante — orientation

The analysis uses the Data East USA disk from the C64 Preservation Project's 10th Anniversary Collection. The archive member is `c64pp-g64-zip/v/vigilante[data_east_1988].zip`, containing a 286,164-byte image with the `GCR-1541` header. The local copy is `work/vigilante.g64`, SHA-256 `40477fe2561c37ea93bcc82095943f822119170c6956d4874d469b08e22d3c9c`.

[Preservation collection](https://archive.org/details/C64_Preservation_Project_10th_Anniversary_Collection)

## Boot and play

1. Start the kit's VICE C64SC with dummy audio. The installed macOS arm64 headless build is v3.14.0. The kit health check reported 56 passes and failures in `keys-host` and `no-exception`. Matrix keys, PC stops and instruction counts passed.
2. Hard reset and autostart the G64 from unit 8. The initial `VIGILANTE` file loads at `$0110` and reaches `$0203` during the load. VICE reports ending its autostart sequence there. The game's loader continues independently. Turn warp on if it stopped when VICE ended autostart.
3. Stop on execution at `$0D6B` before the engine's startup decode. Save `work/entry.vsf`, with the disk and without ROM images. At this stop, RAM `$0314` contains `$EA31`, the effective processor port reads `$37`, and the RAM IRQ vector contains `$FFFF`. At this point `COD1` matches the entire 13,055-byte disk payload.
4. Resume until the Hall of Fame appears. Turn warp off and save `work/title.vsf`. Hold port 2 fire for 25 frames, release and let the loading and story screens advance. Hold port 2 fire again for 60 frames when the story is showing. Save `work/play-round1.vsf` once the street and player are visible. For an input-ready baseline, advance another 150 frames without input and save `work/round1-steady.vsf`. The street at the start is shown in `reference/stage-1.png`.
5. RAM `$FFFE` points to `$0F32` during play, with processor port `$35` and the KERNAL banked out. `$0314` instead points to `$0F38`. Non-stopping instruction checkpoints hit `$0F51` and `$0F90` four times apiece over four frames. The full-frame capture stopped when VICE exited during checkpoint cleanup. The two smaller instruction probes worked after a VICE restart and snapshot restore.

The boot chain installs `FAST` at `$7000` and runs `VIG1` at `$0800`. VIG1 loads the bitmap splash, colour cells and screen cells. It then loads the resident files and jumps to `$0D6B`. The engine snapshot for the listing is `parts/engine/work/play-round1.vsf`, where the startup section has been decoded into instructions. Its handover snapshot retains the pre-decode bytes.

## Stage loads

The five files arrive at the same addresses for each stage. The engine keeps `COD1`, its load dispatcher, the panel and the common sprite library resident. To reach each stage without a playthrough, restore `work/play-round1.vsf`, set `$0D16` to the zero-based stage number, set PC to `$3C33` and resume with warp on. `$3C43–$3C49` computes five times the stage index. Stop at `$0D98`, where the engine resumes initialisation. A non-stopping checkpoint at `$3C5B` counted five completed file loads per stage. Compare the disk payloads to RAM at the stop. Save each part's `work/entry.vsf` there and `work/play.vsf` after the street appears. Hold fire through the message, then release it when the playfield is visible. The extractor and local route script are under `work/`.

| Load or purpose | Address range | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 |
|---|---|---|---|---|---|---|
| Tile character patterns | `$4000–$47FF` | A | F | K | P | U |
| Character and colour maps | `$5400–$79FF` | B | G | L | Q | V |
| Stage parameters and message | `$7A00–$7AC9` | C | H | M | R | W |
| Actor headers and scripts | `$CB00–$CFFE` | D | I | N | S | X |
| Stage sprite image slots and ROM fill | `$E000–$FEFF` | E | J | O | T | Y |

| Other file | Load range | Evidence |
|---|---|---|
| VIGILANTE | `$0110–$0208` | First directory item, hardware autostart stub |
| FAST | `$7000–$71DF` | Exact body except three bytes at engine handover, overlaid by stage maps |
| VIG1 | `$0800–$094F` | Boot stub and file names, partly overwritten by LOADER |
| LSTXT | `$0400–$07E7` | Exact match at engine handover |
| LSHIRES | `$2000–$3F3F` | Loaded before COD1, which occupies this address range at handover |
| LSCOL | `$D800–$DBE7` | Splash colour RAM, outside the snapshot's ordinary RAM array |
| PCOL.DAT | `$D800–$D8EF` | Panel colour RAM, outside the snapshot's ordinary RAM array |
| LOADER | `$0900–$0CFE` | Exact handover match, deliberately retained and called by the stage dispatcher |
| COD1 | `$0D00–$3FFE` | Exact handover match |
| PANAL.DAT | `$4800–$50EF` | Exact handover match, panel glyphs and initial six rows of screen cells |
| SPRITES | `$8000–$CAFE` | Exact handover match, includes executable routines and music tables |
