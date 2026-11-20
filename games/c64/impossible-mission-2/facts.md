# Impossible Mission II facts

This analysis uses the PAL tape edition. The five part folders carry the annotated listings and their own evidence. The entry routes and file provenance are in [orientation.md](orientation.md).

## Loading and ownership

- VICE stopped at $0880 on the title loader's JMP from $ACFD. The body of tape record 490 matched all 39,840 bytes from $0880 through $A41F. It includes the engine and its resident data.
- The opening tape requests were observed at execution checkpoints on $37A2. X was $05 for record 000 into $A500, $0A for record 130 into $A520, and $28 for record 328 into $F000. The live bytes of each five-byte record were read at the checkpoint.
- $399F builds the first tower record number by multiplying $86BA by 16. $2C2A builds the second by multiplying the same value by 16 and adding 130. $39AE uses a $01E0-byte template stride and copies $01A9 bytes before decoding a room record. $2202–$2204 requests the special record 128 via $2C42, which doubles $40 to get the file number.
- A controlled request for record 315 copied 3,072 bytes to $F400–$FFFF, ending with the store at $6232. The copy includes the agent sprite groups and the timer-driven speech driver at $F880–$FB05. The [scene resource facts](parts/scene-resource/facts.md) give the instruction checkpoints and store watches.
- The title, final sequence and scoreboard contain code that occupies addresses used for other purposes in the engine image. Their listings use snapshots of those actual loaded states. The final sequence swaps one compressed image for another at $A800 while retaining the same code at $7800.

## Opening elevator

- The processor uses RAM interrupt vectors. The live IRQ vector is $2F86. The handler saves A, X and Y, then dispatches through a writable JMP at $2F8B. $2FC4 selects the next target from the split pointer tables at $368C and $3694.
- The elevator alternates $C6 and $C4 on $D018. VICE store watchpoints stopped immediately after $2F08 and $2F32 respectively. In VIC bank $C000 both values select screen $F000. The former selects character RAM at $D800 for the scene and the latter selects $D000 for the pocket computer.
- Port 2 left changes the value returned by the CIA1 port A read at $336C from $7F to $7B. Three read watchpoints tripped after the same instruction in each trial. $336F ANDs that value with port B, and $3372–$3379 builds and stores the positive five-bit mask.
- The lower panel uses a private numeric display. In the character set at $D000 the colon is $08, digits one through nine use $09–$11, and zero is $12. This follows from rendering the eight-byte glyphs. The resume prompt at $0AAA and $0ABF uses ordinary C64 screen codes instead.

## Register use supported by instructions

| Register | Access and purpose |
|---|---|
| $01 | $2D90 selects RAM with I/O visible at engine entry. $7971 and $798A around the final bitmap copy switch I/O out and back. |
| $D012 | $2F9F programs the next interrupt line from the raster table. $47B7 reads the live raster low byte for its 9-bit comparison. |
| $D018 | $2F08 and $2F32 select two character sets during the elevator frame. |
| $D019/$D01A | $2E98 disables the VIC interrupt sources and acknowledges pending flags. $2FA2–$2FA5 acknowledges within the IRQ. |
| $D022/$D023 | $2F0E/$2F14 apply scene colours. $2F37/$2F3C apply the panel's fixed colours 6 and 14. |
| $D418 | $AFE6 calls the title SID driver through $1004. The sampled-speech path at $A588 uses the same register for volume playback. |
| $DC00/$DC01 | $336C–$3374 reads and combines the two joystick ports. |
| $DD00 | $2EAD selects VIC bank $C000 by clearing its two low bits. |
| $DD0D/$DD0F | $A971 sets up CIA2 timer B for speech playback and enables its timer interrupt. |

The complete mechanical register census and string sweep are in ignored `work/census.txt` and `work/strings.txt`. Unattributed accesses are still open.

## The listing's error rate

An independent gpt-6.2-sol checker sampled 60 of 1,890 comments using seed 1120. Six of 60 had incorrect details, an estimated 10.0% with a 95% Wilson interval of 4.7% to 20.1%. The checker may have missed errors. The six findings concerned the melody panel's colour override and row count, the redraw column stride, actor state selection, an indexed actor coordinate, a repeated wall tile motif and an alternate title pitch path. All six comments were corrected, along with related actor coordinate and movement comments. The sample describes the listing before these edits.
