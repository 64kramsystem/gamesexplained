# Local analysis files

The original ATC / Brute Force program is in `mouse-trap.prg`.
`entry.vsf` is the handover snapshot at PC $8E00. `gameplay.vsf`
is the comparison snapshot for the listing build. The title snapshot
is `attract.vsf`. See [orientation](../orientation.md) for the boot
sequence and program source. The archive and comparisons stay local.

From the repository root:

```sh
python3 kit/scripts/listing.py games/c64/mouse-trap games/c64/mouse-trap/work/entry.vsf --entry games/c64/mouse-trap/work/gameplay.vsf
python3 kit/scripts/coverage.py games/c64/mouse-trap
```

Local `probe.log`, `rooms.log`, `room-watches.log`,
`lastwrite.log`, `resident-watch.log` and `verify.log` contain the
instruction and memory watchpoint observations described in the
notes. The independent sample and its verdicts are under
`reports/sample-5031/`. The annotation log and disassembler project
also stay in this directory.
