# Tower engine

The listing is based on the snapshot immediately before the loader transfers to $0880. The played snapshot preserves the first elevator and the loaded first-tower resource at $A520. The hand-over retains initialization instructions at addresses that are rewritten after startup.

$0AD4 bypasses the saved-game question when $A1D1 is nonzero. $A1D1 is one in this tape's hand-over. $0A4A would otherwise draw messages at $B9C2 and $BA12 and scan the keyboard for Y. The same flag skips the random tower choice at $0A1B. A store watch stopped after $0A1E wrote tower index zero with the shipped flag value. The title and engine use different raster and sound setup. See the watchpoint results in [the game facts](../../facts.md).

A separate load probe used the resident call at $0A0A to request record 315. All 3,120 tape bytes matched at $A520. A store watch at $F400 stopped after $6232 during the backward copy from that buffer. The natural opening checkpoints instead recorded requests 000, 130 and 328.

A targeted run entered $7C26 on the hand-over snapshot. The $EC80 store watch stopped just after $7C2A, and the execution breakpoint at the return showed all 64 bytes set. The first seven matched $7C20–$7C26, including the entry opcode $A2, and the remaining 57 were zero.

With A set to layout zero at $59E2, the $E788 store watch fired just after $5A41. Execution to $5A56 produced all 120 glyph bytes at $E788–$E7FF. They matched the fifteen IDs in the list at $9641, taking eight bytes per ID from $9D54.

## Room drawing and actors

- The room renderer at $4EFD pairs two seven-byte target tables at $4EDA and $4EE1 and patches the JSR at $4F71 before drawing each group of records. Controlled entry at $4F56 with X from zero through six stopped after the store to $4F73 in every case. The targets were $51C4, $5230, $533C, $5402, $54F0, $5646 and $5106.
- The rectangle blitter at $337F reads an origin, dimensions and source pointers from the descriptor in Y:X. Entering it on the elevator snapshot with the descriptor at $8922 and A equal to two fell back to source variant zero. A read watch on $92BE stopped after $33EB loaded tile $0B. That descriptor specifies column 16, row 13, width eight and height two.
- The actor interpreter at $7311 fetches two bytes through actor fields $0C and $0D. It advances the pointer by two, saves the command and operand in fields $0E and $0F, then dispatches through a little-endian handler table. With a seeded actor record, a read watch stopped after $7327 and execution stopped at $7353, $73AB and $748C for commands $01, $05 and $1D respectively. The instructions allow doubled indices below $44, while the contiguous handler table ends at command $1D. Behaviour for indices beyond that table is open.
- The raster targets at $2F6F, $2F74, $2F79 and $2F7E select offsets zero, eight, sixteen and twenty-four for the shared sprite writer at $302D. In a controlled run from the first target, a $D000 store watch stopped after $307E wrote the first value from $A193.
- The zero-filled 40×25 tile-class plane at $82D1 is regenerated during room drawing. The fill at $50DE clears all 1,000 bytes. A controlled $51C4 run with a one-cell strip at column zero, row one stopped after $51F5 wrote $0B at $82F9. A separate controlled run of $5FCB cleared the 300-byte glyph allocation workspace at $9B36–$9C61, stopping at $625F with a sentinel at $9C62 intact.
- Selector value six uses a charge at $88E4 and clears the $8DC5 room display flag. A controlled run beginning at $69C0 stopped on both writes, after $69E2 reduced the charge from two to one and after $6A2C cleared a seeded flag value of one.
- The increment path at $18BF admits movement when the scroll counter plus fifteen is below $9577. With the scroll counter at zero, a limit of $0F reached the exit at $1974. With limit $10, a store watch stopped at $18ED just after the increment at $18EA.
- The room decoder at $2BCA emits three groups of 254 bytes. A controlled run with an all-zero compressed source and the destination seeded to $5A stopped at $2BDB after the last store. All 762 cells at $7FD3–$82CC were zero, and the sentinel at $82CD remained $A5. The loaded resident image has zeros throughout that workspace.
- The agent update at $4A51 consumes pending X and Y deltas at $4D and $4E. With sprite 7 seeded at X $FC and Y $70 and deltas of eight and three, VICE store watchpoints on $D00E and $D00F stopped at $4A61 and $4A70. The updated coordinate pair in RAM was $04/$73. At the execution checkpoint at $4AA0, bit seven of $46 was set and both deltas had been cleared.
- In a controlled entry at $65DF, an execution checkpoint at $65DE caught the early exit when either $A396 was zero or bit zero of $4C was clear. The seeded object countdown stayed at five. With both conditions set, a store watch on record byte three at $80B6 stopped at $6608 after $6606 reduced the countdown from five to four.

