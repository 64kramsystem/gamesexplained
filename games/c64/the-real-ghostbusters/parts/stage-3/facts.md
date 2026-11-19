# LEVELC

The breakpoint at `$5613` caught the KERNAL LOAD return. All 8,183 payload bytes matched the disk file at `$6000`. At `$3302` after both expansion passes, the output pointer was `$CA36`, one past the expanded range `$6000`–`$CA35`.

The engine reads the setup callback `$C28B` from `$C002/$C003` before dispatch at `$1527`. It reads the update callback `$C2AF` from `$C00F/$C010` before dispatch at `$096F`. Both calls use the indirect jump at `$15EB`.
VICE single-stepped this setup path against the expanded snapshot. Successive PCs were `$1527 $15EB $C28B $C28D $C28F $C290 $C292`.

LEVELC supplies 21 stage-specific actor descriptors from `$C011` and 105 four-byte placed-object records from `$C0E3`. The record column at `$C287` is the `$FF` terminator. The engine uses `$C2B7` to find the tile patch addresses. It writes the selected rectangles into the character map at `$8000`. The listing comes from the expanded capture, before this setup modifies the map.
