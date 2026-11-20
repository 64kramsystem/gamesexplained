# High scores

- $C42E loads the five-record H file into $C868. A checkpoint at the LOAD jump table confirmed destination $C868 and secondary address 0. $C44E saves the same 60 bytes under the replacement name @:H.
- $C36C converts the 16-bit score to decimal using four nibble-specific tables. $C3EE adds each table contribution into five decimal digits and carries across the digits in software.
- Execution reached the fire poll at $C231 after displaying the panel. Fire led to the LABLE LOAD call at $C921. The native entry preserves the title's result-border templates and supplies an identical copy of the loader block at $CA00–$CDFE.
- The decimal formatter stores its four nibble lookup offsets at $C860–$C863. Across the five records, the live watches counted 20 stores and 20 reads there. With a top-score insertion, the copy at $C29A also read ten bytes after the five records and wrote through $C8B9. The save end remains $C8A4.
- The three score tune tracks begin at $E824, $E831 and $E867. Track bytes select entries in the phrase directory at $E729. A $FF track command takes its next address from the following two bytes. Instrument data drives separate waveform, pulse and control sequences.
- The score program accesses the KERNAL ROM in the same address window as the tail of the song data. Stopping on a live hit in $EAD5–$EFFF caught execution at $ED0C and a read by $C252 at processor port $36. In the instruction trace of the RAM-mapped tune player, the highest data read was $EAD4. Phrase directory slot 15 points to the zero byte at $EAD5.
