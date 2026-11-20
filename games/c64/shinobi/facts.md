# Shinobi (C64) facts

## Loader and stage data

- The X-Large loader's handover at `$1904` holds all 47,103 resident PRG bytes at `$0801-$BFFF`. The engine stores 1 as the initial mission number at `$FCC0`. The transition code increments this number at `$B00F`.
- The stage loader writes the mission digit to `$3E45` in the twelve-byte DOS name at `$3E3E`, opens the file on drive 8 and reads through KERNAL CHRIN. It switches the processor port before each store at `$3F60`. A running checkpoint counted 768 stores in about two seconds.
- An execution stop at `$3F22` follows both transfers. Each mission's payload matches `$6400-$68FF` for 1,280 bytes and `$C000-$FEEF` for 16,112 bytes. The routine then closes the channel. Its delay counts 255 visits of raster line `$F8`.
- A controlled instruction run of the placement copy at `$8FE8` reached its return at `$9010` for all four stage indices in each of the five overlay images. The destination matched the 128 bytes at the selected source. The monitored copy made zero reads from `$FD30–$FD4F`. The 32 bytes in that range match the C64 KERNAL RAM vectors at `$0314–$0333` in all five mission PRGs and handover snapshots. The loaded copy’s runtime role remains open.
- A controlled Mission 1 placement scan stopped just after the indexed load at `$8F4D` with X=59 at the end of each of the first two stage scans. The final reads were `$E4DF` and `$E9DF`. Load watchpoints recorded zero reads in the corresponding tails before the scanner's return at `$8FA4`. The scanner initializes its row count to one and reads eight rows when the declared height is nine.
- The Mission 1 bytes at `$E1E0–$E23F` match the playfield glyph bytes at `$D1E1–$D240`. The Mission 2 bytes at `$F146–$F1FF` match the alternate image at `$F246–$F2FF`.
- At the release loader entry `$02A7`, an execution checkpoint at KERNAL LOAD `$FFD5` found the filename pointer `$02E5` and length seven. The bytes at that pointer spell SHINOBI. A separate store watch at `$037F` stopped just after `$3EDA` with X=`$FF`, after the resident loader cleared every byte from `$0280` through `$037F`. The remaining loader bytes at `$0380–$03F7` match the X-Large boot PRG.
- Stage metadata gives separate pointers for tile and attribute grids, widths and heights, initial display parameters, palette and object placement sources. The setup builds separate row-pointer tables at `$0856-$08D5`. Stage placement entries contain a low destination byte, a high destination byte and a value. The resident setup applies the value and stops at the first zero value.
- A load checkpoint over the mission 1 tile dictionary stopped after `$17E5`, the indirect character load in the initial screen renderer. The dictionary entry has 16 character indices arranged as four rows of four. `$17CD` obtains that tile's colour from `$CF00`. `$1856` writes both screen pages and colour RAM.
- The resident program fills `$0600-$06FF` before the gameplay screen overwrites its setup routine at `$4C00`. All 256 resulting bytes match reversal of the four 2-bit pixel pairs in the input byte. Mission 5 uses this table in its sprite mirror routine at `$F836`.

- A controlled execution stop at `$0B7D` in Mission 3, with stage index one, found X=32 after the row pointer builder finished. The last tile-row pointer was `$E860`. The two striped rows starting at `$E880` are beyond that table, followed by the 96-byte loaded block at `$E8C0–$E91F`. A controlled initial draw starting at character row 107 reached `$1855` with zero reads from the block. Its purpose remains open.

## Controls and video

