# Flimbo's Quest analysis history

The numbered stage files first booted via a direct call to the loader. The resulting hand-over snapshots were suitable for data analysis, but resuming that route omitted the preceding transition state. A direct jump to stage initialisation showed stages 2–6 and left stage 7 garbled. The capture route now enters the shop under a debugger flag and invokes the resident completion transition with its IRQ chain installed. That route reaches the re-entry point at $14A1 and renders stage 7 cleanly.

The macro-expanded map code initially left several auto-labelled address spans that cut short the coverage of known display data. Stage tables are typed and commented by field or row. Untyped and unexplained bytes remain visible in the ledger.
