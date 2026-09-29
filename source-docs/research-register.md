# Preliminary research register

This is an inventory of source documents for models not yet supported by the skill, not an endorsement of their instructions. Review each source before using it in user instructions.

## QUAD 33

Now supported; sources are registered in `quad-upgrade/reference/quad-33/source-register.md`. The inventory below is kept for history.

| ID | File | What it appears to be | Review notes | Origin |
|---|---|---|---|---|
| Q33-S01 | `quad-33/Dada - Quad_33_Revision_V2.8.pdf` | DADA Electronics illustrated upgrade guide; 17 pages; PDF metadata names Joost and records 22 May 2023 | Cover identifies v2.8, but extracted page footers say v2.7 and page 1 says 15 pages although the PDF has 17. Resolve the version/page-count discrepancy before citing an instruction. Treat its power-supply and circuit changes as modifications, not routine restoration. | DADA Electronics |
| Q33-S02 | `quad-33/QUAD 33 Instruction Booklet.pdf` | QUAD 33 user instruction booklet; 25 pages | Sourced through ManualsLib metadata. Useful for operation and external identification; not a substitute for service data. | QUAD document, via ManualsLib |
| Q33-S03 | `quad-33/Quad 33 Switching.pdf` | Mono/stereo switching note; 3 pages; PDF metadata names Joost Plugge and date 13 June 2026 | Author says its diagram is based on the circuit above serial 11,500, describes differences below 7,500, and flags a Vintage-Radio.net diagram credited to user Trigon. Compare against the official service data before using. | Community material (Joost Plugge; diagram credited to Trigon) |
| Q33-S04 | `quad-33/Quad Document -33-Service-Manual.pdf` | QUAD 33 service data; 10 pages | Scanned pages include service information, parts lists, diagrams and board views. Verify scan legibility at full size before transcribing. | QUAD document |
| Q33-S05 | `quad-33/Quad-33-M12065-iss-2-Schematic.pdf` | M12065 issue 2 schematic; one scanned page | Verify exact revision, applicability and drawing legibility against the service data. | Origin not recorded |
| Q33-S06 | `quad-33/Quad-33-Schematic-all-versions.pdf` | Multi-version schematic sheet; one scanned page | Verify each circuit's serial range and identify the source of the drawing before extracting values. | Origin not recorded |

## QUAD 303

Now supported (limited); sources are registered in `quad-upgrade/reference/quad-303/source-register.md`. The inventory below is kept for history.

| ID | File | What it appears to be | Review notes | Origin |
|---|---|---|---|---|
| Q303-S01 | `quad-303/303 Output Cap Frequency Responce.pdf` | One-page response comparison, apparently generated with LibreOffice Calc | Author and assumptions are not identified in the PDF metadata. Treat all results as unverified calculations until the circuit model, load assumptions and method are documented. | Author not identified |
| Q303-S02 | `quad-303/Quad 303 DIY Changing the sensitivity V1.0.pdf` | Three-page sensitivity modification note; author Joost Plugge; dated 20 March 2026 | Provides theoretical and practical R108/C103 pairs and a bandwidth rationale. This is modification guidance; do not turn it into a default recap or beginner soldering procedure. Check against the applicable board and service schematic. | Joost Plugge |
| Q303-S03 | `quad-303/QUAD 303 Service Supplement Manual.pdf` | QUAD 303 service supplement; 29 pages | Scanned document with parts lists, diagrams, board photographs and test information. Page images need full-size reading before any component data is transcribed. PDF metadata identifies ManualsLib as the download source. | QUAD document, via ManualsLib |
| Q303-S04 | `quad-303/Quad-303-improved-wiring.pdf` | One-page wiring drawing | Scanned image; author, evidence and intended board revision are not identified. Do not present the change as factory wiring without corroboration. | Origin not recorded |
| Q303-S05 | `quad-303/Quad-303-MK2-M12160-iss-1-Schematic.pdf` | M12160 issue 1 schematic; one scanned page | Verify its model/revision applicability and compare against service supplement before using it for a variant-specific instruction. | Origin not recorded |

## Current use boundary


Supported models are listed in `quad-upgrade/reference/index.md`. Any model listed here without a guide remains unsupported until their source versions, serial/revision applicability, component claims and safety procedures have been reviewed. Do not cite them as supported skill sources or give component values or repair steps for these models based only on this inventory.
