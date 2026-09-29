# Quad 606 — amplifier boards

**Status:** draft; all values provisional (unverified against a physical board).

The two amplifier boards are identical, one per channel, so every quantity in `../../data/quad-606-bom.csv` is for both boards. Do one board at a time and use the other as a reference for polarity and position (Q606-S01 p7).

## Applicability

- MK I and MK II use the same board recap; MK II already has the input/feedback update (Q606-S01 p11).
- The service-manual PCB layouts are drawn **from the copper (track) side**, not the component side (Q606-S01 p7). The PCB issue number is on the copper side.
- Stop and ask if the board has previous repairs, non-original parts, or values that differ from the table.

## Restoration (both variants) — DADA basic kit

| Ref | Quad original (Q606-S02 p21) | DADA replacement (Q606-S01 p4) | Notes |
|---|---|---|---|
| C1, C4, C6 | 330 pF 10 % 50 V ceramic | 330 pF polystyrene | 6 in total |
| C7 | 47 µF 20 % 63 V, 5 mm pitch | 100 µF 63 V | Check the new part fits 5 mm pitch |
| C9 | printed "200 µF" −10/+50 % 63 V, part no. C220UTA | 470 µF 63 V | The part number and C11 suggest 220 µF; "200" looks like a misprint. The replacement is the same either way. |
| C11 | 220 µF −10/+50 % 63 V | 470 µF 63 V | |

Watch electrolytic polarity (Q606-S01 p13 explains the markings). Re-check both sides of the board for polarity and solder bridges when finished (Q606-S01 p9).

## Zener decoupling (added parts, both variants)

DADA adds 8 × 100 nF ceramic capacitors (4 per board) across zener diodes D1, D2, D12 and across C7, soldered on the **copper side**. They are additions, not replacements: **do not remove the zeners or C7** (Q606-S01 p4, p7). Quad lists D1, D2, D12 as 6V8 500 mW zeners (Q606-S02 p22–23).

## MK I input/feedback update (MK I only)

DADA brings the MK I input and feedback circuit to MK II values "like Quad did in the 606 MKII" (Q606-S01 p1). This is a circuit change, not like-for-like.

| Ref | Quad MK I original | DADA value | Source |
|---|---|---|---|
| R5 | 120 kΩ 5 % 0.25 W carbon film (Q606-S02 p20) | 62 kΩ 1 % | Q606-S01 p4 |
| C2 | 100 nF 10 % 100 V (Q606-S02 p21) | 330 nF MKT | Q606-S01 p4 |
| C3 | 680 nF 10 % 63 V (Q606-S02 p21) | 1 µF MKT | Q606-S01 p4 |

## Input sensitivity (optional modification)

R11 sets input sensitivity by changing local feedback in the input circuit (Q606-S01 p1, p8). Quad fitted 7R5 1 % metal film from about S/N 2000 (9R1 before; sometimes 39 Ω in parallel) for 140 W at 0.5 V input (Q606-S02 p12, p20).

| R11 | Sensitivity | Source |
|---|---|---|
| Leave as fitted (7R5) | 500 mV | Q606-S01 p8 |
| 12 Ω 1 % | 775 mV (0 dBm) | Q606-S01 p4, p8 |
| 15 Ω 1 % | 1000 mV (professional use) | Q606-S01 p4, p8 |

Explain the trade-off to the user: higher sensitivity figures mean the amplifier needs more input voltage for full power; DADA says it improves signal-to-noise and suits modern sources (Q606-S01 p1). Their preamp must be able to drive it.

## MK I rewiring and input sockets

DADA's basic kit also replaces the RCA input sockets, the input screened cable and, in the MK I only, all internal wiring with 0.75 mm² cable colour-coded red (+50 V), black (−50 V), orange (output and PSU earth), yellow (loudspeaker outputs) (Q606-S01 p4–5). **Never swap the + and − supply leads to the boards; it destroys the output transistors** (Q606-S01 p6). MK II wiring does not need replacing (Q606-S01 p11). Supply wiring is technician work.

## Transistors

Not part of the recap. If driver or output transistors are ever replaced, new thermal pads must be fitted — never reuse the old ones — and the Belleville washers refitted (Q606-S02 p9).

## After the work

See `tests.md`.
