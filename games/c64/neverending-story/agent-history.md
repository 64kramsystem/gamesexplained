# Publication history

30 September 2026: contributor authorized publication directly from the existing exhaustive disassembly, online research, and a separate PR for each game. Imported annotations without claiming a new reverse-engineering run. Measured the repository’s own prose coverage and retained Bronze pending completion and maintainer review.

1 October 2026: fresh Part-1 command capture, custom font recovery, parked-loader tracing and dictionary/operand annotation checks. Earlier article and imported facts retained privately as leads. The duplicate RASTER_DISPATCH_OFS alias was removed from the map; carry this removal into the rebuilt project before exporting again.

On 1 October 2026 a live load stopped at the Part-1 entry $0400. RAM watchpoints with bank conditions and injected positive controls observed no $D000-$D0FF access during title-to-narrative-to-command loading. Restoring a snapshot without embedded disks initially stalled its loader; reattaching the private disk resolved that. Native consumer tracing corrected the exported source-pointer fields $295D/$295E and $2963/$2964. The hidden page and four newly exposed hand-over ranges remain open.

All 21 Part-1 illustration descriptors were decoded from the fresh snapshot and passed native-blitter output checks, including the final source pointer. The picture browser was restored from those bytes and its pixels compared independently in Firefox. Explicit picture extents exposed additional ledger gaps; record-specific continuation comments cover them without discarding authored data. The text-font tail at $FD30 was identified as cells 166–255. Tracked coverage is 48,455 of 48,711 bytes (99.5%); hidden $D000-$D0FF and two untracked title-stage tails remain open.
