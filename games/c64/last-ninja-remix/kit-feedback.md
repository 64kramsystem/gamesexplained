# Last Ninja Remix — kit feedback

The imported composition combined resident and level bytes with no matching stopped machine. Review required a real boot. This revision boots disk 047 through both intros and the unmodified trainer into Central Park, compares its RAM with the composition, and builds Source only from active play.

The comparison found the composition’s `$0E00` startup code overwritten by sprite buffers. A live store checkpoint and the pointer tables confirmed double-buffered sprite output at `$0C00–$0FFF`, so stale startup code/names/comments were removed. The map is loaded into regenerator2000, exported through `symbols_export.py`, and rendered only through `listing.py` (rebuilt after each annotation session). No composed image or extra state listing is published.

The external export is private and its unknown makers’ models are explicit in `game.json.imported`. Coverage follows game data/runtime scope; the article carries the independently checked sprite browser, with other mechanics added only as verified. Shared tooling is separate in #125. The one-level scope and later-load TODO follow RFC #124.

VICE MCP 3.13.1’s pause and transport workarounds apply. It runs silently on a virtual display with dummy audio at the contributor’s request. Clocks retain only actual publishing and orientation work; outside analysis is not represented as timed here, and import metadata excludes the game from the runs table.

The three checks, complete site build and article/Source browser checks are run before publication. Full coverage, verification and the required maintainer check remain open for Silver.

The imported map omitted some runtime memory. regenerator2000 defaulted those holes to code and minted false references from buffer contents. The shared importer in #125 now fills uncovered ranges as byte data while preserving declared code, with three regression tests. Its reusable sweep notes require checking imported types before trusting generated labels. A changelog lesson can be added when this game folder is present in the kit branch; the documentation checker requires the named game to exist there.

A hand-over capture also exposed capped table spans: validating records alone does not keep an entire pointer table in the ledger. Declare the proven complete directory/resource extents and resolve every newly uncovered range instead of reporting the earlier percentage as complete coverage.
