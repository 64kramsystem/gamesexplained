# LEVELB

The breakpoint at `$5613` caught the KERNAL LOAD return. All 9,138 payload bytes matched the disk file at `$6000`. At `$3302` after both expansion passes, the output pointer was `$CC2D`, one past the expanded range `$6000`–`$CC2C`.

The engine reads the setup callback `$C273` from `$C002/$C003` before dispatch at `$1527`. It reads the update callback `$C292` from `$C00F/$C010` before dispatch at `$096F`. Both calls use the indirect jump at `$15EB`.
VICE single-stepped this setup path against the expanded snapshot. Successive PCs were `$1527 $15EB $C273 $C275 $C277 $C278 $C27A`.

LEVELB supplies 23 stage-specific actor descriptors from `$C011` and 94 four-byte placed-object records from `$C0F7`. The record column at `$C26F` is the `$FF` terminator. The engine uses `$C295` to find the tile patch addresses. It writes the selected rectangles into the character map at `$8000`. The listing comes from the expanded capture, before this setup modifies the map.
