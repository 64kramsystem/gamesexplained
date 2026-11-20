# Analysis handoff

## Disk and stage selection

The resident engine stays in memory as the game replaces the stage overlay.
At `$3331` the engine adds `$41` to the stage index in `$11` and writes
the suffix of the six-byte PETSCII filename at `$3387`. The KERNAL LOAD
return at `$5613` caught the packed file. Two unpacking passes leave an
overlay at `$6000`, with its exclusive end in `$0A/$0B` at `$3302`.
Each [part](parts/) records those measurements for its file.

The boot trace from the explicit R. GHOSTBUSTERS+ autostart to
the resident entry at `$0820` recorded one KERNAL LOAD. No further
LOAD occurred through the OUG intro and two trainer exits.
A control from the stage selection snapshot recorded one SETNAM and
one LOAD for LEVELA. The resident SETNAM call is at `$3362` and its
LOAD call is at `$5610`. The eleven return snapshots each match their
decoded filename suffix and their complete packed disk payload.

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

The filtered bits reach the weapon branch at `$1F39`. With player zero
facing direction zero, a checkpoint at `$1FAC` caught the first held
poll calling the allocator with type `$12`, control byte `$2F`, and
counter 1. In a fresh capture, holding fire reached `$1F65` with type
`$0A`, control byte `$1F`, and counter 5. In this branch the code first
subtracts ten from the 16-bit player value at `$89/$8A`. If the balance
allows it, it attempts two allocations of the same directional type,
setting `$E8D0,X` to zero before the first and eight before the second.
Breakpoints then caught the two actor initializers at `$180D` and
`$16B1` and the corresponding updates at `$211F` and `$210E`.
Each trace allocated slot ten. The watchpoint on its lifetime byte
at `$E9CA` recorded an initial value of twelve for type `$12` and
one for type `$0A`. The consequences of collision remain open.

## Animated playfield tiles

The stage update changes the shape of map tiles in place by rewriting
the playfield character set. LEVELA decrements `$CB24` and, on
underflow, advances its four-state animation phase at `$CB25`.
The offsets at `$CAC0` select three frames in order 0, 1, 2, 1. At
`$CAB5` the trace caught Y = `$3F` and X = `$1F`. The store
watchpoint at `$78D8` stopped at `$CABB`, where the 32 destination
bytes matched the second frame. LEVELB uses five phases and copies 72
bytes forwards. At `$C849` the trace caught source offset zero in X.
The watchpoint on the last destination byte, `$79A7`, stopped at
`$C84F`. The destination matched the 72 bytes at `$C88C`.

## Music setup

At startup the resident title code calls `$EF8C` with A = 0. The
initializer reads a seven-byte record at `$FB3B` consisting of a timing
byte and three little-endian voice order-list pointers. Each list holds
pattern pointers. A breakpoint at `$FB05` and a watchpoint on
`$F0C6` caught the reset at `$FB0A`. Stepping the store at `$F056`
then left `$F0C6` set to 1. The three voice states had order-list
pointers `$FB8B`, `$FBC1` and `$FB57`, and initial pattern
pointers `$FC8D`, `$FDC7` and `$FFEE`.


The playback trace for voice three reached `$F26F` with its
pattern pointer at `$FFEF` and A = `$FF`. One instruction changed the
pitch calculation operand at `$F443` to that value. The next pattern
command reached `$F20A` and selected `$FC01` from the voice's order
list. The first short-fire sound uses a separate twelve-byte effects
preset. The checkpoint at `$F74A` caught selector three. A store
watchpoint at `$FAEA` confirmed that the copied record matched
`$F801–$F80C`. The first control-register write to `$D412` stopped at
`$F79B` with X = `$80`.

## Runtime workspace

A store watchpoint on `$E3FF` stopped after the final store of the
startup clear loop at `$085D`. All four pages starting at `$E000`
were zero. A second watchpoint at `$E509` stopped after the map
builder's final high-byte store at `$12E7`. Each of the 191 words
split between `$E38C` and `$E44B` equaled `$8000` plus its row index
times 86.

In the LEVELA unpacker, store watchpoints at `$553F` and `$554E`
stopped after `$5636` with Y = `$F0` and `$FF` respectively. That loop
saves sixteen bytes that the decompressor's last pass restores. A
breakpoint after the restore confirmed that the scratch contents matched
the sixteen output bytes at `$6000`.

The zero-page swap at `$34B7` uses the page at `$CF00` as
runtime backing storage. The page was all zero at the resident
hand-over. Watchpoints on the first swap stopped at `$34C0` after
`$00EF` received zero from `$CFEF` and at `$34C4` after
`$CFEF` received the previous value of `$00EF`, `$87`.

## Sprite scheduling and spawn cursors

In Stage 1, the store to `$E08D` at `$2F98` recorded Y-coordinate
byte `$A4` for the first gathered actor. The store at `$2EEC`
staged its shape pointer, `$10`, at `$E02F`. A watchpoint at
`$E11A` also caught the scheduler writing `$FC` at `$2E80`
as the first entry of a schedule with no intermediate reuse boundary.

The spawn-window initializer at `$35A3` walks the stage's four-byte
spawn records. In the Stage 1 expansion, store watchpoints at
`$0016` and `$0018` identified the writes at `$35CD` and
`$35F8`. Both cursors ended at `$C310` in that capture.

## Glyph copying in Stages 3–9

Store watchpoints at the first destination byte stopped after the
last iteration of each backward copy, with X = 0 and Y = `$20`.
In each capture the 32 destination bytes matched frame one in the
expanded overlay.

| Stage | Store instruction | Destination | Frame one source |
| --- | --- | --- | --- |
| 3 | `$C890` | `$79C0` | `$C8BC` |
| 4 | `$C64C` | `$7960` | `$C678` |
| 5 | `$C618` | `$78F8` | `$C644` |
| 6 | `$C621` | `$7988` | `$C64D` |
| 7 | `$C5E0` | `$7960` | `$C60C` |
| 8 | `$C866` | `$79C0` | `$C892` |
| 9 | `$C5ED` | `$7988` | `$C619` |

## Boot copy under I/O

The OUG loader writes the first byte of the 116-byte sound initializer
prefix twice with I/O banked out. Store watchpoints at `$DF8C`
and `$EF8C` stopped immediately after the store at `$0183` with
A = `$AA`. The 116 bytes match at the resident hand-over and
in Stage 1. The resident music calls name the initializer at `$EF8C`.
The counted copy under I/O remains at `$DF8C`.

## Actor slots and contact

The resident allocator at `$374B` scans `$02–$2E` and returns X =
`$2F` on exhaustion. With all 45 slots marked active in the Stage 1
snapshot, a breakpoint at `$22AD` caught X = `$2F` before the
comparison against `$FF`. A watchpoint at `$E74F` then stopped
at `$22B4` after type `$27` was stored in that extra slot.

The resident player callback at `$1DD5` normally reaches the filtered
movement logic at `$1E56`. A controlled test of its two-player special
state with the selected slot matching `$70` stopped before the
immediate return at `$1DF8`.

With Stage 7 loaded, a controlled `$28AF` call started from
a parent 44 coarse columns away from player zero. It reached
`$2930` with Y = 3. A watchpoint on `$E813` stopped at `$2938`
after the removal flag was set.

## Round bonus

A controlled call to the resident exchange at `$3B96` started
with one ghost remaining, 49 credited and five lives. The store
watchpoint on `$81` stopped after the instruction at `$3BAE`
with six lives and no remaining ghost. The following store to
`$8F` cleared the running credit counter.

## The listing's error rate

At seed 6050, a separate gpt-6.2-sol checker read 65 of 1,845 comments.
Three findings held (4.6%, with a 95% Wilson interval of 1.6% to 12.7%).
The weighted estimate was 4.6%. The sample found an early return in the
resident special player-control path, a Stage 5 contact branch whose
shot update requires the removal counter to be clear, and a Stage 7
spawn request that can reject its new actor by distance. All three
comments were corrected. A fourth finding about the Stage 6 overlap
extent and sprite colour was settled by observing separate stores of
five to `$EA82` and `$E932` with X = 2. The affected comments name
the two fields separately. This is an estimate from one sample, and
the checker may have missed errors.
