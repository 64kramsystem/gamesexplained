# Dragon facts

- The small bitmap clear at `$2BB5` doubles A and saves the result at `$31CE`. Stepping the store at `$2BB6` with A entering the routine at 2 wrote 4. The restore path at `$2BD4` reloads the value for the palette destination lookup.
- The ending instruction at `$21D3` jumped to the resident score path at `$0CD9`. The next instruction called `$12D8`, past the disk-load call at `$0CD3`.
