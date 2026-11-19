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
