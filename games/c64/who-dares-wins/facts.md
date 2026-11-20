# Who Dares Wins technical facts

The listing uses the original Alligata cassette at the handover to `$4000`. The two checksummed tape payloads account for all 48,896 bytes at `$0900–$C7FF`. Both tape recordings contain these same payloads. See [orientation](orientation.md) for the load order and hashes in [the media ledger](media.json).

## Memory layout

| Range | Role and evidence |
|---|---|
| `$0200–$03FF` | KERNAL and tape boot workspace. The resident engine reuses `$02B2/$02B3` for fire state, `$02BC–$02C9` for music state and `$0314/$0315` for each successive raster vector. |
| `$0400–$07FF` | Generated video screen and sprite pointer table. `$1608` selects screen `$0400` and characters `$3800` in VIC bank zero by writing `$1F` to `$D018`. |
| `$0900–$0A60` | Victory text, title animation seeds and title credit strings. The animation reads eleven positions, colours and velocity pairs from tables at `$09C8–$09FE`. |
| `$0C00–$0FFF` | Title sprite shapes `$30–$3F`. `$4D55` seeds the sequential pointers, then `$4D8A` substitutes `$3E` for the soldier below the title letters. |
| `$1000–$13A6` | HUD, intermission text, dispatch tables and initialized object and SID state. The tape seeds the data in this allocation. |
| `$13A7–$1EF2`, `$4000–$4E53` | Engine, IRQ and NMI handlers, object updates and drawing helpers. |
| `$1F00–$1FFF` | Terrain flag lookup by screen code, used by movement and priority code. |
| `$2000–$37FF` | 96 64-byte sprite slots `$80–$DF`, including the sinking sprite work slot at `$2A40`. |
| `$3800–$3FFF` | 256 eight-byte character cells. Two cells at `$3F30` are animated from the source at `$3F40`. |
| `$5000–$BFFF` | World data in resident RAM. The complete rows have 38 bytes each and extend through `$BFEB`. |
| `$C000–$C7FF` | Two frequency tables followed by two music streams and their prefix bytes. |

The ledger retains the fill-dominated intervals between these structures, including the isolated non-fill bytes at `$0A61–$0BFF` and `$4E54–$4FFF`. Their interpretation is limited to position and byte pattern. RAM at `$FD30–$FD4F` matches the KERNAL ROM vector table byte for byte and sits outside both tape payloads. It is excluded with the generated screen, runtime workspace, hardware regions and stack.

## Timing and video

The raster scheduler at `$150A` selects its next IRQ from `$1180` and next raster line from `$1192`. The vectors captured in one gameplay frame were `$152F`, `$14FA`, `$154E` and `$1ADF`. The game increments its tick at `$1B4E` when the sprite-band handler reaches band four.

| Hardware | Access and role |
|---|---|
| `$D011/$D016/$D021` | `$14FA` sets up the black HUD band. `$154E` switches to the brown, multicolour playfield and applies the vertical fine scroll from `$A2`. |
| `$D012/$D019/$D01A` | `$1568` enables the raster IRQ, and `$150A` schedules and acknowledges interrupts. |
| `$D000–$D010`, `$D01B`, `$D027–$D02E` | `$1B5A` groups visible objects into six Y bands. `$1ADF` rewrites sprites 1–7 from those bands. The high X bits, priority and colours come from the software slots. |
| `$D01E/$D01F` | `$1748` captures sprite collision for object hit checks. `$1A3D` reads sprite/background collision for the sinking test. |
| `$D800–$DBE7` | `$4D11` fills colour RAM. The HUD writer at `$4DF5` and intermission at `$175E` also set individual rows. |
| `$DC00` | Port 2 active-low directions and fire in the title loop at `$1653`, the direction read at `$1939` and fire polls at `$1C07/$1D40`. |
| `$DC00–$DC02` | `$402B` scans CIA 1 port B with a walking bit on port A. |
| `$DC04–$DC05`, `$DD04` | CIA timer bytes used as varying inputs for spawn choices, shot timing, ammunition and animated ground. The title initializes CIA 1 timer A at `$160B`. |
| `$D400–$D414`, `$D418` | Three voice register sets addressed through `$3D/$3E` by `$13A7–$1484`. The title and play paths set volume directly at `$15E6` and `$1666`. |

Checkpoint counts over 120 PAL frames from the play snapshot were 120 at the playfield IRQ `$154E`, 120 at the collision latch `$1748`, 119 at the rifle poll `$1C07`, and 59 at the direction read `$1939`. The main loop uses alternate tick parity before calling movement.

## Text and graphics

The rendered font has blank code `$00`, A–Z at `$01–$1A` and digits at `$30–$39`. The stock and score formatter writes the digit codes directly. The title, HUD and intermission copy stored uppercase text through `AND #$3F` at `$1616`, `$4E04` and `$1796`. The HUD template at `$1036` uses `$5B` for the icon beside the grenade count. Its screen code is `$1B`, the leftmost symbol after Z in the rendered character table.

The VIC sprite slots have 21 rows of three bitmap bytes and a spare 64th byte. The game supplies one hardware sprite for the player and multiplexes other visible objects through the remaining seven. The software arrays at `$11DB`, `$11EF` and `$1203` describe object type, X in units of two VIC pixels, and Y. The update loop at `$1BCE` processes 18 software slots and patches a JSR through the table at `$1104`.