## Additional instruction probes

- At $675C, setting $A39D to two and $A397 to three made the routine save $F053 and $D853 as its two plane pointers. A store watch at $A39E stopped after $67A7 and confirmed that the first copied byte came from $F053.
- With the two vertical references equal and $8CC2 clear, entering $72B6 with horizontal differences of −4 and +25 reached the store at $7309 and wrote $0A to $9A3F. Differences of −5 and +26 reached the rejection instruction at $730D with $9A3F unchanged.
- A store watch on the actor workspace stopped after $7A56 wrote the final cell at $7116. All 160 cells from $7077 were cleared and a sentinel at $7117 was intact.
- Execution checkpoints confirmed four targets of the indirect jump at $62A1. With $8CC2 clear and the first command byte at $A1C5 set to $E1, $E2, $F0 and $FF respectively, VICE stopped at $62EE, $62FE, $62E0 and $62B2.
- The controlled record 315 route at $0A0A stopped after the store at $622B wrote $FF40. The 192 bytes from $FF40 through $FFFF then exactly matched the last 192 bytes of the twelve-page copy from $A520. The $0880 snapshot predates this copy. The elevator snapshot still matches the record from $FF40 through $FFBF. The special actor coordinate stores at $3985 and $398B, class stores at $3967 and $3991 and the hardware vector setup reuse addresses above that.

## Melody panel rectangles

The draw routine at $337F takes a ten-byte descriptor in X/Y, with column, row, width and height first, two source pointers next and a colour byte for each mode last. Two read watches in controlled calls from the opening elevator stopped immediately after $33EB read the first source glyph. The call beginning at $0E05 selected $98C5 and wrote $80 at screen address $F35C. The call beginning at $0E13 selected $98C9 and wrote $7B at $F356. Both screen watches stopped at $32FD.

The fixed-address speech code and initial high-RAM graphics copied by $39FB are listed in the [scene resource part](../scene-resource/facts.md). The tracked bytes there are from the moment the copy completed.

## Record 267 copy extent

The title loader requests record 267 at $ACCF into $1000. The call at $ACE7 specifies $24 pages. A checkpoint at $ACEA found all 9,216 copied bytes at $C000–$E3FF, the remaining 144 tape bytes at $3400 and the title bitmap bytes still at $E400–$E48F. The engine hand-over still holds that 144-byte title stretch and its listing is in the title part.

## Bootstrap and sprite band probes

A controlled entry at $02A7 with a one-byte filename hit a store watch on $FFFE after $02E2 wrote $70. The instruction at $02E7 supplies the high byte $03. The original $0370 IRQ had been overwritten by the time of the resident hand-over.

For the fourth-sprite update, controlled entries at $3063 with X zero tested both phase values in $9AF4. The watch stopped at $306B for initial phase zero and at $3074 for initial phase one. The first path calls $30AC using the same X. The second adds four to select the adjacent band record.

A controlled call at $6B61 selected the search panel's lower tile rectangle. A watch caught the first tile read at $33EB from $96C8 and the corresponding screen store at $32FB to $F34B. Both carried tile $0C.

