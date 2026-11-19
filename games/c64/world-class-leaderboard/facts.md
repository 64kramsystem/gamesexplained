# World Class Leaderboard technical facts

The Nostalgia disk set loads a resident golf engine and can replace the golfer sprite work area with a scorecard printer. The active C64 banking configuration determines whether the CPU addresses print module source RAM or chip registers.

| Part | Evidence | Analysis |
|---|---|---|
| Golf engine | Course prompt and Cypress Creek first tee snapshots share the engine entry, IRQ setup, projection code and packed sprite source. | [Engine facts](parts/engine/facts.md), [symbols](parts/engine/symbols.json), [listing](parts/engine/listing.json) |
| Scorecard printer | A load of PRNT reached $6800 with the six pages at $6800–$6DFF replaced. | [Printer facts](parts/print-scorecard/facts.md), [symbols](parts/print-scorecard/symbols.json), [listing](parts/print-scorecard/listing.json) |

## Disk files and loader

The [media ledger](media.json) identifies both D64 images and the files visible to the directory reader. At $A291 the engine calls KERNAL LOAD through a loader that ultimately runs at $CC06. It copies the filename into $CD56 and uses the second character to dispatch:

- **Letter + CT.** The player selection code sets the first filename byte and calls the loader. A targeted trace of BCT returned through $A294 with carry clear, changed the title at $BEE0 to DORAL COUNTRY CLUB, wrote the 18 names B01–B18 and set all 18 terrain prefixes to B. The listed A–P CT files are the course selection tables.
- **Letter + 00.** The loader reads the two requested digits, sets a stream count, and normally changes the disk name to 00, as at $CC7B–$CCA4. The A01 trace entering $A291 returned with carry clear and changed the decoded hole block starting at $C554. The available directory files A00–P00 contain packed course streams.
- **Letter + TF.** The gameplay path builds a three-byte TF filename at $B9C9. The traced ATF load staged bytes subsequently copied from $C000–$CBFF to $D000–$DBFF by $BF50. The directory contains ATF, BTF, CTF and DTF. The course table supplies the leading letter per hole.
- **DMO and RNG.** $B968 selects DMO for the demonstration and RNG for the driving range. The DMO trace returned carry clear and populated the decoded hole block starting at $C554.
- **PRNT.** The second letter R selects a memory copy at $CC3C. This explains why the request succeeds without a PRNT entry in either directory.

The boot material and the bundled documentation program are listed separately in the media ledger. The course editor described in the publisher's manual is open for this release.

## Analysis status

The [handoff](TODO.md) records the measured ledger coverage and the outstanding attribution and verification work. Local traces, disk images and snapshots are under the ignored `work/` directories. The [orientation](orientation.md) gives the routes and the debugger intervention used for the printer capture.
