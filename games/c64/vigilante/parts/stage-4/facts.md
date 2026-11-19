# Stage 4 — Vigilante

Five named disk files (P, Q, R, S, T) match the memory at the reload exit `$0D98`. The route and snapshot names are in the game's orientation notes.

- `$4000` holds the stage's 256 character patterns.
- `$5400` and `$6700` store the 19 character rows and colour rows respectively, each with stride 256. The engine copies a 40-column window to the running display.
- The panel message at `$7A64` reads: You still have not rescued her. The Skinheads are heading downtown.
- The eight pointers at `$CB00` select animation headers. Each five-byte animation step gives a frame descriptor, signed X/Y displacements and a duration. The trailing bytes and their matches in other disk payloads are identified in the listing.
- The sprite source file loads to `$E000`. Its final whole slots match the KERNAL ROM bytes at those same addresses.
