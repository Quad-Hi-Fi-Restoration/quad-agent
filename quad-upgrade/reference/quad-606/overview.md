# Quad 606 — overview

**Status:** draft. Built from the DADA upgrade guide (Q606-S01) and Quad's service data (Q606-S02). Not user- or bench-tested; no BOM rows have physical board verification.

The 606 is a two-channel current-dumping power amplifier. It runs from roughly ±55 V DC supply rails (Q606-S02 p9, p10) with large reservoir capacitors. **This is more dangerous inside than a preamplifier.** The reservoir capacitors hold a lot of energy after switch-off, and the output terminals carry high voltage when driven. Follow `../safety.md` strictly; beginners should leave all internal work, measurement and first power-up to a qualified technician.

## Identify the unit (from the outside)

| Ask / inspect | Why it matters | Source |
|---|---|---|
| Serial number | Selects MK I or MK II parts and which factory changes are already fitted | Q606-S01 p1; Q606-S02 p12 |
| Case edges: square or chamfered | Square = MK I, chamfered = MK II — but see the serial exception below | Q606-S01 p1 |
| Loudspeaker outputs: sockets or binding posts | Binding posts were fitted from about S/N 3800 | Q606-S02 p12 (mod 8) |
| Is it a 707 or 909? | DADA's 606 kit also fits these; they are essentially a 606 MK II plus the Quad Bus input | Q606-S01 p1 |
| Previous repairs, mods, transformer hum | The board may no longer match the factory build; mechanical hum points at the transformer | Q606-S01 p2 |

**Serial exception:** a square-cased unit with serial between 19900 and 21600 is an MK II — Quad ran out of chamfered cases (Q606-S01 p1, footnote). Quad itself never used the names MK I / MK II; the differences are the case, the input circuit and the power supply (Q606-S01 p1).

A technician can confirm the PCB issue number, which is marked on the copper side of each amplifier board (Q606-S01 p3, p7). DADA says to double-check the board issue rather than rely on serial number alone (Q606-S01 p3).

If serial, case and board markings disagree, stop and describe the mismatch.

## Variants

| Variant | Evidence | What changes for the recap | Confidence |
|---|---|---|---|
| MK I | Square case, serial outside 19900–21600 | Board recap plus DADA's input/feedback update (R5, C2, C3); rewire recommended; PSU caps 10,000 µF 63 V | provisional |
| MK II (also 707 / 909) | Chamfered case, or square case with serial 19900–21600 | Board recap only — the input/feedback update is already fitted; no rewire needed; PSU caps 15,000 µF 63 V | provisional |

Q606-S02 is the original (MK I) service data. We have no MK II parts list, so original MK II values are not in these sources.

## Factory changes during MK I production (Q606-S02 p12)

| Approx. S/N | Change |
|---|---|
| 1050 | R42 10 k added across T3 (back of PCB); R8 increased 180 Ω → 270 Ω (HF overload stability) |
| 1751 | Rectifier changed PM7A2Q → KBU8DX, mounted on the 'T' board with C15 and fuse |
| 2000 | R11 reduced 9R1 → 7R5 (sometimes 39 Ω across R11) to give 140 W for 0.5 V input |
| 2200 | 2 × 40 nF added on back of 'T' board, secondaries to earth (rectifier interference) |
| 3000 | New transformer mountings (kit Q60SUSP, p14) to reduce mechanical noise |
| 3200 | PCB issue 2 — R42 on component side |
| 3400 | New 'T' board: C18, C19 (2 × 470 nF) replace C15 |
| 3800 | Binding posts for loudspeaker outputs |
| 4500 | 16 SWG link across PCB track earths (p13); C20 330 nF X2 across transformer primary |
| 5700 | PCB issue 3 — better screening; R14, R15, CR1 taken to R20/R26 rail |
| 7000 | New transformer mountings and PSU chassis (mechanical hum) |

## Board map

| Board or task | Reference file | Scope |
|---|---|---|
| Amplifier (driver) boards, one per channel | `amplifier-boards.md` | Recap, MK I input/feedback update, input sensitivity, zener decoupling |
| Power supply | `power-supply.md` | Reservoir capacitors, transformer hum, MK II PSU kit — mostly technician work |
| Checks after work | `tests.md` | DADA and Quad figures |

## Known faults

| Symptom | Possible cause | Next step | Source |
|---|---|---|---|
| Mechanical hum from the transformer | Transformer laminations/mounting | Quad suspension kit Q60SUSP; DADA says the usual cure is a toroidal transformer (MK II PSU kit). Technician work. | Q606-S02 p12, p14; Q606-S01 p2 |
| Damaged R38 / R39 (2k2) | Floating ±55 V centre-tapped line can shift up to 110 V on one side under some faults | Technician should always check R38 and R39 during repairs | Q606-S02 p9 |
| Interference clicks from appliances | Pre-S/N 4500 units lack C20 and the earth link | Factory mod 9 (p12, p13) — technician work (mains primary) | Q606-S02 p12 |
