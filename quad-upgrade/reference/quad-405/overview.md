# Quad 405 — overview

**Status:** draft. Built from the DADA upgrade guide (Q405-S01) and Quad's service data (Q405-S02). Not user- or bench-tested; no BOM rows have physical board verification.

The 405 is a two-channel current-dumping power amplifier, about 100 W per channel into 8 Ω. It runs from roughly ±50 V DC rails (Q405-S01 p5, p9) with two 10,000 µF reservoir capacitors (Q405-S02 p14, p24). **This is more dangerous inside than a preamplifier.** DADA warns the capacitors hold their charge "for a long time" after switch-off (Q405-S01 p9). Follow `../safety.md` strictly; beginners should leave all internal work, measurement and first power-up to a qualified technician.

## Identify the unit (from the outside)

| Ask / inspect | Why it matters | Source |
|---|---|---|
| Nameplate: 405 or 405-2 | Different boards, current limiter and some extra parts (C18, C19) | Q405-S02 p12 |
| Serial number | Places the unit in Quad's change history below | Q405-S02 p8, p12 |
| Loudspeaker outputs: original terminals or 4 mm sockets | 4 mm sockets from S/N 67950 (405-2) | Q405-S02 p12 |
| Inputs: DIN only, or phono (RCA) sockets | Phono sockets replaced DIN from S/N 85000 | Q405-S02 p12 |
| Voltage selector on the back | Omitted from S/N 83000 | Q405-S02 p12 |
| Previous repairs or upgrades | Many 405s were converted to 405-2 boards by owners and dealers; a later clamp circuit may have been retrofitted | Q405-S02 p12; Q405-S01 p5 |

The amplifier board number and issue (M12368.x or M12565.x) settles which parts are fitted. It is inside the unit, so a technician should read it. If serial, nameplate and board disagree, stop and describe the mismatch.

## Variants

| Variant | Evidence | Notes | Confidence |
|---|---|---|---|
| 405 (405-1) | "405" nameplate; boards M12368 (issues 5–10) or M12565.3 | Clamp circuit: none before S/N 9000; separate board on the output terminals from 9000; on the main board from M12565.3 (S/N 59001) | provisional |
| 405-2 | "405-2" nameplate, from S/N 65000 (January 1983); 405-2 modules fitted from S/N 62500 in units still badged 405 | Board M12565.5 onward; thick-film current limiter N1/N2; clamp on the board; extra C18, C19 47 µF | provisional |

## Factory changes (Q405-S02 p8, p12)

| Approx. S/N or board | Change |
|---|---|
| M12368.7 | R4 10K → 22K; R5 10K → 4K7; R9 180 Ω → 220 Ω; R19 removed; R23 3K3 → 1K2; C9 removed; C18 47 nF added; R2 2.2 Ω → 10 Ω |
| 9000 (M12368.9) | R41 22 Ω, L3, C15, C16, C19 1 nF added; C18 47 nF removed; clamp circuit PCB M12400 added on the output terminals |
| 29,000 | R10 1K → 1K8; R27, R29 8K2 → 15K; R35, R36 0.08 → 0.091 Ω; D1, D2 LR120C → LR150C |
| 59,001 (M12565.3) | Clamp circuit and voltage limiter (now a link) on the main board |
| 62,500 | 405-2 modules (M12565.5) fitted, still with 405 nameplates |
| 65,000 | 405-2 introduced |
| 66,700 | C20 4n7 added; D13 added; R44 added (stability) |
| 67,950 | 4 mm output sockets |
| 72,501 | TR4 → BC556B; R18 omitted |
| 83,000 | Voltage selector omitted |
| 85,000 | New mains inlet with fuseholder; DIN input replaced by phono sockets; signal earth isolated by R2 |

## Board map

| Board or task | Reference file | Scope |
|---|---|---|
| Amplifier (driver) boards, one per channel | `amplifier-boards.md` | Recap, op-amp, zeners, input sensitivity, clamp capacitor |
| Power supply, wiring and connectors | `power-supply.md` | Reservoir capacitors, rewiring, output protection — technician work |
| Checks after work | `tests.md` | DADA and Quad figures |

## Known faults

| Symptom | Possible cause | Next step | Source |
|---|---|---|---|
| Poor or intermittent loudspeaker connection | Original terminals oxidised | DADA replaces them in its kit; technician work | Q405-S01 p5 |
| Blown internal 4 A fuses FS1/FS2 | The clamp circuit blows them on excessive output DC or a short, to protect the loudspeaker | Technician fault-finding (Q405-S02 p6) | Q405-S02 p8 |
| Mild instability when switching off | Pre-S/N 66,700 405-2 | Factory mod adds C20 4n7 | Q405-S02 p12 |
