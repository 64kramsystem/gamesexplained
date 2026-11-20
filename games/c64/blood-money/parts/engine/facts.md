# Resident engine technical facts

The engine entry snapshot is `work/entry.vsf`, stopped on an execution checkpoint at `$1CD6` after the Accept intro. The interrupt and level routes are in [orientation.md](../../orientation.md).

- The level transition at `$2BBF` increments `$0442`, compares it with 5 and jumps to `$370A` while the incremented value is below 5 on the normal progression path. The equality branch goes to the completion sequence. This branch is statically traced.
- `$C8B0` constructs the four on-disk names. At `$C969` it copies the end of the CHARS payload out of the staging area before the terrain and screen clear at `$CB40`.
- `$9ED8` multiplies a block ID by 25 and reads 25 terrain character codes. The destination wraps at 45 columns and 26 rows in the terrain staging buffer. The screen writer at `$DE07` copies from that buffer to the selected VIC screen.
- `$D030` reads scroll-timed events from `$8045`. In the eight-byte form, `$D07D` allocates an object slot and installs the pointers for the object's command stream and parameter record. `$D596` selects commands via the jump table at `$D000`.
- `$DC82` expands the sprite record selected by its two offset tables and places the result in a VIC sprite slot. The expansion uses a leading-zero count and an inclusive last index for the packed bytes.
- When the game needs to examine a solid terrain character, `$CA8E` tests the appropriate bit in the 32-byte table at `$8024`. On a hit, `$CAA6` compares the glyph's pixels against an aligned mask. The shot code also reads the solid-character table at `$2FCF`.
- `$E1A5` maintains time for the three SID voices, reading each voice's sequence separately and reading pattern addresses at `$FB56`. In the level 1 probe, a data watchpoint in BLOCKS stopped immediately after the read at `$E253`.

- The SID update reads 16-byte instrument records via the pointer table at `$E0A5`. A frequency-low store watchpoint on `$D4E0` caught `$E662` with `X = 0` and `A = $C3`. A pulse-width-low store watchpoint on `$D4E2` caught `$E5AF` with `X = 0` and `A = $F0`. These are SID mirrors of `$D400` and `$D402`.
- The player sprite update at `$24B2` wrote `$BE` to the player 1 pointer field at `$008F`. With the VIC bank at `$4000`, that selects the bitmap at `$6F80`. A store watchpoint on `$7000–$72FF` stopped just after `$DCBD`, where the packed sprite decoder clears leading bytes in a cache slot.
- The shop purchase dispatcher at `$2713` compares two packed decimal balance bytes to the price before decrementing the item's stock and jumping through the split table at `$02F1/$0340`. The payment loop at `$27DE` deducts ten per pass and redraws the balance. The tile-object dispatcher at `$3893` reads interleaved handler addresses at `$38B9`. Its handlers include relative movement, counted repeats, sound and the terrain charset swap.

- The title sprite reveal reads 240 countdowns at `$16DD + Y` for Y from 240 to 1. A forced call to `$C735` with schedule selector `$FF` stopped on a read of `$17CD` just after `$C757`, with Y equal to 240. Expiring timers allocate title sprite slots. Each active slot steps from shape `$B6` through `$BB` and clears at `$BC`.

- Level initialization writes the sprite cache free list at `$0DAB–$0DEA` and clears the slot and reference arrays at `$0DEB–$0FEA`. Combined read/write checkpoints over those ranges, armed at the loader return, first hit on initialization stores. The title also writes 240 countdowns into `$10EA–$11D9` before its timer loop reads them. These ranges are runtime state.

- A level 1 watchpoint on $0BB0–$0BBB stopped at $D346 following the $D343 store of tile-object property byte 0 to slot 11. The constructor at $D332 takes a direct image pointer when byte 8 is zero. Otherwise it fetches the first image address from the pointer table.
- In the first screen copy, watchpoints stopped at $DE19 after the read of the source row high byte and at $DE22 after a store to the first load's operand. The table holds 26 addresses separated by 45 bytes, followed by a second copy of those addresses to support wrapped rows.
- Read and write watchpoints armed at the resident handover first hit on zeroing stores at $CB60, $CB63, $CB66 and $CB69 in the four scroll staging pages at $5C00–$5FFF. At the level 1 loader return, corresponding probes first hit on initialization stores for the projectile state arrays, the cleared tile-object fields and the small tile-slot occupancy and position arrays. The title IRQ was still reading other sprite fields before gameplay set them up, so those addresses remain tracked.

## Verification probes

- The title’s 2 key hit the $C399 store of $FF to $0438. Its 4 key hit the $C3EA store that flipped $046B from $FF to zero. The game scans mapped player ports at $23D7 and $23F6 when both slots are active.
- In a controlled call to the sprite initializer, the level 1 properties at $8F20 yielded initial hit points zero at $D14F and a first animation countdown of one at $D1D2. Byte 7 supplies the recurring delay when $DBFA masks off its high bit.
- With all twelve stamp slots occupied, running $D205 still hit the event pointer store at $D257. The cursor advanced from $8045 to $8049 without allocating a slot. The two small stamp shapes come from the live four pairs of character codes at $0C88 through $0C8F.
- The resident handover's stock KERNAL RAM vectors at $0314–$0333 match the installed 901227-03 KERNAL table at $FD30 byte for byte. A combined watchpoint on zero page hit the first startup clear at $1CE8. The editor code templates spanning $0D00–$0D42 include the literals `for`, `do` and `switch`. The fragment at $0D24–$0D2F lies between the documented twelve-slot arrays and survived both release handovers. Read and store watchpoints on that fragment stayed silent during the short runs from the resident and four level-entry snapshots.