For the search overlay cache, a checkpoint before $67C0 captured the first colour-plane load from the pointer at $0C/$0D with index six. A second checkpoint at $67D1 found that both sets of 35 seeded bytes had been replaced, with the colour byte in its expected slot and the sentinel at $A3E4 intact.

The melody match display at $1435 read its first tile from $99A1, and the map indicator draw at $1F5D read its first tile from $8E30. Both controlled calls stopped after the load at $33EB. The read values were $D9 and $7C respectively.

The elevator backdrop setup builds its row pointer list in RAM. In a controlled entry at $161F with all six selections populated, a watch on $8713 stopped after the final store at $16DA. All 52 bytes at $8710–$8743 had been replaced and the sentinels at $870F and $8744 survived.

The low RAM comparison uses the same VICE build after a hard reset and the resident hand-over snapshot. $02FA–$032F and $0332–$0333 matched the reset baseline byte for byte. The RAM LOAD vector at $0330 instead contained $02A7 at hand-over and $F4A5 after reset. The unchanged ranges are outside the game ledger. The modified LOAD vector remains counted.

The stack-based drawing entries at $24D9, $24FA and $32BF were tested with seeded return and argument bytes. They reached $337F, $3577 and $32DE respectively with the expected register or zero-page arguments. Their callers in normal play remain open.

## Title residue and sprite coordinates

Store watchpoints on the title instrument copier at $1795 confirmed three sixteen-byte transfers in controlled runs. The template at $268D reproduced $033C–$034B and $0354–$0363 byte for byte. The template at $2645 reproduced $036C–$037B. The surrounding $08 bytes lie in the workspace initialized by $1065. The engine also checks $0340 for the resume marker at $0AE1.

The four raster dispatch entries at $2F6F, $2F74, $2F79 and $2F7E reached $302D with X equal to $00, $08, $10 and $18. These are offsets into the alternating sprite bands. In the coordinate setup loop, read watches stopped immediately after $40A3 read $A3EB, $A3E9 and $A3E7 with X equal to four, two and zero. A range watch on $A3ED–$A41F recorded no reads or writes before the loop finished at $40AC. Those 51 bytes are shipped in record 490 and their purpose remains open.

## Rectangle sources and actor slots

- Controlled entries into the room rectangle iterators at $1A60 and $1AD1 stopped after $33EB read their first tile from $927B and $9386 respectively. Their descriptors are $8944 and $894C. Mode two selects source zero and skips the descriptor colour byte. That matters at $8944, where the rectangle's origin shares the bytes reserved for mode-zero and mode-one colours in the preceding descriptor.
- The tower-panel iterator at $249D followed its pointer at $23AC to descriptor $8906 and read tile $01 at $98A0. A separate entry into the second room iterator at $1C48 followed the word at $1C22 to $9B19 and read the first tile at $8F18. Both reads stopped after the blitter instruction at $33EB. Direct calls with descriptor $9C77 read $8DF8 in mode zero and $8DFC in mode one. The normal caller of that descriptor is open.
- At $25DA in the elevator snapshot, the selection index at $11 was zero. Read watches after $25DD and $25E3 returned $5B and $DF from $9751 and $9759. The next instructions store those values in sprite three's X and Y registers.
- With the actor record pointer set to $708B and field $12 set to two, a store watch stopped after $74D1 wrote offset $14 to $A1BD. Starting at $62EE with X equal to one, a read watch then stopped after $62F1 retrieved that offset with Y equal to two.
- With KERNAL ROM visible, the screen editor's initialization at $E544 reached a store watch on $00DD after $E54D. The bytes generated at $00DD–$00F2 matched the resident hand-over snapshot. The initialization writes $FF at $00F3, where the hand-over snapshot has $80.

### Search counters and actor display fields

