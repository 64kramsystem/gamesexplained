# Resident engine technical facts

The engine entry snapshot is `work/entry.vsf`, stopped on an execution checkpoint at `$1CD6` after the Accept intro. The interrupt and level routes are in [orientation.md](../../orientation.md).

- The level transition at `$2BBF` increments `$0442`, compares it with 5 and jumps to `$370A` while the incremented value is below 5 on the normal progression path. The equality branch goes to the completion sequence. This branch is statically traced.
- `$C8B0` constructs the four on-disk names. At `$C969` it copies the end of the CHARS payload out of the staging area before the terrain and screen clear at `$CB40`.
- `$9ED8` multiplies a block ID by 25 and reads 25 terrain character codes. The destination wraps at 45 columns and 26 rows in the terrain staging buffer. The screen writer at `$DE07` copies from that buffer to the selected VIC screen.
- `$D030` reads scroll-timed events from `$8045`. In the eight-byte form, `$D07D` allocates an object slot and installs the pointers for the object's command stream and parameter record. `$D596` selects commands via the jump table at `$D000`.
- `$DC82` expands the sprite record selected by its two offset tables and places the result in a VIC sprite slot. The expansion uses a leading-zero count and an inclusive last index for the packed bytes.
- When the game needs to examine a solid terrain character, `$CA8E` tests the appropriate bit in the 32-byte table at `$8024`. On a hit, `$CAA6` compares the glyph's pixels against an aligned mask. The shot code also reads the solid-character table at `$2FCF`.
- `$E1A5` maintains time for the three SID voices, reading each voice's sequence separately and reading pattern addresses at `$FB56`. In the level 1 probe, a data watchpoint in BLOCKS stopped immediately after the read at `$E253`.

## Open coverage

This listing includes traced routines and source data. The remaining labels, unowned spans and presentation data need attribution. See the game-level [TODO.md](../../TODO.md).
