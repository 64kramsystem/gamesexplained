# Analysis handoff

The analysis is at step 50. The checked-out branch records Bronze. The exact ledger over the exported symbols is 145,524 explained bytes of 170,015 tracked. The rebuilt listings report zero uncounted stretches. There are 24,491 tracked bytes without an explanation.

| Part | Explained | Tracked |
| --- | ---: | ---: |
| Resident | 24,742 | 35,500 |
| Stage 1 | 24,624 | 26,903 |
| Stage 2 | 23,935 | 26,903 |
| Stage 3 | 23,902 | 26,903 |
| Stage 4 | 25,005 | 26,903 |
| Stage 5 | 23,316 | 26,903 |

The next step 50 work is the resident actor handlers, movement branches and remaining register and audio routines. In the stage overlays, start with the handler addresses from the actor-type dispatch table at $1DE6/$1E5C and the stage hook selected at $29CF. The stage 5 queue has the largest remaining overlay runs. The per-part ledger commands and the saved inputs for rebuilding the listings are in the handoff worktree. Instructions for reaching each capture are in [orientation.md](orientation.md).

The media ledger has 14 unresolved sector runs outside the thirteen decoded loader chains. Their status remains open until all possible readers have been traced. Each decoded chain and the sector walks are saved locally under `work/`.

Formal step 60 verification and its independent comment sample depend on completing the step 50 ledger. Stage captures used debugger-triggered loader routes, so those captures have no gameplay input recording. The analysis model is `gpt-6.2-sol`. The kit requires a separate proven-model check before Silver.
