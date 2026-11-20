# LEVELB

The breakpoint at `$5613` caught the KERNAL LOAD return. All 9,138 payload bytes matched the disk file at `$6000`. At `$3302` after both expansion passes, the output pointer was `$CC2D`, one past the expanded range `$6000`–`$CC2C`.

The engine reads the setup callback `$C273` from `$C002/$C003` before dispatch at `$1527`. It reads the update callback `$C292` from `$C00F/$C010` before dispatch at `$096F`. Both calls use the indirect jump at `$15EB`.
VICE single-stepped this setup path against the expanded snapshot. Successive PCs were `$1527 $15EB $C273 $C275 $C277 $C278 $C27A`.

LEVELB supplies 23 stage-specific actor descriptors from `$C011` and 94 four-byte placed-object records from `$C0F7`. The record column at `$C26F` is the `$FF` terminator. The engine uses `$C295` to find the tile patch addresses. It writes the selected rectangles into the character map at `$8000`. The listing comes from the expanded capture, before this setup modifies the map.

The stage update at `$C82C` selects a 72-byte glyph frame. At `$C849`,
X was zero and Y was zero. A store watchpoint on `$79A7` confirmed that
the destination at `$7960–$79A7` matched the first frame at `$C88C`.

## Linked actors

A controlled call to the resident allocator at `$22A6` with type
`$26` reached the initializer at `$C48B` with X = 2. The store
watchpoint at `$CB49` stopped at `$C4E8`. The initializer had
stored the parent and its three child slots at `$CB46–$CB49` as
2, 3, 4 and 5. The child types were `$27`, `$28` and `$29`,
and each child contained the parent slot in its `$E900` field.

The shape reset at `$CA3E` starts with Y = 4 and therefore reads
five indices from a four-byte slot list. In a controlled call to the
row-`$0D` reset at `$CA17`, a read watchpoint at `$CB4A` stopped
at `$CA41` with X = `$AD`, the first opcode byte after the list.
A store watchpoint then stopped at `$CA44` after the loop wrote zero
to `$E88D` (`$E7E0 + $AD`). The effects of this write during
ordinary play remain open.

At the end of LEVELB expansion, store watchpoints at `$CC2B`
and `$CC2C` stopped after the run-length store at `$1AA1` with
A = 0. The destination pointer was `$CC2D` on return at `$3302`.
