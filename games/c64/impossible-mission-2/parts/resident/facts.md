# Tower engine

The listing is based on the snapshot immediately before the loader transfers to $0880. The played snapshot preserves the first elevator and the loaded first-tower resource at $A520. The hand-over retains initialization instructions at addresses that are rewritten after startup.

$0AD4 bypasses the saved-game question when $A1D1 is nonzero. $A1D1 is one in this tape's hand-over. $0A4A would otherwise draw messages at $B9C2 and $BA12 and scan the keyboard for Y. The title and engine use different raster and sound setup. See the watchpoint results in [the game facts](../../facts.md).

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
