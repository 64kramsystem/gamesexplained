# Last Ninja Remix — kit feedback

The imported composition combined resident and level bytes with no matching stopped machine. Review required a real boot. This revision boots disk 047 through both intros and the unmodified trainer into Central Park, compares its RAM with the composition, and builds Source only from active play.

The comparison found the composition’s `$0E00` startup code overwritten by sprite buffers. A live store checkpoint and the pointer tables confirmed double-buffered sprite output at `$0C00–$0FFF`, so stale startup code/names/comments were removed. The map is loaded into regenerator2000, exported through `symbols_export.py`, and rendered only through `listing.py` (11,410 records). No composed image or extra state listing is published.

The external export is private and its unknown makers’ models are explicit in `game.json.imported`. Coverage follows game data/runtime scope; the article is Bronze form until normal verification. Shared tooling is separate in #125. The one-level scope and later-load TODO follow RFC #124.

VICE MCP 3.13.1’s pause and transport workarounds apply. It runs silently on a virtual display with dummy audio at the contributor’s request. Clocks retain only actual publishing and orientation work; outside analysis is not represented as timed here, and import metadata excludes the game from the runs table.

The three checks, complete site build and article/Source browser checks are run before publication. Full coverage, verification and the required maintainer check remain open for Silver.
