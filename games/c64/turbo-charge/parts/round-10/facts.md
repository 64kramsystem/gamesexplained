# Turbo Charge — round 10

File `0A-N0S` loads via `$0433` and hands off at `$0801`. The stage prologue installs the pointers $3327 and $3467 at `$8D32–$8D35`, patches source $3557 into the road colour lookups, sets the indirect road script pointer to $1677, and sets the scenery table pointer to $1742.

This load preserves the preceding odd round’s music image apart from the one-byte write to `$B7B0`.
