# Resident engine and title

The resident listing uses the cold-boot snapshot at $8A00. The game initialization at $1700 is present there and later becomes a tile workspace. The handover captures the original bytes of self-modifying instructions. During play the game patches, among others, $4004, $50AF, $50E1 and $51D4.

The even/odd stage requests at $5B5C and $5B67 return to $5B6A. The resident play loop at $29CF uses a JSR operand patched by the stage setup at $2EA4–$2EAD, so the active target is specific to the stage and section. The five targets seen in first-section play are $91EB, $8EB2, $8BB5, $8ED5 and $92FE.

During the stage-one weapon probe, actor and collision fields were read through the resident dispatch and overlap routines. The weapon icon update at $3F61 separately patches four weapon shapes' colours at $2399 through $23A2 and copies their X and Y extents from $3FAE and $3FC6. The selected source graphics page is copied to $FC00.
