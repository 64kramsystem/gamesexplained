# Ghouls 'n Ghosts — technical facts

These are findings from the TWT disk release. The disk fingerprint, snapshot routes and loader entry table are in [orientation.md](orientation.md). Instruction stops and watchpoints cited below support the corresponding observations. The formal step 60 listing review depends on completing the step 50 ledger.

## Program layout

| Address | Contents | Evidence |
| --- | --- | --- |
| $0400–$10FF | Arthur pose slots | The page and offset tables at $49DF and $49C1 supply the source for the copy at $4990. $A5 selects the costume or transformation offset. |
| $1700 | Game initialization, then a playfield tile buffer | The boot jump at $8A31 enters this address. $4CB5 replaces the bytes with visible tile indices during play. |
| $2993 | Title/game loop | The entry checkpoint caught this address before interrupts were enabled. It calls the title at $538C and then starts play at $29A0. |
| $86E9–$BFFF | Stage-specific code and tables | All five even loader IDs decode to this exact window. |
| $C000, $C400 | Two screen pages in play | The playfield IRQ chooses between these using the two entries at $5D84. |
| $C800–$E7FF | Stage sprite patterns | A 64-byte-aligned render exposed the sprite frames. VIC pointers use the low two bits of CIA2 port A to select the $C000 bank. |
| $E800, $F000 | Terrain character sets | $5CDD writes the VIC pointer using the charset offsets $0A and $0C at $5D86. |
| $F800–$FFBF | Title and panel glyph load | The decoded font matches boot RAM. The game reuses part of this area for generated sprite shapes. |

## Timing and input

- The hardware IRQ at $5C31 increments $0D and dispatches according to the operand at $5C3B. An execution checkpoint counted four entries in four frames in stage 1. $5F5E waits for $0D to change.
- CIA2 Timer A supplies timed raster splits through the changing NMI vector. The normal play path at $5CA2 configures the timer and $5D88 waits past line $C6 before selecting the panel font. The gameplay update at $29AE waits on $DD, which the NMI handler at $5E80 increments.
- Title input uses CIA1 port A at $5F19. Left selects MUSIC and right selects SOUND FX. A store watch on $1F while holding right stopped at $5F30 with $1F=$FF. Fire is tested at $541B after the IRQ writes the button sample to $D9. The joystick port used for this is port 2.
- During play, $5176 reads and inverts the direction bits and $52BF tests the fire bit. $302A reads the keyboard by selecting a matrix row through $DC00 and sampling $DC01.

## Tiles and actors

- Stage layout rows are 19 entries wide, as shown by the row offsets at $1BCB. Each nonboundary byte is an even offset into the little-endian pointer table at $4CF0. $FF marks a boundary checked at $528B and $52A6.
- Each chunk pointed to by the table contains 20 by 10 tile indices. The copy at $4C76 resolves visible tiles into $1700. Four lookup pages at $BC00–$BFFF expand each index into an upper-left, upper-right, lower-left and lower-right character.
- $4BF8 flips the screen index in $BD and maps terrain character codes through one of the two colour pages at $BA00 and $BB00. The bank chosen by $2EEF also determines the terrain property page and the vertical offset page used by $48CC.
- $30B3 uses fixed six-byte actor records with little-endian tile X and Y, a byte of sub-tile offsets and an actor ID. $3175 scans five-byte optional spawn records and applies a visibility check and a random condition. Stage-section initialization at $2E4D sets both table pointers.
- $29FE checks the outcome at $9C. A negative result other than $FF advances to the next even stage selector. $FF decrements the remaining-life counter at $A4. Stops at $29FE and $5B6A reproduced the four subsequent stage loads using the outcome branch.

## Text and sound

- Rendering eight bytes per glyph starting at $F800 gives digits at $00–$09, uppercase letters at $0A–$23 and lowercase at $24–$3D. $3E is blank and $3F is the full stop. At $40–$49 the image shows exclamation, double exclamation, comma, apostrophe, colon, semicolon, question mark, a line, an arrow and a heart. The high glyph positions include the large title shapes.
- $5F67 takes a script inline after the JSR and returns past the terminator. $5F85 outputs glyphs for nonnegative tokens and dispatches $80–$EF as commands. Tokens $F0–$FF select a colour. The routine at $5FD5 patches the target screen and colour pointers using the row table at $1B84.
- $6150 selects three voice pointers, one for each SID voice, through six seven-entry tables at $730E–$7337. The call at $5405 starts title track zero. The stage descriptor at $2ECB installs the three track-six pointers from the active stage overlay. The voice-one decoder at $6360 selects either a note or a command using the high bit. The note-frequency tables at $6D35 and $6D96 supply the low and high SID registers. Dummy output was used for the emulator session.

## High scores and the name check

$5589 reads ten 20-byte records starting at $5971. The first three bytes carry the packed decimal score and the other 17 hold the player's name. $562B performs ordered insertion. The cursor loop at $57B3 uses the joystick to navigate the glyph grid.

$58ED compares 17 screen cells with `WIGAN RLFC` padded with seven blanks. An exact match decrements the immediate operand at $303B. The extra keyboard scan can then reach $3090, which sets the stage transition flag, or $3097, which resets the armour graphic selector and player state.
