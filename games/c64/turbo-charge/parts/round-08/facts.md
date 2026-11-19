# Turbo Charge — round 8

File `08-N0S` loads via `$0433` and hands off at `$0801`. The stage prologue installs the pointers $2C88 and $2DC8 at `$8D32–$8D35`, patches source $2EB8 into the road colour lookups, sets the indirect road script pointer to $159A, and sets the scenery table pointer to $16AE.

This load preserves the preceding odd round’s music image apart from the one-byte write to `$B7B0`.
