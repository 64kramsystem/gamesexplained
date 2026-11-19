# Space Harrier handoff

The analysis covers one resident image. The exported kit ledger counts
47,901 of 47,901 bytes explained, including 11,360 bytes of code and
36,541 bytes of data. The rebuilt listing has zero uncounted stretches.
The loader and cross-release evidence for the exclusions is in
`facts.md`. No separate part has its own snapshot or listing.

The listing sample found six wrong details out of 65 before corrections.
The six and the repeated order-pointer wording were corrected. The kit
requires a proven-model check for Silver because the analysis used
gpt-6.2-sol. The listing still needs an audit. The site and its review
remain outside this analysis handoff.

The listing rebuild uses `work/entry.vsf` with `work/active-moot.vsf`
as the comparison snapshot. The ignored work folder retains the media,
snapshots, watchpoint scripts and output, annotation log and sample
verdicts. Step 65 required no recording. The verification establishes
bounded instruction and memory behavior, and the resident image has no
part route.
