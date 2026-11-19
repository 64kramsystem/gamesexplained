# Nebulus local work files

The analysis uses the Danish Gold C64 disk linked in orientation.md. Keep the input image and VICE snapshots in this directory.

- `nebulus.d64` is the input disk.
- `entry.vsf` is the captured hand-over at `$8017`.
- `play-tower1.vsf` is the snapshot used to build the listing.
- `nebulus.regen2000proj` is the local disassembler project.
- `final-coverage.txt` is the measured coverage and remaining queue.
- The trace scripts and their output are local evidence for facts.md.

From the repository root, reproduce the listing with:

```sh
python3 kit/scripts/listing.py games/c64/nebulus games/c64/nebulus/work/play-tower1.vsf
```
