# Resident engine — Vigilante

The game-level [facts](../../facts.md) describe the engine and its evidence. This part owns the decoded COD1 payload, load dispatch and host transfer code, panel, shared sprite library, resident routines and music data.

The main dispatch from `$0E0F` tests a series of enable bytes beginning at `$0D59`. The VIC uses the screen matrix at `$5000` and switches character bases during its two raster interrupts. The common actor animator at `$1371` advances a five-byte step stream and writes intermediate records, then `$25D9` synchronizes with raster line `$E1` to publish those records to the VIC.

Stage overlay exits go through `$0D98`. `$3BD7` converts each remaining timer unit to 30 points and advances the level. After the final stage, the transition dispatch shows the record at `$3D46` and reloads the first stage files.
