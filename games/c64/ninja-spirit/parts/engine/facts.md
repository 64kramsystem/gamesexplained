# Shared engine

- The IRQ entry at `$2405` saves the CPU registers before tail-jumping through the pointer at `$12`. The watch on that pointer identified the playfield and HUD handoffs.
- The code at `$2126` loads three sets of callbacks for the selected weapon. The active selector is even, from 0 through 6, so each fetch can take a low and high byte at consecutive addresses.
- Sprite positions and pointers are copied by `$1304` after the game has updated its objects. The IRQ consumes the copied arrays and uses the slot order from `$2363`.
- The common serial loader at `$BCA7` invokes the backward decoder at `$BB00`. The order, note-pattern and instrument tables beginning at `$AAA0` support the music procedure called by the HUD split.

See the [game facts](../../facts.md) for the memory map, alphabet and trace evidence.
