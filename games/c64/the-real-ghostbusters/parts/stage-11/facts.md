# LEVELK

The breakpoint at `$5613` caught the KERNAL LOAD return. All 5,703 payload bytes matched the disk file at `$6000`. At `$3302` after both expansion passes, the output pointer was `$C110`, one past the expanded range `$6000`–`$C10F`.

The engine reads the setup callback `$C011` from `$C002/$C003` before dispatch at `$1527`. It reads the update callback `$C0E2` from `$C00F/$C010` before dispatch at `$096F`. Both calls use the indirect jump at `$15EB`.
VICE single-stepped this setup path against the expanded snapshot. Successive PCs were `$1527 $15EB $C011 $C012 $C015 $C017 $C019`.

LEVELK is the congratulations screen. The breakpoint at `$C09F` reached
the display code after the three copies and VIC mode change. Two frames
later the picture showed the Ghostbusters headquarters and a
congratulations message. The source bitmap occupies `$9800–$B7FF`,
with screen and colour attributes at `$B800–$BBFF` and
`$BC00–$BFFF` respectively. The installed raster handler at `$C0E3`
ticks the resident sound driver. The input code at `$C09F–$C0C8`
waits for release, press and release.
