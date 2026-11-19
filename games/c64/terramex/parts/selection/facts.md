# Explorer selection

## Display and input

A fixed RAM hardware IRQ vector `$FFFE–$FFFF` points to `$5C45`. The routine switches I/O in, acknowledges the raster source and selects one of two internal branches through a writable displacement at `$5C6E`. At `$5C7E` it selects VIC bank `$4000`, screen matrix `$5400`, and character table `$4800`. It places sprite 0 with both position biases set to `$38`, and points it at `$4FC0`. The phase also writes the input flag at `$82` and schedules line `$B5`. The other phase switches the glyph address to `$5000` and schedules raster 1. CIA2 selects the video bank and CIA1 supplies both joystick reads and keyboard scanning. The install routine at `$5D04` clears CIA timer start bits.

The control reader at `$5B3C` checks active-low bits at `$DC01` first and `$DC00` second. Table `$5BAE` maps physical inputs to bit 0 right, bit 1 left, bit 2 down, bit 3 up and bit 4 fire. The program falls back to its keyboard matrix scanner at `$5C02` when both stick inputs are idle.

`$5A00` moves the cursor by two units per accepted axis update and uses the coordinate pairs below. The bounds are in cursor coordinates, before the hardware position bias, and the tests run in this order.

| Portrait ID | Explorer | X | Y |
|---|---|---|---|
| 0 | Fortisque-Smithe | `$4C–$90` | below `$4D` |
| 1 | Herr Krusche | at least `$BC` | `$0C–$56` |
| 2 | Henri Beaucoup | `$B0–$DA` | `$6E–$A8` |
| 3 | Big John Caine | below `$36` | `$3C–$7C` |
| 4 | Wu Pong | `$52–$7E` | at least `$86` |

The fallback corner rectangle can return `$FE`. A miss returns `$FF`. Fire with either of these IDs stays in the selection loop at `$59C5`.

## Sprite handoff

Selector `$5B02` contains the five source addresses `$6840`, `$7800`, `$87C0`, `$9780` and `$A740`. The selection transfer at `$5B0C` copies 15 pages plus 192 bytes from the selected source. Each block has 64 frames of 63 bytes. The expedition's decoder shows the frame format consists of three 21-byte columns of four packed multicolour pixels per byte.

Selector `$D000–$DFFF` at handoff matches `$19C1–$29C0` byte for byte. The relocated packed windows in high RAM also match low RAM and the disk file with a shift of `$B63F` between the two RAM locations. The selector's I/O accesses and explorer-source pointers are accounted for separately. The remaining 79 bytes at `$5843–$5891` have no identified consumer in the selector's decoded flow.

## Live instruction and store checks

Two 25-frame probes started from the same snapshot. Both counted 49 IRQ entries at `$5C45`, 24 port-2 scan entries at `$5B58` and 24 stores to `$0300`. With up held there were 24 executions at `$5A41` and 48 stores to cursor Y at `$5B01`. Y changed from 80 to 32 and the hit ID changed from 255 to 0. The idle control had zero executions and stores on that movement path, and its Y and hit ID stayed at 80 and 255.
