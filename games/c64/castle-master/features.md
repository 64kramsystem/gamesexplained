# Castle Master — features

Sources: [game documentation](https://mocagh.org/miscgame/castlemaster-alt3-manual.pdf) and the contributor’s annotated listing, consulted 30 September 2026. The documentation supplies the feature inventory; the imported annotations supply verification leads.

| Feature | Status | Evidence or open work |
|---|---|---|
| First-person movement and stone throwing | open | $47C5 main loop; gameplay reached live, individual action paths not replayed |
| 3D rooms and objects | traced / partly live | All 34 headers/546 objects parsed; all area loaders and fourteen projected vertices checked natively; complete transforms/renderer still open |
| Object and room interactions | traced / partly live | All 193 streams/809 tokens parse; six controlled event-selector fixtures pass; ordinary interaction routes remain open |
| Language and character selection | live | Hard-reset disk boot through to WILDERNESS |
| Saving and loading | live (disk), open (tape) | Native device8 SAVE/LOAD restores the entire652-byte payload; tape transfer is untested |
| Strength, keys and spirits | traced | Initial strength16 from$9D05; runtime keys$245A, spirits$2454, target21$9D49; full interaction progression remains open |
| Riddles and messages | traced / partly live | Nine panels independently parsed;61 fixed16-byte messages; six native font expansions exact |
| Run/walk/crawl and view controls | traced / open boundaries | Raw distances30/60/240 at$9D46-$9D48; input and signed movement routines traced, complete input replay remains open |
| Music and effects | traced / partly live | Eight instrument windows native checked;17 request groups run for25 ticks each; exact sustained audio/waveforms remain open |
| Information display and sound selection | traced / live UI | $77FE menu,$123A/$123B sound flags; native disk UI accepts device/name/Return |
| Lightning and hazards | traced / open routes | $483E scheduler and$4FA3 collision paths; boundary/ordinary-route tests remain open |
| Full rescue route | open | Database and scripts are preserved; no end-to-end input replay |

Imported annotations seed the listing; the checked contracts are recorded in facts.md. Scope and the disk boot are described in `orientation.md`.

Packed text and loaded HUD graphics are traced and checked independently. Six native glyph fixtures and all eight default instrument windows pass; the initialized HUD frame reconstruction matches every emulator pixel.
