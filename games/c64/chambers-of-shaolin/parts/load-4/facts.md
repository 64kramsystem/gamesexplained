# Combat

- The introductory text accepts port-2 fire through $EC4C and $EC62. Independent entry produced a mountain backdrop and two fighters. It omitted the training results and therefore does not establish the observed default score and hit values for ordinary play.
- The routine at $1E9E decodes four background streams identified by instruction tracing. Its first stream begins at $D000 and is read with the chips banked out. All four decode to the same display ranges.
- The transition at $C300 restores the ROM mapping and requests HIGH. Its call at $C326 reached the KERNAL LOAD entry, and the new program ran from $C200.
- The first 82 fighter bitmap records are contiguous. Their two-byte dimensions predict each next pointer at $8000. The succeeding entry starts at $C254 with dimensions spanning $C300, where the disk-exit routine lives. The listing leaves this overlap open pending a trace of which frame indices the fight selects.
