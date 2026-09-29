# Quad 44 — overview

**Status:** draft. Built mainly from the DADA upgrade guide (Q44-S01), with Quad's service data (Q44-S02) for the switching fix, faults and tests. Quad's per-board parts lists have not yet been transcribed, so original values come from DADA's kit lists. Not user- or bench-tested; no BOM rows have physical board verification.

The 44 is Quad's op-amp preamplifier (1979–1989, about 40,000 made), usually paired with the 405. It has plug-in input modules (radio, aux or CD/aux, disc, two tape), a motherboard with the power supply and electronic input switches, and a tone-control board (Q44-S01 p1). The supply rails are ±15 V (Q44-S02 p9). The mains is inside the case; follow `../safety.md`.

## Identify the unit (from the outside)

| Ask / inspect | Why it matters | Source |
|---|---|---|
| Serial number | Selects DADA kit I, II or III | Q44-S01 p2–3 |
| Finish: brown or grey | The two external series | Q44-S01 p1 |
| Input sockets: DIN or phono | First models used DIN | Q44-S01 p1 |
| Which input modules are fitted and the cartridge type | Modules are interchangeable; non-standard (mostly MC) modules need a special DADA kit | Q44-S01 p1 |
| Symptoms: inputs switching on their own, relay chattering at switch-on, thump at switch-off, noise at volume zero | Each has a documented fix (see below) | Q44-S01 p7; Q44-S02 p9, p45 |

## Variants (DADA kits)

| Kit | Serial range (Q44-S01 p2–3) | Tone board | Notes |
|---|---|---|---|
| Kit I | 0–12,000 | M12512 iss 8 | Radio board M12511 iss 1 |
| Kit II | 12,000–23,000 | M12512 iss 9 | Adds C407 on the motherboard; AUX board M12511 iss 2 |
| Kit III | 23,000 and higher | M12784 iss 1 | Tone and volume circuits based on the Quad 34; dual op-amps; CD/AUX board M12815 iss 1 |

DADA's ranges meet exactly at 12,000 and 23,000. For a unit at a boundary, a technician should confirm the tone-board number before choosing a kit. DADA offers to pick parts from the serial and module PCB numbers (Q44-S01 p1).

## Board map

| Board or task | Reference file | Scope |
|---|---|---|
| All boards | `boards.md` | Motherboard/PSU, electronic switches, tone board, input modules, Quad's switching fix, optional mods |
| Checks after work | `tests.md` | Quad and DADA |

## Known faults

| Symptom | Cause | Fix | Source |
|---|---|---|---|
| Unit changes input by itself, or to no input | Pulses triggering the electronic switching | Quad TI 003: resolder the 10 feed-through pins on the motherboard (ideally replace with tinned copper wire) and fit at least 4.7 µF across the +8.5 V and −7.5 V rails on the back of the motherboard. DADA includes the capacitor. | Q44-S02 p45; Q44-S01 p2, p4 |
| Relay chatters or rattles at switch-on | Low supply (HT) voltage | DADA: R400, R405 → 1 Ω and R402, R403 → 1500 Ω, only if it happens | Q44-S02 p9; Q44-S01 p7 |
| Loudspeakers thump at switch-off (relay on the tone board) | Relay switch-off too slow | Quad: 4.7 µF from +15 V to the base of TR501 | Q44-S02 p9 |
| Not silent at volume zero (Model I before S/N 2401) | Circuit design | Optional tone-board resistor change (`boards.md`) | Q44-S01 p7 |
| Low-frequency oscillation after fitting modern op-amps | Long supply tracks and wiring | 100 nF from each supply pin to ground at IC500/IC501 (IC700a/IC701a above S/N 23,000) | Q44-S01 p7 |
| Switch clicks, intermittent volume | Dirty switch/pot contacts; open joint between volume pot and tone board | Contact cleaning; technician resolders | Q44-S02 p9 |
| Excessive noise on all inputs | IC500/IC501 (volume at 22) or IC502/IC503 (volume at 1) | Replaced in the recap | Q44-S02 p9 |
| Excessive crosstalk | Loose motherboard earth screws | Technician tightens them | Q44-S02 p9 |
