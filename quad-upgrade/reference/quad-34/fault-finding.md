# Quad 34 — fault finding (S8 p11–13)

Quad's flow diagram (S8 fig 13, p13) leads to 35 diagnoses. It assumes a **single** fault; multiple faults can mislead it. Always sanity-check a diagnosis against the circuit diagram. Walk the user through the flow diagram in the PDF rather than reproducing it from memory.

Useful diagnoses:

| # | Symptom area | Likely cause |
|---|---|---|
| 2 | Fuse blown | Mains spike — replace fuse, re-apply volts via variac; if current exceeds 15mA see #3 |
| 3 | High current | Voltage selector set wrong; transformer L1 |
| 4 | Transformer loose/faulty | Mostly pre-S/N 2000 units — replacement transformer has redundant tags for rigidity |
| 5 | No regulator output | IC21 |
| 6 | Disc fault, left channel | IC7; T1, T2 on the module; IC22; ribbon cable open circuit |
| 7 | Disc fault, right channel | IC8; T3, T4; IC22; ribbon cable |
| 13 | Various | D32 — particularly pre-S/N 6000; IC1; IC27 (post-8000) |
| 17 | Disc fault on both channels | Disc board edge connector not seated; IC22 |
| 22 | Any | An IC that is hot to the touch is faulty |
| 23, 24, 26 | LED/indicator faults | Associated BC183; LED |
| 29, 30, 35 | CMOS logic short | Isolate by unsoldering pin 14 (and/or 7) of IC1, IC2, IC11, IC14–IC18, IC22 in turn |
| 32 | High current op-amp | Isolate op-amp supply pins in turn |

Isolating the regulator: remove it and resolder it to the rear of the PCB with the output pin disconnected, then measure output to the +8.6V rail: about −18V (S8 p11).
