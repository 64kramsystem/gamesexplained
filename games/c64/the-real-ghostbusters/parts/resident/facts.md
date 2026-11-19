# Facts

These are orientation observations. Step 60 verification depends on closing
the Step 50 coverage ledger.

- The OUG intro checks control port 1 fire by comparing a read of `$DC01`
  with `$EF` at `$2065`. The next jump on equality is to `$3502`.
- The first stage uses the disk filename `LEVELA`. The observed KERNAL LOAD
  return stack leads to `$3367`, and `$BB/$BC` pointed to the filename at
  `$3387` while the serial receive code ran.
- In the saved Stage 1 state the RAM hardware interrupt vector points to
  `$0C31`. The processor port is `$35`; the handler writes `$01` to
  `$D019` and reads `$DC0D`.

The resident hand-over was captured with a stopping breakpoint at
`$0820` after the trainer became visible. The first instruction is
`LDA $D011`. A hit at the same address during unpacking executes
`LDA $AC`, which identifies the earlier wrapper state.

The display writes primarily use `$D011–$D019`, the sprite
position and colour registers, and the three background registers.
Stage IRQs program the video mode through `$D011/$D016` and the
screen and character bases through `$D018`. The CIA1 port accesses at
`$18EF/$18FF` sample controls. Sound code uses the SID voice and
envelope registers, including the voice 1 frequency pair at
`$D400/$D401` from `$F11A/$F120`. The per-instruction census is in
the game's ignored `work/census.txt`.
