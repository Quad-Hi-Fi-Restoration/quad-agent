# Quad 34 — power supply

> **Technician-only internal section.** Mains and stored energy are present here. A beginner must not open the unit or probe C74. A competent restorer must follow `../safety.md` and verify stored voltage using suitably rated equipment before touching parts.

## How it works (S8 p4)
Transformer secondary about 27V AC, rectified and smoothed by C74 to about **30V DC**, which feeds IC21 (7918). The regulator output is −18V referenced to the positive rail. IC23 with R123/R124 splits this into +8.6V and −9.4V. R84, D30 and R85 derive the ±7.5V rails for the CMOS logic, decoupled by C57 and C59. C58 and C84 decouple the HT rails.

**Clamp circuit:** T14/T15 short the audio output to earth at switch-on until the rails settle (C69 via R102 delays T13), and again at switch-off as C74 discharges. A unit that stays muted may have a clamp fault — see `fault-finding.md`.

## Parts (S1, S8)

| Ref | Value / type | Function |
|---|---|---|
| D34 | VM18 | Bridge rectifier |
| C81, C82 | 47n | RF click suppression, added at PCB iss 4 / S/N 6001 (S8 p21). RATA (S9) removes them — see `recap-kit.md` |
| C74 | 1000µ | Reservoir — sees about 30V DC (S8 p4) |
| IC21 | 7918 | Negative regulator |
| T13 | E5270 | Positive rail pass transistor |
| D32 | 12V zener | Reference |
| R103, R104 | 3K3 | |
| C69 | 100µ | |
| IC23 | TL071 | Rail splitter |
| R123 / R124 | 8K2 / 9K1 | Splitter divider |
| C58, C84 | 22µ | Splitter output. C84 is on issue 5 (S1) only, not on issue 3 (S6) — check whether the board has it |
| C57, C59 | 100µ | Rail decoupling |

The +8.6V / −9.4V rails are deliberately asymmetric, and low overall because the CD4066 switches can be damaged by peaks above ±7.5V (S5). Don't "correct" them to symmetrical — see `recap-kit.md` → Before swapping op-amps.

Issue 5 uses a mains voltage link for 200–240V or 100–127V (S1); issue 3 uses a selector socket S9 (S6). Fuse: rear panel shows T63mA (S11 back view) and the S8 parts list says 63mA, but the S8 assembly list and S11 text say 100mA. **Fit what the unit's own rear panel states.** Quad's test: current at 240V should not exceed 15mA, typically 10mA (S8 p15). Low-voltage rails: +7.5V / −7.5V taken from the main rails via R84 180R, D30 15V zener and R85 300R (S6). Leave the mains wiring as it is.

## Restoration
C57, C58, C59, C69, C74, and C84 (serial ≥ 8001) are in the later DADA kit list (S3 p2). See `recap-kit.md` for the serial 8000 boundary and polarity.

## Checks
See `tests.md`.
