# Castle Master — features

Sources: [game documentation](https://mocagh.org/miscgame/castlemaster-alt3-manual.pdf) and the contributor’s annotated listing, consulted 30 September 2026. The documentation supplies the feature inventory; the imported annotations supply verification leads.

| Feature | Status | Evidence or open work |
|---|---|---|
| First-person movement and stone throwing | open | $47C5 main loop; gameplay reached live, individual action paths not replayed |
| 3D rooms and objects | traced / partly live | All 34 headers/546 objects parsed; all area loaders and fourteen projected vertices checked natively; complete transforms/renderer still open |
| Object and room interactions | traced / partly live | All 193 streams/809 tokens parse; six controlled event-selector fixtures pass; ordinary interaction routes remain open |
| Language and character selection | live | Hard-reset disk boot through to WILDERNESS |
| Saving and loading | open | $0423 and $7B03; round trip remains open |
| Full rescue route | open | Database and scripts are preserved; no end-to-end input replay |

The imported annotations are leads. Technical claims await tracing or live tests in this kit run. Scope and the disk boot are described in `orientation.md`.

Packed text and loaded HUD graphics are traced and checked independently. Six native glyph fixtures and all eight default instrument windows pass; the initialized HUD frame reconstruction matches every emulator pixel.
