# Test of Speed

- The instruction screen selects $A400 as its matrix and copies its custom font from $FA00. The scene uses a bitmap copied in part from $6000, and separately updates the water and suspended ball.
- The fire acceptance path is at $0A54. Joystick actions are sampled from CIA1 port A. The state machine at $1275 treats $C8 and $CC as control bytes for waiting or advancing with respect to the stored stick sample.
- The exit copies five pages from $EB00 to $C900 before jumping into the relocated loader. An execution checkpoint caught the subsequent KERNAL LOAD of file 3.
