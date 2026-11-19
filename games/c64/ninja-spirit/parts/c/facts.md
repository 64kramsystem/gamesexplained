# Disk load C

- `$291B` initialises the narrow map mode with `$277E=$60`. `$3BE9` uses that mode to patch the 19 source operands of the shared screen-copy loop at `$222A`.
- `$2905` selects one of two local round setups. `$28FB` draws the level-6-cleared message and calls the entry for the D loader.
- At handover, `$3D77–$3FFF` matches the earlier B map at `$59F7–$5C7F`. Stage component writes indexed from `$3D65` use indices 0–3. The CPU watches over the copied map tail found zero reads or writes during the local gameplay probe.
