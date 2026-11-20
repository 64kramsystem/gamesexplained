# Local analysis inputs

`entry.vsf` is the ROM-free handoff at the execute stop at `$0850`.
`play.vsf` is the graveyard comparison snapshot. `title.vsf`
preserves the title before the press of port 2 fire.

From the worktree root, rebuild the listing with:

```sh
game=games/c64/ghosts-n-goblins
python3 kit/scripts/listing.py "$game" "$game/work/entry.vsf" --entry "$game/work/play.vsf"
python3 kit/scripts/coverage.py "$game"
```

The disk image and boot procedure are named in `../orientation.md`.
The stage, padding, gameplay and score-dispatch probes use
`PYTHONPATH=kit/c64` and the kit's assigned VICE port. The source
annotations can be reloaded into regenerator2000 by starting it on
`entry.vsf` with the kit launcher. The applied annotation log is
`annotations.jsonl`. The independent sample is in
`reports/handoff-sample/`.

The snapshots, disk images, extracted files, logs and probe scripts
stay in this ignored work folder.
