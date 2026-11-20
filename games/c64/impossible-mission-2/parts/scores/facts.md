# Scoreboard

The engine loads all 4,560 bytes of resource 664 into $A520 before the JSR at $2C88. The entry JMP leads to $B253, which pulls and preserves the return address while establishing its own software and hardware stacks. $A653 reads the inline data after the resident call and uses the resident tape callback for two display assets.

Record 264 supplies the screen codes at $F000. The entry screen rewrites some of those cells. Record 358 supplies 512 bytes of glyph data at $C000, which match the name-entry snapshot exactly. The display labels count pins, objects, music, towers and time remaining. The [scoreboard screenshot](../../reference/scoreboard.png) shows the result of directing VICE into the loading path from the opening elevator.

The tally uses weights 1, 2, 3 and 20 for pins, objects, music and towers respectively. Execution from $A520 to the $ADAE name-entry poll hit the access watch at the fourth weight's high byte $B59B twice. The watch over the following 340 bytes at $B59C–$B6EF did not fire. Both the weights and the suffix remain tracked in the listing.
