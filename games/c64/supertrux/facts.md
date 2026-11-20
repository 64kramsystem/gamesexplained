# Supertrux — technical facts

The input is the Elite C64 tape. Static addresses refer to the handoff snapshot `work/entry.vsf`. The PAL VICE measurements and checkpoint logs are in the local work directory.

## Startup and display

- The loader jumps to `$080D`, which jumps to `$1461`. Both execution stops were observed. The game installs its own vectors from `$116C`: NMI at `$0B33`, reset at `$0B5E`, and IRQ at `$0B7F`.
- Startup selects VIC bank `$4000` through CIA 2 at `$1244`. The loop at `$1391` copies 21 pages from `$CBC0–$E0BF` to `$6900–$7DFF`. From the handoff snapshot, store watchpoints at `$6EFF`, `$7008` and `$7BFF` stopped immediately after the store at `$1393`. A load watchpoint at `$7008` stopped after the read at `$1401` and returned the copied value `$44`.
- The transpose writes its first cell at `$6800` through `$1403`. The race matrix clear at `$1172` runs later, from the call at `$12B8`. The title matrix watchpoint at `$5C00` first hit on the initialization store at `$3BF0`. See `work/verify-handoff.log` for the stopped PCs. Tape handoff bytes in these allocations belong to the ledger, including the original character fragments with unresolved attribution in `$7000–$7BFF`.
- The race raster IRQ selects `$A8` in `$D018` at `$0C95` and `$AC` or `$BE` at `$0BE2` to switch the screen/character base pairing. A PAL frame capture shows writes of `$AC` at line 99 and `$A8` at line 259. In 150 frames from the moving-race snapshot, the hardware IRQ entry hit 600 times, the clock updater hit 150 times, and the divider expiry at `$0A89` hit three times. Local evidence is in `work/race-frame.json`.
- The NMI at `$0B33` switches the road stripe color through `$D022`, acknowledges CIA 2 via `$DD0D` and supplies the next timer latch at `$DD04/$DD05`. Both that routine and the raster setup at `$0BC6` index the table at `$E000` using values taken from `$0919`.
- The title map comes from `$CBC0–$DFFF`. The last 4 KB load at `$4000` and relocate under I/O before the game gets control. `$137D` derives color attributes with the palette at `$E071` and transposes the source rows. The title renderer exchanges map and play graphics using `$3CC7`.
- Each four-byte entry starting at `$7C00` supplies width, a height field, and a two-byte offset relative to `$8000`. `$1270` builds the width, rounded height and address arrays used by `$09EC`. Rendering the descriptor-selected bytes resolves the roadside and gantry artwork, including the Shell, Lucas, BMW, Pirelli, Dunlop and Elite signs. These are multi-cell graphics. The VIC sprite slots for trucks, skyline pieces and flags are separate at `$4000`.

## Controls and speed

- At `$0A29` the game makes CIA 1 port A inputs, then reads active-low joystick bits at `$0A2E`. With port 2 Up held, VICE stopped before the read and one instruction advanced the PC to `$0A31` and loaded A with `$FE`.
- Up reaches `$1D1C` once the start sequence passes its wait for Up. The routine adds a value from `$1D11` indexed by speed band and skips the store if the sum is at least `$7E`. An execution checkpoint at `$1D2A` stopped with A at `$01` and speed at `$00`. Single-stepping the store made speed `$01` at `$08E1`.
- Down subtracts the braking value at `$1D2E` and saturates to zero at `$1D39`. Left and right subtract or add the step indexed at `$1B2D`. A bend can add another lateral term using the table at `$1B38`. These paths are traced in the code at `$1B84`.
- The title draws the strings for F1, F3, and fire after calls to `$3AF4`. Its reader consumes bytes until a caret. The keyboard checks in `$1477` use CIA 1 matrix values. F1 sets a new-rally flag and returns to setup. With matrix F3 held, VICE stopped at the store at `$14DC`. One step changed `$08BA` from `$00` to `$01`. The code waits for release and another press before clearing it.

## Routes, clocks and obstacles

- `$2813` uses the speed band to advance a fixed-point distance accumulator. `$2B86` multiplies the current command's first byte by ten. The engine consumes the command once enough distance has accrued. At an execution stop on `$2B11`, the stream pointer at `$0F/$10` held `$E0AC`. A single instruction advanced it to `$E0AE`, leaving the restart pointer at `$E079`.
- The course command data starts at `$E079`. The fork setup at `$28E8` stores two destination words and sign indices. At `$2891`, a truck coordinate below `$50` takes the pointer in `$57/$58`. At or above `$50` it takes the pointer in `$55/$56`. Starting directly at the decision and holding the two destination values fixed, `$4F` selected `$E366` and `$50` selected `$E1CC` in the five instructions from `$28CF`. This tests the branch and pointer stores.
- Opcode 8 writes four display bytes into the stage clock. The route starts with `1:25`. The clock update at `$0A83` counts calls in groups of 50, holds the clocks when flagged, and advances rally time while reducing stage time. The timeout path starts at `$1E0E`.
- An obstacle command selects its formation through `$EEB9`. `$2CA7` schedules its entries into the active object array at `$252B`, and `$1E7B` checks active depth and lateral overlap. The air-horn behavior remains open. The explicit references to the input latch `$08DA` cover movement, restart, the title start and initials entry. The three direct effect calls to `$F3CE` come from start lights or obstacle/rival reactions.

## Text

- The city records at `$1639–$167A` are six-byte PETSCII fields, including the initial blank row. The four message pointers start at `$167B`, with index one addressing the first record from the code's base at `$1679`.
- The HUD writer at `$3851` uses control bytes for attributes and cursor placement. Printable characters are remapped through the pairs at `$F205` before the renderer subtracts `$2C` and, from `$41` upward, a further seven. The pairs give space, period, colon, and slash the stored glyph indices `0, 1, 2, 3`. The rendered face at `$6000` shows digits at `4–13` and letters at `14–39`.
- The high-score records starting at `$F214` have a four-character name, five printed time characters, and four score bytes per entry. `$3D5A` inserts qualifying scores. `$3E9C` handles initials entry.

## Sound

- The title credits Jas. C. Brooke in the inline text at `$3E3A`. `$F410` reads the three voice configurations at `$FA07`, and the pattern interpreter at `$F57E` advances the note stream when its duration expires.
- `$F33D` services music or the engine tone and mixes active effects. `$F637` indexes the SID frequency tables at `$F821/$F875`. Engine tone frequency is written to voice 2 at `$F376/$F37B`. The routine writes filter routing and master volume at `$F3B4/$F3C4`.

- In 50 title frames, `$F33D` ran 50 times, `$F57E` ran 42 times, and the SID register store watchpoint counted 951 writes. In 150 moving-race frames, the engine frequency store at `$F376` ran 150 times.

## The listing's error rate

Seed 20261120 drew 60 of 906 comments from the listing before the handoff-range annotations were added. A separate gpt-6.2-sol checker found four wrong artwork identifications. The estimated error rate is 6.7%, with a 95% Wilson interval of 2.6% to 15.9%. The checker may have missed errors. The four findings were corrected along with the other annotations from the same shape families.
