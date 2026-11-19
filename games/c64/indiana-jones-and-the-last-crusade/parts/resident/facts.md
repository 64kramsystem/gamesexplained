# Resident engine

The bootstrap reaches `$7D5C`. The resident code handles both the title and play. During play its two raster handlers alternate at `$809C` and `$81CF` and the serial load path at `$B80F` replaces the map and field charset for the requested stage.

See [facts.md](../../facts.md) for the instruction stops, writes and bank values.
