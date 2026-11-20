# Wellington

M4 loads to $9800–$CFFF. Its entry snapshot matches the file byte for byte. DR restores the shared sprite bank at the end of the sequence.

The round pointer directory at $9D04 selects an initial object list. The map grid begins at $A000, its expanding glyph definitions at $B000 and its character set at $C800. Wellington skips the B file. The old $6000 bytes from Waitomo are outside this part. Its fourth round has a separate overlay.
