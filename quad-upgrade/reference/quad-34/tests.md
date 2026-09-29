# Quad 34 — tests after work

All powered measurements and internal tests below are for a qualified technician. Follow `../safety.md` first. A beginner may record external symptoms after a technician has confirmed the unit is safe to use. Where no tolerance is given by a source, record the measurement; do not call it "fine" without a reference.

## Quad's own test procedure (S8 p14–20)
Quad tests with a variac, signal generator, AC microvoltmeter, scope and an inverse RIAA network. Key figures:

| Test | Expected | Source |
|---|---|---|
| Mains current at 240V | Not more than 15mA, typically 10mA | S8 p15 |
| Rails | +8.6V, +7.5V, −7.5V, −9.4V (test points shown in S8 fig 16) | S8 p15–16 |
| Regulator input | About 30V | S8 p4, p13 |
| Regulator output | −18V measured from the +8.6V rail (regulator isolated) | S8 p11 |
| Channel balance at volume 21 | Within ±0.5dB | S8 p19 |
| Volume law | Table on S8 p19, ±0.5dB | S8 p19 |
| Crosstalk | At least 50dB below full output | S8 p20 |
| Noise, volume at zero | At least −90dB (−100dB A-weighted) | S8 p20 |
| Output | 500mV RMS | S8, S11 |

Disc test (S8 p17): drive through the inverse RIAA network (fig 18) at 4V p-p (100µV module), 8V p-p (200µV) or 22V p-p (3mV).

These service-manual measurements require suitable equipment and competence. The following checks are not a beginner procedure and must not be presented as safe just because they use a multimeter.

## Supply rails (technician-only powered measurements; S1, S2 excerpt)

| Test point | Expected | Source |
|---|---|---|
| IC7 / IC8 pin 7 (to ground) | +8.6V | S1; S2 p1 |
| IC7 / IC8 pin 4 (to ground) | −9.4V | S1; S2 p1 |
| Switching logic rails | +7.5V / −7.5V | S1 |

Tolerance: not stated in sources. Check the ±7.5V logic rails too (S8 p15).

## Output (powered measurements: technician only)
- Standard output level 500mV RMS (S3 p6).
- With a signal generator and scope, output voltage and input sensitivity can be measured; without them, no calibration is required (S3 p6).
- DC at output terminals: should be 0V with the output capacitors C77/C78 fitted (S5). Keith found +11mV on one channel — the sign that C77 was fitted reversed. Measure each channel before connecting to a power amplifier.
- Modern op-amps give very low offset of unpredictable polarity (S3 p10).
- After an op-amp swap: if the user has a scope, check the output clips symmetrically at maximum output (S5).

## Disc-to-line conversion (S2 p2)
After a qualified technician has completed the first-power checks and confirmed the unit is safe to use, this external listening check can be done by the owner: set the volume to zero, select Disc, connect a CD/AUX-level source and raise the volume one notch. It should play without distortion or hum. This is not an instruction for a beginner to modify, open or power up the unit after repair.

## Listening
- Only listen after a qualified technician has confirmed the unit is safe to use. Start at low volume; both channels should be present and balanced.
- No hum, crackle, oscillation or new thumps.
- Compare with the baseline taken before work.
