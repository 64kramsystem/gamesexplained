# The NeverEnding Story — kit feedback

## Lessons

The CPU-view imported listing omitted an authored font beneath KERNAL and a parked loader beneath I/O. Broad runtime exclusions also hid the resident loader wrapper at $03A0. Fresh snapshots and the hidden-memory ledger exposed all three. Imported operand labels required actual offcut addresses; the shared fix is in kit PR #125.

## Scope and timing

One Part-1 command-prompt state. Later parts remain open under RFC #124. Tier remains Bronze while coverage, verification and the required maintainer check are incomplete. `timings.json` records the original publication and fresh work; its first coverage interval explicitly includes a requested pause, discussion and another game’s work, so it is unsuitable as an active-work benchmark.

## Maintainer asks

Existing discussions #113 (imports) and #124 (multiple states). No new ask or relaxed rule.
