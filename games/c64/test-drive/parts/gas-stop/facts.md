# Gas stop

The directory names the module `GS`. VICE captured it at `$B567–$BFFF`, with entry `$B56B` and body length `$0A95` after its four-byte header. The recorded entry was reached by stepping the indirect jump at $1AD8 while exercising the driving engine’s own module call. The caller state was set up from the first road stage.

The result module first shifts time and accumulated speed together until the high time byte clears. Its loop at `$B580` divides the remaining accumulated speed by the byte of time using repeated subtraction. The quotient is stored at `$BFCC`.

The points path uses two words selected by stage, from `$BFE8` and `$BFF2`. The first is subtracted from `$68 + 60 × $69` with a floor of zero. The second enters a repeated subtraction loop that increments the award by four at `$B63C`. The final loop bounds and the meaning of the low-denominator adjustment remain open.

The initial result text has replaceable fields for average speed, elapsed time and points. The module then chooses a comment from the groups that follow, whose text covers speed, shifting and road hazards. The encoded letters are $01–$1A, words are separated by $20, and the script uses $00 to end a line and $FF between groups. The renderer at $B912 stages each line in a 40-byte buffer before drawing it.
