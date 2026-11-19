# Facts

## Boot and interrupt dispatch

The final decoder writes through the pointer at $AE/$AF from $0F00 and hands off at $801A. The saved entry was captured on a stopping execution checkpoint at $801A. Initialization at $80A8 sets the RAM IRQ, reset and NMI vectors to $80A0, $8091 and $8090. The software IRQ vector at $0314 dispatches the raster callbacks.

The title and play share one loaded image. The disk has one PRG, which the media ledger accounts for as the packed game. The instruction scan found no direct KERNAL LOAD call or jump at $FFD5. The indexed references that can numerically touch $FFD5 are data operations with operands that the drawing routines patch before use. The terrain and actor placement paths read the resident world arrays.

| IRQ entry | Next raster line | Work before returning |
|---|---|---|
| $814C | $D6 | Select the lower display character base, reset fine scroll, update the game and tick the sound driver. |
| $823A | $F6 | Clear bitmap and extended-colour mode bits. |
| $8259 | $30 | Set background colours, apply fine scrolling and select playfield character and sprite state. |
| $8302 | $CC | Select logo sprite pointers on the title or restore the actor frame pointers in play. |

Each entry ran 60 times in a 60-frame gameplay capture. The tick through $E003 and the ground movement dispatcher at $8F9A also ran 60 times in that capture.

## World and display

The VIC-II bank is $4000–$7FFF, selected through CIA2 port A at $80CF–$80D6. The screen matrix begins at $4400 and the terrain character set at $4800. The panel raster selects the alternate character base at $5000. The $8B17 initializer copies 160 panel screen codes from $FD80 into $471F and the corresponding colour cells from $FE20 to $DB1F. The tail of the screen matrix at $47BF–$47F7 retains its loaded bytes.

The world is a 208-column metatile grid at $1F00. Forty complete rows occupy $1F00–$3F7F. $896C reads eight rows of thirteen metatiles beginning at $02A9/$02AA, with a $D0-byte source stride. Each metatile index selects sixteen character codes at $0F00 plus sixteen times the index. Those codes form a 4-by-4 square. The expander lays them out in a 52-column buffer at $0880. A forced call with the starting map pointer $20A8 hit the world load watch 104 times, the dictionary load watch 1,664 times and the expanded-buffer store watch 1,664 times. $87EE copies a 40-by-20 window of those character codes into the top screen rows.

Six actor slots correspond to VIC sprites 2 through 7. The scanner at $9C06 interprets map codes $E0 and above as actor markers. The type is $20 minus the low five bits. The slot requirement comes from $9F33 and the initial sprite frame, offsets and attributes come from four-byte records reached through $9F4E. The renderer uses the one-hot masks at $9F2D to manipulate the actors' bits in the sprite registers. The collision pass at $B354 combines the latched sprite collision flags with software position bounds.

The VIC sprite bank starts at $4000. The first sixteen frames show the rope at different angles. The bank also holds item, Jack and actor shapes. $8DD9 exchanges 576 bytes between $F200 and $5380 to display the title logo. Actions including $C551 and $C6C0 construct transitional Jack frames in the mutable sprite slot at $68C0.

## Controls and movement

The walking dispatcher at $8F9A uses the current movement mode at $02C5 to index ten pointers at $8F86 and patch its JSR. On the opening snapshot, mode zero selected $8FBA. A CPU instruction trace of its read at $8FF3 showed the five-bit result $1F when neutral and $17 with right held. A stopping checkpoint reached $9198 on neutral, $9121 with right and $9108 with left.

The documented pause controls were confirmed at the instruction level. Commodore produced $DF at $8B9F and set the flag at $02CB before $8BAB. Port 2 fire reached $8BC1 with the flag cleared. RUN/STOP while paused branched to the title restart at $8015.

**Parachute.** In the falling path, $9833 increments the count at $03C4. The fire test at $9851 is reached at counts 30 through 49 when the early-fire latch and the other blocking flag are clear. That instruction masks only bit 4. Controlled calls from the play snapshot hit the parachute-flag store at $985A for both fire alone and up plus fire at count 30. Fire at 49 also hit it. At count 29 it bypassed the test, and at 50 it took the late-fall path at $989F. Setting the early-fire latch blocked activation at 30. These are routine tests from controlled state.

## Inventory, meter and restarting

$8B35 copies the forty six-byte initial item records from $F880 to $0500. $CD4C searches these records by world address when Jack crouches near an eligible item actor. It exchanges the stored fields with the held item, or sends pickups in the special slot class to another handler. $C7CE checks fire and selects an item slot. The handler index comes from the actual item value in that slot and is doubled for the pointers at $C7AE. Position-specific handlers such as $CC86 and $CD1F test both axes before setting their event flag.

The score has seven displayed decimal digits. $CF58 increments at the selected digit and carries left. $CF47 adds $40 to each display digit before writing it to the panel. $CFBB uses the same digit base for lives below ten. $CF9D renders the Naughtyometer into ten cells starting at $477E. With meter value four, the live routine hit four filled-cell stores and six space stores and wrote $52, $53, $52, $53 followed by six $20 bytes.

Some actor reactions increment $046E and request an extra life through $046D. In the event at $ACAB, negative differences are complemented without adding one. With saved X equal to 40 and the prerequisites set, the transition store at $ACD0 ran for actor X 37, 43 and 44, and missed X 36 and 45. The event at $ACEA compares the low sprite X byte for exact equality. At the completion actor, $ADFE requires player contact and that the Naughtyometer equals ten. With contact forced, the ending-flag store ran for meter values 9, 10 and 11 only in the case with value 10.

$BCFC saves the camera pointers, offsets and sprite positions. The restore path begins at $8C23. The game-over path at $C344 renders the alternate title frame and message, plays sound $0C and returns carry set to restart.

## Text and sound

The printer at $8EAD walks title text at $8EE5 and the game-over message at $C37D. Letters are stored as uppercase bytes. Subtracting $20 selects the screen glyph, while $20 itself passes through as a space. $F0 advances the row destination by forty cells and takes the next byte as the new column. $FF returns. The title credits Andrew Green, Terry Lloyd, Greg Holmes, Ben Daglish, Rob and Chris, and Gremlin Graphics.

The caller loads A with the sound number and calls $E000. Initialization multiplies the request by six to index three order-stream pointers at $E94C. The order reader selects note patterns through the low and high pointer arrays at $EB39 and $EB75. Notes carry a duration byte, and $A0 begins a timed gate-off rest. The main tick at $E003 refreshes the three SID voice register banks and writes master control through $E2AF. In thirty title frames it ran thirty times, with 550 writes to $D400–$D418. The $D418 store ran 25 times. A pending note or rest timer completion defers a register flush. Audio output used VICE's dummy device.

## The listing's error rate

Seed 411987 drew 60 of 839 comments. The independent checker ran on gpt-6.2-sol and found six errors, all corrected. The errors concerned coordinate asymmetry, the low-byte X comparison, the horizontal edge classifier, contact bounds, the ordering of queued movement and checkpoint saves, and the SID timer completion flag. The unweighted estimate was 10.0%, with a 95% Wilson interval of 4.7% to 20.1%. The strata-weighted estimate was 10.0%. The checker may have missed errors.
