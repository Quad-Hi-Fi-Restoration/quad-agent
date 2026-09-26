# Quad 34 — line stage, tone, filter and output

## Restoration
Op-amps and electrolytics in this area are covered by the DADA kit — see `recap-kit.md`.

## Op-amp decoupling (S3 p7)
If a low-frequency oscillation occurs (caused by long supply tracks), fit 100nF film or ceramic capacitors between pin 3 and pin 7, and between pin 3 and pin 4, of IC9 and IC10. That's two per op-amp. Pin 3 is already grounded there. Solder them on the copper side. Included in the ≥ 8000 kit.

## Early-unit input values (S7, serial 6001–8000)

| Ref | Value | Notes |
|---|---|---|
| C3, C4 | 330n | Radio input coupling |
| C5, C6 | 330n | AUX input coupling |
| C7, C8 | 680n | Tape input coupling |
| R11, R13 | 100k | Radio input to ground |
| D3–D14 | 6V8 zener | Input switch protection |
| R16, R18 | 82k = 300mV tape playback; 0R link = 100mV | |
| R27, R28 | 1k = 300mV tape record out; not fitted = 100mV | |

Switching transistors T5–T12 are BC183L or BC182L and are **not in numerical order** on the PCB (S7).

## Sensitivity flags (S8, S11 — from S/N 8001)
Input and tape sensitivities are set by plug-in resistor "flags" on the main PCB:
- **CD:** flags in R135/R136 — 300mV as supplied; 100mV (to suit Quad tuner) and 500mV flags available (S11 p11).
- **Tape:** replay and record set by flags, 300mV as supplied; 100mV flags come in the MC module pack (S11 p11; S8 p23 SF1–SF8).
- **X1/X2 flags** bring the spare sockets between CD and Tape Replay into circuit as a second tape record output (S11 p11).

Input specs (S11 p16): Radio 100mV / 100k; CD 300mV / 49k (max 20V); Tape replay 300mV / 57k.

## Input sensitivity (S5, early units)

| Input | Sensitivity | Impedance | Notes |
|---|---|---|---|
| RADIO | 100mV | 100kΩ (R11/R12 to ground) | |
| TAPE, AUX | 100mV | 39kΩ | TAPE can be set to 300mV by fitting 82kΩ at links R16/R18 |

Nominal output 500mV at full volume. Later units (8001+) have input buffers (S5).

### AUX as a 300mV CD input (S5, early units)
C5/C6 → 1µF with 82kΩ in series for 300mV sensitivity. For TAPE: C7/C8 → 1µF, and 82kΩ at R16/R18. **Warning:** on Keith's early unit this exposed a frequency-selective crosstalk problem that collapsed the stereo image. The fix involved cutting and grounding PCB tracks — see S5. Tell the user about this before they do the input mod on an early unit.

### Output coupling capacitor options (S5)
Keith Snook tried C77/C78 as 150µF 6.3V tantalum bypassed with 1µF 63V polyester, and later replaced them with wire links. A way to keep capacitors in place: 1µF polyester on top of the PCB with a small 100µF 3V tantalum across it underneath. S3 advises keeping output caps because you can't know what's connected (S3 p10).

### Tape outputs (S5)
Keith added 100kΩ from each tape output to ground to give C16/C17 a DC path.

## Output level (S3 p6)
Standard output is 500mV RMS from 830Ω (S11). Original output resistors: R117/R120 2K7, R118/R121 2K2, R119/R122 1K (S7, S8 p23). Maximum 1.5V (S11). Increasing the output also tends to increase the momentary switch-on noise (S11 p9). The same tables appear in the Quad instruction book (S11 p9).

To **reduce** it (e.g. for a Quad II valve amp), fit an extra resistor in parallel with R119 and R122:

| Parallel resistor | Attenuation | Output |
|---|---|---|
| 470Ω | 9 dB | 180mV |
| 180Ω | 15 dB | 90mV |
| 100Ω | 20 dB | 50mV |

To **increase** it, change resistors:

| Output (RMS) | R118 / R121 | R119 / R122 |
|---|---|---|
| 1.6V | shorted | 3k3 |
| 1.1V | 1k | 2k2 |
| 775mV | 1k5 | 1k5 |

## Balance control repair (S3 p9)
Original balance pots (RV4a/b) are no longer available. They can be replaced with fixed resistors, RI = 330Ω and RII = 1500Ω, positioned per the S3 p9 photo, which preserves the original volume setting. For extra volume, replace RI with a wire link and omit RII. Use the photo for placement — don't describe positions from memory.

## Switching faults (S3 p8)
Erratic input switching or mixed inputs is often damaged tracks under leaked electrolytics. Bypass with insulated wire between the matching pins.

## Front panel LEDs (S5)
Red LED resistors R109 and R116 are 3k3 (about 4mA). Keith changed R95–R97 from 1k to 2k7 (about 5mA) when fitting yellow/amber LEDs to match the buttons. Early units have 5mm LEDs.

## Other value notes
- R55/R60 changed from 680K to 2M2 at about S/N 3700 for improved bass (S8 p21) — earlier units may still have 680K.
- R45/R46: 1K3 in Quad's parts list and diagrams (S8); Keith Snook's redraw (S7) shows 1k5. Read the fitted part.
- Clicks when switching: clean switches with contact cleaner (S8 p20).
