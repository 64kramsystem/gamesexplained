# Loaded stage slot

The loader reaches `$8000` after unpacking this stage into `$0B00–$4FFF`. The entry snapshot preserves the loaded values before the engine draws into the screen buffers. The four tile-quadrant tables are at `$0B00–$0EFF`. The renderer uses a tile map stride of 96 bytes and a character set at `$4800`. See the [game orientation](../../orientation.md) for the selection and store-watchpoint evidence.
