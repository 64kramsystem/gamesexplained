# Turbo Charge — round 4

File `04-N0S` loads via `$0433` and hands off at `$0801`. The stage prologue installs the pointers $2591 and $26D1 at `$8D32–$8D35`, patches source $27C1 into the road colour lookups, sets the indirect road script pointer to $15CB, and sets the scenery table pointer to $16A3.

This load preserves the preceding odd round’s music image apart from the one-byte write to `$B7B0`.
