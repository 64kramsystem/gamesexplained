# Turbo Charge — round 6

File `06-N0S` loads via `$0433` and hands off at `$0801`. The stage prologue installs the pointers $3887 and $39C7 at `$8D32–$8D35`, patches source $3787 into the road colour lookups, sets the indirect road script pointer to $15BA, and sets the scenery table pointer to $16BB.

This load preserves the preceding odd round’s music image apart from the one-byte write to `$B7B0`.
