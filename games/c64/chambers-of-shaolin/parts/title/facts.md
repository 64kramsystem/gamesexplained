# Title and apprentice form

- The picture selector at $C5A4 reads bitmap addresses $4000, $6400 and $8800 and screen-colour matrices $6000, $8400 and $A800. The destination bitmap at $2000 matches the publisher source at hand-over. The game writes it again before enabling the VIC-II bitmap display.
- Port-2 fire accepts the title images. The form uses matrix codes, and a checkpoint caught the one-apprentice branch at $C33C. A complete name transfers to $CE03 and the LOAD call at $C9DA requests file 1.
- The IRQ vector $C500 alternates raster compares and serves the title tune. Music command and instrument tables remain open.
