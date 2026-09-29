# Quad 33 — overview

**Status:** draft. Built from the DADA upgrade guide (Q33-S01) and Quad's service data (Q33-S02). Not user- or bench-tested; no BOM rows have physical board verification.

The 33 is Quad's transistor control unit (preamplifier), usually paired with the 303 power amplifier. It has plug-in boards: a Disc Adaptor board (sets the pickup input: M1 low-output magnetic, M2 high-output magnetic, C1 ceramic, S1 spare), a Tape Adaptor board, a pre-amp board, two amp (tone/volume) boards, a filter board and a power supply board (Q33-S02 p6–7; Q33-S04 p8). It runs from a low-voltage supply, but the mains is inside the case and on the rear mains outlets. Follow `../safety.md`.

## Identify the unit (from the outside)

| Ask / inspect | Why it matters | Source |
|---|---|---|
| Serial number | Places the unit in Quad's change history below | Q33-S02 p5 |
| Disc and Radio input sockets | 3-pin DIN before S/N 1225 | Q33-S02 p5 |
| Which Disc Adaptor position is in use (M1, M2, C1, S1) and the cartridge type | Decides phono gain; DADA's gain changes affect it | Q33-S04 p8; Q33-S01 p8 |
| Tape Adaptor screw settings | Sets tape levels; DADA leaves this as an owner setting | Q33-S04 p11; Q33-S01 p10 |
| Sources used (CD, streamer, tuner) and power amp | DADA's gain reduction is aimed at modern line sources | Q33-S01 p5 |
| Mains voltage marked on the rear | The transformer tap must match local mains | Q33-S04 p14; Q33-S01 p14 |
| Previous repairs or upgrades | Boards may no longer match the factory lists | — |

The Disc and Tape Adaptor boards are plug-in parts that Quad's booklet expects owners to set (Q33-S04 p8, p11). Anything beyond those, including reading board numbers, is technician work.

## Factory changes (Q33-S02 p5)

| Approx. S/N | Change |
|---|---|
| before 1225 | Disc and Radio inputs on old 3-pin DIN sockets |
| before 7500 | Radio 2 and Tape replay had no two-channel mono switching |
| 21,913 | Disc pre-amp and amp board edge connectors changed |
| — | C202, C203 increased from 0.33 µF to 0.68 µF |
| 41,000 (March 1974) | Disc and Tape Adaptor edge connectors changed |
| 71,000 | Shroud added to the mains outlet sockets |
| 80,000 | DC supply removed from pin 4 of the signal output socket |

Early white-bodied edge connectors are known for intermittent contact that looks like switch or solder faults; Quad describes closing the socket contacts gently (Q33-S02 p4). The pushbutton switches are also a common source of trouble: a signal passes through many contacts in series (Q33-S03 p1).

## Board map

| Board or task | Reference file | Scope |
|---|---|---|
| All boards | `boards.md` | Power supply (16 V modification), filter board, amp boards, pre-amp board, disc and tape adaptors |
| Checks after work | `tests.md` | Figures from the booklet and DADA |

## Known faults

| Symptom | Possible cause | Next step | Source |
|---|---|---|---|
| Erratic operation, crackles, channel drop-outs | Edge connector contacts (early white sockets) or pushbutton switch contacts | Technician: clean or close edge-connector contacts; switch cleaning | Q33-S02 p4; Q33-S03 p1 |
| Hum that changes with filter setting and disappears with Cancel pressed | Filter coils picking up a nearby transformer | Move the 33 away from the power amp's transformer | Q33-S02 p4 |
| No signal at all | Control unit or power amp | Quad's quick check at the amplifier input is for a technician | Q33-S02 p4 |
| Mono/stereo behaviour seems wrong after an upgrade | Quad's input-dependent switching, not a fault | Explain the switching (Q33-S03) | Q33-S03 p1–2 |
