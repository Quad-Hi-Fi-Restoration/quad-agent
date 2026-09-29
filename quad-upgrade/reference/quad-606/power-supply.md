# Quad 606 — power supply

**Status:** draft; technician-only reference. The reservoir capacitors store enough energy to injure and to destroy tools. A beginner must not open the unit or touch the power supply.

## Reservoir capacitors

DADA "strongly advises" replacing the power supply capacitors (Q606-S01 p1, p3).

| Variant | Quad original | DADA replacement | Source |
|---|---|---|---|
| MK I | C12, C13 listed as 6k8 µF 63 V, tag connection (Q606-S02 p21) | 4 × 10,000 µF 63 V (BHC/Kemet Aerovox) | Q606-S01 p3–4 |
| MK II | Not in our sources | 4 × 15,000 µF 63 V (BHC/Kemet Aerovox) | Q606-S01 p3–4 |

Quad's parts list names two references (C12, C13); DADA supplies four capacitors. The count actually fitted must be confirmed on the unit by a technician before ordering.

Procedure outline (Q606-S01 p5–6, p11) for a competent restorer:
- Photograph or note capacitor polarity before removing anything. **Reversed reservoir capacitors can explode** (Q606-S01 p5).
- MK I: remove the four mounting rings and desolder the capacitors from the pins; fit the new ones on the top plate, mounting rings secure but not over-tight.
- MK II: remove the bottom and U-shaped chassis part, the amplifier boards, the LED board and the PSU connectors (no soldering needed on the PSU), then the four posidriv screws around the transformer.
- Re-check capacitor polarity against the schematic and the wiring diagram in the service manual before connecting power.

## Transformer hum and the MK II PSU kit

Some 606s have mechanical transformer hum. Quad's suspension kit Q60SUSP (from S/N ~3000) and later mountings (S/N ~7000) addressed it (Q606-S02 p12, p14). DADA says in most cases the only cure is a toroidal transformer, as in the MK II / 707 / 909, and sells a complete MK II PSU kit (Q606-S01 p2–3). The kit's toroid is data-sheeted in Q606-S04 (Amplimo 8N1787P, 500 VA, primaries in series for 230 V; the sheet specifies time-lag primary fusing and NTC inrush resistors).

**Transformer replacement is mains wiring: qualified technician only.** Do not give primary wiring instructions to a user.

## Factory supply figures

- Supply rails approximately 53–56 V DC each side, no signal (Q606-S02 p10).
- The centre-tapped DC line (+55 V, −55 V) floats; some faults can shift it, putting up to 110 V on one side and damaging R38 and R39 (2k2) — check these during repairs (Q606-S02 p9).
- Mains fuse FS1 4 A T 20 mm at 240 V; circuit breaker 2 A at 240 V (Q606-S02 p23). Always confirm against the unit's own rear-panel marking.

## Optional

DADA sells a mono DC-protection / delay board (two needed) (Q606-S01 p4). It is an addition, not part of the recap.
