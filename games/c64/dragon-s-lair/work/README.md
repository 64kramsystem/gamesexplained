# Local analysis files

The disk, snapshots, projects, trace logs and helper scripts in this directory are gitignored. Part snapshots and Regenerator2000 projects live in each part's own ignored work directory.

The main captures and route are described in `../orientation.md`. The observations are in `../facts.md`. A project can be recreated from its exported symbols with `python3 kit/scripts/symbols_import.py <part directory> <snapshot>`. The second descent uses `work/prepared.vsf` for its listing, and the other parts use `work/entry.vsf`.

`capture.py` records forced selector transitions, `instruction_probes.py` holds the focused instruction tests, and `build_analysis.py` holds the local project export and listing recipe. Run them from the repository root with `PYTHONPATH=kit/c64:kit/cpu` and the batch's assigned tool ports.
