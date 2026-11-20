# Ghouls 'n Ghosts — technical facts

These are findings from the TWT disk release. The disk fingerprint, snapshot routes and loader entry table are in [orientation.md](orientation.md). Instruction stops and watchpoints cited below support the corresponding observations.

## Program layout

| Address | Contents | Evidence |
| --- | --- | --- |
| $0400–$10FF | Arthur pose slots | The page and offset tables at $49DF and $49C1 supply the source for the copy at $4990. $A5 selects the costume or transformation offset. |
| $1700 | Game initialization, then a playfield tile buffer | The boot jump at $8A31 enters this address. A store watchpoint at $1700 during play stopped at $4CB8, just after the tile write at $4CB5. |
| $2993 | Title/game loop | The entry checkpoint caught this address before interrupts were enabled. It calls the title at $538C and then starts play at $29A0. |
| $86E9–$BFFF | Stage-specific code and tables | All five even loader IDs decode to this exact window. |
| $C000, $C400 | Two screen pages in play | The playfield IRQ chooses between these using the two entries at $5D84. |
| $C800–$E7FF | Stage sprite patterns | A 64-byte-aligned render exposed the sprite frames. VIC pointers use the low two bits of CIA2 port A to select the $C000 bank. |
| $E800, $F000 | Terrain character sets | $5CDD writes the VIC pointer using the charset offsets $0A and $0C at $5D86. |
| $F800–$FFBF | Title and panel glyph load | The decoded font matches boot RAM. The game reuses part of this area for generated sprite shapes. |

## Timing and input

- The hardware IRQ at $5C31 increments $0D and dispatches according to the operand at $5C3B. An execution checkpoint counted four entries in four frames in stage 1. $5F5E waits for $0D to change.
- CIA2 Timer A supplies timed raster splits through the changing NMI vector. The normal play path at $5CA2 configures the timer and $5D88 waits past line $C6 before selecting the panel font. The gameplay update at $29AE waits on $DD, which the NMI handler at $5E80 increments. An instruction stop at $5C3A in stage 1 read mode zero and the next stop at $5CA2 confirmed the playfield branch.
- Title input uses CIA1 port A at $5F19. Left selects MUSIC and right selects SOUND FX. A store watch on $1F while holding right stopped at $5F30 with $1F=$FF. Fire is tested at $541B after the IRQ writes the button sample to $D9. The joystick port used for this is port 2.
- During play, $5176 reads and inverts the direction bits and $52BF tests the fire bit. $302A reads the keyboard by selecting a matrix row through $DC00 and sampling $DC01.

## Tiles and actors

- The fine horizontal scroll counter runs from $00 to $27. In a probe at $51FB, setting the leftward movement bit and starting the counter at zero produced a write of $FF from the decrement at $5205, then $27 from the wrap path. A watch on the coarse column stopped after its decrement at $520D.
- The resident sprite-list builder reads a descriptor using the shape-index tables at $1F44 and $2044. The single-piece descriptor at $2386 contains $00, $06 and $2B. Execution stops after the writes at $36A3 and $36A9 showed colour $06 entering the list at $1830 indexed by the render slot and sprite pointer $2B entering the list at $1848 indexed by the same slot. For composite descriptors, $36C0 reads a shared colour, then a pointer and two coordinate offsets for each piece.

- Stage layout rows are 19 entries wide, as shown by the row offsets at $1BCB. Each nonboundary byte is an even offset into the little-endian pointer table at $4CF0. $FF marks a boundary checked at $528B and $52A6.
- Each chunk pointed to by the table contains 20 by 10 tile indices. The copy at $4C76 resolves visible tiles into $1700. Four lookup pages at $BC00–$BFFF expand each index into an upper-left, upper-right, lower-left and lower-right character.
- $4BF8 flips the screen index in $BD and maps terrain character codes through one of the two colour pages at $BA00 and $BB00. The bank chosen by $2EEF also determines the terrain property page and the vertical offset page used by $48CC.
- $30B3 uses fixed six-byte actor records with little-endian tile X and Y, a byte of sub-tile offsets and an actor ID. $3175 scans five-byte optional spawn records and applies a visibility check and a random condition. Stage-section initialization at $2E4D sets both table pointers.
- $29FE checks the outcome at $9C. A negative result other than $FF advances to the next even stage selector. $FF decrements the remaining-life counter at $A4. Stops at $29FE and $5B6A reproduced the four subsequent stage loads using the outcome branch.

- The actor dispatcher at $36FC reads the type for each slot, patches the call at $370D from the paired tables at $1DE6 and $1E5C, and visits slots in descending order. In a targeted probe, setting slot $17 to type $20 at $36F5 reached its handler at $3A00. A store watch on the slot’s X coordinate stopped at $3A06 after the handler copied the base value from $199C indexed by the slot. In a second run with shape $16, read watches stopped just after the two extent loads at $3D65 and $3D6A, with X extent $10 and Y extent $04.
- The charged weapon handler at $33AF writes a JSR at $29B8 and sets its target from the tables at $33C3 and $33C9. With the screen-strike target $33CF set in the call and the phase gate set to zero, an instruction stop hit $33CF and a colour RAM watch stopped after the first cell-colour write in the vertical drawing helper. This probe exercised the handler with the debugger setting its entry conditions.

## Text and sound

- Rendering eight bytes per glyph starting at $F800 gives digits at $00–$09, uppercase letters at $0A–$23 and lowercase at $24–$3D. $3E is blank and $3F is the full stop. At $40–$49 the image shows exclamation, double exclamation, comma, apostrophe, colon, semicolon, question mark, a line, an arrow and a heart. The high glyph positions include the large title shapes.
- $5F67 takes a script inline after the JSR and returns past the terminator. $5F85 outputs glyphs for nonnegative tokens and dispatches $80–$EF as commands. Tokens $F0–$FF select a colour. The routine at $5FD5 patches the target screen and colour pointers using the row table at $1B84.
- $6150 selects three voice pointers, one for each SID voice, through six seven-entry tables at $730E–$7337. The call at $5405 starts title track zero. The stage descriptor at $2ECB installs the three track-six pointers from the active stage overlay. The voice-one decoder at $6360 selects either a note or a command using the high bit. The note-frequency tables at $6D35 and $6D96 supply the low and high SID registers. In a title snapshot the voice-one decoder hit $6360, and a SID frequency watch then stopped at $639E after the write to $D400. The emulator used dummy audio.

- The SID command decoder uses 21 handlers per voice for commands $80–$94. The actual voice-one low and high address tables start at $6CB7 and $6CF6, because the decoder adds the unsigned token value to the instruction operands $6C37 and $6C76.
- Command $94 consumes two fallback pulse-width arguments. All three voice handlers store both arguments at their respective low-byte address. A targeted title probe supplied $34 followed by $12 to voice one. Two write stops on $6A05 caught the stores at $6C8C and $6C92, and the stored pair was $12,$00.

## Ending, controls and score

- In the resident keyboard routine at $302A, Commodore yielded $DF and reached $3064. A watch on $DB2F stopped after $3068 wrote colour seven into the pause indicator. Q yielded $BF and reached $3051. A watch on the most significant score byte at $1C51 stopped after $3055 cleared it.
- The resident extra-life routine at $6115 compares the score at $1C51 with the packed decimal threshold at $6141. In a stage-one probe, setting the score to 2,000 at the routine entry took the life increment at $6126. The watch on $A4 caught four becoming five. The watch on $6142 caught the threshold rising to 9,000.
- From stage five, setting the outcome to $80 at the resident test at $29FE reached $2A1C with selector $0A. Execution then reached $2A23 with text pointer $2ADD and $2A28 with song index five. The resident continue prompt at $2A93 instead waits for fire and decrements the allowance at $2A91 before restarting the current section through $29A2.

## Disk reads

The TWT introduction and `LOADER` are directory files. The named request reused by the resident wrapper at $03A2 sets its name from $03EE through $03F3. The bootstrap calls the raw loader at $C006 with $0A, $0B and $0C at $02AC, $02B4 and $02C1. The resident title call at $5391 supplies selector zero to $5AF6. The transition at $2A13 supplies the successive even selectors and branches into the ending at $0A. The two raw requests at $5B5C and $5B67 load the even selector and its successor. The sector ledger follows both named file chains and all thirteen raw chains. The repeated fill and other sectors outside those chains are recorded in [media.json](media.json).

## High scores and the name check

$5589 reads ten 20-byte records starting at $5971. The first three bytes carry the packed decimal score and the other 17 hold the player's name. $562B performs ordered insertion. The cursor loop at $57B3 uses the joystick to navigate the glyph grid.

$58ED compares 17 screen cells with `WIGAN RLFC` padded with seven blanks. An exact match decrements the immediate operand at $303B. The extra keyboard scan can then reach $3090, which sets the stage transition flag, or $3097, which resets the armour graphic selector and player state.


## The listing's error rate

The independent sample with seed 20261120 drew 75 of 1,804 comments. The checker used `gpt-6.2-sol`. Seven findings held, for an estimated 9.3% error rate, with a 95% Wilson interval from 4.6% to 18.0% and a weighted rate of 9.3%. The seven corrections cover Arthur's hardware sprite pointer, weapon collision extents, the SID cutoff condition, relative-facing logic, the order of actor initialization, the first falling update and a zero-step flight branch. The checker may have missed other errors.
