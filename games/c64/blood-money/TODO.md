# Blood Money analysis handoff

The exact coverage ledger passes for the engine and all four overlays. The rebuilt listings report zero uncounted stretches.

| Part | Explained bytes | Tracked bytes |
|---|---:|---:|
| Resident engine | 31,749 | 31,749 |
| Level 1 | 21,469 | 21,469 |
| Level 2 | 21,469 | 21,469 |
| Level 3 | 21,470 | 21,470 |
| Level 4 | 21,469 | 21,469 |
| Total | 117,626 | 117,626 |

The engine and levels 1 through 3 use their part's `work/entry.vsf`. Level 4 uses `work/menu-entry.vsf`. The exported projects matching the listings are in each part's `work/resume-coverage.regen2000proj`. The disks, play snapshots, instruction watchpoint logs and independent sample are in the ignored work folders. The local rebuild command is `bash games/c64/blood-money/work/rebuild_analysis.sh`.

The written routes in [orientation.md](orientation.md) reproduce the loader handovers. The verification probes start from saved states and test individual routines. The scoped analysis uses those routes and probes as its evidence, so 65-inputs did not require a recording.

A listing audit is recommended. The first sample verified seven errors in 60 comments before corrections. [Facts and sample results](facts.md)

The game remains Bronze pending a proven-model check and the minisite and reader review required for Silver. Score persistence and the consumer of the two extra hull mask banks at $5A00 and $5A80 remain open.
