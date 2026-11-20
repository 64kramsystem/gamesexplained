# High scores

- $C42E loads the five-record H file into $C868. A checkpoint at the LOAD jump table confirmed destination $C868 and secondary address 0. $C44E saves the same 60 bytes under the replacement name @:H.
- $C36C converts the 16-bit score to decimal using four nibble-specific tables. $C3EE adds each table contribution into five decimal digits and carries across the digits in software.
- Execution reached the fire poll at $C231 after displaying the panel. Fire led to the LABLE LOAD call at $C921. The native entry preserves the title's result-border templates and supplies an identical copy of the loader block at $CA00–$CDFE.
