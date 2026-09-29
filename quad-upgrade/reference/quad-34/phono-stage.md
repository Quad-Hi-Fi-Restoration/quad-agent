# Quad 34 — disc (phono) stage

> Internal module replacement and board work are for a competent restorer after the safety check in `../safety.md`. Do not ask a beginner to open the unit to identify the module; use the panel marking if it is already visible or ask a technician to inspect it.

All values below are from the sources named. The disc module and RIAA stage values are identical in two Quad diagrams, issue 3 (S6) and issue 5 (S1), and Keith Snook's redrawn diagram for serials 6001–8000 (S7) shows the same values, so the originals are cross-checked from serial 6001 onwards. Serial 1–6000 is not yet covered by any source. Originals are read from S1; where only one source gives a value, treat it as provisional and have a qualified technician compare it with the fitted board before ordering.

## How it works (S1)
Disc module (plug-in, MM or MC) → C18 (L) / C22 (R) 2.2µF → RIAA amplifier IC7 (L) / IC8 (R), TL071 on +8.6V / −9.4V rails, with a passive network around it → R41/C27/C26/R42 (L), R43/C29/C28/R44 (R) → IC22 disc/monitor switch.

The plug-in module is a buffer amplifier ahead of a shunt-feedback RIAA stage built around a TL071. It sets cartridge loading and adds gain for better signal-to-noise. The module PCB is common to all versions: MM and MC differ only by component values (S5).

A solder-side component map of the module PCB (M12728 iss 1) is in `images/phono-module-silkscreen-M12728.png` (S10, CC0). The PCB is identical for MM and MC; service references take suffix **a** on MC modules and **b** on MM modules. Left-channel refs are white, right yellow.

## Module types (S8 p27–28, S11 p10)

| Module | Load | Key differences | Notes |
|---|---|---|---|
| MM 3mV | 47K // 220p | R5b–R10b 82K, R21b/R23b 220R, R22b/R24b 910R, C12b–C15b 1µ5, T1b/T3b BC214C, T2b/T4b BC413 | Fitted as standard (S11) |
| MC 100µV | 100Ω // 22n | R5a–R10a 2K2, R21a/R23a 6R8, C12a–C15a 47µ, ZTX750/ZTX650 | |
| MC 200µV | 100Ω // 22n | R5a–R10a 5K6, R21a/R23a 15R, C12a–C15a 22µ, ZTX750/ZTX650 | Supplied in the box as the MC option (S11) |
| MC 400µV | 100Ω // 22n | R5a–R10a 15K, R21a/R23a 30R, C12a–C15a 10µ, ZTX750/ZTX650 | |

S11 guide: the right module gives a normal listening volume setting of about 12–17.

Changing module (S11 p10): undo the two screws, withdraw the module, unplug the 8-way flat cable, fit the new module making sure all pins are correctly inserted, refit.

First ask which module the user has. The MM panel reads "3mV 47K/220p" (S2 p2).

## MM module (S1, suffix b)

| Ref (L / R) | Value | Function |
|---|---|---|
| R1b / R2b | 47K | Input resistance |
| C1b / C2b | 220p | Input capacitance |
| T1b / T3b | BC214C | Input transistor |
| T2b / T4b | BC413 (parts list S8 p28); diagrams label it E5270 | Input transistor |
| R5b, R6b / R9b, R10b | 82K | Bias |
| C12b, C13b / C14b, C15b | 1µ5 | Coupling |
| R21b / R23b | 220R | Feedback |
| R22b / R24b | 910R | Feedback |

## MC module (S1, suffix a)

| Ref (L / R) | Value | Function |
|---|---|---|
| R1a / R2a | 100R | Input resistance |
| C1a / C2a | 22n | Input capacitance |
| T1a / T3a | ZTX750 (PNP) | Input transistor |
| T2a / T4a | ZTX650 (NPN) | Input transistor |
| R5a, R6a / R9a, R10a | 2K2 | Bias |
| C12a, C13a / C14a, C15a | 47µ | Coupling |
| R21a / R23a | 6.8R | Feedback |
| R22a / R24a | 1K1 | Feedback |

