# Test Drive technical facts

## Loading and relocation

The two disks have a private two-byte-ID directory, in addition to the Commodore DOS directory. `$131E` searches the resident list at `$0900`. The serial routine at `$0B6B` receives each byte through CIA2 port A. `$192B` wraps logical sectors at 16 and translates logical tracks at or above `$24` through the track/sector pairs at `$1829`.

The resident call at `$081E` jumps to `$1A3A`. The handler loads the selected module, computes the relocated entry, and adjusts operands in executable bodies. The dispatch at `$1AD8` uses `JMP ($0A52)` with the original A, X and Y restored. Live stops at that instruction recorded these calls:

| X/Y ID | Relocated entry | Evidence |
|---|---|---|
| GS | `$B56B` | X=`$47`, Y=`$53`, vector `6b b5`. Single-stepping the dispatch reached `$B56B`. |
| HS | `$E804` | X=`$48`, Y=`$53`, vector `04 e8`. Single-stepping the dispatch reached `$E804`. |

The caller paths were exercised by setting the program counter to the existing interlude and ending handlers in a saved machine. These traces establish the load and dispatch addresses. The game outcomes still need evidence from their own decision branches.

## Driving and road stages

The RD module is relocated from `$6500` to `$6A00`. Its four-byte header gives entry `$6A04` and body length `$387D`. The main road-stage setup at `$6A1B` invokes a module whose ID is `R` followed by `$52 + $31`. Live checkpoints at `$6A2C` caught returns with X=`$52`, Y=`$31–$35` and the selected stage present at `$3600`.

The first 31 bytes of each module's executable body install three pointers. The pointer at `$4E–$4F` addresses the stage sequence, `$50–$51` points to the element pairs, and `$6B–$6C` points to the relative substream offset table. See the individual stage facts for the lengths and boundaries.

The renderer at `$7845` and driving update at `$9004` read the stage sequence. Negative entries supply a byte offset into a little-endian relative pointer table after masking bit 7. A negative byte from the resulting substream advances the enclosing cursor. The sequence's literal `$FF` takes the stage-end branch at `$905A` and sets `$A9` to 1.

## Controls and timing

A CPU load watchpoint on `$DC00` fired in the driving input routine. The stop PC was `$8EA8` immediately after the `LDA $DC00` at `$8EA5`. A released stick read $7F and selected direction row zero. Held up plus fire read $6E, selected row one and reached the store to $45 at $8EF4 with A equal to 1. The released case reached $8F0E with the fire mask still set. That path masks the direction nibble, searches `$9D53`, then rereads CIA1 port A at `$8EB9` and masks bit 4 for fire. The shift path reads the alternate-shift flag at `$5D` and can use the lookup at `$33F4` when it is set.

The control path at `$6D1B` polls the resident keyboard service. In direct
dispatch probes from the saved road, VICE stopped on these stores after
each character was supplied in A. The probe starts at the first
comparison at `$6D1E`.

| Key | Store | Effect traced in the code |
|---|---|---|
| D | `$6D40` complements `$5C` | Changes the condition at `$86C5` that controls cockpit overlay visibility. |
| M | `$6D4A` complements `$5A` | Switches the mask applied to the SID music mode and volume value at `$65E1`. |
| S | `$6D54` complements `$5B` | Switches the mode and volume mask used when applying an effect at `$2B3C`. |
| O | `$6D5E` complements `$5D` | Enables or disables the alternate shift lookup. |
| V | `$6D72` complements `$5E` | Enables or disables the numeric speed and engine readouts drawn by `$98D6`. |
| P | `$6D29` clears `$5B` | Suspends the usual driving pass while waiting for a character, then restores the previous mask. |

The local store-watch results are in `work/resume-keyboard-watch.log`.

## Register census

| Register | Routine and use |
|---|---|
| `$01` | `$8AB3` saves the port. `$8AB8` sets additional banking bits on entry to the driving IRQ. |
| `$0314–$0315` | The title, selector and driving images observed `$31DB`, `$33CB` and `$8AB3` respectively. Driving setup installs its word at `$73ED` and `$73F3`. |
| `$D019`, `$D012` | `$8AB3` acknowledges VIC-II IRQ status and writes the next raster line from the table at `$9E53`. |
| `$DD00` | `$8ACB` combines the old port's upper bits with per-phase bank bits. `$8B36` toggles bank-select bit 1 when a buffer change is pending. The frame trace shows writes of `$C6` and `$C4` at raster lines 2 and 165. |
| `$D000–$D010`, `$D015`, `$D01C`, `$D025–$D02E` | The driving IRQ feeds sprite position and display registers from the prepared tables. The frame trace includes changes on both sides of the raster split. |
| `$D018` | The opening-road register sample read `$81`, giving bitmap base at the start of each active bank and screen matrix at bank base plus `$2000`. |
| `$D400–$D401` | The selector writes a calculated word to voice 1 frequency at `$34EB` and `$34F2`. |
| `$D418` | The selector fades master volume in the loop at `$32D8`, paced by the counter at `$30`. |
| `$DC00` | Road and selector input loops at `$8EA5` and `$346B`. |
| `$DC04–$DC05`, `$DC0E` | `$73CB` and following instructions configure CIA1 timer A. The driving code reads the timer bytes again at `$90FF` and `$9102`. |

