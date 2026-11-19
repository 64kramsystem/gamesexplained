# Analysis history

On 19 November 2026 the two packed gameplay entries booted separately
on the assigned headless C64 tools. The analyzed RAM states were saved
without ROMs. Executed-address maps seeded Regenerator2000. Each listing
was generated from the same snapshot used by its disassembler.

The core coverage loop identified the main video, input, map and sound
paths and the large authored graphics banks. Targeted instruction and
memory watch tests pinned down the base access-code accept store and
the surface port-2 poll. The disk inventory is closed against the
three PRGs in the input release.

## Coverage handoff

The two gameplay snapshots rebuilt their committed listings byte
for byte before annotation resumed. The coverage pass matched
loading-picture fragments against the standalone loader's bitmap,
followed reverse-scroll reads before the forward cursors, and
identified additional SID streams through their pointer setup.
Store watchpoints covered both retained decompressor bytes and live
sprite copies. Exact ledger counts passed before and after the
verification edits. Scripts, snapshots and probe output are under
`work/` locally. The supplied model was used throughout.
