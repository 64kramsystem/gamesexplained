# Turbo Charge — round 5

File `05-N0S` loads via `$0433` and hands off at `$0801`. The stage prologue installs the pointers $29E8 and $2B28 at `$8D32–$8D35`, patches source $2C18 into the road colour lookups, sets the indirect road script pointer to $09F9, and sets the scenery table pointer to $0C9F.

This load replaces the music image beginning at `$B000`.
