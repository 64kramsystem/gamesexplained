# Dragon's Lair — technical facts

## Loader and memory

- The disk loader at `$0334` adds `$40` to the selector and patches the second byte of a two-byte name beginning with `L`. It switches the processor port to `$37` for KERNAL I/O and uses device 8, secondary address 1. Instruction stops at `$FFD5` recorded requests for `LA` through `LH` when the resident dispatcher at `$0CD1` received indices 1 through 8. The dragon code at `$1E0F` makes the additional `LI` request with selector 9.
- The staged scene number at `$8010` is compared with `$26` at `$0DBB`. A mismatch selects the embedded first scene at RAM `$D010`. When it matches, the file contents are staged at `$8010`. The copy loop at `$0DE8` reads through `$2A/$2B` with I/O banked away, restores I/O, and writes to `$1E00` through `$2C/$2D`. It includes the eleven bytes `END OF CODE`, compared against the table at `$1C40`. The shared caller at `$0CA2` or `$0CAC` begins execution at `$1E01`, one byte after the identifier.
- The graphics stream begins on the page after the marker. The decoder at `$0E37` takes literals unless the byte equals the selector-specific value from `$1CBA`. An escape consumes the repeated byte and a count. It clips the output against the exclusive limit `$7FFF`, or `$9FFF` for scene 8. A count of zero can perform 256 writes with the eight-bit countdown. The measured stream boundaries are in orientation.md.
- The second descent scans the embedded record again at `$1E16`. The stop at `$1E58` showed input `$E200` and output `$4000` in the two zero-page pointers. Stepping `LDA ($2A),Y` at `$0E3C` read `$54`, the escape byte. After the transformation loop at `$1E5D`, a stop at `$1E72` showed an exact match to first-descent entry RAM across `$4000–$7DFF`. There were 140 differences in the transformed `$7E00–$7FFF` pages. The first descent owns the common image and the second owns the transformed pages.
- At `$1E12` in the dragon scene, the 2030 bytes at `$9A00–$A1ED` match the `LI` file exactly. The retained `LH` bytes at `$A1EE–$BF0F` are sometimes read as raw data as well as staging for decompression. For example, `$22A9` copies 65 bytes from `$A9F9` to the sprite area at `$6800`, and `$21E7` takes the low nibbles of five bytes at `$B002–$B006`.

## Input and timing

- The initial castle picture takes fire on port 1. From the title snapshot, stepping the read at `$C053` returned `$EF` with port 1 fire and `$FF` with port 2 fire. The next two instructions advanced to `$C05A` with port 1 held and returned to `$C053` with port 2 held.
- The inter-scene prompt at `$0CF2` takes fire on port 2. Stepping its read and branch with port 1 pressed returned to `$0CF2` and with port 2 pressed advanced to `$0CF9`. The live port samples were `$7F` and `$6F` respectively. During gameplay the common routine at `$1592` writes `$FF` to CIA1 port A, latches the input at `$28` and restores `$7F`. Several rooms also read the port directly and invert the input before comparing exact masks.
- CIA2 timer A provides polling delays at `$15A5` and a separate NMI-counter wait at `$1625`. The latter compares `$156F` before and after the NMI handler at `$1566` increments it. The resident raster handler at `$1647` acknowledges VIC raster bit 0 and dispatches through `$42/$43`. The hallway changes these pointers between raster bands so hardware sprites 5–7 can represent different body pieces in a single frame.

## Graphics and text

- Attract uses the character screen at `$0400`. A store watchpoint there stopped with PC `$15F1` just after the `STA ($2A),Y` in the shared display-clear loop. Sprite pointers at `$07F8–$07FF` are also written by `$125F` as part of the interstitial setup.
- The first descent, Skull Hallway, Burning Ropes, Weapons Room, Ramps and Tentacle Room play captures show the `$4000` VIC bank in character mode with `$D018=$0F`, screen at `$4000` and glyphs from `$7800`. The board capture sets `$D018=$F1` in the same bank and uses bitmap mode, with bitmap at `$4000` and matrix at `$7C00`. The dragon capture uses `$D018=$81`, bitmap at `$4000` and matrix at `$6000`.
- The ten eight-byte score glyphs at `$0A60–$0AAF` render as digits 0 through 9. The copier at `$1880` with A equal to `$78` installs them at `$7D80`, corresponding to glyphs `$B0–$B9` of the scene character set. The game also holds PETSCII title and credit strings beginning at `$19E4`.
- The shared pose records begin at `$3200`. The Skull Hallway instructions at `$1E70–$1E75` copy 90 bytes to `$44–$9D` with X descending. At the first read, stepping the load with X=`$59` returned `$D0`. The selectors at `$2ABA` in that scene, `$2B34` in Weapons Room and `$2A61` in Tentacle Room use a stride of 90. The hallway raster handlers starting at `$2B2E` read sprite positions, colours, pointers and expansion masks from these zero-page records.

## Sound and code census

| Register or area | Evidence in the decoded code |
|---|---|
| `$D011/$D012/$D019/$D01A` | Screen blanking, raster target and interrupt handling at `$0EAE`, `$1570` and `$1647`. |
| `$DD00/$D018` | VIC bank and display memory selection at `$1E4E–$1E58` in the hallway and `$1E63–$1E81` in the dragon scene. |
| `$DC00/$DC01` | Port 2 fire at `$0CF2` and common joystick sampling at `$1592`. Port 1 fire at `$C053` in the castle title. |
| `$DC04` | The resident random seed at `$1732` reads CIA1 timer A low. Tentacle Room also reads it at `$2957` and XORs it with the raster count. |
| `$DD04/$DD05/$DD0D/$DD0E` | Polling and NMI timing at `$15A5` and `$1625`. |
| `$D400–$D41C` | SID setup clears this range at `$C1AC`. The player at `$C004` advances five logical channels using three physical SID voices. |
| `$C1CA–$CFDA` | Cue and pattern pointers, instrument settings, timed note data and the split frequency table. The interpreter at `$C0D3` uses a cue selector with bit 7 set, and then reads repeat-count and pattern-index pairs. Pattern bytes below `$80` are note indices followed by duration. The high-bit commands either select a five-byte instrument or end the pattern, according to bit 6. |

## Open

The documented Giddy Goons set piece has no confirmed mapping in this disk edition. The loader's request path for `LJ`, the complete roles of several data ranges and the effects of all action and failure branches remain open. The listing accuracy sample belongs to step 60 after coverage reaches the required total.
