# Quad 303 — driver boards, regulator and power supply

**Status:** draft; all values provisional. Original values from Quad's components list (Q303-S01 p10–11). There is no kit source for replacements: replace electrolytics with the **same capacitance and an equal or higher voltage rating**, and check size and lead spacing before ordering (`../general-practice.md`). Do not change film, ceramic or resistor values without a source.

## Electrolytic capacitors (like-for-like)

| Ref | Where | Quad original | Qty (whole amplifier) |
|---|---|---|---|
| C1, C2 | Output capacitors, one per channel | 2000 µF 100 V | 2 |
| C3 | Supply reservoir | 2000 µF 100 V | 1 |
| C101 | Driver board | 300 µF 10 V | 2 |
| C104 | Driver board | 12 µF 50 V | 2 |
| C106 | Driver board | 50 µF 50 V | 2 |
| C100 | Driver board input | 0.64 µF +100/−10 % (Mullard C426) | 2 |

C1, C2 and C3 are listed under "Quad 303: General" (Q303-S01 p11); the output capacitors are off the driver board (Q303-S01 p5). C100's voltage rating is not printed; a technician must read it from the fitted part. C201 on the regulator (2.2 µF 250 V, Hunts/Mullard) and C108 (0.1 µF 250 V) are film parts and are not part of an electrolytic recap.

**Larger output capacitors:** an unattributed spreadsheet (Q303-S03) calculates less bass roll-off with larger output capacitors (4700 µF or 10,000 µF) and a 1 µF input capacitor. Its method is not stated. Do not present this as a recommendation; if a user asks, explain it is an unverified calculation and a circuit change.

## Input sensitivity (optional modification)

Standard sensitivity is 0.5 V. To lower it, increase the input-stage feedback by changing R108 and C103 together so their product stays constant, which keeps the bandwidth (Q303-S02 p1). Quad fits R108 = 22K and C103 = 100 pF (Q303-S01 p10).

| Sensitivity | R108 | C103 |
|---|---|---|
| 0.5 V (standard) | 22K | 100 pF |
| 0.733 V | 15K | 150 pF |
| 1.1 V | 10K | 220 pF |
| 1.6 V | 6K8 | 330 pF |

These are the author's practical values (Q303-S02 p1). For about 1.0 V, the note suggests soldering a second 22K and 100 pF in parallel with the existing R108 and C103 on the copper side, checking they cannot touch the bottom plate (Q303-S02 p1). Change both channels the same.

## Setting up (technician only; Q303-S01 p6)

The 303 has three adjustments. They are live measurements on a powered amplifier:
1. Set the mains voltage adjustment for the local supply.
2. RV200: 67 V DC between tags 1 and 9 on one driver board.
3. RV100: 33.5 V between tags 5 and 9 on the left driver board (the output centre point).
4. RV101: 5–10 mA quiescent collector current, measured by breaking the external lead to tag 2 of the left driver board and inserting a meter in series, with no signal.
5. Repeat 3 and 4 for the right channel.

## After the work

See `tests.md`.
