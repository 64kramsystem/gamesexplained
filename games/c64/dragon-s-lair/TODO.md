# Dragon's Lair — analysis handoff

The work is at Bronze. Resume step 50. The exported ledgers count **157,200 of 218,205 tracked bytes explained**. Verification and input recording depend on finishing that ledger.

| Part | Explained bytes | Tracked bytes | Uncounted stretches |
|---|---:|---:|---:|
| resident | 8,991 | 14,123 | 0 |
| title-picture | 10,180 | 10,180 | 0 |
| first-descent | 17,127 | 20,822 | 0 |
| skull-hallway | 19,144 | 21,922 | 0 |
| burning-ropes | 17,640 | 20,964 | 0 |
| weapons-room | 17,203 | 21,725 | 0 |
| ramps | 16,685 | 23,722 | 0 |
| tentacle-room | 18,193 | 21,179 | 0 |
| second-descent | 1,330 | 5,120 | 0 |
| phantom-knight | 15,133 | 20,826 | 0 |
| dragon | 15,574 | 37,622 | 0 |

The most substantial open regions are the dragon's additional graphics and staging at `$8600–$BF0F`, and the unclassified code and tables in the second descent, Phantom Knight and ramps. The dragon reads some of its staging area as raw source data, so the whole staging range cannot be excluded as a duplicate without tracing its individual uses. The directory item `LJ` remains open. Use the resident loader, the play snapshots and the targeted instruction logs to continue the burn-down. Each part's local project and the exact snapshot used for its listing are in its ignored work directory.

The captures used debugger scene selection. They establish entry points and screen states. They do not establish a route through ordinary play. No recording was needed for the captures.
