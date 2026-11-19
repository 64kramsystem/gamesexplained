# Turbo Charge — round 7

File `07-N0S` loads via `$0433` and hands off at `$0801`. The stage prologue installs the pointers $264D and $278D at `$8D32–$8D35`, patches source $287D into the road colour lookups, sets the indirect road script pointer to $09F9, and sets the scenery table pointer to $0C86.

This load replaces the music image beginning at `$B000`.
