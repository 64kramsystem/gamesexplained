# Level 1 technical facts

The BLOCKS, CHARS, LEVEL and DATA payloads are compared with the disk at the return from the engine loader at `$C9B6`. The route and snapshot are in [orientation.md](../../orientation.md).

- The first four bytes of LEVEL are the source addresses for the low and high bytes of sprite frame pointers. The engine copies the addresses into the loads at `$DCA3` and `$DCA8`.
- The LEVEL scroll stream at `$8045` uses the low six bits to schedule events against the scroll step. A low field of `$3F` waits for the next strip, and `$3E` stops the stream.
- The terrain table starts at `$EF70`. The engine at `$9ED8` copies a 5-by-5 patch from the table, indexed by the map at `$FBF0`.
- Sprite records in DATA begin with two padding and copy-length bytes. The detailed record headers and known consumers are annotated in the listing.
