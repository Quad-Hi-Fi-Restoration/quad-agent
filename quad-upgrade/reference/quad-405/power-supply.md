# Quad 405 — power supply, wiring and connectors

**Status:** draft; technician-only reference. The reservoir capacitors store enough energy to injure and to destroy tools. A beginner must not open the unit.

## Reservoir capacitors

| Quad original | DADA replacement | Source |
|---|---|---|
| C13, C14 10,000 µF 63 V (Q405-S02 p14; 10,000 µF also on the 405-2 list, p24) | 2 × 10,000 µF 63 V (or 100 V) | Q405-S01 p2 |

A community list (Q405-S03) uses 15,000 µF 63 V instead. Physical fit must be checked by a technician.

Outline for a competent restorer (Q405-S01 p4, p7, p9):
- Note capacitor polarity before removal. **Reversed capacitors can explode** (Q405-S01 p9).
- New capacitors fit in the old rings with silicone (24 h to cure), or in DADA's optional rings, which need two 4 mm holes drilled in the bottom plate.
- Check the supply first: about ±50 V DC. The capacitors stay charged for a long time; DADA discharges them through a 1 kΩ resistor and checks with a meter (Q405-S01 p9). **Never swap the + and − leads to the boards; it destroys the output transistors** (Q405-S01 p9).

## Rewiring and connectors (DADA kit)

DADA replaces the loudspeaker terminals, RCA inputs, board connectors and all wiring on the transformer secondary side, leaving the mains-side loom and the three secondary link wires in place (Q405-S01 p4–5). Colour code: yellow AC, red +50 V, black −50 V, green earth, blue loudspeaker outputs (Q405-S01 p8). The central earth point takes four wires (Q405-S01 p9). Hot and earth loudspeaker terminals must be insulated and aligned so they cannot touch (Q405-S01 p8).

**Mains-side work, voltage selection and transformer wiring are for a qualified technician only.** Set the voltage selector for the local mains, or on units without one follow the service manual (Q405-S01 p4–5; Q405-S02 p12).

## Output protection

The 405 has no DC protection before S/N 9000; after that a clamp circuit blows the internal 4 A fuses on output DC or a short (Q405-S02 p8). DADA says there must be some DC protection: keep the clamp, or replace it with DADA's delay/DC-protection boards (two needed) (Q405-S01 p5). Quad's clamp test (Q405-S02 p5, test 13) is technician work.

## Options

DADA also sells a dual-mono supply board, a 300 VA toroidal transformer, OPA627 op-amps and MJ15003 output transistors (Q405-S01 p3). These are upgrades, not part of a recap.
