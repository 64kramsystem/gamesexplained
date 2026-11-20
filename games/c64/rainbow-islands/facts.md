# Rainbow Islands technical facts

The game uses a resident engine, seven island loads and an ending
program. The island selector is zero-based at $A8 and the resident
loader compares it with $A9 at $7EDB. The selected player's island and
round fields are restored at $4E0C and $4E11. $62DA advances the round.
Every fourth increment also advances the player's island and $A8.

The loader fills a two-character KERNAL filename at $7FEC. Selectors
zero through six request suffixes 1 and 2 in order. Selector seven
instead requests file 71 at $0801, after saving the player records in
page $F0. The loader reads the first drive status character before
continuing. With the boot disk still mounted, a breakpoint-driven
request for the second island reached the retry loop with the filename
11 in $7FEC–$7FED. The complete supplemental disk reached $7EEA
after both reads for each of the seven islands.

Each first island file is copied from $9800 to $1B00 by $467A. The
type-indexed low and high script pointers are stored at $1B00 and
$1B20, with the initial object fields at $1B40, $1B60 and $1B80.
$6C57 interprets object script bytes by looking up a handler and reading
up to two following bytes. The map setup at $4ECB chooses one of four
round setup pointers and consumes the packed bit streams beginning
at the offsets in the $2100 header.

Each second island file holds character images, attributes, display
parameters and sprite images. $0F57 copies character pixels to
$C800 and uses per-slot flags, pointers, dictionary and offsets from
the disk data to build the sprites at $E800. Direct mode copies
63 pixel bytes and the slot stride is 64 in both modes.

## Display and input

- $4DB4 selects VIC bank $C000. The two play NMI handlers set
  $D018 to $13 for the playfield and $05 for the panel. The first
  combination selects screen $C400 and charset $C800. The second
  selects screen $C000 and charset $D000.
- The sheet rendered from $D000 shows the panel digits in slots
  $40 through $49 and uppercase letters in slots $4A through $63.
  The panel writer fills blank cells with $64. This is a private
  alphabet. The playfield set rendered from $C800 primarily holds
  tiles. The local sheets are `work/font-d000.png` and
  `work/font-c800.png`.
- $53BD is the play raster IRQ. $551E calls the multiplex setup
  through $5663 and advances the sound callback when $96 is zero.
  The NMI split alternates $5419 and $5464.
- $4BBF writes $FF to CIA 1 port A and ANDs the values read from
  $DC00 and $DC01 before consulting the direction tables at $163B
  and $164B. Fire is active-low bit 4. $4BDE stores its inverted value
  in $98, and the previous sample is retained in the patched
  operand at $4BDD.

## Instruction tests

| Test | Evidence |
|---|---|
| Attract credit | Holding F7 at the saved attract screen stopped at $4156. Stepping the store advanced $18B7 from $40 to $41. Carry was set on return to $4128. $416D and $4C27 handle the later player selection. |
| Joystick port selection | Single steps at $4BC4, $4BC7 and $4BCA distinguished the two reads. Right plus fire yielded the same $E7 combined sample on port 1 and port 2, with $98–$9A equal to $10, $00, $01. Neutral yielded $FF and three zero fields. |
| Right movement | A twelve-frame run from the saved Round 1 state executed six input reads. Right changed player X from $0C80 to $0E90. The neutral case kept $0C80. |
| Up and fire | In a twelve-frame up run, $746F and $748B wrote the jump phase and the high byte of the initial vertical speed once each. Neither store ran in the neutral control. A separate fire run hit the rainbow allocation decrement at $7D02 once, versus zero hits in the neutral case. |
| Spawn lookup after casting | With fire held, a stop at $5C13 captured the cast variant's fractional X store to $0941. The next stop at $5C2F read a byte from the round spawn records at $0200. |
| Island 2 starting height | With X equal to zero, stepping $4269 loaded $F8 from $1BB8. The next instruction at $426C wrote $F8 to the active player's Y field $0970. |
| Timing | During 120 PAL frames from the Round 1 snapshot, the main update at $4066 ran 60 times. The raster IRQ at $53BD and both NMI entries at $5419 and $5464 each ran 120 times. |

The private work folder contains the instruction and checkpoint traces.
The later island and ending captures use saved-state load fixtures.
They establish the loaded bytes and display states reached by that
setup. Natural progression to those states remains open. Step 65
therefore needed no input recording.

## Listing accuracy

An independent check on gpt-6.2-sol used seed 42 and found five wrong
details in 95 sampled comments out of 2,017. The observed estimate was
5.3%, with a 95% Wilson interval from 2.3% to 11.7% and a 5.3%
estimate weighted by the sample strata. The checker may have missed
errors. The listing incorporates all five findings. The raw draw and
verdicts are in
`work/reports/sample-42/`. A full audit on a proven model remains open.
