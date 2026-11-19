# Fusion trainer

Answer N for all three prompts to reproduce the analysis. The Y paths in the trainer write opcode `$AD` over a three-byte `DEC abs`, replacing it with `LDA abs` on the same address.

| Prompt | Trainer store | Decrement affected |
|---|---|---|
| Unlimited lives | `$072D` | `$0F60` decrements remaining cars at `$1C98`. |
| Unlimited bullets | `$073F` | `$1B87` decrements ammunition at `$1C99`. |
| Unlimited gas | `$0751` | `$1C40` decrements the gas gauge index at `$1C52`. |
