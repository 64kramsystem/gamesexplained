# Turbo Charge — title and high scores

File `00-N0S` hands off at `$0F00`. `$0812` initializes the title, starts the music and compares the saved score. After fire, `$0860` pushes the synthetic return address `$68FF` and dispatches file 1. The loader’s RTS then transfers to `$6900`.
