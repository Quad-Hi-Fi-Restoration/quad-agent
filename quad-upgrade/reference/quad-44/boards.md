# Quad 44 — boards

**Status:** draft; all values provisional. Original values and replacements are from DADA's kit lists (Q44-S01 p2–3) unless stated.

DADA's recap replaces every electrolytic capacitor, every op-amp and the four electronic switch ICs (Q44-S01 p2). **Most boards have no + or − marking for capacitors.** Note or photograph each capacitor's polarity and each op-amp's pin 1 before removing it; a pencil mark on the board helps (Q44-S01 p4). Replace parts one at a time.

Access: remove the cover and the input modules, then the white plastic locator and the cardboard from the module rack. The motherboard can be removed for easier access; the tone board can be worked on in place. Above S/N 23,000, IC701 is easier to reach with the front and the plastic on/off switch rod removed (Q44-S01 p4).

## Motherboard and power supply (all kits)

| Ref | Quad original | DADA replacement | Notes |
|---|---|---|---|
| C402, C403 | 47 µF 63 V | 47 µF 63 V | |
| C404, C405 | 1000 µF axial | 1000 µF 25 V axial (Kit I: axial or radial) | |
| C407 (Kit II, III) | 100 µF 16 V | 100 µF 16 V | |
| IC400–IC403 | 4066 electronic switches | CD4066 (DADA writes "CDC4066BNC") | 4 in total |
| Added | — | 4.7 µF 63 V axial across the +8.5 V and −7.5 V rails, back of the motherboard | Quad TI 003 fix for erratic switching; placement photo in Q44-S01 p6 and Q44-S02 p45 |

Quad's TI 003 also says to resolder both sides of the 10 feed-through pins marked D, E, +, −, B, C, H, G, F and A, ideally replacing them with tinned copper wire (Q44-S02 p45).

**Only if the relay rattles at switch-on:** R400, R405 → 1 Ω and R402, R403 → 1500 Ω. The resistors are in DADA's kit but only needed for this fault (Q44-S01 p7). The original values are not in the sources read so far.

## Tone-control board

| Kit | Ref | Quad original | DADA replacement |
|---|---|---|---|
| I, II | 4 op-amps | TL071 | OPA604 or LME49710 |
| I, II | C522, C523 | 100 µF 6.3 V | 100 µF 10 V |
| I | C528 | 47 µF 40 V | 47 µF 63 V |
| III | 5 dual op-amps | TL072 | OPA2604 or LME49720 |
| III | C702, C703, C706, C707, C731, C735 | 100 µF 6.3 V | 100 µF 10 V |

If modern op-amps oscillate at low frequency, add 100 nF from pin 3 to pin 7 and pin 3 to pin 4 at IC500 and IC501; above S/N 23,000 (dual op-amps) at IC700a and IC701a, pin 3 to 4 and pin 3 to 8 (Q44-S01 p7).

**Optional, Model I before S/N 2401 only:** to make volume position zero nearly silent (−72 dB), change R500, R501 from 22K to 6K8 and R502, R503 from 6K8 to 2K2 (Q44-S01 p7).

## Input modules

| Module | Board | Quad original | DADA replacement |
|---|---|---|---|
| Tape (two modules) | M12496 iss 3 | 4 × TL071 in total; C3, C4 100 µF 6.3 V (4 in total) | OPA604 or LME49710; 100 µF 10 V |
| Disc | M12515 iss 5 | 2 × TL071; C316, C317 2.2 µF 50 V | OPA604 or LME49710; 2.2 µF 50 V |
| Radio | M12511 iss 1 (Kit I, II) or iss 2 (Kit III) | 2 × TL071 (DADA's Kit I list says 4, for two radio boards) | OPA604 or LME49710 |
| AUX (Kit II) | M12511 iss 2 | 2 × TL071 | OPA604 or LME49710 |
| CD/AUX (Kit III) | M12815 iss 1 | 1 × TL072 | OPA2604 or LME49720 |

Moving-coil and other non-standard modules came in seven variants; DADA supplies a separate kit for them (Q44-S01 p1).

**Optional unity-gain change** (Q44-S01 p7): Quad added gain resistors because op-amps of the time could not run at unity gain; with modern op-amps DADA removes them to increase local feedback and lower noise and distortion.
- Radio module M12511 iss 1 and 2: remove R204, R205; replace R202, R203 with wire links.
- AUX module M12511 iss 2: remove R606, R607; replace R604, R605 with wire links.

## After the work

See `tests.md`.
