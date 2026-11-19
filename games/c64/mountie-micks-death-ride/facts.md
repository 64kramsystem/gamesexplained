# Mountie Mick's Death Ride technical facts

## Build

The analysed release is the single-PRG disk build catalogued as CSDb 246550. The [boot recipe](orientation.md) describes the crack intro and unpacker. The packed image, the two engine snapshots, the annotation log and trace scripts are in local `work/`.

## Memory layout

| Range | Use |
|---|---|
| $0003-$00FF | Screen, input, actor and audio work bytes. |
| $0300-$03FF | Eight actor slots in parallel arrays, starting with state at $0300, X low at $0310, Y at $0320 and image pointers at $0330. The high X bits and software visibility mask are in $34 and $35. |
| $0400-$0517 | Seven 40-column terrain ring rows. $1AFE-$1B24 write the next column at the index $C2. |
| $1000-$3FFF | Engine startup, the raster and main loops, the train and scenery renderer, actor states and data. |
| $4000-$47FF | Playfield and alternate screen, with sprite pointers at $43F8 and $47F8. |
| $4800-$7FFF | VIC character graphics and sprite patterns, with overlapping use where a sprite points into character memory. |
| $8000-$9FFF | Title and high scores, equipment and sound effects, wagon scripts and mutable wagon definitions. |
| $A000-$AC0F | Three-voice music driver and its song data. |

Boot enters at $1000 and the loader's high RAM staging residue begins at $AC10. The load counter, source and destination boundaries were read at CPU checkpoints. The resident train data selects a new script by pointer. The disk directory contains no separate level files. A Train 9 initialisation probe hit two pointer reads and 158 script reads, with 268 hits at the control IRQ breakpoint and no hits at the KERNAL LOAD entry $FFD5 during those 45 frames.

A consistent sequence of high-memory byte runs resembles the unpacked material at lower addresses, with varying offsets. The stores at $0836 and $0166 distinguish the source staging copy from the ascending output. See the [loader description](orientation.md).

## Timing and display

The running game takes interrupts through $FFFE, which points to $1220 in play and $8525 on the title. The handler at $1220 cycles through six positions. A 40-frame probe counted 240 entries at $1220, 40 entries at the slot-four body $127D and 11 control-sampler entries at $14FA. The game does its playfield work on divided timing. The $110A poll also runs as a busy wait and its hit count is unsuitable as a frame rate.

The six reached stores at $1255 showed the following pre-store state. Raster is the line when the watched instruction was reached.

| Raster | Table slot | $D018 | Character base |
|---:|---:|---:|---|
| 46 | 5 | $04 | $5000 |
| 85 | 0 | $04 | $5000 |
| 110 | 1 | $02 | $4800 |
| 169 | 2 | $02 | $4800 |
| 178 | 3 | $06 | $5800 |
| 210 | 4 | $06 | $5800 |

The $5000 characters draw the top backdrop and $4800 the train section. $5800 includes the lower track and panel graphics. $8D2C writes $1E for the title, choosing screen $4400 and characters at $7800 in the same VIC bank.

| Registers | Role and evidence |
|---|---|
| $0000-$0001 and $DD00/$DD02 | $102C-$1045 set the CPU port and the VIC bank. |
| $D012, $D016, $D018, $D019, $D021-$D023 | $1236-$1273 adjust the raster compare, fine scroll, character pointers and colours, and acknowledge the raster interrupt. |
| $D000-$D010, $D015, $D017, $D01C-$D01D, $D027-$D02E | $132A-$1437 publish the staged actor coordinates, image flags and colours. |
| $D01E | $1315 reads the sprite collision latch. $2851 and $28BF then refine candidate collisions using positions. |
| $DC00-$DC03 | $14FA-$1544 read both joystick ports and scan the keyboard when both sticks are neutral. |
| $D400-$D418 | $8DF2 and the music tick update the SID. $8E33 copies its second-voice-onward shadow group in the effect branch. |

## Controls

$14FA makes both CIA1 ports input, combines their low-active values, and inverts the five direction and trigger bits. The instruction at $150E stores the result in $30. If this is zero the loop at $1512 scans the keyboard using the 64-entry table at $15D2. The named keys below were stopped at $1546 after the complete keyboard scan. Bits may combine for diagonal and simultaneous joystick directions.

| Control | $30 at sampler exit | Observed downstream |
|---|---|---|
| Up / A | $01 | State $05 and $2E21 jump update. |
| Down / Z | $02 | State $06 from the standing test. |
| Left / O | $04 | $2F55 called twice in an 18-frame Train 1 probe. |
| Right / P | $08 | Sampler output checked. |
| Fire / Space | $10 | Reaches the shot path in standing play. |
| T | $80 | Torch path at $8214. |
| G | $A0 | Gas mask path at $82D3. |
| H | $E0 | Four matching samples reached the pause store at $81DA, clearing $36. |
| M | $FC | Four matching samples reached $157F, changing $F0 from one to zero. |
| S | $FD | Sets Mick's damage state to $13 at $15A6. |
| Q | $FB | The static decoder exits via $155B to the title path at $107F. |

## Mechanics

