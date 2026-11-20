# Road stage 5

The side B loader selects `R5` when `$52` is 4. A controlled stop at `$6A2C` after the call at `$6A29` captured the relocated module at `$3600–$3CAE`. Its disk entry word is `$2004` and the in-memory entry word is `$3604`. Its length field is `$06AB` bytes, following the four-byte header.

The entry at `$3604` sets the three driving pointers. `$4E–$4F` points to the stage sequence at `$3B5E`, `$50–$51` points to the element pairs at `$362D`, and `$6B–$6C` points to the substream offsets at `$36EB`. The controlled capture stopped again at `$6A37` after initialization.

The readers at `$7845`, `$9004` and `$915B` support direct elements and high-bit references within the sequence. The latter take a word offset from `$36EB` and add that same base. A high-bit byte in the resulting substream ends that substream and advances the enclosing cursor. The main reader's comparison at `$905A` checks for the stage terminator `$FF`.
