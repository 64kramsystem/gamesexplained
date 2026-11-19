# Local analysis work

This folder holds the DCS D64 image, the first gameplay snapshot,
the loader, IRQ and control traces and the listing sample. The four
load folders and the engine each have their own `work/entry.vsf` and
`work/play.vsf`. Those binaries and the trace scripts stay local.

The routes are in [orientation.md](../orientation.md). From the
repository root, rebuild a part’s listing with
`python3 kit/scripts/listing.py <part directory> <part directory>/work/play.vsf`.
Use the same snapshot with
`python3 kit/scripts/symbols_import.py <part directory> <part directory>/work/play.vsf`
to recreate its Regenerator2000 project.
