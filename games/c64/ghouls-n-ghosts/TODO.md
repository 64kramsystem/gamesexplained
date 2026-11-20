# Analysis handoff

Steps through verification are complete for the local analysis handoff. Step 65 required no recording because the probes used instruction stops, watchpoints and debugger-driven state changes. They make no claim about reaching those states with a recorded input route.

| Part | Explained | Tracked | Uncounted stretches |
| --- | ---: | ---: | ---: |
| Resident | 35,244 | 35,244 | 0 |
| Stage 1 | 26,903 | 26,903 | 0 |
| Stage 2 | 26,903 | 26,903 | 0 |
| Stage 3 | 26,903 | 26,903 | 0 |
| Stage 4 | 26,903 | 26,903 | 0 |
| Stage 5 | 26,903 | 26,903 | 0 |
| Total | 169,759 | 169,759 | 0 |

The six part exports are canonical. [Orientation](orientation.md) names their listing snapshots. The disk, disassembler projects, annotation logs, test scripts and the listing sample are under the ignored `work/` directories.

The listing sample found seven wrong details in 75 comments. All seven were corrected. A full audit remains worthwhile for the remaining comments. The `gpt-6.2-sol` analysis and sample require a proven-model maintainer check for Silver. Site, review and retrospective were outside this handoff. See [features.md](features.md) for the individual mechanics and branches left open.
