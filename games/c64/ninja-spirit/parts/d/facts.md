# Disk load D

- `$2B15` dispatches two section initialisers. The first uses the wide map layout, and the other sets `$277E=$60` for 96-byte rows.
- At `$2923` the completion branch initialises a figure and advances its pose using `$2A72`. Later branches scroll a horizontal view with paired sprites and a vertical view using the 96-byte map stride.
- At handover, `$3A29–$3FFF` is identical to the corresponding copied C map segment at `$56A9–$5C7F`. The local probe recorded no CPU reads or writes to the copy beyond `$3A28`, the ending animation counter.
