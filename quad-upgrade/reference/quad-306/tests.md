# Quad 306 — checks after work

Follow `../safety.md`. All powered checks are for a competent restorer or qualified technician. DADA says no calibration is needed on this current-dumping design (Q306-S01 p6). Never connect loudspeakers until the output DC check passes.

| Check | Setup | Expected result | Source | Who |
|---|---|---|---|---|
| Visual: polarity of C7, C10, C11; decoupling caps on the copper side; zeners still fitted; terminals Red–Black–Black–Red | Unpowered | As described | Q306-S01 p4–5 | Restorer |
| Mains current | 240 V, no signal | Typically 60 mA (120 mA at 120 V) | Q306-S02 p8 | Technician |
| Supply rails | No signal | Quad: approximately 36–41 V DC each side. DADA: +40 V and −38 V. | Q306-S02 p8; Q306-S01 p6 | Technician |
| Output DC | No signal, no load | 0.01 V or less | Q306-S01 p6 | Technician |
| Output before clipping | One channel driven, 8 Ω, 240 V mains | Around 20 V AC (50 W into 8 Ω). The trip will operate after 10–20 s at full power; that is normal — switch off and reset. | Q306-S01 p6 | Technician |
| Input sensitivity | 8 Ω, 1 kHz, 50 W (20 V) | Factory 0.375 V ± 0.5 dB, or the value chosen with R13; no instability at clipping | Q306-S02 p8; Q306-S01 p6 | Technician |
| Distortion (factory) | 8 Ω, 50 W | < 0.01 % at 100 Hz, 1 kHz, 3 kHz; < 0.03 % at 10 kHz, 20 kHz | Q306-S02 p8 | Technician with analyser |
| Frequency response (factory) | 8 Ω, 50 W, ref. 1 kHz | 10 Hz −2.5 dB; 20 Hz −0.25 dB; 20 kHz −0.25 dB | Q306-S02 p8 | Technician |

## Stop conditions

- Smoke, heat, a tripped breaker at low level, rails far outside 36–41 V, or output DC above 0.01 V: switch off at the wall and investigate.
- Output transistor paint spots turned purple: thermal problem (Q306-S02 p10).

## Job record

- Unit / serial / PCB issue:
- Date and restorer:
- Parts changed, R13 choice, reservoir capacitor value:
- Rails and output DC, each channel:
- Differences from the references:
