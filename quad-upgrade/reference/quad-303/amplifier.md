# Quad 303 — power supply, regulator and driver boards

**Status:** draft; all values provisional. DADA's kit replaces all electrolytic capacitors, the trimmer potentiometers and some wiring (Q303-S06 p1). Quad originals are from its components list (Q303-S01 p10–11). DADA warns the old boards' tracks lift easily: little heat or pressure, a desoldering pump, 60/40 leaded solder (Q303-S06 p2). Do one driver board at a time and use the other for comparison (Q303-S06 p8).

## Reservoir and output capacitors (technician work)

| Position | Quad original (Q303-S01 p11) | DADA (Q303-S06 p3, p5) |
|---|---|---|
| Output capacitors, one per channel | C1, C2: 2000 µF 100 V | 4700, 6800 or 10,000 µF, 63 V or 100 V |
| Supply reservoir | C3: 2000 µF 100 V | 1 × 4700 µF 100 V |

DADA describes the original supply capacitor as "2 × 2000 µF in parallel", while Quad's list names one reservoir capacitor (C3). A technician should count what is fitted. Larger output capacitors are a circuit change that extends the bass; an unattributed calculation (Q303-S03) shows the same trend but is unverified.

Wiring to the capacitors (all versions, Q303-S06 p5):
- Left output capacitor: green/red to +, yellow/red to −.
- Right output capacitor: green/white to +, yellow/white to −.
- Supply capacitor: red to +, blue to −.

**Reversed capacitors can explode.** Modern capacitors are smaller; tape around them may be needed to fit the mounting rings (Q303-S06 p5). DADA rewires the supply: blue from the bridge rectifier − to the capacitor −, red from bridge + to capacitor +, yellow from the bridge AC terminals to the transformer secondary (Q303-S06 p5). Transformer and mains wiring are technician-only.

If the neon mains indicator is broken, DADA's kit includes a red LED with a 12K ½ W series resistor, connected across the supply capacitor: LED long lead to +, short lead to the resistor, resistor to − (Q303-S06 p5).

## Regulator (PSU) board (Q303-S06 p3–4, p6)

| Ref | Quad original (Q303-S01 p11) | DADA |
|---|---|---|
| R200, R201, R204 | 10K 10 % | 10K ½ W 1 % |
| R202 | 8K2 5 % (6K8 on early units, Q303-S01 p9) | 8K2 ½ W 1 % |
| R203 | 2K2 5 % | 2K2 ½ W 1 % |
| R205 | 4K7 10 % | 4K7 ½ W 1 % |
| R206 | 10 Ω 10 % | 10 Ω ½ W 1 % |
| R207 | 68 Ω 10 % | 68 Ω ½ W 1 % |
| MR200 | 1S920 diode | 1N4004, 1N4005 or 1N4006 |
| MR201 | 12 V zener (1S2120 or ZE12V7) | 12 V 1.3 W zener |
| RV200 | 4K7 trimmer | 4K7 trimmer — **leave in the middle position** until calibration |

Diode and zener cathodes (stripe) point to the middle of the board (Q303-S06 p6).

## Driver boards (two) (Q303-S06 p4, p7)

| Ref | Quad original (Q303-S01 p10) | DADA |
|---|---|---|
| C100 | 0.64 µF (Mullard C426) | 1 µF film, 10 mm pitch |
| C101 | 300 µF 10 V | 470 µF, 16 V or more |
| C104 | 12 µF 50 V | 22 µF, 25 V or more |
| C106 | 50 µF 50 V | 47 µF, 25 V or more |
| RV100 | 4K7 trimmer | 4K7 trimmer |
| RV101 | 2K2 trimmer | 2K2 trimmer; **22K for boards below S/N 11,500 (version 9 or lower)** |

**Polarity:** + of C104 and C101 towards the inside of the board; + of C106 towards the back of the board (Q303-S06 p7).

Driver board wiring, left channel (right channel: white reads red) (Q303-S06 p8): 1 red + supply; 2 red TR1 collector; 3 violet/white TR1 base; 4 black/white TR1 emitter; 5 green/white output to output capacitor; 6 blue/white TR2 collector; 7 orange/white TR2 base; 8 brown/white TR2 emitter and − supply; 9 brown/white − loudspeaker. PSU board: 12 red +; 13 brown negative and TR3 collector; 14 orange TR3 base; 15 blue −.

## Input sensitivity (optional modification)

Standard sensitivity is 0.5 V. To lower it, change R108 and C103 together so their product stays constant, which keeps the bandwidth (Q303-S02 p1). Quad fits R108 = 22K and C103 = 100 pF (Q303-S01 p10).

| Sensitivity | R108 | C103 |
|---|---|---|
| 0.5 V (standard) | 22K | 100 pF |
| 0.733 V | 15K | 150 pF |
| 1.1 V | 10K | 220 pF |
| 1.6 V | 6K8 | 330 pF |

Practical values from Q303-S02 p1. For about 1.0 V, the note suggests a second 22K and 100 pF in parallel with the existing parts on the copper side, clear of the bottom plate. Change both channels the same.

## Calibration (technician only)

Live adjustments on a powered amplifier, **with no source and no loudspeakers connected** (Q303-S06 p9). **Lift the boards fully off the plastic clips and keep the copper side away from the chassis, for example on a wooden block; contact destroys the driver boards and output transistors** (Q303-S06 p9).

1. RV200: exactly 67 V DC between pins 1 and 9 on one driver board (Q303-S06 p9; Quad: tags 1 and 9, Q303-S01 p6).
2. RV100: exactly 33.5 V DC between pins 1 and 5 on each driver board (Q303-S06 p9). Quad measures 33.5 V between tags 5 and 9 (Q303-S01 p6); by the figures, both are half the 67 V supply.
3. RV101 quiescent current:
   - DADA: at least 6 mV DC between pins 4 and 6, ideally 6–9 mV and no more than about 15 mV; that is roughly 10–18 mA (Q303-S06 p9–10).
   - Quad: 5–10 mA, measured with a meter in series with the tag 2 lead (Q303-S01 p6).
   - DADA deliberately sets it higher than Quad for margin with modern parts. Tell the user both.
4. Repeat for the other driver board. Run the amplifier for some hours at normal volume, then repeat the calibration (Q303-S06 p10).

## Options

DADA also sells RCA sockets, loudspeaker binding posts, 35 mm capacitor rings, replacement 2N3055 or MJ15003 output transistors, and complete "high-end" replacement boards (Q303-S06 p4).

## After the work

See `tests.md`.