- The train advances through fine scroll and then shifts its character and colour rows one cell right at $19AA. $24F0 selects a script using the one-based train index. The script pairs hold an event byte and an even wagon type. The latter indexes little-endian definitions at $9212, where the type-zero pointer terminates playfield columns. The leading nine-byte header includes mutable count and cursor and a setup callback copied to $1AD3-$1AD4.
- $32B9 and $3368 map the actor position to a ring row and column, then consult the $9100 contact table. Per-state handlers use the samples around the actor. $2B68-$2B76 patch the call to the selected word at $2B99. A resulting A value becomes the slot's next state.
- Standing fire reaches $314C when slot three is free and $CF is nonzero. In the Train 1 probe $CF was $13 at $315D and $12 at $31B7, where the new slot's state is about to be stored. $1464 later moves state-$11 projectiles eight pixels horizontally and updates the wrapped terrain column. $2851 uses VIC overlap plus distance tests before assigning a hit state. Ducking fire reached $3C21. With supply type two set in the starting inventory, the slot was cleared and the routine reached its template call at $3C83.
- $82D3 equips a mask by replacing item type $01 with $81 and setting $0F. $362F checks wagon high nibble $50 and $0F before setting the damage state. $8214 tests the slot-two terrain flag and charge before the torch can be enabled. In a controlled probe with charge $20 and the tested terrain flag set at the branch, three $80 samples reached $826D with the torch latch set. The torch draw in $832A can use up to six columns across three rows.
- $10A5 starts the retry counter at three and $2396 displays that many icons. The damage test reaches $1166. If the counter is nonzero, $1171 debits it and the retry path searches backward for the wagon checkpoint tag. At zero it goes to the title. Pressing S gave $03 and $02 on either side of the debit.
- The handcar code at $3DBF starts slots zero, one and six from staged position templates. $3E42 checks the rider's up and down controls for pumping and returns the rider to the already selected train when its position and terrain tests pass. $3F15 clears the approach flag and $3F22 saves that train as the retry point. The train scroller selects the next script earlier at $1AAA, when the trailing gap reaches $2D.

## Data tables and text

| Train | Script | Progress cells |
|---:|---:|---:|
| 1 | $922C | 5 |
| 2 | $9244 | 8 |
| 3 | $9266 | 10 |
| 4 | $9292 | 13 |
| 5 | $92C8 | 15 |
| 6 | $9308 | 21 |
| 7 | $9360 | 27 |
| 8 | $93D0 | 33 |
| 9 | $9458 | 36 |

The diagram setup reads every second byte until the type-zero terminator at $24B0. It divides the terminating offset by four at $24B8 to obtain the displayed diagram length. $24E0 marks type-$02 engines. The opening display of each train was captured after entering its own initialiser. Those captures establish the resident starting data and do not establish player reachability between trains.

The title text renderer at $8577 reads the banner as direct character indices. Its $7800 character map has space at $20, digits $30-$39, A-Z at $41-$5A, and conventional punctuation in the $21-$2F and $3A-$3F ranges as rendered. Its $5E/$5F glyphs are up and left arrows. $85CB starts the fire prompt and control legend, $86A6 begins the extended credits, and $881D is the initials prompt. The score rows are stored at $8C1B in ten-byte records. The play HUD uses a different font. The visible train and score labels use $01-$1A for A-Z, the digit run is $30-$39 and another numeric glyph run starts at $21.

## Sound

The raster-side audio path selects the music driver or alternate play sound using $F0 and $F1. $A01F advances three track counters. Stream values $01-$21 dispatch through $A644, and note and duration data continue at $A153. $A536 converts notes through a semitone frequency table and octave shifts. $A700 holds the header for streams starting at $A704, $A8F2 and $AA6E. $8E85 loads one effect record with seven SID register settings and a duration, and $8DF2 combines the active effect and music shadow when writing the chip.

## Open questions

- The reported Train 7 obstruction and left-edge bypass are unresolved for this disk build. The Train 7 script at $9360 and its opening picture identify the wagon order. The terrain probes at $32B9 and movement boundary branch at $3B5A are the starting points for a focused check of the obstruction.
- The embedded filename marker at $9FE9 and the retained tile sequences at $8F22 and $9E00 have no established runtime consumer. The direct address search was checked with the full index range and the active wagon pointer table was decoded. Other computed uses remain open.

## Live tests

The local scripts are `work/entry-trace.py`, `work/loader-watch.py`, `work/levels.py`, `work/verify.py`, `work/verify-actions.py` and `work/verify-effects.py`. They use the assigned VICE ports. Instrumented probes restore the same Train 1 snapshot for the neutral and input runs. The movement/no-input comparison used six IRQ entries per frame as its positive control. The torch and grenade probes seed the stated prerequisites. They establish the inspected instructions' effects.

## The listing's error rate

An independent `gpt-6.2-sol` checker sampled 65 of the 995 pre-correction comments with seed 20261119. Four findings held and all four were corrected. The estimates are 6.2% unweighted and 6.3% weighted by stratum, with a 95% Wilson interval of 2.4% to 14.8% for the unweighted estimate. The checker may have missed errors. The corrections concern when the handcar approach flag clears, the train character patched by a late event, the first offset in the stored HUD definition and the start of the equipment row.
