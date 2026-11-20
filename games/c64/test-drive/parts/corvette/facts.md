# Corvette

The directory names the module `D5`. VICE captured it at `$2E64–$32EC`, with entry `$2E68` and body length `$0485` after its four-byte header. The selection was forced in the car selector before invoking its normal confirmation and loader path.

The Corvette draws bars and decimal digits in sprites. The road speed
update at $2F66 scales $41 and copies rows upward from the bottom of
the source. The engine-speed update at $2F7F scales $42 and masks three
bytes per row. Both paths convert the original value for the digits
and copy seven glyph rows into the third sprite.

In a direct probe from the Corvette snapshot with A equal to 127 and
both selectors equal to one, a read watch on the mask table stopped at
$30AE after the first mask load. Repeating with a watch on the numeric
font stopped at $30F6 after reading the first row of digit one. A
separate probe entering the driving patch routine with X/Y equal to
$29/$31 stopped at $730B after reading the first descriptor address
byte, $2C. These are controlled routine probes. The log is
`work/resume-corvette-watch.log` at the game root.
