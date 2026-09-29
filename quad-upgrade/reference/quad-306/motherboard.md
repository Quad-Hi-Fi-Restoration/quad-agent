# Quad 306 — motherboard

**Status:** draft; all values provisional. Quantities cover both channels. Quad originals from Q306-S02 p15–16; DADA values from Q306-S01 p2.

DADA's approach: remove all the parts to be replaced in one channel, then the other; clean the board (Kontakt LR); fit the new parts and double-check everything (Q306-S01 p3–4). DADA brings the input and DC-feedback circuit in line with what Quad did in the 606 MK II, 707 and 909 (Q306-S01 p1).

## Restoration

| Ref | Quad original | DADA replacement | Qty |
|---|---|---|---|
| C1, C5, C6 | 330 pF 10 % 50 V (UP125) | 330 pF polystyrene | 6 |
| C4 | 180 pF 10 % 50 V (UP125) | 180 pF polystyrene | 2 |
| C8 | 47 pF 1 % 350 V silver mica | 47 pF polystyrene | 2 |
| C7 | 47 µF 20 % 63 V | 100 µF 63 V | 2 |
| C10, C11 | 4700 µF 20 % 50 V | 6800 µF or 4700 µF, 50 V or 63 V, snap-in | 4 |

**C10/C11 are the reservoir capacitors: technician work.** The + side is marked on the board; the band on the capacitor is −. **If the polarity is wrong they will explode** (Q306-S01 p5).

Quad lists one C10 and one C11 but DADA supplies four, one pair per channel; a technician should confirm the count on the board before ordering.

## Input and DC-feedback update

| Ref | Quad original | DADA | Qty |
|---|---|---|---|
| R6 | 120K 5 % carbon film | 62K 1 % | 2 |
| C2 | 100 nF 10 % 250 V | 330 nF MKT | 2 |
| C3 | 680 nF 10 % 63 V | 1 µF MKT | 2 |

## Zener decoupling (added parts)

10 × 100 nF MKT soldered on the **copper side** across zeners D1–D4 and C7 (five per channel). They are additions: **leave the zeners and C7 in place** (Q306-S01 p2, p5).

## Input sensitivity (optional)

Quad fits R13 = 9R1 1 % metal film, giving 0.375 V for 50 W (Q306-S02 p8, p15).

| R13 | Sensitivity | Source |
|---|---|---|
| Leave as fitted (9R1) | 0.375 V | Q306-S01 p4; Q306-S02 p8 |
| 18 Ω 1 % | 0.775 V | Q306-S01 p2, p4 |
| 27 Ω 1 % | 1.0 V | Q306-S01 p2, p4 |

DADA's kit list calls these "R13b" and "R13c", but its instructions and Quad's parts list have one R13 (Q306-S01 p2, p4; Q306-S02 p15). With a Quad 33, 34, 44 or 66 preamp the owner may prefer to keep the standard sensitivity, though DADA says 0.775 V or 1.0 V usually makes the volume control more usable; with other preamps it suggests 1.0 V (Q306-S01 p4). It can be changed later.

## Loudspeaker terminals

DADA replaces the loudspeaker posts. The holes fit without drilling; each post is wired to the board. **Order: Red – Black – Black – Red** (Q306-S01 p4). Quad's parts are 4 mm sockets, red SK2 and black SK3 (Q306-S02 p14). DADA suggests cleaning the RCA input contacts with Kontakt 61 (Q306-S01 p5).

## After the work

See `tests.md`.