Module supply on main board: R3 560R, R4 470R, D1, C10 100µ (positive side); R7 470R, R8 680R, D2, C11 100µ (negative side) (S1, S8). **D1/D2 conflict:** every diagram shows 5V2 zeners; the S8 parts list says 5V6. Have a qualified technician confirm the fitted part before choosing a replacement; do not ask a beginner to open the unit to read it.

## RIAA amplifier on main board (S1)

| Ref (L / R) | Value |
|---|---|
| C18 / C22 | 2µ2 |
| R33 / R37 | 4K7 |
| R36 / R40 | 750K |
| C21 / C25 | 47p |
| C19 / C23 | 47n |
| C20 / C24 | 15n |
| R34 / R38 | **56K on all diagrams; 54K9 (1% stock code R54K9FN) in S8 parts list — conflict, part of the RIAA network. Read the fitted part; don't change it on the basis of either source** |
| R35 / R39 | 4K99 |
| IC7 / IC8 | TL071 |
| R41 / R43 | 750R |
| C27 / C29 | 470n |
| C26 / C28 | 15n |
| R42 / R44 | 39K |

## Restoration
Covered by the DADA kit (S3 p2) — see `recap-kit.md`. Phono-relevant parts: IC7/IC8 → OP07DP or OPA604; C18/C22 2.2µF; C10/C11 100µF.

**Leave alone unless faulty:** the RIAA network (R33–R40, C19–C21, C23–C25) and the module components are not in the DADA kit. Neither S3 nor S4 recommends changing them for restoration.

Changing IC7/IC8 changes the RIAA amplifier itself. If the user is happy with the phono sound now, take a baseline before swapping them.

## Optional modifications
Each is a change in behaviour, not restoration. Explain the effect and let the user decide.

### MM input capacitance — C1b/C2b 220pF → 47pF (S3 p10)
For MM cartridges that sound dull on the 34. The 220pF plus arm-cable capacitance can be too high for modern MM cartridges; 47pF raises HF output. S3 suggests silvered mica (Cornell Dubilier 47pF 500V) or ceramic (Vishay 47pF 100V). Before recommending it, ask for the cartridge's recommended load capacitance and the arm-cable capacitance if known.

### MC module low-noise transistors (S4, K. Snook 2007)
Replaces the input transistors with 2SA1085E (PNP, replacing ZTX750) and 2SC2547E (NPN, replacing ZTX650), running at 1mA collector current for lowest noise with low-impedance cartridges. Bias resistors R5, R6, R9, R10 → 3.9k.
- S4 draws two modules, labelled 100µV and 200µV. The S8 parts list explains its apparent double values: the 100µV module has R21/R23 6R8 and C12–C15 47µ; the 200µV module has 15R and 22µ. So **keep R21/R23 and C12–C15 at the values for the user's module** — confirm on the board.
- The TO-92 replacements have a different pinout from the ZTX parts. Check datasheets against the PCB.

### LF response trim (S4 note)
C18/C22 may be bypassed with 330nF–510nF, or changed to 2.2µF–3.3µF, to fine-adjust low-frequency response.

### Convert disc input to line input (S2)
For use with an external phono preamp. Output 500mV or 300mV sensitivity.
- Main board, per channel: R41/R43 → 39k, one end to C27/C29, other end wired to the RCA input terminal; remove C26/C28; C27/C29 → 680nF; R42/R44 → 10k (500mV) or 18k (300mV).
- Disc module: disconnect the flat cable and the two short signal leads from the RCA terminals. Refit the module with the flat cable folded under it. Solder the new wires to the white (L) and red (R) RCA terminals, and add a ground wire from the RCA negatives to the nearby ground terminal.
- Test per S2 p2: volume at zero, select Disc, raise one notch with a line-level source connected.

## Reference performance (S8 p20, S11 p16)

| Module | Sensitivity | Max input | A-weighted noise (S11, vol max) | S8 test: A-wtd / flat S/N at vol 21 |
|---|---|---|---|---|
| MM 3mV | 3mV | 135mV | 75dB | 75 / 65 dB |
| MC 100µV | 100µV | — | — | 68 / 53 dB |
| MC 200µV | 200µV | 9mV | 72dB | 72 / 57 dB |

RIAA accuracy ±0.5dB, 30Hz–20kHz (S11).

## Checks after work
See `tests.md`.
