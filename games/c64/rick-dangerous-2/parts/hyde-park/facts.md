# Level load

The streamed disk depacker writes $8A00–$BFFF and $D800–$EFFF. The second span begins under the I/O registers, which are banked out during the corresponding stores. The loader returns at $7CF4. The use and format of each subrange remain open.
