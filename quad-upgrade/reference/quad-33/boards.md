# Quad 33 — boards

**Status:** draft; all values provisional (unverified against a physical board). Original values are from Quad's components list (Q33-S02 p6–7). DADA replacement values are from Q33-S01. DADA supplies audio capacitors rated "10 V or more" and 1 % 0.5 W metal-film resistors, and says a higher voltage rating is never a problem (Q33-S01 p1).

**Order matters.** DADA's kit starts by raising the supply from 12 V to 16 V, and the pre-amp change (R300) depends on it (Q33-S01 p3, p7). Do not fit R300 = 2K7 without the 16 V supply modification, or the reverse. After the 16 V change, a technician should confirm every replacement capacitor's voltage rating suits its position.

DADA warns the old circuit boards' tracks lift easily: little heat, a desoldering pump or station, leaded solder, eye protection (Q33-S01 p1). One board at a time.

## Power supply board — 16 V modification (Q33-S01 p3)

This is a circuit modification: it raises headroom and lowers distortion, and disables the unused DC switching output on pin 4 of the output socket (Quad also dropped it from S/N 80,000, Q33-S02 p5). Remove the board (two screws) and all parts except the transformer. Do not remove PCB connector pins on early boards.

| Ref | Quad original (Q33-S02 p7) | DADA |
|---|---|---|
| R500, R501 | 120 Ω 10 % | 27 Ω |
| MR500 | LR120C 12 V zener | 16 V 1.3 W zener |
| MR501, MR502 | IS920 diode | 1N400x |
| C500, C501 | 1000 µF 25 V | 680–2200 µF 25 V radial |
| C502 | 400 µF 25 V | 1000–2200 µF 25 V axial (or radial) |
| C503, C504, MR503, R502 | MR503 IS920 listed; C503, C504, R502 not in the components list | Remove |

Rectifier and zener cathodes (banded ends) point to the middle of the board (Q33-S01 p3). Mains wiring on this board is technician work; the transformer tap must match local mains (Q33-S01 p14).

## Filter board ("motherboard" in DADA's guide)

| Ref | Quad original | DADA |
|---|---|---|
| C5, C6 | 100 µF 6.3 V (filter board, Q33-S02 p6) | 100 µF (Q33-S01 p4) |

## Amp boards (two, one per channel) (Q33-S01 p5)

| Ref | Quad original (Q33-S02 p6) | DADA |
|---|---|---|
| C401 | 2.2 µF 63 V | 2.2 or 4.7 µF radial |
| C405 | 47 µF 16 V | 47, 68 or 100 µF radial |
| C406 | 10 µF 63 V | 22 µF radial |
| TR400, TR401, TR402 | E5270 | BC550 |

**Optional gain reduction:** R411 (1K8 2 %) → 1K and R412 → 1K3. This lowers the volume/tone stage gain by about 2.5 times (about 8 dB), letting a CD player go into Radio 1 or 2 without overload, and improves signal-to-noise by about 8 dB (Q33-S01 p5, p16). Quad's list prints R412 as "407" with part number R470RJ1, which suggests 470 Ω (Q33-S02 p6). If the owner uses Quad tuners or connects the CD player to the Tape input, DADA says **not** to change the sensitivity (Q33-S01 p5).

## Pre-amp (disc) board (Q33-S01 p7)

| Ref | Quad original (Q33-S02 p7) | DADA |
|---|---|---|
| R300 | 560 Ω | 2K7 carbon — **only with the 16 V supply** |
| R305, R308 | 82K 5 % | 82K 1 % metal film (lower noise) |
| C300, C303, C307, C308 | 22 µF 40 V | 47 or 68 µF radial |
| C311, C312 | 47 µF 16 V | 47 or 68 µF radial |
| C301, C302 | 100 µF 6.3 V | 100 µF radial |
| C313 | 100 µF 16 V | 220 or 470 µF 16 V radial |
| TR300–TR303 | E5270 | BC550 |

## Disc Adaptor board (Q33-S01 p8)

The gain reduction on the amp boards also lowers phono gain. To restore it, either move the Disc Adaptor from M2 to M1 (an owner setting, Q33-S04 p8), or, if M1 is already used, raise the M1 section's gain:

| Ref (M1 position) | Quad original (Q33-S02 p6) | DADA |
|---|---|---|
| R105, R106 | 470 Ω | 560 Ω |
| R107, R108 | 220 Ω 2 % | 120 Ω |

**Optional MM loading:** R101–R104 (68K) → 47K each with 180 pF in parallel, to suit modern moving-magnet cartridges (Q33-S01 p8). Not in DADA's kit.

## Tape Adaptor board (Q33-S01 p9)

| Ref | Quad original (Q33-S02 p7) | DADA |
|---|---|---|
| R203, R204, R215, R216 | 220K 5 % | 220K 1 % metal film |
| C202, C203 | 0.68 µF 100 V (0.33 µF on early units, Q33-S02 p5) | 2.2 or 4.7 µF axial electrolytic, **+ towards TR200/TR201**; or 2.2 µF MKS/MKT film |
| TR200, TR201 | E5270 | BC550 |

DADA says the larger C202/C203 considerably improve bass response (Q33-S01 p9).

## After the work

See `tests.md`.
