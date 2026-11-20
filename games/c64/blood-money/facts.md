# Blood Money technical facts

## Disk loading and level selection

- The level number at `$0442` is ORed with `$30` at `$C8BF`. Four stores put the result into the filename templates at `$C9BD`, `$C9C3`, `$C9C9` and `$C9CE`. A store checkpoint on the first address and execution checkpoints at the four SETNAM calls fired during the level load.
- The Accept disk's level 4 load reaches the return at `$C9B6` with carry set. The intervening port restore changes A, so the KERNAL error number is unspecified at that stop. The same transition with the Syntax disk reached that return with carry clear and loaded the missing character and sprite data. See the disk identities and route in [orientation.md](orientation.md).
- After loading CHARS, `$C969` copies page `$5B00` to `$6F00`. The clear routine at `$CB40` later reuses `$5B00–$5FFF` for the scroll buffer.

## Graphics and timing

- The gameplay IRQ at `$2034` switches video settings and sets sprite pointers for the bottom panel. The captured level 1 frame shows writes to `$D011` and `$D018` on line 202, and writes to `$43FA–$43FF` on line 203. A non-stopping execution checkpoint at `$2034` fired 14 times across the 15-frame probe, which began partway through a frame.
- The title renderer reads display text as byte values. At `$C4F4`, space selects glyph 0, dollar selects 37, digits select 27–36, and letters select 1–26 by masking with `$1F`. The renderer uses two tile codes from `$1531` for the upper row and two from `$1581` for the lower row. The glyph sheet rendered from the character data at `$4800` is in `work/display-glyphs.png`.
- A load watchpoint in the first level's terrain glyph and staging range stopped after the load at `$DE31`. That instruction reads the scroll staging buffer at `$5B00`, and `$DE34` writes the byte to the first screen matrix. The alternate destination path starts at `$DEB2` for the second matrix.
- The four level parts have their source payloads captured at `$C9B6`. The graphics byte counts and observed consumers are in the part facts. The last 2,048 bytes of each DATA payload are an alternate terrain charset. A load watchpoint at `$B800` during a forced call to the swap routine at `$3A81` stopped just after `$3A9A`. The loop exchanges `$5000–$57FF` with `$B800–$BFFF`. The object command handlers at `$398A` and `$DA8C` call it and set the swap flag at `$0499`.

The banks at `$5A00` and `$5A80` use the same 4-by-4 character-cell mask format as the four banks selected at `$CAA6`. In levels 1, 2 and 4, mapping each set pixel of the inverted `$5800` mask from X to 23 minus X gives the first extra bank exactly. The second is that shape shifted two pixels right. Both banks are empty in level 3. The lookup at `$11E6/$11EA` names only the earlier four banks. A consumer for the extra banks remains open.

## Object scripts

The command stream uses separate dispatch tables for sprites at `$D000` and tile objects at `$38B9`. The same opcode can consume different operands. Sprite opcode 2 reads two signed increments in immediate mode and four target-and-step operands in the other mode. A level 1 load watchpoint stopped just after `$D5C7` as it read opcode 2 at `$8BA9`. The static walk decodes that address as a five-byte command. Local streams reached through the event pointers and decoded branches are annotated in each level listing.

## Projectiles and tile objects

- Holding fire in the level 1 snapshot triggered a load watchpoint at $1241. The CPU stopped at $307E with A=$02, X=28 and the path pointer $1241. The path interpreter at $3065 reads signed X and Y deltas, treats $7F as a jump to another path address and releases the projectile on $80.
- The $A0 projectile tests the terrain solidity bitset at $8024 and takes the contact branch directly on codes $FA–$FF. The contact branch at $2FE1 sets up the 5-by-5 tile effect. A forced invocation of $D332 with the effect's property pointer $1CB2 stopped just after the load at $D3CB from $1CBE. This pointer table begins with $9800 and selects successive 25-byte frames. The first nine images at $9800–$98E0 are identical in the four LEVEL files.
- Tile object property records identify a constant frame or an array of frame pointers. $37B8 advances the animation. An entry with a zero high byte makes $3808 read the following word as a new frame table pointer. The rectangle reader at $3B2C clips the frame and skips zero characters. With the first level's $98E1 frame selected in a controlled probe, a load watchpoint stopped just after $3BB6 as the reader fetched character $01.

## Controls

A stopping load watchpoint on `$DC00` caught `$22BB` reading the port 2 joystick. The next instruction was `$22BE` with A equal to `$E7` while right and fire were held. Both input bits were low in that read. The engine then inverts the byte and tests bit 4 for fire.

## Shops, money and damage

- The engine's shop dispatcher checks the selected cell's stock and compares the high then low packed decimal balance against the price. With cell 1 available and enough money in a controlled probe, a store checkpoint stopped at $276A just after the dispatcher’s handler set the rising-shot upgrade in $0514. The payment loop at $27DE subtracts $10 from the packed decimal balance per pass.
- The engine treats a class 1 contact as a credit of 10, class 2 as 25, and class 4 as a debit of 5 for a nonzero balance. In a controlled overlap starting at $3410 with 30 units, store checkpoints caught the arithmetic writing $40 and $55 at $3297, and $25 at $3283, for the three classes.
- One level 1 enemy property record at $8EC7 supplies a replacement script at $8DE8 and replacement properties at $8F9A. In a controlled run of the resident replacement routine at $D4D1, a store watchpoint stopped after $D106 installed class 1 from that replacement record. The replacement script sends the coin up first and then loops through +5 vertical steps at $8E0D. Its type has the boundary-cull bit set, which the resident update tests at $D473.
- A class 5 overlap calls the engine’s damage progression at $31B9. With its countdown at one and the damage display index at six, a forced call advanced the index, entered the life-loss path and hit the $3204 store of two lives from a starting value of three. The engine also has a separate terrain hull test at $CA26.

## Listing coverage and accuracy

The five parts have an exact match between explained and tracked bytes. The figures and local working files are recorded in [TODO.md](TODO.md).

## The listing's error rate

Sample seed 31749 drew 60 of 2,175 comments. An independent checker on gpt-6.2-sol found seven verified errors in the draw and all seven were corrected. The estimated rate before corrections was 11.7%, with a 95% Wilson interval from 5.8% to 22.2% and a rate weighted by stratum size of 11.9%. The findings concerned sprite hit points and animation reloads, frame limits, the meaning of the tile-object property slot, scroll cursor advance at capacity and the boundary between padding and a mine image. The fixes also update other comments made from the same templates. The checker may have missed other errors.
