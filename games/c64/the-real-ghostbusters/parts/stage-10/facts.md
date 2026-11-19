# LEVELJ

The breakpoint at `$5613` caught the KERNAL LOAD return. All 9,988 payload bytes matched the disk file at `$6000`. At `$3302` after both expansion passes, the output pointer was `$CD99`, one past the expanded range `$6000`–`$CD98`.

The engine reads the setup callback `$C15B` from `$C002/$C003` before dispatch at `$1527`. It reads the update callback `$C17A` from `$C00F/$C010` before dispatch at `$096F`. Both calls use the indirect jump at `$15EB`.
VICE single-stepped this setup path against the expanded snapshot. Successive PCs were `$1527 $15EB $C15B $C15D $C15F $C160 $C162`.

LEVELJ supplies 33 stage-specific actor descriptors from `$C011` and 118 four-byte placed-object records from `$C17D`. The record column at `$C355` is the `$FF` terminator. The engine uses `$C359` to find the tile patch addresses. It writes the selected rectangles into the character map at `$8000`. The listing comes from the expanded capture, before this setup modifies the map.
