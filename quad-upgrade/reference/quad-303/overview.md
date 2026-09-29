# Quad 303 — overview

**Status:** draft. Built from DADA's upgrade guide (Q303-S06) and Quad's service supplement (Q303-S01). Not user- or bench-tested; no BOM rows physically verified.

The 303 is Quad's first transistor power amplifier, usually paired with the 33. It has two identical amplifier circuits and a common regulated power supply. Each channel's circuitry, except the output transistors and its 2000 µF output capacitor, is on a hinged driver board (M12038); the regulator is on board M12035. The bottom transistors on the heatsink and the board nearest the front panel are the left channel (Q303-S01 p5). The regulated supply is set to 67 V DC (Q303-S01 p6). **The reservoir and output capacitors hold a lot of energy after switch-off.** Follow `../safety.md`; beginners should leave internal work, adjustment and first power-up to a qualified technician.

## Identify the unit (from the outside)

| Ask / inspect | Why it matters | Source |
|---|---|---|
| Serial number | From S/N 11,500, Tr107 replaced MR103/MR104 in the bias circuit; DADA supplies a different RV101 below 11,500 | Q303-S01 p9; Q303-S06 p1, p4 |
| Mains voltage setting | Must match local mains before power-up | Q303-S01 p6 |
| Loudspeakers used | Quad ESL loudspeakers before serial 16800 need a modification before use with the 303 | Q33-S04 p8 |
| Preamp used | The standard 0.5 V sensitivity suits the Quad 33; a sensitivity change is optional (`amplifier.md`) | Q303-S02 p1 |
| Previous repairs | Board may differ from the factory list; Quad says values vary slightly with age | Q303-S01 p10 |

## Versions

DADA says there are three versions of the 303; the first two (up to S/N 11,500) have different driver boards, so the matching schematic must be used (Q303-S06 p1). One DADA kit covers all versions; only RV101 differs (Q303-S06 p1, p4). **DADA does not advise revising driver boards older than version 9** (M12038 issue 9): board quality is often poor and the circuit differs. It suggests its replacement "HE" driver boards instead (Q303-S06 p1, p10). A unit can even have mixed issue 5 and issue 9 boards (Q303-S06 p11). A technician should read the board issue.

## Factory changes (Q303-S01 p9)

| Change |
|---|
| From S/N 11,500: Tr107 and its components replaced MR103/MR104, so RV101 (quiescent current) can vary the voltage between Tr103 and Tr104 bases without altering Tr102 collector current |
| R202 changed from 6K8 to 8K2 (regulator board) |

## Board map

| Board or task | Reference file | Scope |
|---|---|---|
| Driver boards, regulator and power supply | `amplifier.md` | DADA kit recap, capacitors, trimmers, rewiring, sensitivity option, calibration |
| Checks after work | `tests.md` | Quad's setting-up figures |

## Known faults (Q303-S01 p6–7)

| Symptom | Cause / check | Who |
|---|---|---|
| No sound: is it the 303 or the preamp? | Remove the signal lead and touch the live input pins (1 and 3) with a simple probe; a fairly substantial hum from both channels means the 303 is working | Technician (the probe touches a live input) |
| Output centre point (A) wrong | If RV100 sets point A correctly, the transistors are probably working; Quad describes further checks by shorting Tr102 or Tr101 base to earth | Technician |
| Open-circuit MR103 or MR104 | Likely damage to Tr102–Tr106, Tr1, Tr2; also check the power supply and regulator | Technician |
| Intermittent faults in a 33/303 system | Plug-in board edge-connector contacts (33) | Technician |