- At Mission 1, execution stopped at the joystick load `$3B84` and advanced one instruction to `$3B87`. The accumulator was `$7F` with no input, `$77` with port 2 right and `$6F` with port 2 fire. The keyboard merge at `$3B8F` can clear seven masks in the same input byte.
- The attract routine at `$98CA` checks the latest input mask in `$0ADC`. Left writes mode 2 and right writes mode 3. Fire branches to the player initialization at `$19B5`.
- The control handler also plays the demonstration from paired control and duration tables at `$3C6E/$3C8F`. Mode 2 fills these tables on input changes. These modes are traced in the handler at `$3BF3`.
- The mode-two recorder advances its byte index without a length check. With the index forced to 63 and 94, store watchpoints stopped after `$3C25` wrote the elapsed duration to `$3CCE` and `$3CED` respectively. The initial purpose of the intervening bytes remains open.
- At Mission 1, the processor port is `$35` and the hardware IRQ vector is `$1E87`. A checkpoint at that instruction hit, and a single step reached `$1E88`. The handler acknowledges VIC status and selects its branch using the index at `$1ED3` and paired tables from `$1ED4`. The return path sets the next raster compare.
- A controlled raster dispatch with X=8 at `$1EAA` patched the jump at `$1EB6` to `$1EE7`. A VIC store watch stopped after `$1EEE` wrote `$10` to `$D016`.
- The Mission 2 stage-index-2 routine at `$8FAF` restores the previously changed glyph byte and draws a new mark from the fine-scroll phase. With the prior offset eight and the fine-scroll phase set to one, watchpoints at `$4648` stopped after the restore of `$FF` and the next write of `$FE`.
- At the masked graphics read `$1E17`, a trace stopped with the RAM bank selected (`$01=$30`), source `$CB00`, destination `$4000` and Y=2. Stepping the load returned `$98`, matching the source byte at `$CB02`. In other paths the wipe selects mission graphics at `$D000` or `$D800`.
- The 8×8 font starts at `$5000`. Glyphs 0–9 are digits. Glyph `$0F` is the two-dot separator, `$20` is blank, and `$21-$3A` give A–Z. Text templates at `$9722-$9860` store ordinary uppercase ASCII with position and zero terminator bytes. The renderer at `$9611` maps these characters to the custom glyph indices and copies the rows to text sprites.

- The eight directions each have a copy routine for both screen pages. The dispatcher at `$1465` selects a target from the split tables at `$1330/$1338` or `$1340/$1348`, depending on `$2E`. Each routine copies 21 rows of 40 bytes with a source displacement of one row, one column or both. The next pass redraws the exposed edges using targets from `$1350-$136F`.
- With direction 1 pending, `$14DC=4` and `$2E=0`, an execution stop at `$3035` confirmed the dispatcher patched `$1483` to `JSR $3030`. Stepping its store copied `$1F` from `$484E` to `$4C27` with X=39.
- The alternate scene font at `$CB00-$CEFF` is identical across the five mission files. With `$ADF7` set, a load watchpoint at the final glyph slot stopped immediately after `$1E17`. The source and destination pointers were `$CEF8` and `$43F8`, with Y=2 and the byte `$1F` in A. The wipe advances by eight bytes per glyph.

- For pending scroll direction zero at phase six, an instruction watchpoint stopped after the store at `$0CE8`. The dispatcher patched its call at `$14BF` to `$0C8D`, which wrote the first bottom-edge cell at `$4F20`. The other table targets draw the top row and the two side columns.
- The text renderer clears `$5400–$553F` before drawing its sprite glyphs. A watchpoint stopped after the final store at `$9620` with X=`$9F` and A=0. The five generated sprite slots start at `$5400`.

- Controlled execution stops at Mission 1’s secondary-scene store at `$FA23` confirmed that directions 0 and 1 select fine-scroll axis zero, while 2 and 3 select axis one. A separate load watch at `$F862` confirmed that the secondary row renderer can read the isolated codes at `$F32F`, `$F34A` and `$F4D5`. A controlled draw starting at image row five and column origin `$10` also read zeros from `$F349` and `$F34B` at the same load instruction. The normal-play trigger for that renderer remains open.

## Player attacks

- The launcher at `$2413` tests the active-low fire bit, the fire latch and the movement gate, then selects a free slot. In a controlled left-facing launch from X `$0180` with `$0AD3` clear, a store watch after `$2476` measured X `$0168` in slot zero, an offset of 24.
- The actor hit test at `$B862` also checks a third slot near the player on an eligible fire press. It places this slot 24 units to the facing side and six pixels above the player before applying actor overlap and hit rules.

## Actor dispatch and mission panel

- The player-contact scan at `$BAF0` runs when the cooldown at `$0C4D` is clear. In a controlled trace with same-plane actor slot zero at the player's half-resolution X and 21 pixels above the player, a watchpoint on `$BB7B` stopped with outcome `$01` and cooldown `$17`. The next instruction calls the separate contact effect handler at `$BBF1`.
- In the patrol routine at `$A480`, forcing direction one with no terrain mask changed the actor's low X byte from zero to `$FE`. A store watchpoint stopped after `$A518`. In the update at `$AAED`, an actor with its contact counter set to seven was retired on update eight. The store watchpoint at `$AB03` observed its Y byte become zero.

- The stage setup call at `$1AB3` gets its target from `$FCFE/$FCFF`. A controlled Mission 1 trace stopped on that call with operand `$0BBC`. The next execution checkpoint hit the resident return at `$0BBC`. The separate alternate-stage hook at `$FCF6/$FCF7` supplies the operand at `$1642/$1643` when the selected stage equals `$FCF5`.

