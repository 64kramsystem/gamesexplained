# Title and resident code

The title-entry snapshot stops at `$2E68`. The module header at `$2E64` contains the relocated entry and the size `$055A`. Entry code clears the input latch at `$46` and installs a title IRQ from the vector word at `$31D9`. The IRQ restores the processor port when returning to the interrupted code.

The first disk's named DM program loads at `$0800`. Its jump table provides services which also remain available to later modules. `$0800` resolves module IDs, `$0806` releases them, and `$081E` calls a module's relocated entry. The drive byte loop at `$0B6B` and the logical sector transfer at `$192B` are in the same resident body.

The music control entry at `$6400` and music tick at `$6403` dispatch into the same routine family. The title exit at `$31BC` queues the stop using Y equal to `$FF` and restores the prior interrupt vector. The register writes for the full tune are open.
