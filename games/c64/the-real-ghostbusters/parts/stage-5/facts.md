# LEVELE

The breakpoint at `$5613` caught the KERNAL LOAD return. All 6,939 payload bytes matched the disk file at `$6000`. At `$3302` after both expansion passes, the output pointer was `$C993`, one past the expanded range `$6000`–`$C992`.

The engine reads the setup callback `$C227` from `$C002/$C003` before dispatch at `$1527`. It reads the update callback `$C24B` from `$C00F/$C010` before dispatch at `$096F`. Both calls use the indirect jump at `$15EB`.
VICE single-stepped this setup path against the expanded snapshot. Successive PCs were `$1527 $15EB $C227 $C229 $C22B $C22C $C22E`.

LEVELE supplies 19 stage-specific actor descriptors from `$C011` and 85 four-byte placed-object records from `$C0CF`. The record column at `$C223` is the `$FF` terminator. The engine uses `$C251` to find the tile patch addresses. It writes the selected rectangles into the character map at `$8000`. The listing comes from the expanded capture, before this setup modifies the map.

## Type $31 callback

In a controlled allocator call, the breakpoint at `$C4CB` caught
initialization of slot 2. A watchpoint at `$E9F0` then stopped at
`$C504` with A = 4 and X still 2. The store at `$C501` writes
the fixed field of slot zero.

The update at `$C801` calls the resident removal routine before
testing `$390C`. A controlled nonzero value at the test at `$C809`
took the branch to the immediate return at `$C855`.
