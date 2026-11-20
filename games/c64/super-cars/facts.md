# Super Cars analysis

This record covers the Airwolf-Team +7 C64 image with the seven race options disabled and the trainer's £20,000 default. Addresses refer to RAM from `work/entry.vsf` unless noted. The source maps and descriptors are resident in that snapshot.

## Track data and scrolling

- The nine little-endian pointers at $9C40 select nine 308-byte tile maps. $0BD4 walks 14 rows of 22 indices. $0C2C multiplies each index by 16 to find the four-by-four character pattern at $9440 and scatters it into the 88-by-56 character map at $8100. On entry to Track 1, an execute counter on $0C57 measured exactly 4,928 writes and store watches on $8100 and $943F each hit once.
- A separate nine-pointer directory at $7F8D selects a 47-byte race descriptor. Track 4's descriptor and lists are at $E766 under the KERNAL. $1F28 reads the first four bytes as coarse camera origin and limits. $1F72 reads seven start positions as little-endian X/Y words plus start heading, checkpoint and target settings. The last eight bytes give four little-endian pointers.
- In descriptor order, the four lists hold nine-byte covered-region records read at $3D0E, twelve-byte checkpoint rectangles read at $3D57, three-byte marker instructions read at $2108 and four-byte class-gated character replacements read at $20B8. Every list's terminator was found at its record stride on all nine tracks. The region flag affects sprite priority and whether a pair of cars can collide at $3BC1. The checkpoint command $FF increments lap when the car's progress equals the required checkpoint.
- $0B22 limits camera motion toward the player to three pixels per axis. $0ABD applies fine scroll. A character boundary crossing changes the coarse coordinates and requests a viewport update. $0C7C builds the visible character screen at $4400 from the expanded map.
- An independent reconstruction of the Track 1 expansion from the 308 indices and sixteen-character patterns matched 4,903 of the 4,928 race snapshot bytes. The initialiser also runs the explicit marker and character-replacement passes. The expanded destination is working RAM and its packed inputs are counted in the listing.

## Input, simulation and race outcome

- $054B changes CIA1 port A to input, reads $DC00 and stores the raw bits to $0F. A stop at $0553, before the store, returned A=$FF on neutral and $EF, $FB, $F7, $FE and $FD on fire, left, right, up and down respectively. Each stop started from the same race snapshot.
- $2170 inverts the lower five control bits. The car's movement checks the fire bit at $26A1 and the turn bits at $26DA and $26E8. $24D6 saves the old coordinates and heading, computes signed 24-bit movement from speed and the 16-direction table at $2DEF, then applies collision checks. $3E86 constructs the same controls from a rival's heading and target and calls the movement routine.
- $2388 and $23A7 handle up and down. A missile needs a purchased item and a free slot. Launch consumes the item and sets object slot seven up in $23C8. A rear launch adds eight to the 16-direction heading. $2450 advances the projectile and explosion state.
- The race pause routine at $1C8C waits for the Space sample at $EC to toggle and gates audio during the wait. $1CAC obtains Space from bit four of the selected keyboard row $7F. $1E01 checks the same row, bit six, for Q and requests race exit.
- The initial Track 1 field is four cars and the lap target shown is five. $1D74 counts active rivals whose lap and checkpoint pair is at least the player’s, and puts their indices in slot order. $1D35 returns carry when the player or three rivals have met the completion test. $1DD3 checks fuel, engine, body and tyres in that order against four and selects the message for the first condition below the threshold. The display order is engine, body, fuel and tyres.
- Surface type five can start a spin at speed $3C or higher. Surface type six subtracts $27 when speed is at least $28. These thresholds and results come from $397F. The material names for those two codes remain open.

## Menu, sales and garage

- $0E4F runs the sales-office dispatch. Fire activates a hit box from the table selected at $07C7. Each hit record is row, left bound, right bound and result code, and ends on a first byte of $FF. For a negative track option the low seven bits give the track index.
- The driver-name prompt runs the game's own CIA scan at $0556. $16A4 accepts letters, spaces, Delete and Return with a limit of seven characters, and joystick fire can finish the prompt. The hand-over started with £20,000, encoded as six digits in $049A.
- $772F contains LOADED, HARVEY, ELLA and FONDLE. $15A1 compares all four names. The first three dispatch to cash or class setup, while the fourth sets $0202. The garage purchase loop reads this flag before processing action two.
- $180A runs purchases, availability and cash checks. $1ACE makes twelve prices from packed decimal seeds and a sampled adjustment table. The car sales sequence uses seven 34-byte variant records, grouped in the on-screen specs as Taraco Neoroder, Vaug Interceptor and Retron Parsec Turbo. $1316 computes trade-in from current car and condition, and $127C applies the new balance if affordable.
- The sales dialogue at $7532 explicitly says negotiation is unavailable. The race and garage have separate graphic and text planes. $04AB reads two consecutive 1,000-byte planes and banks I/O out for RAM reads. $04FE swaps 2 KB at a time between an active character set and retained picture glyphs.

## Character encoding and graphics

The glyph sheet rendered from $4800 shows screen-code letters $01–$1A and digits $30–$39. The text font pairs $1C with £ and uses $20 for a blank. The high bit selects alternate/inverse glyph designs for the menu and HUD. Game text at $7532 includes row delimiters $00 and terminators $FF, interpreted by $105E. Name input uses the separate keyboard-position table at $FE6F before converting letters to glyph indices. The separate sixteen-glyph hexadecimal font at $8008 has matching bytes in the Airwolf and Silicon builds. It starts on the final byte of the CBM80 signature. The Airwolf vectors at $8000 point to the cracker-specific reset shim at $6E9F. The hand cursor and menu upgrade lettering are stored as sprites, as are the car directions and missile graphics. The local sheets are `work/glyphs.png` and `work/shapes.png`.

## Hardware and sound

| Registers | Observed use | Code |
|---|---|---|
| $01 | $35 in the race exposes VIC and CIA registers and selects RAM at the high vectors. $04AB and $04FE access artwork in RAM under I/O. | $06B6, $04AB, $04FE |
| $D011, $D012, $D016, $D018, $D019 | Split the HUD and scrolling playfield, update fine scroll, choose character/screen bases and acknowledge interrupts. | $06B6, $0A24, $0A77 |
| $D000–$D010, $D015, $D01B, $D027–$D02E | Publish positions, enable/priority bits and colours for the visible sprites. | $21E2, $2275, $22B1 |
| $DD00, $DD02 | Select VIC bank $4000 and configure its two bank bits as outputs. | $0661–$0670 |
| $DC00–$DC03, $DC0D and $DC0E | Read controller and keyboard, configure port direction and drive the timer source used by camera updates. | $054B, $0556, $0A16, $0A77 |
| $D400–$D418 | SID voices, envelopes, volume and effects. $EC7F advances the sequence player, while $FE02 controls the race sound and feeds the engine pitch. | $EC7F, $F3A4, $FE02 |

Two ten-frame race windows each counted 30 entries at $06B6, ten executions each of $0A24 and $0A77, ten reads from $DC00, and twenty stores each to $D012, $D018 and both callback operand bytes. The first window was neutral and the next held fire. The RAM IRQ vector stayed at $06B6. The SID data directory contains three voice-order pointers per sequence at $FC36 and thirty pattern pointers split across $FBFA and $FC18.

## Targeted live checks

- Restoring the same post-countdown race snapshot for each of two 12-frame windows produced 36 IRQ entries and 12 calls of the player control routine in both. Neutral took the player acceleration store at $26B9 zero times and left speed at $00. Held fire hit it eleven times and left speed at $21.
- A five-frame Space press hit $1CC7 five times and the pause branch at $1C94 once. Release and another five-frame Space press reached the resume store at $1CA6 once. The IRQ control continued counting during both attempts.
- Eight frames with Q held hit the pressed branch at $1E19 and the transition at $1C78 once each. The IRQ control counted 20 entries and the KERNAL LOAD checkpoint stayed at zero.
- The disk directory contains one live named PRG. The eight extra sectors are two orphan BASIC chains. Searches across the exported code for $FFB1, $FFBA, $FFBD, $FFC0 and $FFD5 found no resident references. CIA2 port A and its direction register are accessed at $0661–$0670 for VIC bank selection.

## The listing's error rate

Seed 2064 selected 60 of 813 comments. The independent gpt-6.2-sol checker found nine wrong details, an estimated 15.0% with a 95% Wilson interval of 8.1% to 26.1%. The nine sampled comments and related descriptions were corrected. The errors covered rival ordering, class-independent artwork overlays, duplicate finish records, SID order dispatch and the events in two SID patterns, plus the meaning of the waveform/control effect fields. The checker may have missed errors. The sample measures the listing before those corrections.
