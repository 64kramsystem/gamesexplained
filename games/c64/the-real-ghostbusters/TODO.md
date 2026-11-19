# Analysis handoff

Step 50 is incomplete. The following counts come from the kit ledger against the exported symbols. All rebuilt listings have empty uncounted lists.

| Part | Explained bytes | Tracked bytes | Uncounted stretches |
| --- | ---: | ---: | ---: |
| resident | 10,563 | 28,042 | 0 |
| stage-1 | 25,846 | 27,430 | 0 |
| stage-2 | 24,723 | 27,693 | 0 |
| stage-3 | 24,871 | 27,190 | 0 |
| stage-4 | 24,720 | 27,328 | 0 |
| stage-5 | 24,594 | 27,027 | 0 |
| stage-6 | 24,741 | 27,040 | 0 |
| stage-7 | 24,770 | 27,005 | 0 |
| stage-8 | 24,862 | 26,984 | 0 |
| stage-9 | 24,731 | 27,044 | 0 |
| stage-10 | 25,913 | 28,057 | 0 |
| stage-11 | 24,848 | 24,848 | 0 |
| **Total** | **285,182** | **325,688** | **0** |

The remaining work is concentrated in resident mechanics and sound, stage-specific actor callbacks and their data, and stable loaded ranges tracked in the resident ledger pending decoding. In particular, the bytes under I/O at `$DF8C–$DFFF` match `$EF8C–$EFFF` at hand-over. Their consumer is open.

Four disk items still need media answers. The pictures, Crazy Toaster II and the accompanying note have independent directory entries. Their relationship to the game remains open.

The exact coverage gate precedes Step 60. Verification and any Step 65 input recording are pending. The kit lists the requested model as unproven for Silver.
