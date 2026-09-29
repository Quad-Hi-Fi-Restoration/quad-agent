# Quad 34 — fault finding (S8 p11–13)

This file summarizes Quad's flow diagram (S8 fig 13, p13), which assumes a **single** fault; multiple faults can mislead it. The table is diagnostic context for a qualified restorer, not a beginner repair procedure. A beginner can describe symptoms and provide externally visible information; do not coach them to probe, touch, desolder, or power a unit with the cover off. For internal or powered diagnosis, refer to a qualified technician and the original flow diagram.

Useful diagnoses:

| # | Symptom area | Likely cause |
|---|---|---|
| 2 | Fuse blown | Quad's service manual discusses a monitored variac procedure. Do not repeatedly replace a blown fuse or power the unit again before a technician checks it |
| 3 | High current | Voltage selector set wrong; transformer L1 |
| 4 | Transformer loose/faulty | Mostly pre-S/N 2000 units — replacement transformer has redundant tags for rigidity |
| 5 | No regulator output | IC21 |
| 6 | Disc fault, left channel | IC7; T1, T2 on the module; IC22; ribbon cable open circuit |
| 7 | Disc fault, right channel | IC8; T3, T4; IC22; ribbon cable |
| 13 | Various | D32 — particularly pre-S/N 6000; IC1; IC27 (post-8000) |
| 17 | Disc fault on both channels | Disc board edge connector not seated; IC22 |
| 22 | Any | Quad flags an unusually hot IC; never touch a powered board. Have a technician assess it using an appropriate method |
| 23, 24, 26 | LED/indicator faults | Associated BC183; LED |
| 29, 30, 35 | CMOS logic short | Quad's flowchart includes isolating logic ICs; this involves desoldering and is technician-only |
| 32 | High current op-amp | Quad's flowchart includes isolating op-amps; this involves live fault-finding and is technician-only |

The regulator-isolation procedure in S8 p11 involves modifying the live test setup and measuring powered circuitry. Do not give it as a user procedure; a qualified technician should consult the original service manual.
