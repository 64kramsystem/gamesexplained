# Turbo Charge — round 9

File `09-N0S` loads via `$0433` and hands off at `$0801`. The stage prologue installs the pointers $2656 and $2796 at `$8D32–$8D35`, patches source $2886 into the road colour lookups, sets the indirect road script pointer to $09F9, and sets the scenery table pointer to $0C93.

This load replaces the music image beginning at `$B000`.
