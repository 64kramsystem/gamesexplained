# Grail temple

The renderer reads 256-byte rows from the map at `$3600` and displays the loaded glyphs from `$2800`. The filename stop at `$B85E` selected `INDIANA5  (EBES)`. The part listing uses the snapshot taken at `$B861`, when the loaded cells are present before stage initialization changes them.


The load leaves `$FF` at `$3000`. Starting at the saved disk return, a write watchpoint stopped just after the store at `$B7FF`, which wrote `$0B` there. A read watchpoint on the same address had zero hits before that store.

The last byte written to the map slot is `$02` at `$7600`, at the start of row 64. Staging the camera at X=0 and Y=512 pixels makes the load at `$8957` fetch it. How far normal play can scroll into that row remains open.

See [orientation.md](../../orientation.md) for the measured write ranges and [the stage screenshot](../../reference/temple.png).

The panel timer selects sprite slots $04 and $05 in VIC bank 3. Starting at $8C27 with timer low bytes zero and one, a store watchpoint at $7C10 stopped after $8C48 with pointer values $05 and $04, respectively. The two slots start at $C100 and $C140. The panel IRQ copies the selected value into the sprite pointer array at $C3F8.
