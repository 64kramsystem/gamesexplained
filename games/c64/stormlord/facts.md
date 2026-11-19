# Stormlord findings

## Startup and graphics

- The hand-over is at `$C000`. Startup sets the port to `$35` and banks to `$34` during copies that touch hidden RAM. The IRQ and NMI vectors are the hardware vectors in RAM while the KERNAL is out.
- `$C0C3` builds tile pointers with a stride of 32 bytes. `$E000` reads 156 records of 40 bytes each from `$6000`. A record has four ten-byte sections. Each section has eight bitmap bytes, a screen byte and a byte with a color nibble. The first 133 records supply fresh bitmap data. For 23 more, the loader advances over those bitmap bytes and uses pointers from `$E129` while still loading the color fields.
- The sprite source at `$C500–$DBFF` has 92 slots of 64 bytes. Rendering its three-byte rows shows layered player poses, shot and sword shapes and enemy frames. The two VIC banks share the slot indices. `$C1EF` writes the second copy with I/O banked out. A load and store checkpoint pair saw 0 reads and 5,888 writes to its destination before the copy returned.
- The panel IRQ at `$2513` stages six foreground sprites. It writes `$17` to `$D016` and zero to `$DD00`, selecting bank `$C000`. The playfield handler at `$25F8` draws from the bank and scroll variables. The shared scheduler from `$2612` advances its phase, changes the raster comparison and installs the next IRQ address from split tables. The handlers at `$26A5`, `$26D4` and following addresses reuse hardware sprites with later entries from the object queue.
- `$1C6C` clears `$FE63` and spins at `$1C71` until the IRQ changes it. A store watchpoint stopped after `DEC $FE63` at `$287D` in live play. The foreground then takes the current X, Y and shape fields for the player sprite pair.

## Controls

- The title path at `$AA6B` switches between keyboard and joystick. `$23D2` splits active-low bits 0–4 of CIA1 port A into up, down, left, right and fire. The keyboard path at `$23F3` writes each configured row mask and tests the matching column mask.
- The boot key screen displays left O, right P, up Q, down A and fire Space. The code at `$7A60` waits for N or Y, and the redefinition path checks a pressed key against already selected row/column combinations.
- In normal play the fire dispatcher at `$3E03` increments a counter up to nine while fire is down. Release with a count from 1 through 8 reaches the short-shot path at `$3E3B`. A count of nine reaches the sword path at `$3EEB`. On identical paused snapshots, a two-frame hold produced two hits at the counter increment, one at the shot path and zero at the sword path. A ten-frame hold produced nine increments, zero shot hits and one sword hit. These are instruction checkpoint counts. Each path also tests object availability before creating a projectile.
- The NMI at `$36B7` sets `$FDF8` to `$FF` and `$FE5E` to `$51` when `$FE5E` was clear. The game loop checks this abort flag at `$074A`.

## Level selection and map format

Level records begin at `$2DCE`. `$2CA2` wraps level 5 to 1 and passes the selected source to `$3102`. Its output starts at `$7D00` and uses a page per map row. The renderer at `$388D` takes 20 columns and nine rows. The map expander uses `F9 count value` for repeated literals and `F8 count` for blank or alternating fill. `FF` ends the stream. A subsequent scan at `$34AC` extracts some tile values into object and command lists. The loop at `$073C` compares the rescued count with the target, then calls the round that uses record zero and advances the stored level afterward.

| Map | Packed bytes inclusive | Packed size | Expanded cells |
| --- | --- | ---: | ---: |
| 0, title and bonus | `$9E3E–$9F02` | 197 | 2,304 |
| 1 | `$9F03–$A1D5` | 723 | 2,304 |
| 2 | `$A1D6–$A4B3` | 734 | 2,304 |
| 3 | `$A4B4–$A735` | 642 | 2,304 |
| 4 | `$A736–$A9CC` | 663 | 2,304 |

## Items, time and lives

