# Language and title

The first game screen offers English, German and Italian. $1664 holds the four-byte PETSCII filename OPEN, used at the load handoff. $1669 installs the RAM vectors to $16A8 and disables the CIA interrupt sources. The listing uses the snapshot at the language hand-over at $12ED.

The two picture sources start at $1E6F and $466F. The code selects bitmap mode with bank $C000 and matrix $CC00. The four-page matrix and colour copies for the two pictures are at $19A2/$19C0 and $19E4/$1A02. Both pictures use $1A26 for their 31-page bitmap copy. An instruction stop at $1A34 during the first copy showed the source pointer on $1E6F and the destination on $E000.

The character-mode selector initializes around $12ED. The stack in the boot capture at $1669 holds the return address from the call at $1305. After the return, the setup copies a 1024-byte base matrix from $6E6F to $C000 and 2040 glyph bytes from $7257 to $F800. Stops at $18B1 and $1331 confirmed the source and destination pointers and the first byte written by each loop. The glyph copy matches all 2040 bytes at the keyboard polling loop. The stored glyphs overlap the last 24 bytes of the base matrix copy, past its visible cells.

The text renderer reads the script pointer table at $1A8A, including the initial language choices and the localized manual prompts. Each segment selects a row and column. $FE starts another segment and $FF ends the script. At the first store at $1949, X and Y were both eight, A held the first glyph index $08, and the matrix pointer held $C050. The keyboard poll at $138B accepts codes $31 through $33 and $13A0 saves the corresponding zero-based language index.

At the trainer, F7 transfers to the disk-loader setup. A breakpoint at $7D1E and one CPU step confirmed the jump to $12ED. The copy at $7D05–$7D0E installs the loader from $7D80 and the overlapping source at $7D8C into low RAM, then $7D16 and $7D1B set the LOAD vector to $0200.

The image also contains the manual question routines. The stored branch at $13AA jumps to the picture setup. A controlled entry at $13AD with A=$10 selected the record at $7AC8. At $13EC, the value $7D became $30 after XOR with the byte in $2E. In a separate step at language entry, $12F5 read $4D from the visible BASIC ROM at $A006 and $12F8 stored it into $2E.

The loader at $C029 sends 29 blocks of 32 bytes from $C0AD to drive RAM beginning at $0300. At the loop exit $C07B, the traced destination cursor was $06A0 and the source cursor was $C44D. The memory-execute command targets drive address $03A0. A depacker store watch on $C400 stopped at the boot copy at $0120 before the hand-over. The bytes through $C44C belong to the uploaded loader payload.
