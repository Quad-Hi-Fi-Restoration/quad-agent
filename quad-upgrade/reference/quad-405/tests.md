# Quad 405 — checks after work

Follow `../safety.md`. All powered checks on a 405 are for a competent restorer or qualified technician. Never connect loudspeakers until the output DC check passes.

| Check | Setup | Expected result | Source | Who |
|---|---|---|---|---|
| Visual: polarity of every electrolytic and diode, no solder bridges, both sides of each board | Unpowered | Matches the other board and the appendix photos | Q405-S01 p7, p11 | Restorer |
| Wiring continuity and terminal insulation | Unpowered, ohmmeter | All wiring checked; hot terminals isolated from chassis | Q405-S01 p8, p10 | Restorer |
| Board bench test (optional) | Board on a lab ±50 V supply, earth to heatsink, not the input earth | About 110 mA in the − line and 80 mA in the + line | Q405-S01 p5 | Technician |
| Supply rails | Before connecting the boards | About ±50 V DC | Q405-S01 p9 | Technician |
| Supply current per channel | Powered, no signal | DADA p10: about 120 mA in the + line and 80 mA in the − line — **this contradicts its own p5 figures above**; record both lines and do not judge from one figure | Q405-S01 p5, p10 | Technician |
| Mains current | 240 V, no signal | Should not exceed 0.12 A | Q405-S02 p5 | Technician |
| Output DC offset | Powered, no signal, no load | DADA gives "max 0.01 V" (p7) and "less than 0.1 V, typically 0.01 V" (p10). Treat above 0.01 V as needing investigation. | Q405-S01 p7, p10 | Technician |
| Output before clipping | Lab supply, generator, scope, true-RMS meter | 30–32 V AC (about 110–125 W into 8 Ω); input at clipping 1.5 V, 0.775 V or 0.5 V depending on sensitivity chosen | Q405-S01 p7 | Technician |
| Input sensitivity (factory) | 8 Ω load, 1 kHz | 0.5 V ± 0.5 dB gives 100 W with no clipping | Q405-S02 p5 | Technician |
| Distortion (factory) | 8 Ω, 100 W | < 0.01 % at 1 kHz, 100 Hz, 3 kHz; < 0.05 % at 10 kHz; < 0.1 % at 20 kHz and 80 W | Q405-S02 p5 | Technician with analyser |
| Low-frequency response (factory) | 8 Ω, 100 W, ref. 1 kHz | −0.3 dB at 30 Hz; −1 dB at 20 Hz; −7 ± 1.5 dB at 10 Hz | Q405-S02 p5 | Technician |
| 4 Ω output | 4 Ω load, 1 kHz | About 70 W just before clipping | Q405-S02 p5 | Technician |
| Noise | Input loaded with 1 kΩ | Better than −93 dB unweighted | Q405-S02 p5 | Technician |
| Clamp circuit | Clamp disconnected, 6 V DC applied | Current not over 0.5 mA each polarity; about 1 A with 12 V through 10 Ω | Q405-S02 p4–5 | Technician |

The factory sensitivity figure applies only if R4, R6 and C4 were left as fitted.

## Stop conditions

- Smoke, a hot component, blown fuse, supply currents far from the figures above, or output DC above 0.01 V: switch off at the wall and investigate.
- DADA recommends checking the finished amplifier's total standby supply current is 200–300 mA maximum (Q405-S01 p7).

## Job record

- Unit / serial / nameplate / board number and issue:
- Date and restorer:
- Parts changed (with values), sensitivity chosen, clamp kept or replaced:
- Supply currents, rails and output DC, each channel:
- Differences from the references:
