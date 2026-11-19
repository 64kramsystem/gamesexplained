# Mission A.D. technical facts

## Machine and display

The disk game runs with CPU port `$35`, with BASIC and KERNAL ROM out and I/O visible. `$57CD` installs the RAM interrupt vectors and enables VIC raster interrupts. `$5818` selects raster `$84` and the handler at `$5895` during play. `$5895` selects `$CC` and restores the vector to `$5818`. The first-room capture shows the `$5895` handler publishing sprites with Y values 160 and 181 after entering at line 132. The `$5818` handler publishes Y values 80 and 101 for the next frame. Sprites 0 and 1 represent the agent, and the two raster updates reuse sprites 2–7.

| Hardware | Use and evidence |
|---|---|
| CPU port `$01` | `$5804–$580A` clears the low two banking bits and sets bit 0. VICE reads `$35` in the first room. |
| VIC `$D000–$D010`, `$D015` | `$B33F` positions the agent's two sprites. `$61F6` and `$622D` load the other six positions and apply their enable masks. |
| VIC `$D011`, `$D016`, `$D018` | `$591C` selects multicolour bitmap mode and the matrix/bitmap offsets. CIA2 port A read `$97` in the first room, selecting bank 0. Matrix `$0400`, bitmap `$2000`, sprite pointers `$07F8–$07FF`. |
| VIC `$D012`, `$D019`, `$D01A` | Raster comparison, acknowledgement and interrupt enable. Writes at `$586C`, `$587D`, `$58AB`, `$58A6` and `$57EC`. |
| VIC `$D025–$D02E` | `$58D9` sets shared sprite colours. `$61F6` and `$622D` publish individual colours from RAM. `$6278` reads the shared colours for the modal target icon. |
| SID `$D400–$D414`, `$D418` | `$5940` clears the registers and sets volume 15. The title/mode music engine enters via `$4001`. Voice 3 effects `$4B2F` read control commands and frequency pairs from scripts. |
| CIA1 `$DC00`, `$DC01` | `$1828` reads joystick port 1 or scans the five keyboard assignments via `$187B`. `$AF0C` scans the title menu digits directly. |
| CIA1 `$DC04` | `$17D3` advances a patched memory read operand and XORs the addressed byte with CIA1 timer A low. |

The mechanical census, including indexed register operands and access counts, is retained in `work/census.txt`. The frame capture is `work/first-room-frame.json`.

## Input and shot paths

`$1828` uses `$14` to select keyboard when zero or joystick when nonzero. `$1833` reads CIA1 port B, masks its low five bits and inverts those bits into `$13`. The bit values are up 1, down 2, left 4, right 8, fire 16. The keyboard scanner returns the same layout using the three five-byte tables at `$18A1`.

The first-room probes restored the same snapshot for each input. Over each 20-frame window `$1828`, `$1833`, `$5818`, `$5895` and `$B1B0` each executed 20 times. Without fire the probes saw no writes to `$F6`. Holding fire reached `$B595` and its start store at `$B5C7` twice, with 20 total stores to `$F6` while the shot animation ran. The paired execute and store watchpoints are logged in `work/probes.txt`. `$B595` checks for support-cell type `$0B`; the separate directional movement path uses the table at `$B190` to patch the handler address into the call at `$B243`.

## Rooms, map and timing

- `$5E0D` indexes a 16-by-16 room layout selector at `$F800`. `$5EAF` resolves the base layout through the 35 entries at `$6393`, including the high-bit position-reversal path. A separate 256-entry overlay index has low bytes at `$7830` and high bytes at `$7930`.
- `$5ED4` draws each placement list. A count precedes pairs of packed position and shape bytes. The 35 base lists occupy `$63D9–$6C91` and the 196 nonempty overlays occupy `$6C92–$782F`. The empty overlay is `$7A30`. Counting records according to the routine reaches the next pointer for every list.
- `$5CAC` uses the low seven bits of the shape number to index the pointer table at `$1F06`. Each row of a shape uses five screen cells and forty bitmap bytes. The descriptor selects either one repeated screen byte or explicit screen bytes for each row. The height comes from the low nibble of the first byte.
- `$C31F` plots one of four states in two bits at a time in a 16-by-16 map. `$C2B2` clears the packed workspace, plots the destination highlights, targets and current room, then copies the two bands into the visible bitmap.
- `$C282` sets the time limit, target count and variant using the mission index. `$5951` advances the subsecond, second and minute counters using underflow and reload. The briefing for mission 001 shows five targets and 16 minutes in the disk run. The gameplay time bar reads `$18`, and the energy bar is drawn from `$E1`.

## Bitmap text

The game does not store ordinary screen codes for its title and briefing. `$AD43` takes a seven-byte header (column, row, glyph count, screen/colour pair for each row) followed by glyph indices. It retrieves each glyph from the `$4D24` pointer table and writes its two 16-byte strips into the bitmap. The codes were checked by rendering the packed pixel pairs of the glyphs in their directory order and decoding the title and briefing records.

| Codes | Glyphs |
|---|---|
| `$00–$19` | A to Z |
| `$1A–$23` | 0 to 9 |
| `$24` | Space |
| `$25`, `$26`, `$28` | ©, period, colon |
| `$27`, `$29–$33` | Other punctuation and pictorial forms. Their individual uses are open. |

The title's menu directory is `$A8A3`, the title fire prompt is `$AD0E`, and the briefing records begin at `$C417`, `$C42B` and `$C43E`. `$C45A` overwrites the decimal glyphs in the three briefing records before drawing them.

## Mission results and bonus

The play loop checks time, energy and outstanding targets in that order at `$5B0B`, `$5B18` and `$5B21`. With each condition forced separately, VICE hit the corresponding result store at `$5B15`, `$5B1E` or `$5B27`, writing 1, 2 or 4 to `$5F`. The dispatch at `$5C02` uses that byte to select a result handler. The time and energy handlers decrement lives and branch to the briefing if lives remain or to game over otherwise.

The bonus handler at `$C5C6` counts down from `$E4` and `$DC`, calling the time and ally adders at `$C6B6` and `$C6DB`. With those inputs set to 2 and 3, execute checkpoints counted two time additions and three ally additions. The ally addend at `$C6D8` is 025. The friendly-hit handler at `$C0F0` decrements `$DC`. The bonus handler copies the total into the pending score digits after confirmation.

## Verification checkpoints

- With a jump phase forced, the player update entered the geometry probe at `$B255`, then jumped through `$B1CB` to `$B47D`. With `$DB` set instead, it returned at `$B1C6` after probing. Neither case hit the normal finish at `$B24E` before the stopping checkpoint.
- Projectile flags masked with `$60` select four source pointers. For values `$00/$20/$40/$60`, the live watchpoints saw the matching directory reads and writes of `$02B4/$102B/$1053/$107B` into the load operand at `$BF3E–$BF3F`.
- The sprite setter at `$B82D` wrote position and colour into RAM. The raster publishing routines at `$61F6` and `$622D` write staged attributes to the VIC.
- The title directory high byte at `$A8A4` was read at `$AD33`. In the wipe's inner copy, read watchpoints hit `$8596`, `$859E` and `$85A6`. These are three successive cells within the third bitmap row of room shape 03.
- A direct call to the short entry at `$B632` hit the store at `$B634` and the write watchpoint on `$F7`. Its caller remains open.

The forced-state tests are logged in `work/resume-trace.txt`. They establish the branches and memory accesses under the inputs listed in `work/resume-trace.py`.

The disk contains one packed PRG. The listing covers the resident image entered by the final restore. The original tape is a comparison copy. Later media reads remain an open check.
