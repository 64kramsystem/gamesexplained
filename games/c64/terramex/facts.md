# Terramex facts

Terramex uses a separate explorer-selection program and expedition program in the RCS/HCC release. The selector's `$5A00` maps the cursor to an explorer index. The accepted selection copies one 4,032-byte sprite block at selector `$5B0C` and leaves the ID in `$0300`. The expedition reads the ID at main `$810D` to choose a sprite colour and uses it at main `$82A1` to install twelve explorer parameter bytes. Main `$A310` reads the selected sprite data at `$F036` in 63-byte records.

| Listing | Snapshot | Addresses |
|---|---|---|
| [Explorer selection](parts/selection/facts.md) | `parts/selection/work/selection.vsf` | Portrait renderer, controls and all five explorer sprite blocks |
| [Expedition](parts/main/facts.md) | `parts/main/work/entry.vsf` | Game initialization, title, map, actors, items, HUD and sound |

## Media and remaining boundaries

The two answers in [media.json](media.json) refer to the RCS/HCC disk used for this analysis. A comparison against the separately released ROM disk found its `MENUE/ROM` data near selector `$4800`, its `MEN 0/ROM` through `MEN 4/ROM` image portions at the five corresponding explorer ranges, and `ZEI 1/ROM` within two bytes of the 4,096-byte scenery charset block at expedition `$4800`. Those are corroborating layouts across two releases. Runtime route and load observations here belong to RCS/HCC. The original disk-side prompt is retained in the expedition at `$A273` and the message choice is controlled by `$A2E8`. Other routes to that prompt, alternate-release file boundaries, and disk activity during later play remain open.

## Listing coverage

The final coverage queue and missing byte ranges are in [TODO.md](TODO.md). The analysis retains open code and data where address evidence did not establish a role. In particular the expedition image contains a large instruction-like block after `$E51C`. Direct flow from the initializer, hardware vectors, and three decoded word dispatch tables does not resolve its entry. It stays in the main ledger without an attributed purpose.

## The listing's error rate

A same-model independent sample drew 60 of 300 listing comments with seed 56119. The checker used `gpt-6.2-sol`. Ten comments had incorrect details, for an estimated rate of 16.7% with a 95% Wilson interval of 9.3% to 28.0%. All ten sampled errors were corrected. The errors concerned banked interrupt paths, conditional map expansion, sprite buffer selection, dispatch state, coordinate inputs and action operands. The estimate applies to the listing before the corrections. The checker may have missed other errors.
