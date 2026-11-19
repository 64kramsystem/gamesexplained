# Turbo Charge — round 3

File `03-N0S` loads via `$0433` and hands off at `$0801`. The stage prologue installs the pointers $2590 and $26D0 at `$8D32–$8D35`, patches source $27C0 into the road colour lookups, sets the indirect road script pointer to $09F9, and sets the scenery table pointer to $0C91.

This load replaces the music image beginning at `$B000`.
