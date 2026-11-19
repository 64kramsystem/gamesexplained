# Catacombs

The renderer reads 150-byte rows from the map at `$3600` and displays the loaded glyphs from `$2800`. The filename stop at `$B85E` selected `INDIANA3  (EBES)`. The part listing uses the snapshot taken at `$B861`, when the loaded cells are present before stage initialization changes them. The purpose of the loaded bytes after the last whole map row is open.

See [orientation.md](../../orientation.md) for the measured write ranges and [the stage screenshot](../../reference/catacombs.png).
