# Index

## Supported models

| Model | Status | Folder | BOM |
|---|---|---|---|
| Quad 34 preamplifier | Restoration + phono data in; all values single-source (provisional) until checked on a board | `quad-34/` | `../data/quad-34-bom.csv` |
| Quad 33, 303, 405 / 405-2, 306, 606 | Planned | — | — |

If a user's model isn't supported yet, say so. You can still help with general practice and safety, but do not supply component values.

## Quad 34 files

| File | Covers |
|---|---|
| `quad-34/overview.md` | Serial ranges, board map, disassembly, known faults |
| `quad-34/phono-stage.md` | MM and MC disc modules, RIAA stage, phono mods, disc-to-line conversion |
| `quad-34/recap-kit.md` | Whole-board recap and op-amp upgrade (DADA kit), polarity traps |
| `quad-34/power-supply.md` | PSU parts and rails |
| `quad-34/line-tone-filter.md` | Output level, balance control repair, op-amp decoupling |
| `quad-34/tests.md` | Checks after work, Quad test procedure and specifications |
| `quad-34/fault-finding.md` | Quad's fault diagnoses (S8) |
| `quad-34/images/phono-module-silkscreen-M12728.png` | Solder-side component map of the disc module (S10) |

## Source documents

| ID | Title | Author / origin | Date | File in `source-docs/quad-34/` |
|---|---|---|---|---|
| S1 | Quad 34 circuit diagram M12746 issue 5 (PCB M12730 issue 6) | Quad | — | `Quad_34_Service_Data_diagram_issue_5.pdf` |
| S2 | Converting the Phono input of the Quad 34 to a 300 (or 500) mV line input | Not stated | — | `Quad_34_-adapt_Phono_module_for_Line_Input.pdf` |
| S3 | Quad 34 DIY illustrated guidelines v3.7 | DADA Electronics (Stefaan & Joost) | May 2022 | `Quad_34_Revision_version_3_7.pdf` |
| S4 | Quad 34 RIAA — Moving Coil disc module modification | K. Snook | June 2007 | `QUAD-34-MC-input-mods.pdf` |
| S6 | Quad 34 service data p32: circuit diagram M12746 issue 3 — "From S/N 8001, PCB M12730 ISS 5" | Quad | — | `Quad-34-MK2-Schematic.pdf` |
| O1 | Maintainer's own units (Quad 34, late grey) | Physical inspection | 2026 | — |
| S7 | QUAD 34 schematic, redrawn — circuit M12746 iss 2 onward, serial 6001–8000, PCB M12730 iss 4, plus input buffer info from 8001 | K. Snook | — | https://keith-snook.info/schematic/QUAD-34-Schematic.pdf |
| S8 | **Quad 34 service data** (full manual): circuit description, fault finding, test procedure, modifications (p21), complete parts list (p22–29), circuit diagrams 1 (up to S/N 6000), 2 (6001–8000), 3 (from 8001) | Quad Electroacoustics | — | `quad_34_service_data_manual_1582_.pdf` |
| S9 | RATA upgrade data sheet — Quad 34 preamp upgrade (2 pages; p2 is circuit diagram, apparently M12746 iss 4 / PCB M12730 iss 6) | Russ Andrews Turntable Accessories | January 1993 | `QUAD_34__1_of_2__upgrade_data_sheet.jpg`, `..._2_of_2_...jpg` |
| S10 | Phono input module "silkscreen" M12728 iss 1, solder side, annotated (CC0) | FRO | — | `images/phono-module-silkscreen-M12728.png` (in skill) |
| S11 | Quad 34 Control Unit Instruction Book (grey, RCA version) | Quad Electroacoustics | — | `Quad34UserManualII.pdf` |
| S5 | QUAD 34 Pre Amplifier Modification and Information (web page) | K. Snook | updated 18 Mar 2026 | https://keith-snook.info/quad-34-pre-amplifier.html |

Note: S1 (issue 5) and S6 (issue 3) both depict the later circuit, from serial 8001. S6 says "for minor variations see 'modifications'" — that page of the service manual isn't in the repo yet and is worth finding. S8 contains Quad's own diagrams for all three ranges (up to 6000, 6001–8000, from 8001), so **every serial range is now covered by a Quad source**. S8 is the primary reference; where another source disagrees with S8, say so. Note the S6 print of diagram iss 3 omits C84, but S8's parts list and modifications page say C84 was added at PCB iss 5 (S/N 8001) and S8's own print of iss 3 shows it. Earlier units (serial below 8000) differ in the line-input area. S5 describes an early unit, and Keith Snook's redrawn schematic including his mods is linked from S5 (https://keith-snook.info/schematic/QUAD-34-Schematic.pdf) — worth adding as a source for the early circuit.

## Credits

| Who | Contribution |
|---|---|
| DADA Electronics — Stefaan & Joost | Upgrade kit guidelines (S3). Original site dadaelectronics.eu appears lapsed; documents mirrored at dadaelectronics.com.au/doc/Audio/ |
| Keith Snook (keith-snook.info) | MC module modification (S4); early-34 crosstalk, CD input, capacitor and LED mods (S5); C16/C17 photo in S3 |
| Author of S2 (unknown — please tell us) | Disc-to-line-input conversion |
| Russ Andrews (RATA) | 1993 upgrade data sheet (S9) |
| FRO | Phono module silkscreen image, released CC0 (S10) |
| Quad Facebook group | Collecting and sharing these documents |
