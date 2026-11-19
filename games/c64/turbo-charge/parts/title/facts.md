# Turbo Charge — title and high scores

File `00-N0S` hands off at `$0F00`. The code at `$0812` initializes the title, starts the music and compares the saved score. The dispatch at `$0860` defaults to file `$0D` with a synthetic return address of `$2FFF`. When the option at `$02A7` is set, the wrapper changes the file to `$01` and the synthetic return address to `$68FF`. The loader’s RTS then enters the driving startup at `$6900`, as observed on the title-to-drive route.

The initial bitmap uses VIC bank `$4000` with `$D018=$78`. The title’s character and sprite phase selects VIC bank `$C000` with `$D018=$34`. The loaded screen map starts at `$CC00` and the character set starts at `$D000`. Sprite pointers occupy `$CFF8–$CFFF`. The title message loop copies 36-byte records from `$098F`, with four rows of eight pointers followed by four horizontal offsets. The raster at `$0D51` copies eight pointers per row and updates its next raster line.
