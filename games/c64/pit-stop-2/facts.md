# Pitstop II — technical facts

Static addresses refer to `work/entry.vsf`. Live observations identify
the state and the breakpoint, watchpoint or captured write.

## Loaded image

| Range | Role | Evidence |
|---|---|---|
| `$0800–$0FFF` | Boot residue at handoff, later race workspace | The entry image matches the tape payload from $0801. $43BB builds the $0800 lookup. $4485/$448B build map coordinate arrays. $452A/$4530/$454A/$4550 generate distance tables. |
| `$1000–$32FF` | Five road character source sets | $43C2 copies the first seven pages. $6184 has page indices $10, $17, $1E, $25 and $2C. $42B6 uses these and their pixel-remapped variants. |
| `$3300` onward | Race engine | $3300 jumps to $3314. The foreground loop at $41A0 alternates the driver index. |
| `$6D00` onward | Pit display, crew update and results dispatch | Nine jump entries starting at $6D00. $6DAB/$6DBE prepare the pit graphics in steps. |
| `$9400` onward | Setup menu, name entry and standings | $9400 enters the standings at $9D5C. $9403 initializes the setup menu. |
| `$C000–$C05D` | Title bootstrap | Execution stopped at $C000 after decompression. $9550 later clears these bytes as part of the menu screen. |
| `$C05F–$C7FF` | Screen workspace | Decoder output is zero here. $953E builds the first matrix and $3485 copies it to the second. |
| `$C800–$CBFF` | Race dashboard character bank | Display selected by $D018 value $02. $4F36–$4F4B copy the four pages when drawing the starting grid. |
| `$CC00–$DE3F` | Car sprite area in VIC bank $C000 | $480C adds $30 to selectors from $5B6F–$5BDD. The highest selector $48 gives sprite pointer $78 and slot $DE00. |
| `$E000–$EFFF` | Authored title colour data, matrix and font at handoff | $C000 installs the colour pages. CIA2 and $D018 select matrix $E400 and font $E800. Later states reuse the region. |
| `$F000–$FFFF` | Relocated compressed-stream residue at handoff | This range equals the last 4,096 bytes of the decoder's input. Race setup populates graphics in this range and the game writes the hardware vectors here. |

The listing uses the handoff to retain title material that the menu and
race replace. The one tape directory entry maps to this resident image.
The code mapped from the handoff and race captures contains no direct
call to KERNAL LOAD at $FFD5. A full search of the remaining indirect
paths is open.

## Text encoding

The setup font source at $A600 renders code 0 as blank and $01–$1A as
A–Z. Codes $30–$39 render digits 0–9. $95E5 copies label glyph indices
directly, with $00 between words. The input scanner at $9B84 translates
the active CIA matrix position through $9BCF. In that table $7E and $7F
are edit controls for delete and Return, and $FF is the no-action value.
The title uses composite glyphs at $E800, including distinct shapes
for pieces of the logo and chequered flag.

## Race display and input

- **Live.** The grid frame capture records IRQ vector writes selecting
  $3672, $36B8, $371A, $3ECD and $4008. The moving-race frame captures
  168 watched writes across a PAL frame. A stopping store watchpoint on
  $FFFE caught $4025 with A=$CD and PC=$4028. Stepping twice left PC at
  $402D after the store of $3E to $FFFF.
- $3485 copies the 25-row race screen and colour templates using split
  row tables at $5CFC, $5D15, $5D2E and $5D47. $408D updates nine runs
  in the inactive screen matrix using a road-progress index.
- $480C composes cars from up to three sprites, with separate sprite
  enable, multicolour, horizontal offsets, vertical offsets and pointer
  lists. Raster handlers rewrite those registers and pointers for the
  two views.
- $4FA1 waits for the first fire input on either CIA1 port. It records
  the port index at $7C. $4FCE waits for the other port in two-driver mode.
  $387A reads the selected port first and the other second, into
  $03D2/$03D3.
- **Live.** On loading `work/actual-race.vsf` and holding port 2 up,
  an execution checkpoint at $388C found $03D2=$FF and $03D3=$FE.
  A store checkpoint on $46 then stopped at $395B, just after
  `STA $45,X` with X=1. The speed word changed from $02E1 to $02F3.

