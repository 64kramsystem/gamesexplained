# Ending

File `71` is a packed program loaded to $0801. The resident engine saves
two player records and a four-byte third record at $F000 before loading
it. The ending depacker running at $CDFE expands through the byte before
$C000 and jumps to $0810 at $CE48. A breakpoint at $0810 supplied the
listing snapshot. A snapshot 90 frames later shows the congratulations
screen and treasure pile.

$081F–$082B passes the current result index to $0896, XORs the index with
six and passes it again. $0896 reads the status and following byte at
$F004,Y and $F005,Y. Its alternate result path tests for a value of $7F.
The ordinary play fixture exercised the congratulations display. The
conditions that produce $7F in the player record remain open.
