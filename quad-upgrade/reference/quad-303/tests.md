# Quad 303 — checks after work

Follow `../safety.md`. All powered checks and adjustments are for a qualified technician. Never connect loudspeakers until the centre-point and current checks are right.

| Check | Setup | Expected result | Source | Who |
|---|---|---|---|---|
| Visual: polarity of every electrolytic; no bridges | Unpowered | As photographed before work | `../general-practice.md` | Restorer |
| Mains setting | Unpowered | Matches local mains | Q303-S01 p6 | Technician |
| Regulated supply | Powered, no signal, no loudspeakers | 67 V DC between pins/tags 1 and 9 (set with RV200) | Q303-S06 p9; Q303-S01 p6 | Technician |
| Output centre point | Powered, no signal | 33.5 V on each driver board (set with RV100) | Q303-S06 p9; Q303-S01 p6 | Technician |
| Quiescent current | Powered, no signal | DADA: 6–9 mV between pins 4 and 6 (about 10–18 mA), max about 15 mV. Quad: 5–10 mA. Record which target was used. | Q303-S06 p9–10; Q303-S01 p6 | Technician |
| Re-check after warm-up | After some hours of normal use | Repeat the three settings | Q303-S06 p10 | Technician |
| Listening check | Low volume first | Clean on both channels; no hum or distortion | — | Owner, after the technician's checks |

## Stop conditions

- Supply or centre-point voltage cannot be set, quiescent current cannot be brought into range, smoke, heat or a blown fuse: switch off at the wall and refer for fault-finding (see `overview.md`).
- Any contact between a driver board's copper side and the chassis during calibration can destroy the boards and output transistors (Q303-S06 p9).

## Job record

- Unit / serial / Tr107 fitted yes/no:
- Date and restorer:
- Parts changed, sensitivity chosen:
- Supply, centre-point voltages and quiescent current, each channel:
- Differences from the references:
