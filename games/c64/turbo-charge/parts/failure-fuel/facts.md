# Turbo Charge — Out of fuel

File `0C-N0S` leaves the image at `$0800–$2F3F`. At `$A6CF`, the engine copies colour RAM from `$0800` to `$D800`, screen attributes from `$0C00` to `$6000`, and bitmap bytes from `$1000` to `$4000`. The display uses multicolour bitmap mode with VIC bank `$4000` and `$D018=$80`. The bitmap copy also transfers the tail of the final page from the prior driving image past the 8,000 bytes displayed.
