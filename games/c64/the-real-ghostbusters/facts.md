# Analysis handoff

## Disk and stage selection

The resident engine stays in memory as the game replaces the stage overlay.
At `$3331` the engine adds `$41` to the stage index in `$11` and writes
the suffix of the six-byte PETSCII filename at `$3387`. The KERNAL LOAD
return at `$5613` caught the packed file. Two unpacking passes leave an
overlay at `$6000`, with its exclusive end in `$0A/$0B` at `$3302`.
Each [part](parts/) records those measurements for its file.

The engine reads per-stage setup and update pointers from
`$C002/$C003` and `$C00F/$C010`. It calls through `$15EB`, which
jumps indirectly through `$0C/$0D`. VICE instruction steps captured
the setup dispatch for every overlay. Two successive store watchpoints
on the hardware IRQ vector followed Stage 1's handler changes. The
three-handler chain in the measured state uses `$0C31`, `$0C69`
and `$0A57`. The `$53` branch at `$0B22` also selects `$0D97`
on a different display path.

## Display

In the measured Stage 1 split, the breakpoint before the write at
`$0C84` showed A = `$0E` and CIA2 port A's low bits equal to 2.
The resulting VIC bank is `$4000` and the character set is at
`$7800`. The bottom handler uses `$06`, selecting the HUD and title
character set at `$5800`. Both register values select screen RAM at
`$4000`. For LEVELA through LEVELJ, the engine at `$12CD` constructs
map row pointers from `$8000` with a stride of 86. The viewport copy
at `$1316` uses the level's character indices and looks up their
colours through the table at `$7700`. LEVELK uses a bitmap and its own
raster routine.

## Text

The custom title and HUD font at `$5800` places upper-case letters,
lower-case letters and digits at their ASCII byte values. The rendered
glyph grid shows uppercase A–Z at `$41–$5A`, lowercase a–z at
`$61–$7A`, and digits at `$30–$39`. Glyph `$00` is the copyright
symbol and `$20` is blank. The title emits the bytes of the script
at `$29F0` directly to screen RAM through `$34E5`.
Here `$FE` takes two positioning bytes, `$FD` takes a colour byte,
and `$FF` terminates the script.

## Input sampling

Player index zero uses control port 2. The engine reads `$DC00` at
`$18EF` and keeps its low five bits in `$6D`. It reads control port 1
through `$DC01` at `$18FF` and keeps its value in `$6E`. The reader at
`$190B` selects between the two bytes by player index.

A stopping checkpoint at the hold-counter store at `$1C96` recorded
the Stage 1 player-zero values before, during and after holding fire on
port 2. The counter ran 0, 1, 2, 3, 4, 5, 5, 0. The raw bits in
`$6D` went from `$1F` to `$0F` while held. The packaged output was
`$2F` on the first four held polls and `$1F` from the fifth held poll.
The physical effect of that internal mode change remains open.
