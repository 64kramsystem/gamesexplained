# Turbo Charge — round 1 and shared driving engine

The first driving load provides both the stage script and the shared
engine. The debugger hand-over at `$0801` retains the setup routines
at `$AC00`, which the road colour buffer replaces in play. The root
[facts](../../facts.md) record the measured input and raster branches.

The four alternate sprite banks begin at `$3B00`, `$4800`, `$5500`
and `$5F00`. The exchange helper at `$9B76` routes the first two
into 13 pages at `$C000` and the other two into 10 pages at `$E200`.
The displaced bytes move back into the source banks. The script's
surface-change routine at `$1A03` exchanges the active road character
tail and the associated lookup addresses.

The script sets its scenery type via the records passed by `$7A33`.
`$8ECC` reads width, height and glyph pointer from the type's
depth record. The screen-row loop at `$9100` renders the glyph
bytes and skips writes when the byte is zero.
