# LEVELA

The breakpoint at `$5613` caught the KERNAL LOAD return. All 9,399 payload bytes matched the disk file at `$6000`. At `$3302` after both expansion passes, the output pointer was `$CB26`, one past the expanded range `$6000`–`$CB25`.

The engine reads the setup callback `$C116` from `$C002/$C003` before dispatch at `$1527`. It reads the update callback `$C135` from `$C00F/$C010` before dispatch at `$096F`. Both calls use the indirect jump at `$15EB`.
VICE single-stepped this setup path against the expanded snapshot. Successive PCs were `$1527 $15EB $C116 $C118 $C11A $C11B $C11D`.

LEVELA supplies 26 stage-specific actor descriptors from `$C012` and 118 four-byte placed-object records from `$C138`. The record column at `$C310` is the `$FF` terminator. The engine uses `$C314` to find the tile patch addresses. It writes the selected rectangles into the character map at `$8000`. The listing comes from the expanded capture, before this setup modifies the map.

The stage update at `$CA95` rewrites four playfield glyphs. At
`$CAB5`, X was `$1F` and Y was `$3F`. The watchpoint after the store
to `$78D8` confirmed that `$78D8–$78F7` matched the 32 bytes ending at
`$CB03`.