## Race mechanics and sound

- $392C shifts the accelerate bit into carry and adds $12 when that bit
  is low. $3948 uses the next bit to subtract $40 for braking. $39B3
  applies an additional $09 when the turbo bit is low. Both acceleration
  branches cap the two-byte speed at $29FF.
- $3AFA bounds the pit entrance to road-view selectors $15 through $1E
  after a lateral-position test. Its successful path writes pit state 1
  at $50,X and clears movement variables.
- $3B2B tests the four tyre-state bytes for the active driver. Reaching
  7 saturates the wear byte. The transition sets the driver's $76,X state
  and starts the SID voice-3 noise effect.
- $3553 restores a 25-byte SID default table. $3C8E drives the selected
  engine voice from the current speed bytes through a per-driver SID
  offset at $5078. The register evidence establishes the writes.
  Audible behaviour was outside this dummy-audio run.

## Hardware access census

| Registers | Use | Examples |
|---|---|---|
| $00/$01 | CPU memory mapping | $9407, $940B, $331B |
| $D000–$D010, $D015, $D017, $D01B–$D01D, $D025–$D02B | Sprite positions, masks, priority and colours | $353A, $3ECD, $480C, $7C8F |
| $D011/$D012, $D019/$D01A | Raster selection, acknowledgement and scheduling | $3451, $3672, $36B8 |
| $D016/$D018, $D020–$D023 | Character modes, screen and glyph bank selection, border and road palettes | $3485, $3672, $375C, $4008 |
| $D400–$D418 | SID initialization, engine pitch and effects | $3553, $3B2B, $3C8E |
| $DC00–$DC03 | Joystick reads and keyboard matrix direction/scan | $997C, $387A, $9B84 |
| $DC0D | CIA interrupt masking and acknowledgement | $3458 and $9469 |
| $DD00/$DD02 | VIC bank selection | $3500, $3508, $94D5 |

The full static census is in `work/census.txt`. Indexed accesses can
reach registers beyond the operand shown in the listing. The VIC reads
some graphics beneath the CPU's I/O window.

## Open

The exact refuelling overflow path and the historical purpose of the retained
workspace copy at $6BAE are open. CPU watchpoints on $61E4–$6CFF and
$DE40–$DFFF stayed at zero in the short moving-race probe. The two regions
remain counted. Their table structure, duplicate material and fill records
are described without assuming the short probe exhausts possible readers.

## Live tests

- From the same moving-race snapshot, stop at $388C after both CIA
  samples, then at $39D2 for X=1. The speed starts at $02E1 each time.
  Neutral leaves it unchanged. Up or fire alone adds $12. Down subtracts
  $40. Up and fire together add $1B, including the extra $09 from $39B3.
  The stored input bytes distinguish the five cases.
- With PC set to the position-qualified pit entrance branch at $3AFA,
  stop at $3B17. Selectors $14 and $1F retain state 0 and speed low $34.
  Selectors $15 and $1E set pit state 1 and speed low 0.
- With PC set to $A134 after the standings acknowledgement, course $01
  enters the menu at $9439. Grand Circuit course $83 increments to $84
  and enters the race at $3300. Flagged course $85 clears the course
  option and enters $9439.
- Over 200 PAL frames, execution checkpoints count 399 entries at
  $3822 and six coarse clock updates at $38B0. The two countdown bytes
  at $61B1/$61B2 each fall from $39 to $36. The code reloads the divider
  to $3B, so each displayed second takes 60 updates for that driver.

## The listing's error rate

Seed 1984 drew 80 of 707 comments. An independent gpt-6.2-sol checker
found four errors, all corrected. The corrections cover the shared road
colour row at $5E14, the grid prompt and biased curve-lookup operand
at $5FBD, the tyre colour-cell offsets at $7ACD and the source and
destination pointers for pit graphics at $8200 and its sister pages.
The plain estimate is 5.0%, with a 95% Wilson interval of 2.0%–12.2%.
The weighted estimate is 5.8%. The checker may have missed errors.
