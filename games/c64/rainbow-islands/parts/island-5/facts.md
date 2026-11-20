# Island 5

This load replaces the island windows beneath the resident engine.
The file ending in 1 is retained at $1B00. The file ending in 2 is
captured at $9800 at the breakpoint on $7EEA. The listing uses
the entry snapshot so the compressed map and graphics storage are
available before the round setup reuses the staging area.

The first file uses the resident object script interpreter and
packed map reader. The second file supplies 192 character images,
a page of attributes, a sprite byte dictionary and the source
pictures for the island's sprite slots. See the named tables in
the symbol map for the locations and the resident routines that
consume them.