- Store watchpoints on $238F, $2391, $2393 and $2395 stopped after $66AD, $66A2, $21FC and $669B respectively. These are the increments on the melody-piece, carry-clear search, tower transition and completed-melody paths. The tests start at the increment instructions and check the destinations.
- The actor conversion at $74C7 produced four watched stores from a test actor at $7077. $74E0 wrote the frame pointer to $A196. The next three stores wrote X low $20 to $A193, X high $00 to $A194 and Y $1A to $A195. The input coordinates were X $0148 and Y $B0.
- Read watchpoints at $8E14 and $8E15 stopped after the loads at $1C02 and $1C0C. Those loads supply tiles $C5 and $C6 for the two-column door redraw on row five.
- The eight bytes at $0334–$033B survive from the cassette reader and match bytes at $0939–$0940 in the title state. A controlled execution from $0334 stopped at $0339 on the store to $0335. The title instrument data begins at $033C.
- Read watches at $0FC4 and $0FC5 stopped after $0FDE and $0FF1 returned offsets $14 and $1E for the panel redraws. A read watch on $66B8 stopped after $66CF selected mode three with Y set to two. The five coordinate pairs and trailing zero at $9A93 match the melody-match panel table suffix at $95BD. The five bytes at $4642 match the sprite Y offset table at $A3E7.

The five rectangles selected by the descriptor list at $23A4 have a parallel set of fill tiles. After $20C1 advances the descriptor pointer, $24AB reads ten bytes beyond it and $24AF passes the result to the room cell fill. Read watches stopped after $24AB for $23B0, $23B2, $23B4, $23B6 and $23B8, with values 15, 16, 17, 0 and 0. The unused byte between each tile is zero in the entry snapshot.

A controlled $302D entry with X zero caught the band writer staging per-sprite X and Y coordinates in $5E–$61, the X high-bit mask in $64 and the image pointers in $65–$66. The later stores at $307E–$30A6 send those values to the VIC registers and screen sprite pointer slots.

## Score hand-off and data boundaries

- The resident score call at $2C88 passes the bytes $17 $8C $23 $0F $19. The first byte is the final copy index, the next two identify the source at $238C, and the final pair supplies the scoreboard's resource restore indices. Entering the call with the loaded scoreboard in place stopped at $A67E after the final store to $B360. All 24 copied bytes matched the source. The callback addresses in the block are $37A2 for asset loads, $31DD for the raster change before name entry, and $2C98 for the final transfer.
- Controlled actor encoding from $7D8B with indices 18 and 21 hit the class stores to $82CD and $82D0. In both cases, the two preceding bytes held the column and row. The room's cell grid begins at $82D1.
- A call with descriptor $9578 hit its final matrix tile at $956D after the load at $33EB. The two authored bytes after it, $03 and $04, remain counted. Their consumer is open. A mode-one call with descriptor $9A32 read its final colour at $9A3B after the load at $33A4.
- With X seeded to $40 in the hand-over snapshot, the watch on $9AE6 stopped after $094A read zero. The test establishes what the lookup reads at index $40. Ordinary startup's ability to select that index remains open.
- The melody redraw at $1483 places the left tiles at columns $0C, $10, $14 and $18. At $14A0 the previous CPY leaves carry set, so ADC advances the column by four. A controlled entry at $12EB stopped after $12EF wrote descriptor byte $18 to the colour override at $7FD2.
- Controlled entries at $7833 with bit two set and clear took the two fallback actor-field paths. A store watch on the record's field eight stopped after $7150 wrote $31 from field four and $37 from field five respectively.
- Terminal dispatch at $692F first checks $9761 and then the low coordinate at $8DDF. With the flag set and the coordinate at $0F, a descriptor field-four value of three reached the final sequence call at $6943, while a value of two reached the dissolve at $6949. The coordinate $10 took the standard console path at $6966 with the same flag and value three. A separate execution breakpoint confirmed that $2953 reaches the scoreboard load entry at $2C65. These are controlled branches.
