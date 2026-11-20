# Analysis handoff

The kit ledger reports matching explained and tracked counts after
the verification corrections. Every part listing was rebuilt from
its own snapshot and has zero uncounted stretches.

| Part | Explained bytes | Tracked bytes | Uncounted stretches |
| --- | ---: | ---: | ---: |
| resident | 24,870 | 24,870 | 0 |
| stage-1 | 27,430 | 27,430 | 0 |
| stage-2 | 27,693 | 27,693 | 0 |
| stage-3 | 27,190 | 27,190 | 0 |
| stage-4 | 27,328 | 27,328 | 0 |
| stage-5 | 27,027 | 27,027 | 0 |
| stage-6 | 27,040 | 27,040 | 0 |
| stage-7 | 27,005 | 27,005 | 0 |
| stage-8 | 26,984 | 26,984 | 0 |
| stage-9 | 27,044 | 27,044 | 0 |
| stage-10 | 28,057 | 28,057 | 0 |
| stage-11 | 24,848 | 24,848 | 0 |
| **Total** | 322,516 | 322,516 | 0 |

The disk, resident hand-over and play snapshots, overlay expansion
snapshots, instruction traces, and sampled verdicts are in ignored
`work/` folders. The checked-in symbol maps are the annotation source.

Verification sample 6050 found three errors in 65 comments and the
analysis corrects all three. A full audit remains recommended.
The kit lists gpt-6.2-sol as unproven for Silver, so the tier remains
Bronze until the maintainer’s proven-model check and the site work
required by Silver are complete.

This run establishes instruction behavior with scoped probes and
controlled loader captures. It makes no player-route reachability
claim that requires a Step 65 input recording.
