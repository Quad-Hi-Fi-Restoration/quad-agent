# Index

## Supported models

| Model | Status | Folder | BOM |
|---|---|---|---|
| Quad 34 preamplifier | Draft restoration and phono coverage; not user- or bench-tested. No BOM rows have physical board verification yet; source disagreements are flagged. | `quad-34/` | `../data/quad-34-bom.csv` |
| Quad 33, 303, 405 / 405-2, 306, 606 | Planned; source documents are in `source-docs/` but guides are not written yet | — | — |

If a user's model isn't supported yet, say so. You can still help with general practice and safety, but do not supply component values.

The current QUAD 33 and 303 source inventory is in [`../../source-docs/research-register.md`](../../source-docs/research-register.md). Those PDFs are not included in this skill bundle, and having the documents does not make a model supported until its guide is written.

## Quad 34 files

| File | Covers |
|---|---|
| `quad-34/overview.md` | Serial ranges, board map, disassembly, known faults |
| `quad-34/phono-stage.md` | MM and MC disc modules, RIAA stage, phono mods, disc-to-line conversion |
| `quad-34/recap-kit.md` | Whole-board recap and op-amp upgrade (DADA kit), polarity traps |
| `quad-34/power-supply.md` | PSU overview and technician-only internal reference |
| `quad-34/line-tone-filter.md` | Output level, balance control repair, op-amp decoupling |
| `quad-34/tests.md` | Checks after work, Quad test procedure and specifications |
| `quad-34/fault-finding.md` | Quad's fault diagnoses (S8) |
| `quad-34/verification-log.md` | Dated, serial-specific board checks and test observations |
| `quad-34/images/phono-module-silkscreen-M12728.png` | Solder-side component map of the disc module (S10) |
| `glossary.md` | Beginner definitions for component and restoration terms |

## Source documents

| ID | Title | Author / origin | Date | Repository copy or original source |
|---|---|---|---|---|
| S1 | Quad 34 circuit diagram M12746 issue 5 (PCB M12730 issue 6) | Quad Electroacoustics | — | `source-docs/quad-34/Quad 34 Service Data diagram issue 5.pdf` |
| S2 | Converting the Phono input of the Quad 34 to a 300 (or 500) mV line input | Author not stated | — | `source-docs/quad-34/Quad 34 -adapt Phono module for Line Input.pdf` |
| S3 | Quad 34 DIY illustrated guidelines v3.7 | DADA Electronics (Stefaan & Joost) | May 2022 | `source-docs/quad-34/Quad_34_Revision_version_3.7.pdf`; [DADA mirror](https://dadaelectronics.com.au/doc/Audio/dadaelectronics.eu/downloads/Dada%20Service%20Kit%20Instructions/Quad_34_Revision_version_3.7.pdf) |
| S4 | Quad 34 RIAA — Moving Coil disc module modification | K. Snook | June 2007 | `source-docs/quad-34/QUAD-34-MC-input-mods.pdf` |
| S5 | QUAD 34 Pre Amplifier Modification and Information | K. Snook | Updated 18 Mar 2026 | [keith-snook.info](https://keith-snook.info/quad-34-pre-amplifier.html) |
| S6 | Quad 34 circuit diagram M12746 issue 3 — from S/N 8001, PCB M12730 issue 5 | Quad Electroacoustics | — | `source-docs/quad-34/Quad-34-MK2-Schematic.pdf` |
| S7 | QUAD 34 schematic, redrawn — circuit M12746 issue 2 onward, serial 6001–8000, plus input-buffer information | K. Snook | — | [keith-snook.info PDF](https://keith-snook.info/schematic/QUAD-34-Schematic.pdf) |
| S8 | **Quad 34 service data**: circuit description, fault finding, test procedure, modifications, parts list, and three circuit diagrams | Quad Electroacoustics | — | `source-docs/quad-34/quad_34_service_data_manual[1582].pdf`; [online copy](https://www.meridian-audio.info/public/quad_34_service_data_manual%5B1582%5D.pdf) |
| S9 | RATA upgrade data sheet — Quad 34 preamp upgrade (two pages) | Russ Andrews Turntable Accessories | January 1993 | `source-docs/quad-34/QUAD 34 (1 of 2) upgrade data sheet.jpg`; `source-docs/quad-34/QUAD 34 (2 of 2) upgrade data sheet.jpg` |
| S10 | Phono input module M12728 issue 1, solder side, annotated (CC0) | FRO | — | `quad-upgrade/reference/quad-34/images/phono-module-silkscreen-M12728.png` |
| S11 | Quad 34 Control Unit Instruction Book (grey, RCA version) | Quad Electroacoustics | — | `source-docs/quad-34/Quad34UserManualII.pdf`; [DADA mirror](https://dadaelectronics.com.au/doc/Audio/Quad/Quad%2034/Quad34UserManualII.pdf) |
| O1 | Maintainer's own units (Quad 34, late grey) | Physical inspection | 2026 | No repository copy |

Note: S1 (issue 5) and S6 (issue 3) depict later circuits from serial 8001. S8 contains Quad's diagrams for up to S/N 6000, 6001–8000, and from 8001. S8 is the primary reference; where another source disagrees, show the disagreement and ask for technician-confirmed board information. Do not ask an inexperienced user to open the unit to inspect it. The S6 print of diagram issue 3 omits C84, while the S8 parts list and modifications page state C84 was added at PCB issue 5 / S/N 8001. DADA's guide describes one kit for serial 1–8000 and another for 8000 onwards, overlapping at exactly 8000; have a competent restorer confirm the fitted board before choosing a kit or ordering. The S8 manual is a scan in this repository, so page images may need visual inspection rather than text search. Current source IDs S1–S11 are specific to the Quad 34; prefix IDs for future models (for example `Q33-S01` and `Q303-S01`).
## Credits

| Who | Contribution |
|---|---|
| DADA Electronics — Stefaan & Joost | Upgrade kit guidelines (S3); see source register for current link and kit-boundary note |
| Keith Snook (keith-snook.info) | MC module modification (S4); early-34 crosstalk, CD input, capacitor and LED mods (S5); C16/C17 photo in S3 |
| Author of S2 (unknown — please tell us) | Disc-to-line-input conversion |
| Russ Andrews (RATA) | 1993 upgrade data sheet (S9) |
| FRO | Phono module silkscreen image, released CC0 (S10) |
| Quad Facebook group | Collecting and sharing these documents |
