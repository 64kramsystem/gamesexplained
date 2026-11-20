# Waitomo Caves

M3 loads to $9800–$CFFF. Its entry snapshot matches the file byte for byte. DR restores the shared sprite bank at the end of the sequence.

The round pointer directory at $9D04 selects an initial object list. The map grid begins at $A000, its expanding glyph definitions at $B000 and its character set at $C800. B3 supplies 576 bytes of boss sprite shapes at $6000–$623F. The boss setup copies these into the VIC bank-3 sprite window.
