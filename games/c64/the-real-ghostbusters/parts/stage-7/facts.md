# LEVELG

The breakpoint at `$5613` caught the KERNAL LOAD return. All 7,136 payload bytes matched the disk file at `$6000`. At `$3302` after both expansion passes, the output pointer was `$C97D`, one past the expanded range `$6000`–`$C97C`.

The engine reads the setup callback `$C27F` from `$C002/$C003` before dispatch at `$1527`. It reads the update callback `$C29E` from `$C00F/$C010` before dispatch at `$096F`. Both calls use the indirect jump at `$15EB`.
VICE single-stepped this setup path against the expanded snapshot. Successive PCs were `$1527 $15EB $C27F $C281 $C283 $C284 $C286`.

LEVELG supplies 19 stage-specific actor descriptors from `$C011` and 107 four-byte placed-object records from `$C0CF`. The record column at `$C27B` is the `$FF` terminator. The engine uses `$C2A1` to find the tile patch addresses. It writes the selected rectangles into the character map at `$8000`. The listing comes from the expanded capture, before this setup modifies the map.
