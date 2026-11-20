# Remaining analysis

Step 50 is open. Resume from the exported symbol maps and the five listing snapshots named in [orientation.md](orientation.md). Rebuild each listing from its own snapshot after annotation. The disassembler at port 23026 holds the resident annotation session. The scene resource map was exported from its local project, built from the recorded copy-complete snapshot.

| Part | Explained | Tracked | Bare |
|---|---:|---:|---:|
| Title | 31,047 | 31,047 | 0 |
| Resident | 48,721 | 49,561 | 840 |
| Scene resource | 2,928 | 3,120 | 192 |
| Ending | 6,240 | 6,240 | 0 |
| Scores | 4,560 | 4,560 | 0 |
| Total | 93,496 | 94,528 | 1,032 |

All five rebuilt listings have zero uncounted stretches. The resident queue is in `work/resident-full-queue.log`. The largest runs include the 51-byte tail copied in record 490 at $A3ED, the low-memory run at $00DD and unresolved data following some panel descriptors. The coordinate loop at $40A3 reads three Y deltas before the record 490 tail. A VICE range watch showed that this loop leaves the tail untouched, which bounds that caller's access without establishing a purpose for the shipped bytes. The scene resource has one open run, $F740–$F7FF. Its recurring pattern matches stretches in other tape records and its loader provenance is known. A display or CPU consumer for those three slots is still open. The 48-byte suffix at $B120 matches an earlier cassette record and remains counted. The bytes at $FB06–$FB3F contain a 16-bit x86 fragment and are counted as cassette data.

The resident snapshot predates the record 315 copy. The scene part starts at the last store of the copy and preserves bytes that the engine later overwrites. The actor-plane and vector notes formerly attached to those addresses in the resident session are recorded in [scene resource facts](parts/scene-resource/facts.md). The discarded portion of the resident record 267 range is visible in the title listing as part of the title bitmap. The annotation batches and watchpoint probes are in ignored `work/`.

Step 60 starts after the exact ledgers agree. The independent listing sample is outstanding. Step 65 applies if a required claim or route needs a recorded input sequence. The controlled overlay paths use instruction-entry checkpoints and tape positions documented in [orientation.md](orientation.md).

The recorded tier remains Bronze. The kit requires a proven-model check for Silver, and `gpt-6.2-sol` is absent from its proven list.
