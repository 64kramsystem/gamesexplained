# High scores

The directory names the module `HS`. VICE captured it at `$E800–$ECA6`, with entry `$E804` and body length `$04A3` after its four-byte header. The recorded entry was reached by stepping the indirect jump at $1AD8 while exercising the driving engine’s own module call. The caller state was set up from the first road stage.

## Scoreboard alphabet

The bitmap font begins at `$EB4E`. The drawing routine at `$EAB9` multiplies its glyph index by eight and copies eight rows to bitmap memory. Rendering each group of eight bytes as four multicolour pixels per row gives the following order.

| Indices | Glyphs |
|---|---|
| `$00` | Blank |
| `$01–$1A` | A through Z |
| `$1B–$24` | 0 through 9 |
| `$25` | Filled block |
| `$26` | Horizontal line |

The decimal conversion at `$E88E` adds `$1B` to each digit. This establishes that the score text uses the module's private alphabet. The disk file named CSET had no distinctive eight-byte match with the title, selector or road snapshot; that result does not identify its role.
