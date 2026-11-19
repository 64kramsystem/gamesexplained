# Facts

Addresses refer to the DDT disk build. The cell snapshot and scripts under `work/` provide the reproducible local evidence. Observations with VICE's dummy device establish CPU and register behavior. Audible output was outside these checks.

## Controls and movement

- **Confirmed at the input store and movement instruction.** With P held, a stopping watchpoint on $23 stopped at PC $228A after the keyboard scan stored $00. Released, the same store wrote $02. A breakpoint at $1F6E followed by one instruction incremented $1DC3 from 96 to 97. $217A–$2220 and the sprite upload use doubled horizontal pixels.
- **Confirmed at the thrust instruction.** With Q held, $1F80 decremented $1DC2 from 121 to 120 in one instruction. The next instruction decrements it again. The thrust and fall paths both test tile attributes before changing position.
- **Traced.** $2263 keeps the previous select and fire samples in $28 and $27. It dispatches to joystick port 2 at $2246 when $1B is nonzero, otherwise reads configured keyboard rows and masks. The input latches are active low. $7C5F tests both the old and new select samples to begin an equipment change.
- **Confirmed at the weapon dispatch.** With Space held, the patched jump at $6BF3 selected $76B1 from the rifle record. A stopping watch on $6BD7 caught the increment to one at PC $76BF. The handler caps the count at $1F and compares it to $0A and $14 on release. The successful projectile allocation path at $7729 decrements the stock.
- **Traced.** $74E4 initializes fuel to 80 decimal and $750C charges one fuel unit per $20 eligible iterations while up is held. Fuel exhaustion reaches $6AAE after another interval. Damage is gated by $1F0A and updates a separate counter and panel drawing path. The rest of the loss and restart sequence remains open.

## Raster and hardware

| Register | Traced use |
|---|---|
| $D000–$D010, $D027–$D02E | Sprite position, X high bits and colours. $2407–$2429 uploads slots 1–7 and $23D2–$23F0 handles slot 0 on the sync path. |
| $D011, $D016, $D018 | $26CF sets playfield scroll, screen and charset. $25C8 changes the playfield charset. $236D switches to the lower bitmap display. |
| $D012, $D019 | IRQ timing and acknowledgment, including $271D and $270A. |
| $D020–$D023 | Border and playfield colours. $2703 writes the playfield background override and $6205 sets the multicolour backgrounds. |
| $D400–$D406, $D416–$D418 | The banked BASIC RAM code around $AC64–$AF08 accesses SID controls, frequency, envelope and filter. Voice accesses include indexed stores. |
| $DC00, $DC01 | Joystick port 2 sample at $2246, keyboard row selects and column reads at $2274–$22A7 and $22B3–$22BA. |
| $DD00 | VIC bank selection supplies the bank beginning at $C000 during the opening frame. The IRQs at $22F5 and $23C3 also test bit 2 and branch to $31E3 when it is clear. |
| $FFFE–$FFFF | Hardware IRQ vector in RAM. The captured raster frame records next-handler updates to $236D at lines 151, $26CF at lines 230 and $25C8 at lines 257–258. |

In the captured opening frame $D018 was written $28 in the playfield, $C8 during the lower display transition, and $20 for the next playfield phase. $D011 became $3F with the $C8 write. The store watch independently identified the handler chain. Evidence is in `work/cell-frame.json` and the trace script `work/verify.py`.

## Resident data and text

- **Traced.** $3FA6 indexes the room configuration and builds the working room tables. $40FD decodes the map to $A600 with a $40-byte row stride used by collision and rendering. In the stream, $F8 followed by a count emits zeroes, $F9 followed by count and tile emits a repeated tile, and $FF ends the stream.
- **Traced.** The title text and terminal stream have uppercase PETSCII letters ($41–$5A) and $40 spacing. Gameplay's screen-code renderer subtracts $40 at $3074. The title renderer at $30A5 uses two vertically stacked tiles, starting at `(2 × byte + 6) & $FF`; the second tile is consecutive. The C000 title snapshot glyph rows for $88/$89, $8A/$8B, $8C/$8D and $8E/$8F render A through D. M and W add a column with source codes $5B and $5C.
- **Traced.** The stream reader at $2F70 treats $DF as absolute row and column, $DA as relative column and row, $DB as a nested stream pointer, $DC/$DD as loop start and repeat, and $D9 as a colour change. $65E6 is the terminal menu stream, passed by $63C5–$63C9. The panel bitmap uses 16-byte glyph records at $4A14 and separate nibble-aligned drawing paths.
- **Open.** Full room and object formats, teleport and ending logic, and the source and consumers of all RAM hidden under I/O remain unmapped.
