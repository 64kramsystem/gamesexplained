# Machine facts

The evidence below covers the PAL Ocean Rainbow Collection disk. Source addresses belong to the resident engine unless a part is named. The annotations and the open work queue are in the per-part listings and ledger.

## Disk and progression

- The package chooser at $5C9D reads the world and round indices at $0624/$0625. $5B02 writes the world digit into the M and B file names. At round zero it loads the M file, skips the B file in Wellington and loads it in the other worlds. Captures at $5D51 show each requested file name before the receiver runs. The ranges and direct routes are in [orientation.md](orientation.md).
- Rounds 4-4 and 5-3 change assets within a world. $0A0C–$0A24 selects those two loader calls. The Wellington overlay replaces the glyph attributes, metatiles and font. The Cook Strait overlay replaces metatiles only.
- The final boss exit sets $0629 at $4714 and loads GO through the same chooser. In the ending part, $A000 installs its own vectors and calls $A36B to reveal 16 rows of screen codes. An execution watch on $A107 counted 20 ending IRQ entries in 20 emulator frames while $A3BF was entered four times.

## Map and object records

- The camera uses $23/$24 and $25. $2473 divides the fine camera positions into metatile and character offsets. The grid at $A000–$AFFF is 32 rows of 128 IDs. $B000–$BFFF gives 256 definitions of 16 glyph codes, ordered by column and then by row.
- An instruction stop at $24CB had X=$2D and $08/$09=$A001 in Auckland. The next five instructions read the directory at $5600/$5700 and installed $B2D0 into $0D/$0E. The trace is preserved in `work/map-probe.txt`.
- $2516 uses the selected glyph to read $9F00. The low nibble reaches color RAM. The high bits are tested as playfield properties at $0F34, $0F3B and $5964. O4 or O5 can keep the same map IDs and change how they expand by replacing the definitions.
- $41BE takes a round pointer from $9D04. The first byte sets the scan's starting index at $064B. It transposes the next 64 groups into four arrays beginning at $9800, $9840, $9880 and $98C0. $2968 checks the first array's flags and the next two arrays' coordinates against the active camera window. It sets bit 7 when a record receives a slot.

## Display and glyphs

| Address | Role | Evidence |
|---|---|---|
| $D011, $D012, $D019, $D01A | Screen and raster interrupt timing | $2081 installs $4F37 and arms raster line $FA. $4F37 writes the next vector at $4F45/$4F4A and raster line $40 at $4F4F. |
| $DD00, $D018 | VIC bank and font/matrix selectors | $4EF9–$4F09 selects bank 2 and $8800/$8000 for the status band. $1E23 and $1E63 configure the bank-3 playfield. |
| $D000–$D010, $D015, $D01C, $D025–$D02E | Sprite positioning, enabling and colors | $4F37 configures the earlier phase. $5195 patches its jump from tables at $54F8/$54FF, then the phase handlers assign more sprite coordinates and pointers. |
| $D8F0–$DBE7 | Playfield color RAM | $2410 and $2473 paint glyph colors. $9D0C and $9D8D shift colors with scrolling. |
| $DC00/$DC01 | Controller and keyboard matrix | Port 2 fire started the default title selection. $5972 selects and tests one keyboard matrix row and returns carry set for a matched key. |
| $D400–$D418 | SID voice and filter settings | $6E5E selects and starts the three voice streams. $6EF9 advances them. $71AC, $7347 and $739B update envelopes, pitch and pulse width. |

Rendered glyphs from $8000 show C64 screen-code letters at $01–$1A, space at $20, and digits at $30–$39. The first glyph is @. The upper half mixes status art and title decoration with VIC sprite bytes. Title menu text begins at $9203 and the TIME UP text is at $0B80. The separate $C800 playfield character set changes with the world and is normally interpreted as terrain. GO copies the $8000 font to $C800 for its text.

## Audio structure

$6E5E loads three little-endian order-list pointers from $757A plus the selector in X. $70F5 reads the order list and resolves ordinary indices through $75C2/$75EB. The phrase reader at $6FE4 interprets note plus duration, fixed-duration notes, rests and command bytes. $70E3 dispatches commands $80–$91 through split pointer tables at $7556 and $7568. The instrument handler at $71AC writes SID envelopes from nine-byte records beginning at $76EB. Pulse and frequency effects take duration/delta streams.

## Live tests

- With identical Auckland snapshots, watches on resident $4F37 and $50CA counted 16 raster ticks and 16 joystick reads in each 16-frame run. Up alone entered the jump input routine at $1613 16 times and initialized a jump at $1651 once. Fire alone entered the shot allocator at $1675 once. With the stick centered, none of those three handlers fired.
- In a 96-frame Auckland sample, the resident raster entry at $4F37 and SID update at $6EF9 each hit 96 times. $5195 handled 313 sprite phases. The main loop reached the timer routine at $0B21 48 times and carried out two packed-decimal seconds updates at $0B39.
- The title sequence at resident $905F consists of 25 key indices. An offline C64 machine advanced all 25 from the actual key matrix. A VICE checkpoint at $9097 tested the last match with the starting index at $18. With the matrix clear the index stayed $18 and $0628 stayed zero. With the matching key pressed it reached $19, set $0628 to one and wrote border color $0B. The life-loss path at $0C8A checks the flag before subtracting a life. The progression path checks it at $091A before reading key index $39.
- Read and execute range watches for the padding at $558C–$55FF, $5F3C–$5FFF and $6500–$69EF produced zero hits in the captured phases. The same batch detected 7,128 accesses to the boss staging tail at $6380–$64FF during the Cook Strait boss probe and 534 entries at $47A5. The transfer bounds and exclusions are in the resident part's metadata.
- The disk captures use entry checkpoints and compare each loaded region against its disk file. They establish the loader's behavior when given the requested state. Normal-play reachability of the late snapshots is outside these tests.

## The listing's error rate

Seed 624 sampled 100 of 932 comments with an independent gpt-6.2-sol checker. Fifteen findings held and were corrected. They covered an audio order-list extent, the title cheat, color and movement fields, timing counts and a boss dispatch directory. The unweighted estimate was 15.0%, with a 95% Wilson interval of 9.3%–23.3%. Weighted by the three strata, the estimate was 19.7%. The sample establishes a minimum of 15 errors in the sampled listing version. The checker may have missed others.

## Open questions

The available tests leave the documented simultaneous unlimited-lives key chord open. The title check at $9078 is a sequential key matcher, and the trace and reference search found the associated state at $0628. The full list of music and effect selectors remains to be named from their call sites. The location and interpretation of the sequencer's main tables are described above.