## Controls and collisions

- `$1C03` raises the rifle request only on a newly pressed fire poll. An empty rifle slot consumes it at `$1C1A`. The rifle samples a separate previous-press byte at `$02B2`.
- `$1D3C` increments `$02B3` while fire is down. On reaching `$0D` it raises `$59` and resets the counter to one. Released fire resets the counter to zero. The grenade slot at `$1D58` requires that request and nonzero stock in `$12B0`, then subtracts one in decimal mode.
- `$1928` converts joystick directions to a heading and changes heading before continued input moves the character. The X and Y step tables start at `$11AB` and `$11A3`. Tile bit 7 can stop steps. Infantry at `$40A3` treats either of the top two tile flags as blocking.
- `$1A0F` checks both sampled cells at the player's feet. Bit zero controls priority. Sinking requires both bit-six flags, VIC sprite-zero/background collision, and a fine-scroll-adjusted Y sub-row below four. `$1A64` copies the current figure into the scratch sprite at `$2A40`, and `$4694` erases its bytes from the end as the figure moves down.

## World and scoring

Each fine-scroll wrap at `$1A9C` fetches the next 38-byte row into `$0401` and advances the source pointer by 38 at `$18CD`. When the fine phase reaches one, the scan at `$1AA4` reads the incoming row from right to left. Codes `$F0–$FF` select entries in the table at `$1160`. A leading `$E8–$EF` byte queues a deferred row fill through `$18DA`.

The eight `$FF` commands occupy zero-based rows 116, 210, 311, 418, 505, 605, 705 and 753. Command `$FF` enters `$4B3A`, sets the upward scroll threshold to `$22` and installs the garrison controller. The controller at `$4B93` uses reserve count `$1034` copied into its slot and spawns reinforcements. At the stopped-scroll condition, the main loop checks slots 10–17 for clearance before showing the next-area message. The area-eight branch at `$17B3` resets the map pointer to `$5000` and draws the five-row victory text from `$0900`. The transition raises spawn and reserve settings at `$1825` when the updated cutoff is below `$B6`.

- `$15C2` seeds six grenades. `$422F` tests contact with an ammunition box and adds a timer-derived BCD quantity.
- `$1675` initializes three men. `$4681` removes one after death. At zero, `$46AD` compares the score with the record and returns to the title path.
- `$42D0` adds decimal points to three bytes at `$12B1–$12B3`. `$12C6` starts at 1 and increases by 2 after awarding an extra man, matching 10,000, 30,000 and succeeding 20,000-point intervals when the award test fires. The increment at `$42F5` is capped at nine men.
- The prisoner handler at `$4846` awards 750 when the paired guard becomes type `$0B`. Guard type `$0F` has a separate 50-point award in `$1132`, consistent with the inlay's combined 800.
- Type `$16` has score values `$50` and `$12` at `$1132+X` and `$1149+X`. The rifle path at `$1CB8` uses the full hundreds byte. The blast path at `$1EAE` masks its upper nibble, yielding 250 for this type instead of the rifle's 1,250.
- The map includes motorbike spawn pairs (`$4703`) and paired vehicles (`$4753`), stationary and opening emplacements (`$43B4/$45E0`), throwers (`$4B05`) and rocket infantry (`$4997`). The correspondence of every obstacle silhouette to the names in the inlay remains open.

## Sound

The title sequencer resets five fields at `$4CCB`, including the note countdowns and next-read pointers `$C081` and `$C22D`. Each high-bit command chooses an effect and waveform. Other records pair a pitch index with duration. Index zero is a rest. The low and high pitch tables start at `$C000` and `$C040`. The first sequence loops both voices when its next record pointer reaches `$C22C`. Title and victory playback enable the sequencer via `$1035`. Gameplay calls the same SID effect updater at `$13A7` for frequency, envelope and gate writes, with effects such as rifle, blast and sinking triggered by the object routines.

## The listing's error rate

The independent gpt-6.2-sol sample used seed 1985 and checked 60 of 300 comments. Seven were wrong in detail (11.7%, estimated 95% Wilson interval 5.8%–22.2%). The checker may have missed errors. All seven findings were confirmed and corrected, including the sinking sub-row condition, terrain and animated character flags, carry into an emplacement spawner, the paired motorbike positions, a thrower state byte and the two starting music pointers. A full audit remains due before treating this listing as checked.

## Live tests

- The first map read stopped at `$18C5` with pointer `$A3/$A4 = $5000`. A single step advanced to the corresponding screen store.
- From identical neutral play states, stopped and stepped the rifle poll's store at `$1C16`. Released fire wrote zero to `$02B2` and left `$58` clear. Held fire wrote one and raised `$58`.
- Stopped at `$1D52` on the thirteenth held poll. One step raised `$59`. Stepped the stock store at `$1D6B` from `$06` to `$05` and read the restarted hold count of one.
- Injected an isolated `$FF` row marker before `$1A89`, then stopped at `$4B3A`. The engine had patched the row jump to `$4B3A`. Stepping `$4B3C` changed `$12AE` from `$8C` to `$22`.
- Stopped at `$4CEC` after the title reset stores. Both counters were one and the two pointers were `$C081/$C22D`. At `$4C57` the next indirect load read the second voice's `$9F` command from `$C22D`.
- Counted instruction checkpoints at the playfield IRQ and input/collision instructions across 120 frames. The exact counts are in Timing and video.
