# Quad 44 — checks after work

Follow `../safety.md`. Powered checks inside the unit are for a competent restorer or qualified technician. DADA says no calibration is necessary; a scope and signal generator allow the output voltage and input sensitivity to be checked, but are optional (Q44-S01 p4).

| Check | Setup | Expected result | Source | Who |
|---|---|---|---|---|
| Visual: capacitor polarity and op-amp pin 1 match your notes; 4.7 µF fitted with correct polarity | Unpowered | As recorded before removal | Q44-S01 p4, p6 | Restorer |
| Supply rails | Powered | ±15 V nominal (block diagram). No tolerance given in the pages read; record the figure. | Q44-S02 p9 | Technician |
| Input switching | Powered, each input button | Each input selects cleanly and stays selected | Q44-S02 p45 | Owner, after the technician's checks |
| Input selector and monitor | Signal generator into each input; aux at 500 mV; disc at 3 mV via Quad's anti-RIAA network | Full output on the driven channel, none on the other; monitor buttons behave as described | Q44-S02 p5 | Technician |
| Tone and filters | 100 mV into radio | Waveforms as in Quad's figures; Cancel gives no change with any tone setting | Q44-S02 p5 | Technician |
| Relay | Switch on and off | No chatter; no loudspeaker thump | Q44-S02 p9 | Owner |

## Stop conditions

- Smoke, a hot component or a blown fuse: switch off at the wall.
- Oscillation or instability after fitting new op-amps: see the decoupling fix in `boards.md` (Q44-S01 p7).

## Job record

- Unit / serial / finish / kit used / board numbers:
- Date and restorer:
- Parts changed, optional mods done:
- Supply rails and any measurements:
- Differences from the references:
