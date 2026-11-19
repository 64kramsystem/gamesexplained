# Popeye — facts

## Release and memory layout

- The companion picture on the selected disk shows the Popeye title and both 1986 copyright lines. The resident PRG reaches the controls menu and then the 25-heart adventure. [Copyright](reference/copyright.png) · [Controls](reference/title.png) · [Olive's house](reference/olives-house.png) · [Lighthouse](reference/lighthouse.png)
- The selected PRG hands control to `$4000`. Gameplay uses `$01 = $30` with both ROMs and I/O out of view. The input poll at `$4DC7` and IRQ at `$4E4F` temporarily use `$35`. CIA2 port A read `$97`, and the VIC memory pointer read `$1D`. In the high-resolution bitmap mode observed in play, the bitmap is at `$2000` and its color cells start at `$0400`.
- The room decoder at `$4FE7` initializes three depth groups at `$6000`, `$6400` and `$6800` from the placement stream at `$C000–$C732`. Each group has four consecutive 256-byte planes for scenery, items, flags and actor occupancy. Each room refers to a four-by-four window through the 16-entry origin table at `$50BD`.
- The room renderer uses RAM beneath the chips at `$D000–$DFFF` as scratch and scenery cache. Instructions such as the indexed store at `$494A` address that RAM while I/O is hidden. The matrix read at `$4DDC` addresses the CIA with I/O visible.
- Physical RAM `$FBC0–$FD1F` in both snapshots matches offsets `$0000–$015F` of BASIC ROM 901226-01 byte for byte. Shape table entry `$58` points to `$FBD6` inside this copy. Whether gameplay uses that entry remains open.

## Controls and the first room transition

- The control poll selects each of five matrix rows from `$4DB8 + X`, ANDs the value from CIA1 port B with the mask at `$4DBD + X`, and ORs the selected action bits into `$0940`. It reads the joystick directions on CIA1 port A at `$4DF4`. A nonzero combined mask updates the latch at `$092C`.
- In the measured walk from Olive's house to the lighthouse, the watch on `$0925` recorded two writes. The CPU trace hit `$5835 DEC $0925`, followed by `$583B STA $0925` with A = `$04`. The room index changed from `$05` to `$04`, and an execution checkpoint at `$48F6` recorded one scenery rebuild. Both controls read sites fired during the same capture. The `$FFD5` checkpoint had zero hits on this route. This establishes the observed transition within the resident image. Trace and checkpoint output are in local `work/room-instruction-trace.txt` and `work/room-watch.txt`.

## Counters, inventory and drawing

- The state reset at `$400F` initializes the heart count to `$19`, the inventory count to one, the first slot to `$20`, and the love meter to `$0E`. The count display uses the glyphs at `$9A0E + 8 × index`. Rendering glyph codes `$49–$52` yields the digits zero through nine.
- The pickup routine at `$55B7` checks the item beneath either of two candidate cells. Its ordinary path tests inventory count against eight, clears the item plane byte when accepted and adds the item to the slot array. For item `$10`, the code increments the carried-heart count and decrements the displayed remaining count. These are static findings.
- The main loop at `$407C` increments `$0923` each pass. When it reaches 150, the loop redraws the love meter, clears the prescaler and decrements `$091D`. Reaching zero sets `$0902` to two. This timer counts loop passes. To verify the boundary, an execution stop at `$407C` set the prescaler to 149 and the meter to 14. A stop at `$40BA` found prescaler zero and meter 13. The checkpoints at the redraw call `$40A5` and decrement `$40AD` each hit once. See local `work/verify-meter.txt`.

- When a delivery is already in progress and its animation count reaches zero, the handler at `$466E` adds three to the love meter up to 14, removes one item `$10` from inventory, and decrements the carried-heart count. In an isolated VICE probe, execution checkpoints at `$467F`, `$4687` and `$468A` and store watches at `$091D`, `$091E` and `$0921` fired before the stop at `$468F`. The meter rose from 13 to 14, and inventory and carried hearts fell from two to one. The remaining-heart count stayed at one. See local `work/verify-delivery.txt`.

## Sound and drawing data

- The effect resolver at `$0B39` masks the effect ID to seven bits and resolves its offset relative to `$9000`. In an isolated probe with ID `$06`, load watches at `$900C` and `$900D` each fired once. At `$0B65`, the effective descriptor pointer in `$18/$19` was `$90C6`. The twenty offset words point to descriptors with their own event offset lists. See local `work/effect-boundary.txt`.
- The music scheduler selects among six pattern headers using the split table at `$85C0/$85C6`. Each header has three little-endian offsets relative to its start. The pointer initializer at `$5BE1` converts them to absolute addresses. In an isolated start of pattern 3 at `$957C`, a load watch caught the voice player reading its third stream at `$97CE` before the stop at `$5AC4`. See local `work/music-boundary.txt`.
- The ten entries at `$5110` select the symbol scenery pictures. The drawing streams at `$10AA`, `$10B3`, `$10BC`, `$10C5` and `$10CE` share a drawing substream at `$111D` and jump to separate symbol bodies. The stream at `$120F` uses a two-choice jump list at `$1216`.
- Actor slot five's initial state at `$5A35` names a jump table at `$7C82`. Its five destinations include two patrol sequences, two depth checks, and a random branch at `$7D01`. The branch handler at `$552A` chooses one of four inline indices by masking the random result to two bits.

- An isolated drawing probe read `$113F` twice and `$1140` once. It read `$1141` for the cursor step and again as the next opcode before stopping at the call handler `$43C7`. A second probe read both operands of the position command at `$135F` before the `$FF` at `$1362` dispatched to the return handler. The voice event reader branched on the `$4F` at `$9514` and the `$CF` at `$952E`, leaving their following zero bytes unread in those calls. See local `work/verify-short-gaps.txt`.
- Forcing bank index six and tile index `$E7` at `$4F46` made the cell blitter read two bytes at `$BFFE–$BFFF` and six at `$C000–$C005`. The latter are the start of the room placement stream. Normal gameplay selection of this combination remains open.

## Image ownership

- The startup call at `$4C60` clears the four color-cell pages `$0400–$07FF` and the bitmap at `$2000–$3FFF` before the controls menu. An isolated run of the routine caught writes at both boundaries of each plane and at `$0503`. Both planes were zero at the return instruction. See local `work/display-ownership.txt`.
- The packed `POPEYE 1986` entry on the same disk leaves `$85E0–$8FFF` and `$92F0–$94FF` zero at hand-over. Read watches for both ranges recorded zero hits through the first room draw. Six selected bitmap samples matched the `POPEYE 86` play snapshot, including `$24A8` where the listing initially inferred a copy of bytes from `$8F10`. The original packer's final writes to `$8608` and `$8E05` came from `$0172` and `$0168`. See local `work/compare-cleared-gaps.txt` and `work/loader-stores.txt`.
- The bytes from `$C734` are an earlier layout of scene-handler code. For example, the fragment at `$C764` checks the lower plane, sets bit `$20` in the same cell on a different plane and writes item `$81` before advancing the phase. The resident handler at `$4736` makes the corresponding writes through different addresses. The decompressor writes `$C734` before control reaches `$4000`. Its runtime entry remains open.

- The retained drawing fragment at `$0FF6–$0FFF` matches `$F2E2–$F2EB`. The fragment at `$1070–$107E` has the command sequence seen at `$F35C–$F36A` with a different call target. The six bytes at `$99A5` match part of the sound effect bank at `$90D4`. The eleven at `$99AB` match events from pattern 0 voice 3 at `$9983`. Startup store watches hit the decompressor at `$0172` for all four fragments. See local `work/residual-loader.txt`.

- Three retained unpacked tails use alternating complementary bit patterns. They start immediately after a drawing return (`$1FB1`), a native RTS (`$5FF7`), and the four inline actor-branch operands (`$7D07`). They are present in all four tested boots from the selected disk and in the G-FORCE `POPEYE II` capture. Store watches recorded final writes by the selected boot's literal-copy instruction at `$0172`. The drawing return probe and all four random-branch probes left the respective tails unread. Their original purpose is open.

## Open questions

- Coin and symbol-game interaction, keyed doors beyond the traced conditions, scripted hazards, the trigger for heart delivery, and the ending need their specific script paths checked. The manual documents their player-visible behavior. [Re-release manual](https://www.lemon64.com/doc/popeye/459)

## The listing's error rate

An independent gpt-6.2-sol checker sampled 70 of 403 comments with seed 1986 and found nine errors or material omissions. The raw estimate was 12.9% with a 95% Wilson interval of 6.9%–22.7%. The estimate weighted by stratum size was 11.3%. The checker may have missed other errors. The run corrected all nine findings, including the scenery command dispatch, the descriptor and cell lookup at `$5175`, a spurious reference decoded across RAM vectors, the IRQ banking description and five frame-buffer descriptions. It also corrected other annotations with the same scenery command mix-up. The sample predates the resumed coverage annotations. A full audit and fresh sample remain open.
