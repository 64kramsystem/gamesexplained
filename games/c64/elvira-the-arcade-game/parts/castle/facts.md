# Castle quest

The loader requests G3B and G3A in that order and enters at $0812. The listing uses the capture at that entry. Gameplay uses the IRQ at $13D5 and the raster stage at $147D switches the VIC to the HUD bank.

The header at $4F2C points to character grid $515B. The map pointer at $4F2E holds $685C. The initial viewport draw reads a map ID at $182E, then expands a nonzero ID through the offset tables at $4560 and $461E. The VIC uses the character tiles beginning at $F800 for the playfield.
