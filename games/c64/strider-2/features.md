# Strider II features

Source: [C64 manual, Project 64 transcription](https://www.lemon64.com/doc/strider-2/570).

| Feature | Evidence | Status |
|---|---|---|
| Title and port 2 fire to begin | Booted X-Ray disk, then held port 2 fire | Observed |
| Forest with sentry robots and air support | Manual and [forest screenshot](reference/forest.png) | Forest observed. Enemy behaviors open. |
| Ruined city with artillery and generators | Manual, stage 2 and the position tests at $A901, $A967, $A99B and $A9CF | Area observed. Artillery and generator roles open. |
| Underground aliens and their mother | Manual, stage 3 and the encounter test at $AAD4 | Area observed. Enemy variants and the boss identity remain open. |
| Rooftops with gaps and attacking skulls | Manual, stage 4 and the position test at $AA0B | Area observed. The attacking skulls remain open. |
| Prison ship and rescue | Manual, stage 5 and the stage-specific exit test at $84B9 | Area observed. The rescue sequence remains open. |
| Human sword and standing laser | Port 2 trace and the two action branches at $A1C2 and $BF53, documented in [resident facts](parts/resident/facts.md) | Confirmed in the forest test snapshot |
| Energy icons unlock robot form at the stage's final battle | $BD6C updates the meter target and $A59A toggles player state bit 7 on the encounter path | The manual's threshold is open. The encounter-state and meter paths are traced. |
| Robot walks in both directions and fires the laser | The bit-7 branch at $A17A masks both vertical input bits before reaching the fire test. Position checks are shared with the movement path. | Traced. The full robot encounter is open. |
| Pause with RUN/STOP and quit with RESTORE | The release breakpoint at $843D proves the X-Ray RUN/STOP behavior. The NMI goes through $94BA. | Differs for RUN/STOP, which requests a stage transition. RESTORE behavior remains open. |
| Score, lives, time, and status meters | [Forest screenshot](reference/forest.png), $B01D HUD digits, $AF79 meter update and the timer breakpoint | Confirmed display and timer cadence in the measured forest run |

## Sources

The manual transcription and [X-Ray disk entry](https://csdb.dk/release/?id=35898) were consulted on 20 November 2026. The stage references show VICE snapshots after the loader selects [city](reference/city.png), [underground](reference/underground.png), [rooftops](reference/rooftops.png) and [prison ship](reference/prison.png). The stage screenshots establish the settings. The enemy, boss and rescue behaviors remain open.
