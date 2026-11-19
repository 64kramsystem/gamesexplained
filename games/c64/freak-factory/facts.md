# Freak Factory facts

The addresses refer to the DCS hand-over snapshot `work/entry.vsf`. The user-facing states were inspected with PAL x64sc. The laboratory probes enter the resident code after setting the laboratory number, so their screenshots document the five selections separately from the route through the factory.

## Factory

- Confirmed: the factory polls port 2 at $4136. Active-low bits select up, down, left and right in that order. Bit 4 is kept separately at $40D7. Neutral input did not hit either horizontal handler. With left held, $453B counted 269 hits and the X coordinate moved from $7A to $76. With right held, $45CC counted 267 hits and X moved to $7C. These were short timed probes from the same snapshot.
- Confirmed: down plus fire enters the crawl pose. A short probe hit $4444 and reached $4456 after the input divider expired. It set $40DD to $FF and added $15 to sprite 1 Y, from $6B to $80. $439D contains the reverse adjustment when the agent stands up.
- Traced: $4D4C uses the even byte offset at $4D2B to fetch a vector from $4D62. That table contains 25 little-endian room destinations. The increment and decrement entry points advance by two and honour the $FF and $01 boundary values respectively. The five lab numbers are written at $4F11, $501B, $5395, $55DC and $4C08.
- Traced: the sprite contact handler at $599E includes a pickup path for sprite 5. It calls the capped increment routine eight times, clears the pickup flag at $636A plus room and floor, and disables sprite 5. The other path at $59D2 can decrement energy. Background collisions at $5972 are also qualified by position and a set of room flags. Mapping every interval to the visible hazards remains open.
- Confirmed: the gauge uses one full character per eight energy units followed by any partial cell. Starting $6455 with energy 1 stopped a store watch on $40E0 at PC=$64A0. Energy was then 0 and the flag was $FF. The main loop checks the flag before input and dispatches the fall and exit sequence at $5C9F.
- Traced: $608F saves room, floor and player X, then transfers energy through $BFF7 and jumps to $8000. $60AA restores those three values and energy when $BFF0 is set, choosing sprite Y $6B or $CB from the floor.

## Laboratories

- Confirmed: the lab uses resident code at $8000. In each selection 1–5, a targeted probe hit $8000 and $8129 once, counted 6144 passes on the high-memory store at $80A1 and 2048 on $80D7, and hit the lab-number selector at $9F44. The swap windows are $2000–$37FF with $E000–$F7FF and $0800–$0FFF with $F800–$FFFF. The two lower windows matched the upper factory data where checked before the lab's later sprite updates. The 6144- and 2048-byte factory windows also matched the corresponding saved high windows in the first lab byte for byte. $80F1 and $9E0F call both swaps again on exit.
- Traced: $9F44 selects six 64-byte sprite shapes for lab IDs 1–5 from $0880, $0A00, $0B80, $0D00 and $0E80 after the swap. Its copy destination is $31C0–$333F.
- Confirmed: the fight counts changes in the whole CIA port byte at $9B7F. In lab 1, with the change count preloaded to four and energy at $80, holding left with the previous sample also set to left ($7B) reached $9BB4 without a write to $85B6. Starting with the previous sample set to right ($77) produced one energy write to $81. Changing from neutral ($7F) to fire ($6F) also produced one write to $81. The threshold comes from lab number plus four at $9A45. With too few changes, $9BA7 instead decrements a countdown that can drain energy.
- Confirmed: at $9CE3, zero in each of $92F4, $942B, $9556 and $9681 allowed a write of $FF to lab 1's completion flag $BFF1. With the first three clear and $9681 set to 1, the same probe observed no write and the completion byte stayed zero. The whole-game completion check is traced at $9DF1–$9E0C and tests all five completion bytes.
- Traced: $8D79 paces the machine animation. When the secondary counter expires and the routine's gate is clear, its four branches at $8E03, $8E0B, $8E13 and $8E1B restore any inactive assistant's flag. The exact return timing across encounter states remains open.

## Display and sound

| Register or range | Use | Evidence |
| --- | --- | --- |
| $01 | Hide BASIC during the factory setup. Switch out the KERNAL during the laboratory RAM swaps. | $4015–$4019, $8084–$8088, $80B3–$80B7 |
| $D018 | Select screen RAM at $0400 and character data at $3800 in VIC bank 0. | $4024, $8000 and $C01C write $1E |
| $D002–$D005 | Position the two player sprite layers in the factory. | $4378–$4387 and $487B |
| $D015 | Choose enabled sprite slots. | $434A, $595F and $639C |
| $D01E, $D01F | Read latched sprite and sprite-to-background collisions. | $599E and $5972 |
| $D400–$D418 | Initialise SID registers and write per-effect settings. | $40C7 and the IRQ dispatcher at $C01C |
| $DC00 | Sample the controls, including entire-byte comparison in fights. | $4136, $86AE and $9B7F |

The custom character set retains the screen-code letter order for the tested caption. The seven drawn values at $0400 were $85 $8E $85 $92 $87 $99 $20. Reading the glyphs at $3800 gave E, N, E, R, G, Y and a blank. The factory and lab caption sources are at $5D53 and $85B7. The factory builds $3800 from $7800 during startup. The copy is 2048 bytes, with later glyph changes visible in the play snapshot. Unread glyphs are open.

The play snapshot pointed the KERNAL IRQ vector at $C01C. One recorded video frame watched $0314–$0315 and observed zero vector writes. This measurement covers the captured factory state. The IRQ hook chooses between SID effects via the request bytes at $C000–$C018 and chains to $EA31.


The lab snapshot's KERNAL IRQ vector is $8C2A. In a short lab 1 probe, each of $8C59, $8CDD, $8CFC, $8D1B and $8D38 executed 14 times. $8C76 executed 56 times, four calls per frame. The raster handler reuses sprite slots across the four floors and preserves the player's sprite position while loading the other slots from the selected record.

## Listing coverage gaps

The factory and lab use different graphics at the same addresses. The lab copies its per-lab sprites from the swapped $0800 window. There is no separate executable image in the five lab probes. The same resident code handles the selections.

The hand-over includes old copies from the loader. $1000–$17FF is 2038/2048 bytes equal to $C000–$C7FF, $1800–$1FFF is 1977/2048 equal to $C800–$CFFF, and the RAM under I/O at $D000–$DFFF exactly matches $E000–$EFFF. Byte equality establishes the copies. Their complete read and write history remains open. The lab graphics exchange uses $E000, with the KERNAL banked out, at the observed instruction rather than the corresponding I/O addresses.

## The listing's error rate

The independent gpt-6.2-sol sample drew 60 of 115 comments with seed 61924. Four needed a correction, an observed rate of 6.7% with a 95% Wilson interval of 2.6% to 15.9%. The fixes distinguish stored crawl facing from live facing, describe priority dispatch from the factory loop, identify which Y register terminates the death fall, and note the energy cap during fight recharge. The measured listing preceded the later room, sprite and effect annotations.
