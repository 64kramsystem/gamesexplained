# Analysis handoff

| Part | Explained | Tracked | Uncounted |
|---|---:|---:|---:|
| Explorer selection | 25,359 | 25,359 | 0 |
| Expedition | 54,430 | 54,430 | 0 |
| Total | 79,789 | 79,789 | 0 |

- The game has two exported symbol maps and source listings. The kit expects the listing and symbol map in each part folder.
- The unresolved gameplay questions are the final route and conditions for the ending, the reachable conditions for the retained disk-side prompt, and some item and actor identifications. The two prefix bytes at expedition `$3FFE–$3FFF` remain in the ledger, with their purpose open.
- `work/` holds the disk images and CPU probes. Each part's `work/` holds its snapshots, annotation log and ledger. [Orientation](orientation.md) gives the boot route and input image hash.
- Step 65 did not require an input recording. The short probes use the saved snapshots and verify instruction paths and memory accesses directly.
- The earlier independent sample found 10 errors in 60 comments before corrections. It measures that earlier listing. A full audit remains for a later run. The kit requires a proven-model check and the remaining site stages for Silver.
