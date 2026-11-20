# Shinobi analysis log

- The X-Large release's serial transfers took longer than the first screenshot interval. The watch on the buffer store distinguished a live read from a loop waiting indefinitely on the drive.
- The first forced mission captures re-entered the cold-start code and reached screen data where the cold-start code expected setup instructions. The replacement captures enter the resident mission transition at `$B008`. Stopping at its return instruction and entering the player initializer produced playable first-stage snapshots for missions 2–5.
- VICE's native executed-address map gave 1,698 instruction starts during a short Mission 1 sample. The workspace contains the captured map and the separate seed augmented with known engine entry points.
- A store checkpoint at `$4C00` stopped with PC `$1880`, after the cell renderer's store through the second screen pointer at `$187E`. The difference in this range between initial and later mission snapshots is a screen write.
