# Turbo Charge — technical facts

These notes describe the Nostalgia disk release on PAL C64. Evidence
comes from instruction disassembly, targeted VICE execution and store
checkpoints, snapshot comparisons, and a captured raster frame.

## Stage dispatch and media

- Opening file `0D-N0S` displays a satellite sequence and hands
  off to the garage briefing in `0E-N0S`. At the `$315F`
  checkpoint the first sequence passed A=$0E and Y=2 to the
  loader. The observed boot path on this release began driving
  from the title. The debugger opening route uses the original
  loader from the title snapshot and its fire-to-retry prompt.
- The first drive loads file `01-N0S`. The stage controller calls
  `$0801` at `$A85B` and reads the returned state in `$A7BB`.
  At `$A86F` it loads the car-destroyed picture and at `$A88C` it
  loads the out-of-fuel picture. At `$A8C2` it loads the completion
  picture, then at `$A8E1` it loads the next drive. The debugger
  stopped at `$A8E4` after that call and at `$0801` when the
  stage began. The ending dispatch uses file `$19` and enters
  `$3000`.
- There are ten driving images and five chapter completions. The
  odd-numbered rounds show a border-smash card and the even rounds
  show a capture card. File `18-N0S`, shown after round 10, says
  **Game complete**.
- Every later driving load replaces `$0801–$68FF` and its stage
  sprite/character ranges. Odd rounds replace the music player
  and tune image at `$B000`. Even rounds retain it with a byte
  patch. Music credits in the odd-round snapshots identify Saudi,
  Egyptian, Chinese, Mexican and Thailand tunes. The title player
  credits identify Sean Connolly's **The Fast Lane** at `$B006`.
- The copy routine at `$A6CF` moves the interstitial image's colour,
  screen and bitmap planes from `$0800`, `$0C00` and `$1000`
  to `$D800`, `$6000` and `$4000`. See the picture parts for
  their layouts and display captures.

## Score table

The high-score data in `1A-N0S` is nine five-byte records loaded at
`$0405`. The first three bytes select sprite glyphs for initials.
The last two contain four packed decimal digits. The raster handler
at `$0DCF` reads the table and `$0BB4` inserts a qualifying score.
A VICE store watch from the title comparison at `$0BBA` caught
five writes to the leading record with an injected score of 9999.
The record held three `$24` initial glyphs and the packed score
`$99,$99` before the editor call at `$0BFC`. The path at `$0F44`
attempts a save unless `$02B3` is set. Disk persistence is open.

## Driving and controls

- `$0801` patches common road-blit operands and sets the stage's
  script base in `$0E/$0F` and the scenery descriptor base in
  `$29/$2A`. `$7A1F` doubles the script index in `$12` and jumps
  through the resulting pointer. `$7A33` consumes the next word
  as a scenery-stream address. `$8DE3` consumes scenery record
  triplets and recognizes markers `$FE` and `$FF`.
- The fork handlers at `$7A4B` and `$7A7E` use the following
  script word as a destination when the test at `$7B0E` takes the
  branch. The engine subtracts the script base from the destination's
  low byte and halves the result to recover the script index.
- Road pitch commands install three profiles together. In a targeted
  VICE run of `$7DC8` with `$13=$0A`, five store checkpoints fired
  once each. The routine installed the width, traffic Y and scenery
  height profiles at `$9FAF`, `$A1B4` and `$A064`, respectively.
  It also wrote the horizon and road-band positions at `$A740` and
  `$A746`.
- Traffic uses a stage-local table to map object type to a composition
  table. A composition begins with a sprite pointer, followed by
  relative X, relative Y and sprite-pointer triplets. An X value of
  `$FF` ends it. At round 2's `$1333`, an isolated VICE probe with
  record `$0A36` wrote four sprite pointers and three pairs of
  coordinates before reaching `$136C`.
- The shared bank exchange at `$9B76` swaps thirteen pages at
  `$3B00–$47FF` with `$C000–$CCFF` for selector 1. VICE counted
  3,328 stores in each range and the two saved byte sequences swapped
  places. The separate round-2 script overlay at `$234A` exchanged
  320 bytes between `$2386` and `$E080`, confirmed by a store
  checkpoint on each side. The trace is in
  `work/traces/resume-probes.jsonl`.
- The fire routine tests active-low CIA1 port A bit 4 at `$6D51`.
  A 100-frame hold followed by four released frames hit the initial
  press branch `$6D8B` once and the missile-spend instruction
  `$6DF2` once. The store watch on `$A736` counted one write
  and the stock fell from five to four. The sight at `$F3F8`
  changed from `$69` to `$6A` when held and to `$6D` after
  release. A neutral run from the same snapshot hit `$9392` 624
  times and left stock at five. The held run hit the same control
  624 times. Local trace: `work/traces/input-probe.jsonl`.
- The active-low left/right tests dispatch at `$6E93` and `$6ECE`.
  With up held, the left trial hit `$6E9A` 25 times and the
  right trial hit `$6ED5` 25 times. Holding up alone hit
  neither. Each trial had 624 hits on the hardware IRQ entry.
  Local trace: `work/traces/steering.jsonl`.
- Up took the acceleration branch at `$6F73` eight times in the
  first 30 frames and raised `$A7A4` from 0 to 16. The neutral
  trial stayed at 0. Down took the brake call at `$6F80` eight
  times from a stationary snapshot. In the Space trial the
  set-countdown instruction at `$6FAB` ran once, the countdown
  store watch counted 15 writes, and the speed reached 42 after
  60 frames. All four runs counted 360 hits at `$9392`.
- Turbo initializes `$A7A6` to 50 updates and decrements at
  `$6FD8`. It subtracts 24 fractional fuel units at `$6FCB`,
  compared with two at `$6F54` in the normal acceleration branch.
  Both subtract from `$A73B` and decrement `$A73A` on borrow.
  Local trace: `work/traces/driving.jsonl`.
- RUN/STOP enters the wait at `$6B38`. A VICE matrix-key probe
  reached `$6B42` on the first release, `$6B4C` on the second press
  and the return at `$6B56` after the second release.
- RESTORE triggers the round-one NMI. The handler at `$9365`
  tests the CIA2 interrupt flag at `$936A`. A VICE RESTORE trial
  reached the external NMI store at `$937F`, and stepping it
  wrote reason one to `$A7BB`. The neutral trial reached the NMI
  entry 24 times and the raster IRQ 72 times without reaching
  the external store.
- The crash recovery path tests the remaining-car glyph at
  `$F35D`. With glyph `$9D` and the override byte at `$0402`
  clear, stepping the store at `$6C5D` wrote return reason one to
  `$A7BB`. The controller takes the car-destroyed picture path
  for that reason. This probe isolated the final-car test.
- Round-one fuel vehicle processing at `$9D0F` checks the
  collision flag at `$A77E`. An injected contact produced
  three stores to `$A73A`, taking fuel from 8 to 11, and
  cleared the slot at `$A766`. At depth `$40` without contact
  the slot remained active. At `$3E` without contact it cleared
  without a fuel write.
- The border countdown at `$694A` subtracts one in decimal mode
  from `$A7D2/$A7D3`. The VICE probe starting from zero
  counted one store of reason three at `$A7BB` and 14 stores
  to the lower message row at `$F3DA`. The probe starting from
  one produced neither store and left the countdown at zero.
  The score deposit at `$78A1` carried 1298 + 9 to 1307, with
  one store to each score byte. The RESTORE, fuel, countdown
  and score traces are in `work/traces/verify-resume.jsonl`.

## Music data

The stage driver plays a two-voice tune from separate order streams.
`$B39F` reads an order event, `$B3F5` and `$B3FA` load the
selected pattern address and `$B402` reads the pattern. A pattern
ends with `$FF` after a note or hold. An order list instead uses
`$FF` followed by a byte offset to loop. The title driver uses
the same division between orders and patterns with three voices and
different table addresses. Instruction-read traces in
`work/traces/resume-tune.jsonl` and
`work/traces/resume-title-tune.jsonl` identify the observed extents.

The effect player has its own script and lifetime directories at
`$BE42` and `$BE62`. Calling `$BC4C` with each effect number
in the first lane exercised every byte of the 16 indexed scripts
in the kit CPU simulator. The trace is in
`work/traces/resume-effects.jsonl`.

## Display and text

| Register or address | Use | Evidence |
|---|---|---|
| `$D018` | Changes glyph set during the frame | The capture wrote `$CE` at line 10 cycle 49 and `$CA` at line 210 cycle 61. In VIC bank `$C000` these select glyph bases `$F800` and `$E800`. |
| `$F000`, `$F400` | Two 40-column screen maps | `$927E` clears twenty rows in the page chosen by `$0A`. `$08E6` toggles the page selection. |
| `$F3F8`, `$F7F8` | Sprite pointer 0 in the two screen maps | The fire path updates both and the frame trace shows the other sprite pointers being reused by the raster multiplexer. |
| `$DC04/$DC05` | CIA1 timer A latch | `$93DC` starts it with `$3780`. `$9392` examines CIA1 flags before dispatching the raster path. |
| `$DD04–$DD07`, `$D021/$D022` | Alternating background colour changes | `$93DC` programs CIA2 timers from the values staged by `$69B2`. The NMI at `$9365` chooses between the two colour pairs. |
| `$D000–$DFFF` RAM | Shared sprite shape slots `$40–$7F` | The round-1 sprite atlas renders 64-byte VIC shapes from the underlying RAM. Sight shapes `$69–$6C` lie at `$DA40–$DB3F`. |
| `$D400–$D418` I/O | SID voice, filter and volume writes | `$B000` initializes music, `$B003` advances it, and `$BBF4` advances effects. The instruction census is in `work/register-census.txt`. |

In the dashboard character set based at `$E800`, glyph `$80` is
blank, `$81–$9A` are A–Z, `$9B` is a dot and `$9C–$A5` are
0–9. The letter glyph bytes start at `$EC08`. The code uses this
encoding for **BORDER** and **MILES** templates such as `$09CE` and
for short road warnings near `$79B2`. The rest of the dashboard
and road glyphs are graphics. Renderings are in ignored work images
`font-e800.png` and `font-f800.png`.

## The listing's error rate

A fresh `gpt-6.2-sol` checker examined 95 of 6,047 comments. The
draw used seed 221910 and included 35 comments across seven
generated comment families.
Nine comments were wrong and all nine were corrected, along with
matching claims in other parts. They described the relocation bytes
in a packed picture, the pitch sequence selector and two SID voice
details, and the traffic and scenery projection and sprite fields.
The estimated error rate was 9.5% with a 95% Wilson interval from
5.1% to 17.0%. Weighting by stratum gives 9.1%. The checker may
have missed errors. The draw and verdicts are in
`work/reports/sample-221910/`.
