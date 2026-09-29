# Quad 606 — checks after work

Follow `../safety.md`. All powered checks on a 606 are for a competent restorer or qualified technician. Never connect loudspeakers until the output DC check passes.

| Check | Setup | Expected result | Source | Who |
|---|---|---|---|---|
| Visual: polarity of every electrolytic, no solder bridges, both sides of each board | Unpowered | Matches the other board and the service layout | Q606-S01 p9 | Restorer |
| Wiring continuity | Unpowered, ohmmeter | All wiring checked before mains is connected | Q606-S01 p6 | Restorer |
| Board bench test (optional, before or after recap) | Board on a lab dual supply (about +57 / −54 V), earth to the heatsink, not the input earth | About 110 mA in the − line and 120 mA in the + line | Q606-S01 p7 | Technician |
| Supply current per channel | Powered in the amplifier, no signal | 120–130 mA in each of the + and − lines | Q606-S01 p6 | Technician |
| Supply rails | Powered, no signal | Approximately 53–56 V DC each side | Q606-S02 p10 | Technician |
| Output DC offset | Powered, no signal, no load | Less than 0.01 V (typically 0.007 V or less) | Q606-S01 p6, p9 | Technician |
| Mains current | Powered, no signal | Typically 60 mA at 240 V; 120 mA at 120 V | Q606-S02 p10 | Technician |
| Output before clipping | Signal generator, scope, true-RMS meter, no load | 32–36 V AC (about 130–150 W into 8 Ω); input at clipping 0.775 V, 0.5 V or 1 V depending on R11 | Q606-S01 p9 | Technician |
| Input sensitivity (factory) | 8 Ω dummy load, 1 kHz, 140 W (33.46 V) | 0.5 V ± 0.5 dB input (factory R11); no instability at clipping | Q606-S02 p10 | Technician |
| Distortion (factory) | 8 Ω load, 130 W (32.25 V) | < 0.01 % at 100 Hz, 1 kHz, 3 kHz; < 0.03 % at 10 kHz, 20 kHz | Q606-S02 p10 | Technician with analyser |
| Frequency response (factory) | 8 Ω load, 130 W, ref. 1 kHz | 10 Hz −3 dB; 20 Hz −0.25 dB; 20 kHz −0.25 dB | Q606-S02 p10 | Technician |

The factory sensitivity figure applies to the original R11. If R11 was changed, use DADA's figure for that value instead.

## Stop conditions

- Supply current outside the figures above, a tripped breaker or blown fuse, smoke, a hot component, or output DC above 0.01 V: switch off at the wall and investigate before going further.
- DADA says fault-finding a board that fails these tests is beyond the scope of its guide (Q606-S01 p9); refer to a technician.

## Job record

- Unit / serial / case style / PCB issue:
- Date and restorer:
- Parts changed (with values), R11 choice:
- Supply currents, rails and output DC, each channel:
- Differences from the references:
