# Live and Let Die — features

- [Domark manual transcription](https://www.mi6-hq.com/sections/games/lald?s=articles&t=), read 20 November 2026. The manual covers five machine families. Its C64 control section names a joystick, Run/Stop and Return.
- [C64 longplay chapters](https://www.youtube.com/watch?v=WdpLXFMg3ec), consulted 20 November 2026.
- [Fantasy disk release](https://csdb.dk/release/?id=42805), analysed on PAL VICE. The title, briefing and four running courses appear in `reference/`.

| Feature | Status | Evidence |
| --- | --- | --- |
| Select Practice, North Pole, Sahara or New Orleans | confirmed | `$0D34–$0DA3`, course index at `$033A`, all four course captures |
| Practice shooting at red and black targets | live | Practice start screen labels red and black target counts. The briefing assigns cannon and missiles respectively. The scoring rules are open. |
| Steer with joystick, accelerate and decelerate | confirmed | Up branch read traced at `$AE9C`; Down handling at `$AEB3`. Steering routines traced from `$30B9`. |
| Shoot the cannon and launch missiles | confirmed | Fire branch at `$9E00`. The Down and Fire input was traced into the missile path at `$9E43–$9E56`. |
| Pause with Run/Stop and abort with Return | live | Keyboard read at `$1567`, release and press logic at `$158A–$15E3`. Instruction stepping on the same running snapshot read zero pressed bits for no key, then reached the pause increment at `$15D9` with Run/Stop and the abort store at `$15C7` with Return. |
| Pick up fuel barrels and helicopter supplies | traced in part | `$F84B` refills fuel on contact and `$C0B9` advances a falling supply sprite. The mission events supplying each type are open. |
| Avoid mines, aircraft, enemy boats, booby-trapped supplies and other hazards | open | The section operations trace to projected slots through `$1FFB` and `$2443`. The mapping from those slots to all manual hazard names is open. |
| Traverse tunnels and slopes, and use missiles against closed gates | traced in part | Tunnel approaches at `$FBF2` and `$FC2B` lead to contact checks. The missile overlap path at `$BF93` resolves a special-sprite hit. The mapping to closed gates and the manual’s complete slope behaviour remain open. |
| Destroy Kananga's processing plant in New Orleans | open | The scroll text at `$B600` names the plant. The course-event dispatcher at `$1FFB` has a completion operation, but the plant’s object and contact path are open. |
| Report mission result, score and rating | traced | Display messages from `$CCE0`, ranking comparison and insertion at `$B2F2`. |
