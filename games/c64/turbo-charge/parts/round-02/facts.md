# Turbo Charge — round 2

File `02-N0S` loads via `$0433` and hands off at `$0801`. The stage prologue installs the pointers $2FC2 and $3102 at `$8D32–$8D35`, patches source $2EC2 into the road colour lookups, sets the indirect road script pointer to $15E0, and sets the scenery table pointer to $16EA.

This load preserves the preceding odd round’s music image apart from the one-byte write to `$B7B0`.