- The fairy callback at `$0D1D` adds score, increments the rescued count at `$FE60` and redraws the counter. The round compares it with the level target at `$073C`.
- The gate handler at `$0C35` requires equipment ID `$6A`, vertical alignment and horizontal overlap. It removes the key along with the gate. In the grounded jump handler, equipment ID `$5C` raises the up-input hold limit from `$14` to `$2C`. Eligible odd counts reload the movement index with `$30`.
- The falling-hazard setup compares the held item with `$74` at `$0881` and clears descriptor byte `$1573` on a match. The honey-related handler at `$0CD9` tests `$FE6D` before updating the map-object records and clearing the active sprite with ID `$72` if found. The complete insect attraction sequence remains open.
- The panel clock starts at `$305E`. The two-byte counter at `$3074` reloads on rollover and advances the display phase. Phase `$21` sets the game-end flag.
- `$11D8` handles a caught bonus tear. Two instruction-stepped trials began with nine tears. With eight lives the tenth tear reached `INC $FE5F` at `$11F1`. With nine lives the branch at `$11EF` skipped it. Both trials reached ten tears and nine lives. The trials entered the callback directly from a paused snapshot.
- The title matcher at `$A9EF` reads the ten keyboard indices at `$AA53` for **NAUGHTYBOY**. Completing the sequence toggles `$AA5E`. The damage path at `$5D2D` checks that flag before decrementing lives. This was traced statically.

## Title-to-game entry

Fire transfers control to the BRK at `$06EE`. On the analysed release the instruction trace entered the title IRQ at `$244D` and returned via the RTI at `$2476` to `$06F0`. The undocumented SHS instruction there consumes the next two bytes before the call at `$06F3` initializes tune zero with A clear.

## Text

The title character source is in RAM under I/O at `$DC00`. `$3F35` copies its pages to `$E000`. `$22DB` writes VIC cell codes `2 × (glyph + $D0)` modulo 256 and the next code vertically. The alphabet was read from the rendered pairs in `work/font-pairs.png`. The letters use negative-space glyphs.

| Stored glyph codes | Display |
| --- | --- |
| `$30`, `$31` | Space and dot |
| `$32–$3B` | Digits 0 through 9 |
| `$3C–$40` | Exclamation point, decorative star, heart, left arrow and right arrow |
| `$41–$5A` | Letters a through z |

The stream reader at `$3675` gets its pointer in A and X. `$DF` supplies a row and column. Known scripts use `$FF` to end. Examples are the keyboard definition prompt at `$7D61`, the name-entry prompt at `$5CB6` and the credits at `$9C99`.

## SID driver

The entry table is at `$AA9B`, `$AA9E` and `$AAA1` for tune initialization, silencing and the tick. `$AEE2` initializes the three track pointers from eight-byte tune records beginning at `$AF23`. The track bytes index phrases through `$AF43/$AF80` or set transpose, reset the track indices or stop the player. `$AB25` decodes the phrase tokens and `$AE8A` writes voice registers using the voice register offset table. The program uses separate waveform, pitch, pulse-width and filter streams.

## Register census

| Registers | Use traced |
| --- | --- |
| `$01` | RAM and I/O banking at `$C033`, `$C1F4` and `$3F3D`. |
| `$D000–$D010`, `$D01C`, `$D025–$D02E` | Sprite positions, high X bits, multicolor and colors at `$2513`, `$25C5` and the later raster stages. |
| `$D011/$D012` | Display mode and raster timing at `$2519`, `$2538`, `$261E` and `$36EE`. |
| `$D016/$D018` | Fine scroll at `$2605` and title character/screen bases at `$9BFC`. |
| `$D019/$D01A` | VIC interrupt acknowledgement and mask at `$253D` and `$C185`. |
| `$D020/$D021` | Border and background changes at `$A9E6` and `$5C8C`. |
| `$D400–$D418` | SID voice and mixer writes at `$AC02` and `$AE8A`. |
| `$DC00–$DC03`, `$DC0D–$DC0F` | Control reads, keyboard row selection and CIA1 configuration at `$23D2`, `$23F5` and `$C086`. |
| `$DD00/$DD02`, `$DD0E/$DD0F` | VIC bank selection, direction and CIA2 timer control at `$2533`, `$C053` and `$C08C`. |

The full decoded census and instruction probes are retained in `work/`.

## The listing's error rate

An independent gpt-6.2-sol checker sampled 70 of 924 comments with seed 6510. Seven contained incorrect details (10.0%, with a 95% Wilson interval of 4.9% to 19.2%). The estimate weighted by the three strata was 9.9%. The comments were corrected for the starting object slot, the fall distance on an empty map column, the end-of-game wait and score search, the indexed map read, two panel row numbers and the direction of the panel color restore. Related panel comments were also checked and corrected. A full audit on a proven model is recommended.