- The resident actor updater takes the type from `$0C07`,X and reads split jump addresses at `$9CD3` and `$9CE2`. A controlled trace starting at `$9D63` with Y=2 reached the execution checkpoint at `$A235` with `$C8`/`$C9` holding `$A235`. Starting at the scanner `$9D22` with an active type-two actor and a clear alternate-update timer also reached `$A235` with X=0 and Y=2. The stage placement initializer uses its own split table at `$9CB5` and `$9CC4`.
- The Mission 1 panel update at `$EE3B` draws an eleven-column window across twelve rows from `$EC00`. Non-space characters go to the front screen. Space characters use the corresponding alternate screen cell. With `$EE20` set to 2, a watchpoint on the write at `$EEA8` stopped with source row `$EC00`, Y=12, A=`$66` and destination `$4908`.
- The resident metatile tables at `$08D6` and `$09C6` give the address `$C000` plus 16 times the tile index for 240 entries. The zero-filled suffix before `$CB00` in each mission occupies addressable dictionary slots. In Mission 5 the ending row directory also points to strings at `$C800–$C8F9` within the dictionary address span.

- The Mission 4 sprite installer at `$F727` copies the six contiguous source slots at `$F980-$FAFF` into `$6440-$65BF` in two loops. A store watchpoint stopped after the final write at `$F735` with X=$7F, and all 384 destination bytes matched the source.

## Alternate stages and ending

- With stage index 2 selected in Mission 1, a store watch stopped just after `$1A92` wrote the high byte of the callback at `$1643`. The completed call operand was `$F163`. A separate execution stop confirmed that the call at `$1641` entered that routine. It updates the panel and two actor slots, then checks player and shot overlap.
- Mission 1 also loads scrolling-scene code from `$F808` into the upper overlay. A controlled call with row and origin zero stopped after the load at `$F862` read `$85` from `$F200`. The source overlaps an instruction in the active Mission 1 stage code. Reachability of this second renderer from play remains open.
- Mission 2's alternate-scene renderer at `$F811` selects from 24 image rows, each holding 64 screen codes at `$F200–$F7FF`. With a controlled row difference of 23, the read watch stopped after `$F86A` loaded the first character of the last row from `$F7C0`.
- Mission 3 seeds 20 moving blocks in four groups of five. Each block is six characters wide and seven rows tall. A watch on the store at `$F723` stopped after the first character, `$18`, reached `$4814` from the base pattern at `$F5EB`. The painter selects one of four patterns using the animation count shifted right twice.
- Mission 4 has two sprite installers. In addition to the load from `$F980`, the alternate-stage initializer at `$F73E` copies six more source slots from `$FB00` to the same live sprites at `$6440–$65BF`. A watch stopped after the last store at `$F77B`, and all 384 destination bytes matched the source.
- Mission 5's alternate sprite installer at `$F80D` copies two pages from `$F440` to `$6440`. A store watch at `$65FF` stopped at PC `$F802` while the bulk copy was still running and the 448 bytes copied to that point matched. The following mirror loop writes six reversed frames from `$65C0`, replacing the last two 64-byte slots of the bulk copy.
- A controlled run of the Mission 2 alternate sprite-pair updater at `$FBFC` moved the active pair from X `$0030` to `$002E`. A store watch at `$4BFD` stopped after writing pointer `$BC` with the animation byte at two.
- In Mission 3, starting the stack mover at `$FA0D` in phase one with base Y `$41` produced base Y `$40`. A watchpoint stopped just after `$FA88` stored `$6A` to the third sprite's Y register.
- The Mission 5 ending setup patches its row-store addresses from the resident row tables. A watch after `$F703` found a zero written to `$4827`. The corresponding colour store at `$F710` wrote one to `$D827`. In a separate controlled run, motion flag two patched the call at `$FB1D` to `$F781` and saved the handler index one in the immediate operand at `$FB21`.
- The Mission 5 ending renderer builds its character source from 40 split pointers at `$F87E/$F8A6` and reads the corresponding start columns from `$F8CE`. Nineteen entries select the ending narrative and blank lines, with 21 entries selecting the C64 credits at `$C800–$C8F9`. In a controlled draw of line zero, a watch stopped after `$FA6E` wrote screen code `$0E` from `$F8F6` to `$4809`.

## Bonus scene

- The raster loop at `$AFB6` indexes ten split phase addresses using `$AEDD` and patches the call at `$AFC5`. In a controlled instruction trace, phase 3 reached `$B113`. Within the target renderer at `$B43A`, target state 4 patched the call at `$B44F` and reached `$B33F`. The two dispatch tables are independent.

