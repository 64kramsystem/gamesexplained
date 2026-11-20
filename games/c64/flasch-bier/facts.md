# Flasch Bier facts

## Machine and boot

The tape's one 23,424-byte payload loads at $0801–$6380. Every payload byte matches the RAM in `work/entry.vsf`. The BASIC line at $0801 runs SYS 2112. $0840 installs $084A as the NMI entry, clears the SID gates, sets up the KERNAL screen editor and jumps to the title with IRQs masked.

The title copies $5B14–$5F13 into screen RAM at $0400–$07FF. $5800 enables sprites 0–6 and assigns the four logo parts to sprites 0–3. The last three sprites share a position and change pointers at $5A8B and $5A9D to animate the figure. Before the first switch, their pointers $B5–$B7 read from $2D40–$2DFF, in the second cave's source page. CIA2 port A read $97 during the cave probe, selecting VIC bank 0. $5AB4 reads port 2 fire, and $5AFC clears the SID and disables sprites before the game starts.

## Cave storage and display

| Address | Use |
|---|---|
| $02, $0340–$0370 | IRQ sound divider, score, lives, timer, music indices and working state |
| $0400–$07E7 | Generated screen cells. Bottom row holds the cave number, score, lives and time. |
| $0900–$09FF | Rock and enemy cell lists, each terminated with $FF |
| $0A00–$0AFF | Mutable copy of the selected cave page |
| $0B00–$0BFF | Rock falling flags and enemy headings, indexed by actor slot |
| $0C00–$0DFF | Two 256-entry title pitch tables |
| $1800–$1FFF | Custom character set selected by writes of $1B to $D018 |
| $2C00–$57FF | 44 contiguous cave pages in the one loaded image |
| $6000–$6065, $6080–$60E5 | Gameplay voice 3 pitch sequence |

$2553 copies 256 bytes from the pointer at $AB/$AC into $0A00. $2000 renders the first 240 as 20 columns by 12 rows. Each byte supplies the first of four consecutive screen codes for a two-by-two tile. $24FF scans the same 240 bytes, first for rock class $08 and then for enemy class $04 under mask $3F. The first $00 class supplies Werner's cell. The last 16 bytes travel with each cave page and sit beyond these loop bounds. The source page advances by one on completion and wraps from $57 to $2C via $25A0/$2794. The wrap reduces the delay operand at $2326 from $31 to $21, then $11, then $01, where it stays. A reference search found no reads, writes or calls naming or indexing $FFD5 in the traced program, and the cave loader reads its pages through $AB/$AC.

$5F14 and $2727 draw decimal digits from custom screen code $22. $5F59 lays out score and lives with KERNAL CHROUT and BASIC ROM $BDCD, then subtracts $0E from non-space codes in the HUD field. $2614 selects the default character ROM for the score interlude. The title and cave select the custom set again through writes at $5815, $2596 and $2698.

## Movement, collisions and scoring

$2132 reads active-low direction bits in the order up, down, left, right. The candidate offsets are −20, +20, −1 and +1. A cell matching $10 under mask $38 accepts movement, leaving tile $10 behind Werner. A candidate with its low six bits equal to $18 goes to $2602 instead. $2712 adds the time remaining to the two-byte score and reloads the timer to 100.

A rock falls through a cell whose low six bits equal $10. $22DE records which rocks moved down on the previous pass. A falling rock over Werner branches to $2308 via $229E. If it cannot drop and is supported by class $08 under mask $38, $2098 tries to roll right then left. Both the neighbouring cell and the cell diagonally below must pass the $10 space test under mask $3F.

$2420 uses the enemy’s last successful direction to order the four neighbour probes. For up the order is up, right, left, down. For down it is down, left, right, up. For left it is left, up, down, right. For right it is right, down, up, left. A direction probe can move into $10 or kill on $00, with the low six bits tested in either case.

$26F1 sets the life counter to ten and score to zero. $2308 draws the death tile $1C, then waits for CIA1 port A to equal $6F before losing a life at $26EB. The main loop also goes to $26EB on the same fire pattern or on zero time. On the score screen, nonzero lives go through the cave reload. With zero lives, $269E prints GAME OVER and $26E1 polls for space before returning to the title.

## Timing and sound

The gameplay IRQ vector is $2727. Its timer divider compares with 60. At that value the handler zeroes the divider, decrements time at $2739, uses repeated subtraction to write the two displayed digits and restores the full time byte. The handler chains through $6100 to KERNAL $EA31. The time unit is one decrement per 60 IRQ entries.

The title alternates two voice 2 pitches while moving sprites and reads the split melody at $0C00/$0D00 for voice 1. At indices divisible by 16 it also writes the pitch to voice 3. $6100 divides the gameplay IRQ count by nine, retriggers voice 2 noise on the third step of a six-step cycle and indexes the 102-step voice 3 sequence. A zero high byte skips the pitch and gate writes. Direction movement uses voice 2 noise and falling or rolling rocks retrigger voice 1 noise. These are SID register traces and code readings. VICE used dummy audio.

## Loaded bytes and coverage

The source listing uses the SYS-entry snapshot and compares it with `work/play-round1.vsf`. Listed payload bytes cover $0801–$6200. The excluded tail $6201–$6380 is a linked BASIC directory image headed TEST DISK, including the BLOCKS FREE line and trailing bytes. Outside the load, $FD30–$FD4F matches the KERNAL ROM vector-default table byte for byte. $07C0–$07E7 is the generated bottom screen row and was all spaces at SYS entry.

The listing retains the graphics-like fragments at $27E0–$2BFF, the unselected glyph bank at $1000–$17FF and detached BASIC remnants at $6174–$6200. Their original purpose remains open. CPU-access checkpoints observed zero accesses to those spans across the SYS-entry to first-cave probe in `work/classify.py`. The same probe saw 512 accesses to the first cave source page and 458 accesses to the IRQ vector. The VIC reads graphics separately from the CPU. The observed $D018 writers select the custom character bank at $1800 or the character ROM, and the title sprite addresses follow the pointers set by the game.

## Live tests

- At SYS entry the checkpoint stopped on $0840. The boot passed from title fire through the score/lives interlude to a drawn first cave. The cave snapshot had IRQ vector $2727, NMI vector $084A and PC $2030 writing a screen tile.
- `work/trace.py` recorded a store at $2739 to $0344 and indexed map reads through $200A. In `work/verify_live.py`, stepping exactly one instruction from $2739 changed the timer from 96 to 95 and stopped at $273C.
- Targeted movement fixtures stopped on $2132 and set one adjacent cell. An up press into dirt $14 moved Werner from 181 to 161 by $2174. An up press into $98 reached $2602, added the 95 remaining ticks, advanced from page $2C to $2D and copied all 256 source bytes before $255D. These results establish the branch behavior for the supplied cells.
- With a rock in slot 0 at cell 65 and the right-side pair clear, the $2098 probe stopped at $20EB with slot 0 pointing to 86 and the old cell set to $10. Separate contact fixtures reached $2308 from $229E and $23E3.
- At the gameplay pitch instruction $6146, X was 66. One instruction step loaded the zero high byte stored at $6080 + 66, a rest in the sequence.

## The listing's error rate

An independent `gpt-6.2-sol` sample drew 60 of 173 comments with seed 1985. Seven comments had incorrect details before correction (11.7 percent, 95 percent Wilson interval 5.8–22.2 percent). All seven findings were fixed. The fixes make explicit the title pitch sequence indices and load sites, rock roll offsets, movement and contact masks, the minimum delay after cave wraparound and the identification of detached BASIC tokens. A full audit can measure the accuracy of the remaining comments.
