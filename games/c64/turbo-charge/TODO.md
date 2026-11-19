# Turbo Charge — analysis handoff

The exported kit ledger explains **604,457 of 604,457 bytes**
across 24 parts. Each part meets its exact tracked count and the
rebuilt listings have zero uncounted stretches. The media ledger
answers the 29 distinct disk items.

- The independent listing sample found 9 wrong comments out of 95.
  The sampled findings and matching comments were corrected. A full
  listing audit is recommended. A proven-model listing check remains
  required for Silver. See the error-rate section in [facts.md](facts.md).
- The local analysis scope stops after verification. Its checks
  isolated code paths with debugger checkpoints and did not require a
  replayable input route. The existing capture routes are documented
  in [orientation.md](orientation.md).
- The next tier also needs the minisite, reader review and retrospective.
  Score persistence through a disk write remains an open observation.

Use `work/entry.vsf` inside each part to rebuild its listing. For
`round-01`, supply that snapshot as the listing image and also pass
`--entry work/play.vsf` with the part's full work path. This compares
against the live image while keeping the start-up code in the listing.
