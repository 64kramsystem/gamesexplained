# Rygar analysis history

The first two apparent entry stops led to release intros. Checkpoints at `$C350`, `$0F00`, `$00AF`, `$0812` and `$0915` separated the depackers and intro programs from the expanded game. The title and play snapshots use the game after the last of these stops.

The first execute-map dump after a raster frame capture lost the emulator connection. Starting the same headless build through the kit, loading the round snapshot and using a short input window yielded the recorded instruction ranges. Matrix input worked on the installed headless build despite the host-key probe failure.

The secondary terrain and metatile fragments were retained in the ledger. A capture from the Triton image with both trainer switches off matched those fragments, apart from four stored sprite pointers in the screen tail. The comparison also distinguished the generated glyph buffer and sprite tables in the selected image from source graphics.
