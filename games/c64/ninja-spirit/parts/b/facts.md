# Disk load B

- The loader entered this part at `$2780` after the two measured decompression packets. The first gameplay view shows a forest section.
- `$2963` dispatches the timer and camera setup using the four-section index at `$3FE9`. `$2A03` dispatches the matching colour setup. The round-cleared banner and file C transition are at `$2954`.
- The placement scanner reads two section-bound tables at `$2BA9` and `$2BAD`. The coordinate and work ranges lead to 35 handler pointers at `$2C3E`.
- `$3FBF` samples the map above the player before deciding whether tile attribute 3 should push the player down or trigger the death path.