Local evidence includes `work/probes.log`, `work/interludes.log`, `work/stages.log` and `work/driving-frame.json`. Frame traces include RAM and remain local. Unclassified bytes and unresolved feature questions are tracked in `TODO.md`.

## Packed graphics for the road

The side B file ID `##` is present in the stage-one entry and road snapshots at `$A286–$BFFF`. All 7,546 bytes match the catalogue extraction. The first 256 bytes are 128 ascending little-endian offsets relative to `$A286`. The loader lookup in `$7144` stores that base at `$DB–$DC`, then saves four resolved pointers and a secondary directory base at offset `$88`.

The road projection and sprite routines consume the payload in several ways. `$8236` takes a record offset from the main directory and uses its leading byte to clear a prefix of the destination sprite before copying the graphics. `$8795` reads the first byte of its selected record as a height and `$87F3` uses the subsequent bytes in the bitmap. A stopping load watch on the full module caught the bitmap reader at `$89C8`, with the CPU stopped at the following store at `$89CA`. The two surface-pattern bases used there come from directory entries 50 and 51.

The Lotus, Lamborghini, Porsche and Ferrari modules share a needle drawing routine at `$3170`. The code clears a 64-byte sprite, then steps between a centre and scaled endpoint. A sprite row occupies three bytes. `$3399` contributes the row stride, `$3369` maps pixel columns to sprite bytes, and `$3381` supplies the bit masks. The Corvette uses a different module.

## Bitmap buffers

The opening road uses the bitmap at the base of VIC banks 1 and 3. With `$D018=$81`, the active colour-selection matrix lies at bank base plus `$2000`. The first buffer holds the initial visor at `$4000–$427F` and instrument panel at `$5180–$5F3F`.

The selector creates the second bitmap with a 32-page copy. A stop on `STA ($04),Y` at `$312A` caught source pointer `$4000` at `$0E` and destination pointer `$C000` at `$04`. The saved driving entry has all 8,192 bytes equal in the two buffers. The drawing engine changes the windshield area and the cockpit during play.

## Packed disk resources

The UJ module starts at `$27FD` in the captured selector. It takes the two-byte resource ID from the stack. After resolving the disk item and checking its type and header, it reads the stream from seven bytes past the start of the resource.

`$2974` maintains a repeat count in X. A regular token is an immediate literal. The first escape code reads a byte count and a value. The three other escape codes have fixed counts of three, four and five. The first decoded data are five-byte descriptors containing flags, two ID bytes and a little-endian length. The first zero flag ends the descriptors. The child payloads follow in the same order.

The local decoder `work/unpack_uj.py` reproduced every byte of the eight Lotus cockpit objects from side B resource `#1` and the six selector objects from resource `$2A/$C3`. The check read the live directory's flags, addresses and lengths, then compared the decoded data with the corresponding emulator snapshots. The checks and their byte counts are in `work/uj-match.log`.

An instruction trace from the saved selector entry stopped at the decoder at $2974, the terminating descriptor branch at $28CC and the first payload store at $2951. At that store A held $28 and the destination pointer at $04 held $FED8, the address of the first selector object `_1`. This places the store after descriptor parsing and before the payload pointer increments. The trace is in `work/resume-uj.log`.

The Lotus, Lamborghini, Porsche and Ferrari modules also share two
90-entry needle endpoint tables. The vertical table begins at $32B5 and
the horizontal table at $330F. The gauge routine patches its indexed load
operands from the pointer words at $3226 and $3223. In each module, starting
the tachometer update at $2F23 triggered read watchpoints in both tables.
The horizontal read stopped at $3043 after the load at $3040. The vertical
read stopped at $3053 after the subtraction at $3050. The trace is in
`work/resume-needle-watch.log`.

The cockpit setup returns the address of its patch descriptors to
the driving engine. The engine installs their addresses in indexed
instructions beginning at $7307. Separate CPU probes in the Lotus image
stopped immediately after the steering-wheel table reads at $8DB0
and $8DBB, the gear-lever reads at $8DD3 and $8DD8, the alternate-shift
lookup at $8EE2, and the gear-ratio and acceleration reads at $9802
and $9839. The four needle-driven cockpit modules share this descriptor
format. The Porsche supplies shorter gear tables and different addresses
for the acceleration curve and shift map. See `work/resume-cockpit-tables-watch.log`.


## The listing's error rate

An independent gpt-6.2-sol checker sampled 70 of 1,797 comments with
seed 731. Four comments had wrong details. The fixes clarify the
Corvette numeric font stride, the four first-byte choices for a road
row template, and the final bytes outside the row data in two roadside
bitmap records. The observed error rate was 5.7% with a 95% Wilson
interval of 2.2% to 13.8%. Weighting the sampled strata by their sizes
gives 6.2%. A full audit on a proven model remains open.
