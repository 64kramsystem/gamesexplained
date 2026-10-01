# Publication history

30 September 2026: contributor authorized publication directly from the existing exhaustive disassembly, online research, and a separate PR for each game. Imported annotations without claiming a new reverse-engineering run. Measured the repository’s own prose coverage and retained Bronze pending completion and maintainer review.

30 September 2026: reviewer correction booted disk from hard reset into THE BATHROOM with trainers disabled, compared title/play, rebuilt canonical symbols/listing and held the article at Bronze pending verification. Shared tooling moved to #125.

1 October 2026: resumed coverage, described all room and sprite records, corrected operand-label addresses and misplaced post-row descriptions, and removed duplicate follow-on annotations. Tracked coverage reached 100%; hidden I/O RAM and loader hand-over remain open, so this is not a Silver completion.

The retained `$D000` bootstrap was checked by controlled execution: it relocates a descending-page room-copy loop, rather than being arbitrary residue. Native room-copy checks passed all 60 ids and rope staging passed all 34 positions. Initial comparison against an older saved room image failed because an animated glyph had changed; comparison against each live source immediately before copying passed. Misplaced screen-page prose and color-RAM/template aliases were corrected in the exported listing. Two new trainer/decompression attempts did not reach a healthy title; they are not evidence of absent RAM accesses.