## Demonstration input

- Mode one fetches the recorded duration at `$3C4C` and control mask at `$3C52`. A zero mask sets the stage outcome at `$2C` to one. The built-in mask table ends with zero at index `$20`. Controlled load watchpoints with the duration divider clear and the run index forced to `$3F` or `$5E` stopped after `$3C4C` read `$04` from `$3CCE` or `$20` from `$3CED` respectively. Controlled recorder stores at the same indices wrote both addresses through `$3C25`.

## Stage timer

- From the same Mission 1 snapshot, 150 PAL frames produced 150 execution hits at `$261A` and three at the BCD decrement at `$2631`. The seconds and minutes bytes changed from `$57,$02` to `$54,$02`. The subsecond counter at `$2619` returned to `$29`.
- The routine uses decimal subtraction when its 50-call divider expires. Seconds underflow reloads `$59` and borrows one minute. A minute underflow writes the timeout outcome through `$2C/$27` and clamps both BCD bytes to zero. The panel renderer at `$2688` uses glyphs `$14-$1D` for the digits.

## SID effects

- The resident effect starter at `$BD1B` takes an effect ID in A and advances the voice selector modulo three. It clears the selected voice's control byte and writes its frequency and envelope before restoring the control value from `$BCFC`,X. In a controlled run with effect ID 4, a SID store watchpoint at `$BD69` stopped after the write with A=`$11` and Y=0.
- `$BD72` advances a cursor for each of the three voice slots. It reads sixteen high-frequency bytes per effect from `$BC5C` and writes them to the selected voice's frequency-high register. The cursor stops advancing at sixteen.

## Register census

| Registers | Uses traced in the listing |
|---|---|
| `$0001` | `$1907` selects the engine's RAM view. `$3F4B` and `$3F5E` alternate KERNAL-visible and RAM-visible memory during the disk transfer. |
| `$D011-$D012`, `$D019-$D01A` | `$1E48` sets the initial line and enables raster interrupts. `$1E8E` acknowledges the interrupt and `$1ECA` writes the next line. |
| `$D015`, `$D017`, `$D01D` | `$9889` turns off sprites and clears X/Y expansion after waiting on a message. |
| `$D022-$D023` | `$0B05` and `$0B0B` set stage colours from `$FCDD` and `$FCE1`. |
| `$D027-$D02B` | `$989E` sets the colours of the first five sprites while a message is displayed. |
| `$DC00-$DC03` | `$18D7` drives the keyboard matrix and captures input on port B. `$3B84` reads joystick port 2. |
| `$DD00-$DD02` | `$1922` writes VIC bank select for the playfield and captures values used for the serial clock. |
| `$D400-$D418` | The effect starter and updater write frequency, control and envelope registers. The correspondence between individual IDs and game events and the presence of music remain open. |

The full register census, watch output and snapshot-derived glyph and sprite renders are in ignored `work/`. These findings were collected during orientation and annotation. The step 60 listing sample and feature pass are pending. The exact ledger and remaining ranges are recorded in TODO.md.

## Loaded bytes between engine routines

- The resident PRG contains `$00,$01,$60` at `$1571–$1573`, between the scroll register writer and the joystick mask table. A controlled trace stopped after the store to `$27E0` at PC `$1570`, with zero accesses in the three-byte range.
- The nine bytes at `$8D61–$8D69` follow the object scan's return. A controlled recovery trace stopped after the load at `$8DAD` read `$FA` from the neighbouring recoil byte at `$8D6A`. The watch on the nine preceding bytes recorded zero accesses in that trace. The original uses of both ranges remain open.

## Panel indicators and sprite priority

- The panel routine at `$AACB` renders bits one through three of the active player's byte at `$0817,Y` in three cells. Controlled store watches after `$AADF` measured a space in the first cell for input `$11` and code `$0D` for input `$02`.
- The stage setup copies the mask at `$FCF8,Y` into `$1901`. Controlled watches after `$1F5E` showed that a mask of zero clears an incoming priority value of `$5A` at `$D01B`, while `$FF` preserves it.

## The listing's error rate

The independent `gpt-6.2-sol` sample drew 60 of 1,458 comments with seed 1729. It found nine errors in detail, an estimated 15.0% (95% Wilson interval 8.1% to 26.1%). The checker may have missed errors, and two sampled claims could not be verified. All nine findings were corrected. They concerned the participant countdown, the outcome and display fields cleared at stage exit, the sprite crop baseline, the actor flag threshold, the visible panel bits, the alternate actor update guard, two secondary-scene screen-code ranges, and the sprite priority mask. A full listing audit is recommended.
