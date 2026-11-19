# Freddy Hardest (C64) facts

Two separate packed disk programs implement the surface and the base.
The base's access-code form compares five digits at its own `$0FFE`.
The [base facts](parts/base/facts.md) give the comparison and its
instruction watchpoint. The [surface facts](parts/surface/facts.md)
give its scroll format, IRQ phases and input trace.

Both render the small title font as VIC character codes and maintain an
in-memory SID register shadow during gameplay. The surface writes the
shadow from `$3B50` at `$C3F6`. The base writes it from `$3A49`
at `$AFB8`. Each copy writes 25 consecutive registers from `$D400`.
Both loads contain their own glyph and sprite banks. Their bytes
differ across corresponding regions. The title and gameplay
screen matrices, map cursor and IRQ vector addresses are local to each
part. See the respective part for their meanings.

The retained asset loaders at surface `$09C4` and base `$0960`
call KERNAL SETNAM and LOAD for named resources, including C.B, C.A and
PIC. Those names are missing from this input disk's directory. The
disk's three actual entries are accounted for in `media.json`.
The packed route above reaches gameplay without using those directory
names. The consumers for all retained data have not been established.

## The listing's error rate

The independent gpt-6.2-sol sample drew 60 of 412 comments with seed
1987 and found 13 wrong (21.7%, with a Wilson 95% interval of 13.1% to
33.6%). The checker may have missed other errors. The run corrected all
13 findings, which concerned routine boundaries, branch conditions,
copy lengths, sprite axes, glyph ranges and a generated-value routine.
Related corrections cover the corresponding base panel copy and the
paired sprite paths. A full audit followed by a fresh sample is pending.
