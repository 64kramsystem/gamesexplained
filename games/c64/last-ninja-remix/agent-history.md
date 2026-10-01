# Publication history

30 September 2026: contributor authorized publication directly from the existing exhaustive disassembly, online research, and a separate PR for each game. Imported annotations without claiming a new reverse-engineering run. Measured the repository’s own prose coverage and retained Bronze pending completion and maintainer review.

30 September 2026: replaced the non-running composition with a booted Central Park snapshot. Traced overwritten startup to double-buffered sprite output. Kept the article Bronze pending coverage/verification; later loads remain open under RFC #124.

### Packed resources and indexed aliases

Validated 162 main and 80 auxiliary sprite records independently against the fresh capture; all expansion lengths and boundaries agree. Checked all 118 scene record boundaries and child indices. Added record-specific annotations and restored the sprite browser after comparing its arrays with fresh RAM. Corrected the decoder description: `$68` escapes a literal, while `$69-$6F` encode zero runs. Retyped `$0000-$0FFF` as data, removing false code cross-references produced by decoding runtime sprite buffers. Traced `$159D` as a negative-index base alias for masks at `$1695`, and documented frame read windows whose storage boundaries depend on actor paths. Coverage is 89.9%; this is progress toward Silver, not completed feature verification.
