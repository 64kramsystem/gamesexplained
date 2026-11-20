# Weapons Room facts

- The dispatch entry at `$28DD` calls the strip clear at `$293F`. With test values in screen memory, the call cleared five cells per row for twelve rows starting at `$40F1` with a forty-byte stride. It returned at `$28E0` for the rest of the clear cascade.
