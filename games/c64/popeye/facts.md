# Popeye — facts

## Release and memory layout

- The companion picture on the selected disk shows the Popeye title and both 1986 copyright lines. The resident PRG reaches the controls menu and then the 25-heart adventure. [Copyright](reference/copyright.png) · [Controls](reference/title.png) · [Olive's house](reference/olives-house.png) · [Lighthouse](reference/lighthouse.png)
- The selected PRG hands control to `$4000`. Gameplay uses `$01 = $30` with both ROMs and I/O out of view. The input poll at `$4DC7` and IRQ at `$4E4F` temporarily use `$35`. CIA2 port A read `$97`, and the VIC memory pointer read `$1D`. In the high-resolution bitmap mode observed in play, the bitmap is at `$2000` and its color cells start at `$0400`.
- The room decoder at `$4FE7` initializes three depth groups at `$6000`, `$6400` and `$6800` from the placement stream at `$C000–$C732`. Each group has four consecutive 256-byte planes for scenery, items, flags and actor occupancy. Each room refers to a four-by-four window through the 16-entry origin table at `$50BD`.
- The room renderer uses RAM beneath the chips at `$D000–$DFFF` as scratch and scenery cache. Instructions such as the indexed store at `$494A` address that RAM while I/O is hidden. In contrast, the matrix read at `$4DDC` addresses the CIA with I/O visible.
- Physical RAM `$FBC0–$FD1F` in both snapshots matches offsets `$0000–$015F` of BASIC ROM 901226-01 byte for byte. Shape table entry `$58` points to `$FBD6` inside this copy. Whether gameplay uses that entry remains open.

## Controls and the first room transition

- The control poll selects each of five matrix rows from `$4DB8 + X`, ANDs the value from CIA1 port B with the mask at `$4DBD + X`, and ORs the selected action bits into `$0940`. It reads the joystick directions on CIA1 port A at `$4DF4`. A nonzero combined mask updates the latch at `$092C`.
- In the measured walk from Olive's house to the lighthouse, the watch on `$0925` recorded two writes. The CPU trace hit `$5835 DEC $0925`, followed by `$583B STA $0925` with A = `$04`. The room index changed from `$05` to `$04`, and an execution checkpoint at `$48F6` recorded one scenery rebuild. Both controls read sites fired during the same capture. The `$FFD5` checkpoint had zero hits on this route. This establishes the observed transition within the resident image. Trace and checkpoint output are in local `work/room-instruction-trace.txt` and `work/room-watch.txt`.

## Counters, inventory and drawing

- The state reset at `$400F` initializes the heart count to `$19`, the inventory count to one, the first slot to `$20`, and the love meter to `$0E`. The count display uses the glyphs at `$9A0E + 8 × index`. Rendering glyph codes `$49–$52` yields the digits zero through nine.
- The pickup routine at `$55B7` checks the item beneath either of two candidate cells. Its ordinary path tests inventory count against eight, clears the item plane byte when accepted and adds the item to the slot array. For item `$10`, the code increments the carried-heart count and decrements the displayed remaining count. These are static findings.
- The main loop at `$407C` increments `$0923` each pass. When it reaches 150, the loop redraws the love meter, clears the prescaler and decrements `$091D`. Reaching zero sets `$0902` to two. This timer counts loop passes. To verify the boundary, an execution stop at `$407C` set the prescaler to 149 and the meter to 14. A stop at `$40BA` found prescaler zero and meter 13. The checkpoints at the redraw call `$40A5` and decrement `$40AD` each hit once. See local `work/verify-meter.txt`.

## Open questions

- Coin and symbol-game interaction, keyed doors beyond the traced conditions, scripted hazards, heart delivery, and the ending need their specific script paths checked. The manual documents their player-visible behavior. [Re-release manual](https://www.lemon64.com/doc/popeye/459)
- Data and possible earlier-phase code in the compilation still need confirmed ownership. See the listing's uncounted ranges and `TODO.md`.

## The listing's error rate

An independent gpt-6.2-sol checker sampled 70 of 403 comments with seed 1986 and found nine errors or material omissions. The raw estimate was 12.9% with a 95% Wilson interval of 6.9%–22.7%. The estimate weighted by stratum size was 11.3%. The checker may have missed other errors. The run corrected all nine findings, including the scenery command dispatch, the descriptor and cell lookup at `$5175`, a spurious reference decoded across RAM vectors, the IRQ banking description and five frame-buffer descriptions. It also corrected other annotations with the same scenery command mix-up. A full audit and fresh sample remain open.
