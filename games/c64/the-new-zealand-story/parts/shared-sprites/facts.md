# Shared disk sprite variants

DR reloads sprite slots $E0 through $FE after the regular package sequence. Only three bytes differ from the boot image. Slot $FC row 19 gets $AF in its middle byte. Slot $FE row 11 gets $00 in its last byte and row 13 gets $1E in its first byte.
