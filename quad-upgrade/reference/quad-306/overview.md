# Quad 306 — overview

**Status:** draft. Built from the DADA upgrade guide (Q306-S01) and Quad's service data (Q306-S02). Not user- or bench-tested; no BOM rows have physical board verification.

The 306 is a compact two-channel current-dumping power amplifier, about 50 W per channel into 8 Ω (Q306-S02 p8). It runs from roughly ±36–41 V DC rails with 4700 µF reservoir capacitors C10, C11 (Q306-S02 p8, p16). Both channels are on one motherboard; only the loudspeaker terminals are wired separately (Q306-S01 p3). **The reservoir capacitors hold a lot of energy after switch-off.** Follow `../safety.md`; beginners should leave internal work, measurement and first power-up to a qualified technician.

Its standard input sensitivity is high (0.375 V) because Quad matched it to a 606 for horizontal bi-amping (Q306-S01 p1; Q306-S02 p8).

## Identify the unit (from the outside)

| Ask / inspect | Why it matters | Source |
|---|---|---|
| Serial number | Places the unit in Quad's changes below | Q306-S02 p10 |
| Preamp used and whether it is bi-amped with a 606 | Decides whether to change input sensitivity | Q306-S01 p1, p4 |
| Does it trip after a long loud passage? | The protection trips after 10–20 s at full power; that is normal | Q306-S01 p6 |
| Previous repairs | Board may differ from the factory list | — |

A technician can confirm the PCB issue. On the copper side, component numbers are printed white for the left channel and red for the right; the circuit is the same for both channels but the layout differs (Q306-S01 p3).

## Factory changes (Q306-S02 p10)

| Approx. S/N | Change |
|---|---|
| 1000 (Feb 86) | R27 6K8 → 12K (dimmer mains-on LED) |
| 4000 (Nov 86) | R11 (47 Ω) moved to the junction of R15/R16 and +ve of C5 (stability on clipping) |
| 5500 (Feb 87) | PCB issue 3 with R34, R35 and D13 |

## Board map

| Board or task | Reference file | Scope |
|---|---|---|
| Motherboard (both channels) | `motherboard.md` | Recap, input/feedback update, sensitivity, zener decoupling, reservoir capacitors, terminals |
| Checks after work | `tests.md` | DADA and Quad figures |

## Known faults and service notes (Q306-S02 p10)

| Symptom / note | Meaning | Next step |
|---|---|---|
| Pink paint on output transistors has turned purple | They reached about 115 °C: poor heatsink contact or over-running | Technician: check thermal mounting |
| Damaged R30 / R31 (2K2) | The floating ±40 V line can shift under some faults, putting up to 80 V on one side | Technician should always check R30 and R31 during repairs |
| Transistor replacement | New thermal pads must be fitted, never reuse old ones; replace Belleville washers; reseat heatsink with thermal paste | Technician |
