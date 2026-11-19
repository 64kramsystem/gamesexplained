# Features

Source consulted on 19 November 2026: [The Trap Door – C64-Wiki](https://www.c64-wiki.com/wiki/The_Trap_Door).

| Status | Feature |
|---|---|
| traced | The mode tests at $39C2, $3D40 and $751C change cleanup eligibility, a score bonus and actor $9A99. Instruction traces confirmed the last gate. The final reward depends on further conditions. |
| confirmed | Default keys Q/A/Z/X and joystick port 2 enter the direction dispatcher. The mode and controls screens show the keyboard settings and a redefine option. Room transitions remain open. |
| traced | C and T dispatch to separate drop and tip handlers. The resulting object changes and the rules for pushing, carrying and levers remain open. |
| traced | The door stage and linked-object motion are traced at $8434 and $3BEA. $4121 and $4126 select the task hints. The creature rules remain open. The searches followed the door midpoint at $3CAE and the mode-dependent actor at $751C. |
| live | The anger update at $3A46 and its door-stage gate were checked with a store watch and instruction traces. The request list, delivery response selection and remaining-time score transfer are traced at $4685, $4A6B and $3D56. |
| open | The request records at $46A2 name worms, fried eggs, boiled slimies and eyeball crush. The flag pointer lookup at $4AAA and response parser at $4AC9 select preparation-dependent replies. The full preparation rules remain open. |
| open | The cleanup gate at $39C2 and the final-task response at $4A6B establish when cleanup and the wages message are selected. The connection to the safe and the effect of the weight’s drop height remain open. |
| traced | The controls screen installs the title music IRQ hook at $186E. The sequence and its $57 repeat event were traced. C64-Wiki credits David Dunn. |
