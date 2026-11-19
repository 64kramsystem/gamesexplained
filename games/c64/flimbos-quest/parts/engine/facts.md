# Resident engine

The resident listing uses `work/play.vsf`. It records working code and its stage-one operands. Runtime pointers and immediate values can change with the camera, the actors, the current raster phase and a new load.

The main playfield IRQ begins at `$16AD`, the shop chain begins at `$21A3`, and the lower title IRQ is at `$7CB7`. The resident raster handoff helper is `$791A`. Code at `$215A` loads the next stage and tests for the ending, while `$7992` loads the first stage from the boot path.

The stage parts own the overwritten ranges. Entry snapshots show the loader's output before drawing and gameplay mutate it. The engine owns both playfield screen buffers in `$C000–$C7FF` and the bank-zero panel screen at `$0400`.

Instruction and register evidence for the controls, timing, display and loader appears in the [game facts](../../facts.md).

The actor path at `$44C9` compares the coordinate bytes in `$16` and `$48` by subtraction. With inputs `$40/$60`, instruction stepping reached the overlapping BIT at `$44D2` and the store at `$44D5` wrote opcode `$D0` (BNE) into `$44DD`. With inputs `$60/$40`, the carry branch entered at `$44D3` and the store selected `$F0` (BEQ). The patched branch tests bit zero of `$0396,X`.

The two entries at `$74EA` and `$74F0` share the stores at `$74F4` and `$74F6`. Single-stepping the entries from the play snapshot showed writes of 1 and 10, or 3 and 12, to `$54` and `$02C8` respectively. The panel IRQ selects a sprite frame from `$73A3` using the low two bits of `$54` and sets the sprite colour from `$02C8` at `$1B23`. The natural callers of these entries remain open.

## Screen cells and retained data

Store watchpoints on the room renderer stopped after the writes to `$C000` and `$C2CF`. The low- and high-nibble stores at `$1D05` and `$1D17` emitted tile codes `$7C` and `$DE` at those endpoints. The renderer writes 720 cells, two per packed byte. The other screen page has a 40-byte row stride. The loops at `$109F` and `$1103` draw columns 0 through 38. Store watchpoints caught the writes to `$C4C8` and `$C6CE` after `$10C0` and `$10CC`. The ledger excludes the generated cells. The 16 room colour entries at `$C6E0–$C6EF` match the bytes at `$9760–$976F` in the title snapshot and remain in the ledger.

The actor contact path at `$442E` patches a second branch. Instruction stepping with player and actor X values `$40/$60` and `$60/$40` confirmed that the store at `$443A` writes BNE or BEQ into `$4442` respectively. The branch then tests bit zero of `$0396,X`.

The actor workspace restore maps RAM at $4C2C and copies $D300–$D33F into $0400–$043F. A store watchpoint on $043F stopped at $4C36. The title setup reuses the destination page for screen cells. Its separate copy at $7A6E wrote to $04A0 from the last of 160 bytes starting at $4E60.

The actor progress reset writes zero to two 100-byte arrays at $0600–$0663 and $0664–$06C7. Store watchpoints at the two upper endpoints stopped after the stores at $4BB9 and $4BBC in the same reset loop. The later setup loop at $4C7A preserves bits 3–5 of the first array.

The title transition clears $C300–$C3BF and $C700–$C7BF at $804F and $8052. Its separate save loop copies $0400–$043F into $C780–$C7BF and clears $C380–$C3BF. Watchpoints at both upper endpoints caught each of the four stores. Some saved values in these ranges equal the boot source bytes. The two sets of writes establish multiple uses of these addresses.

Entering the shop top IRQ at $21A3 in the saved play state and stepping through $21AD confirmed a write of $BC to $D018. The corresponding trace of the title lower IRQ at $7CB7 confirmed a write of $1F to $D018 at $7CC9.

## Shop, score and title

At `$26E7`, stepping with A=2 and X=4 reached four stores. They wrote $49, $4A, $4B and $4C at `$2C8D`, `$2C8E`, `$2CB5` and `$2CB6`. These are the upper and lower rows of a two-by-two shop glyph.

The two packed-decimal updates have separate destinations. `$27F9` adds the increment at `$46/$47` to the score at `$02AA–$02A8`. Instruction stepping with score 009999 and increment 0001 reached the high-byte store at `$2818` and produced 010000. `$27CC` applies the increment at `$50/$51` to the shop balance at `$02AD–$02AB` and calls the balance display at `$1185`. Stepping to `$27F5` moved the balance from 009999 to 010000, cleared its two increment bytes and left the score at 001234. The playfield IRQ at `$1A40` alternates between the two updates.

The title high-score code uses 12-byte records. `$83D2` lists their offsets, `$7F72–$7F89` select and change an initial, and `$8155–$8168` convert the score nibbles to display digits.

## Retained ranges

A store watchpoint at `$C6CF` stopped immediately after `$5497`. The patched source and X=$CF gave `$974F` and the copied value was zero. All 18 screen-edge cells from `$C427` at a stride of 40 match the boot source. The generated row fills stop one column earlier.

In the title snapshot, `$74A6–$74E9` matches the 68 bytes at `$7462–$74A5`. The first part duplicates the shop sprite and room tables, while the last six bytes duplicate the setup fields. In play, `$74A2` changes and the corresponding byte at `$74E6` stays zero. The adjacent six bytes at `$74FA–$74FF` hold two zeroes and four values spaced by -8. They sit after the mode routine's RTS and before the depacker. Their consumer remains open.

The two actor award entries at `$1409` and `$140C` set bits zero and one of `$3F` respectively. Stepping the first entry also showed `$3D` set to $FF. The remap entry at `$8778` with base colour $0A returned $06 in mode one, $02 in mode two and $0A in mode three. The isolated mode-zero path wrote zero to six raster instruction and operand bytes.

The targeted trace scripts and results are local to the game's ignored `work/` folder. The main results are in `resident-branches-trace.log`, `retained-edge.log`, `mode-data-watches.log` and `verify-resident-tail.log`.
