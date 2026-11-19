# Turbo Charge — technical facts

These notes describe the Nostalgia disk release on PAL C64. Evidence
comes from instruction disassembly, targeted VICE execution and store
checkpoints, snapshot comparisons, and a captured raster frame. The
formal step-60 verification pass depends on completing the coverage
ledger in step 50.

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

## Driving and controls

- `$0801` patches common road-blit operands and sets the stage's
  script base in `$0E/$0F` and the scenery descriptor base in
  `$29/$2A`. `$7A1F` doubles the script index in `$12` and jumps
  through the resulting pointer. `$7A33` consumes the next word
  as a scenery-stream address. `$8DE3` consumes scenery record
  triplets and recognizes markers `$FE` and `$FF`.
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
- Pause and damage still need coverage work. The manual supplies
  the control names in [the checklist](features.md).

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
