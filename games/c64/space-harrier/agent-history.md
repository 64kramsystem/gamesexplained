# Space Harrier analysis session

The installed VICE headless build with dummy audio passed exact pauses,
instruction stepping and watchpoints. The host-key path failed, and the
health check ended its final quirks phase on a missing checkpoint field.
A full-frame capture lost the emulator at checkpoint cleanup. After
restart, the four IRQ execute stops and small RAM and register
watchpoint sets gave usable measurements.

The JCT image reached the game at $0850 after two unpacking phases.
The execution map contains instructions from startup, title and
active Moot. The other object and wave handlers were recovered through
dispatch tables. The entry snapshot supplies startup data that changes
in the active image. The second disk build was booted only for memory
comparison. Its cracker waited at $036B–$036F for Space. The expanded
image shared the large unresolved $4EEB–$6FFF block with the JCT build.

The local tools and logs are under `work/`. `trace-mechanics.py` records
the control instruction stops, projectile store and four raster phases.
`verify.py` and `verify-followup.py` check the pause sequence, timer,
score carry, life branch, stage wrap and charset load. The isolated
escort-head tail check records the effective store through the
clobbered Y index. `capture-rle-boundaries.py` records the loader's
source pointer and final destination. The listing sample and verdicts
are under `work/reports/sample-20261119/`.

The original emulator ports for this worktree were kept throughout.

The resumed coverage pass matched the entire JCT depacker output to
the saved handover snapshot. Execute and destination-store checkpoints
isolated the title's eight-page character copy and the depacker's
final zero run. The local `work/resume-watch.py` and
`work/rle-provenance.py` retain the probes. The work queue shrank by
2,112 bytes through those two classifications.

The follow-up compared the Elite Novaload tape and Remember Elite disk
at the same $0850 handover. `work/elite-copy.txt` records the store
that ties the upper-RAM tail to the tape's relocation. The Remember
trainer occupied part of the large lower gap and left the rest clear.
`work/resume-ranges.txt` records the last effect's load and cleanup
execute stops. `work/verify-resident-ranges.txt` records the VIC
selector stores, the KERNAL ROM stop while it was banked in, and the
post-banking watches with read and store controls.
