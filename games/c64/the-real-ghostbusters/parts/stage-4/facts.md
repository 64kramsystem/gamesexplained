# LEVELD

The breakpoint at `$5613` caught the KERNAL LOAD return. All 8,650 payload bytes matched the disk file at `$6000`. At `$3302` after both expansion passes, the output pointer was `$CAC0`, one past the expanded range `$6000`–`$CABF`.

The engine reads the setup callback `$C279` from `$C002/$C003` before dispatch at `$1527`. It reads the update callback `$C298` from `$C00F/$C010` before dispatch at `$096F`. Both calls use the indirect jump at `$15EB`.
VICE single-stepped this setup path against the expanded snapshot. Successive PCs were `$1527 $15EB $C279 $C27B $C27D $C27E $C280`.

LEVELD supplies 20 stage-specific actor descriptors from `$C011` and 103 four-byte placed-object records from `$C0D9`. The record column at `$C275` is the `$FF` terminator. The engine uses `$C29B` to find the tile patch addresses. It writes the selected rectangles into the character map at `$8000`. The listing comes from the expanded capture, before this setup modifies the map.
