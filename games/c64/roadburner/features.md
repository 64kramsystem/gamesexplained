# Roadburner features

[Edicola 8 Bit](https://www.edicola8bit.com/gioco?id=1060) documents the Italian release as Speedy and links the Roadburner PRG used for this analysis. Its title and road screenshots are in `reference/`. Title credits, the trainer, live VICE frames and the ROM-free hand-over supplied the game evidence.

| Feature | Status | Evidence |
|---|---|---|
| Title credits, star field and start | confirmed | `$7D00`, `$8265` and messages at `$84A3–$85E9`. Port 2 fire reached `$7E4E`. GET READY appears before play. |
| Four horizontal courses | confirmed | Descriptors `$1F64–$1F93`. The four tracks ran through their opening under the original initialization routines. See the road and track screenshots. |
| Road, buildings and traffic | confirmed | Tile-strip staging at `$1008/$495D`, eight sprite slots, and the `$17AF` traffic event loader. |
| Steering and shot | confirmed | `$4CFD` reads port 2. With up and right held at the instruction trace, X was one and Y was `$FF` before writing the delta bytes. Fire decremented ammo and entered the slot-seven script call with Y=6. |
| Gas, secondary gauge, ammunition and lives | confirmed | Dashboard visible during play. `$1BB0/$1C33` feed the gauges. `$1B87` and `$0F60` change ammunition and lives under the corresponding conditions. |
| Scoring and high score | confirmed | `$0FBC` requests a score update. `$1DB8/$1DDC` carry through the live digit fields, and `$1E55` updates the high score. The small-increment path was observed at `$1DB8/$1E15`. |
| Terrain and sprite contacts | traced | `$4D1E/$1CC4` sample and classify terrain. `$0ECD/$4C6B` combine the sprite latch and coordinates. |
| Remaining cars, interlude and ending | traced | `$0F60` tests remaining cars, `$0FBD` advances the descriptor, and `$1F06`, `$1EB6` and `$1EDE` draw the relevant title-font messages. |
| Title music and driving effects | traced | SID driver at `$5000` for title music and `$9028` for road effects. Instruction stops verified the mode-four oscillator read and its high frequency store for effect 1. Audible output and oscillator variation remain open with dummy audio. |
