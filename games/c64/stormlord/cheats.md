# Stormlord's title code

Type **NAUGHTYBOY** on the title screen to toggle the game's built-in infinite-lives flag. The title matcher at `$A9EF` walks the keyboard matrix indices at `$AA53`. The life-loss routine skips the decrement when `$AA5E` is set. The sequence and flag were traced in the listing.
