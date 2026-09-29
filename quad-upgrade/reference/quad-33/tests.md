# Quad 33 — checks after work

Follow `../safety.md`. Powered checks inside the unit are for a competent restorer or qualified technician. Neither source gives a full factory test procedure for the 33; record measurements and do not call a figure correct without a documented value.

| Check | Setup | Expected result | Source | Who |
|---|---|---|---|---|
| Visual: polarity of every electrolytic, diode and zener; no lifted tracks or bridges | Unpowered | Rectifier and zener cathodes towards the middle of the PSU board; C202/C203 + towards TR200/TR201 | Q33-S01 p3, p9 | Restorer |
| Mains tap | Unpowered | Matches the mains voltage marked on the rear and local mains | Q33-S01 p14; Q33-S04 p14 | Technician |
| Supply voltage | Powered | About 16 V after DADA's modification (12 V zener originally). No tolerance is published; record the figure. | Q33-S01 p3; Q33-S02 p7 | Technician |
| Output level | Radio input, 100 mV | Factory: 0.5 V at the main output. After DADA's gain reduction the required input rises about 2.5 times. | Q33-S04 p21–22; Q33-S01 p16 | Technician |
| Balance | Volume from 0 to −45 dB | Within ± 1.5 dB between channels | Q33-S02 p4 | Technician |
| Listening check | Low volume first, with the power amp | No hum, crackle or channel drop-out on any input; mono/stereo behaviour as in Q33-S03 | Q33-S03 | Owner, after the technician's checks |

## Stop conditions

- Smoke, a hot component, a blown fuse, or a supply voltage far from 16 V: switch off at the wall.
- Signal missing on one input only: likely a switch or edge-connector contact (Q33-S02 p4).

## Job record

- Unit / serial / board numbers and issues:
- Date and restorer:
- Parts changed, gain reduction yes/no, Disc Adaptor position:
- Supply voltage and any measurements:
- Differences from the references:
