# Ninja Spirit technical facts

These findings refer to the DCS disk image and the snapshots in
[orientation.md](orientation.md).

## Loading and memory

The loaders at `$BA00`, `$BA03`, `$BA06` and `$BA09` set the first
letter of the three-byte SETNAM pattern at `$BA68`. The common path
opens the file on device 8 and unpacks two backwards streams. CPU
breakpoints at `$BC73` and `$BC38` recorded the destination moving from
`$A000` to `$2780` and from `$F800` to `$DB40` for each file.
`$BAB8` enters the new load at `$2780` with the KERNAL banked out.
The breakpoint logs and capture scripts are in local `work/`.

| Address | Role |
|---|---|
| `$2780–$3FFF` | Round code and tables in the low part of each first packet. |
| `$4000–$9FFF` | Stage tile maps. Load A's window copier at `$222A` reads 40 bytes per row, using 512-byte row spacing. `$127B` also has a 96-byte stride path selected by the flag at `$277E`. |
| `$C000–$DB3F` | First 109 VIC sprite slots. The rendered atlas shows player frames, life icon, weapons and effects in this range. |
| `$DB40–$EFFF` | Stage sprite slots `$6D–$BF`. Each slot starts on a 64-byte boundary. |
| `$F000–$F7FF` | Stage character patterns, eight bytes per character. |
| `$F800–$FBFF` | Screen RAM and sprite pointers. `$222A` copies the visible map rows here and the IRQ writes sprite pointers at `$FBF8`. |
| `$FC00–$FFF9` | Upper half of the HUD and title character data selected by `$D018=$EE`, before the hardware vectors. |

## Raster and graphics

`$22FC` drives CIA2 port A bits 0 and 1 low to select VIC bank `$C000`.
`$23C5` installs the hardware IRQ vector at `$FFFE` while the KERNAL
is banked out. `$2405` saves the live registers and jumps through
`$0012`. `$2363` orders sixteen logical sprite indices by descending
Y and `$1304` copies their position, shape and colour into the
arrays read by the raster handlers.

A live store watch on `$0012` in Round 1 stopped after the stores at
`$246C`, `$24F0`, `$250E` and `$252F`. These write the low bytes of
`$24A3`, `$2502`, `$252D` and `$240E` respectively. The store
watch stopped before the following high-byte write, so a value read
at the stop can combine the new low byte and the old high byte.
`$24A3` updates the sprite registers and can reuse hardware sprites
lower down the display. `$2502` and `$252D` switch the setup to the HUD.
The latter calls sound updates at `$A287` and `$A543`.

## Controls and HUD

On load A the title waits at `$2A24` for the active-low fire bit of
`$DC00`. Live port 2 fire reached Round 1. The stage loop at
`$2846` reads that port into `$273F`. `$2B7B` compares the keyboard
matrix port with `$EF` and increments the weapon selection by
two, wrapping from eight to zero. A separate latch prevents repeat
selection while the same press remains held.

`$1061` decrements the BCD seconds once each time the active tick
divider reaches zero, with a reload of 50 ticks. A borrow reloads
seconds with `$59` and decrements the minutes. The next borrow at zero
minutes enters `$1219`. Four parallel glyph tables at `$10F7`,
`$1101`, `$110B` and `$1115` provide the two-by-two HUD digits.

### Custom title and HUD character codes

The glyphs rendered from the upper half of the `$F800` character bank
and the selectable initials table at `$0B49` give the following
substitution. `$A3–$B0` spell A through N, `$BD` is O, and
`$B1–$BB` spell P through Z. `$BC` is a dot. `$BE–$C6`
represent 1 through 9. The circular O glyph also serves as 0 in the
ordinal and score text. `$FD` is the space.
Examples include GAME OVER at `$0890`, LEVEL X CLEARED at `$0D3F`
and the title at load A's `$2A2C`.

## Sound

The initialiser at `$A251` clears SID registers and enables master
volume. The raster HUD handler calls two tick routines. `$A287`
processes effect requests indexed by SID voice offsets 0, 7 and 14.
`$A4E6` selects a 16-byte tune descriptor from `$ACC0`, from which
`$A96F` takes the three voice sequence pointers. `$A543` advances the
music. The low and high tables at `$AD50` and `$ADCA` address note
patterns. Read state and envelope writes at the actual SID registers
when considering sound with this setup. The emulator used dummy audio.

## Live tests

- **Controls.** Port 2 Up reached the engine’s jump branch. Stepping
  `$190B` stored the initial velocity `$FD` at `$008D`. The neutral
  control window recorded no jump starts while HUD IRQs continued.
  Matrix P reached the engine’s `$1039` comparison with A=`$FD`.
  Space reached the load A comparison and stepped store described in
  [load A’s facts](parts/a/facts.md).
- **Timer.** Stop at engine `$1061` and set 2:00 with a downcounter of
  1. Execution reaches the redraw at `$1098` with 1:59 and a
  downcounter of 50. At 0:00 it reaches `$1219`, then sets player death
  state 1 at `$1225`. Over 150 PAL frames, the engine’s HUD interrupt
  ran 150 times and the timer divider’s decrement at `$1066` ran
  80 times. The timer uses eligible gameplay ticks.
- **Retained bytes.** The local watches in loads A, C and D each used
  the gameplay input store at `$273F` and reads of the current map at
  `$4000–$9FFF` as positive controls. The packed gap in load A, the
  earlier maps retained by loads C and D, and the engine’s surplus
  boot bytes after `$B903` had zero relevant CPU hits in the measured
  intervals. The decoded direct and indexed references and the
  pointer tables establish the bounds used in the part ledgers.

## The listing's error rate

The sample used seed 20261119 and drew 80 of 1,141 comments.
An independent `gpt-6.2-sol` checker found 11 wrong details, all
confirmed and corrected. They involved the map-refresh branch,
the opening animation, a spawn type, a callback table’s unused zero
entry, a third-hit transition, restart message text, component
coordinates, timing edge cases and two SID effect fields. The
estimated error rate before corrections was 13.8%, with a 95% Wilson
interval of 7.9–23.0%. Weighting the generated and written strata
gives 12.1%. The checker may have missed other errors. A separate
sprite subject identification was inconclusive and its description
now refers to the visible shapes.

Verification uses direct loader entry points for the disk
handover snapshots and isolated instruction tests in play.
Step 65 applies when the workflow needs a play route that
runs again. The loader entry points and instruction checks give the evidence for this run.
