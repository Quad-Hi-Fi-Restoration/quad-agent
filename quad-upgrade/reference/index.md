# Index

## Supported models

| Model | Status | Folder | BOM |
|---|---|---|---|
| Quad 34 preamplifier | Draft restoration and phono coverage; not user- or bench-tested. No BOM rows have physical board verification yet; source disagreements are flagged. | `quad-34/` | `../data/quad-34-bom.csv` |
| Quad 606 power amplifier (MK I, MK II; DADA kit also fits 707 / 909) | Draft board recap, PSU capacitors, input sensitivity and MK I input update; not user- or bench-tested; no BOM rows physically verified. | `quad-606/` | `../data/quad-606-bom.csv` |
| Quad 33, 303, 405 / 405-2, 306, 44 | Planned; source documents are in the repository's `source-docs/` folder but guides are not written yet | — | — |

If a user's model isn't supported yet, say so. You can still help with general practice and safety, but do not supply component values.

The inventory of source documents for planned models is in [`../../source-docs/research-register.md`](../../source-docs/research-register.md). Those files are not included in this skill bundle, and having the documents does not make a model supported until its guide is written.

## What each model folder contains

| File | Covers |
|---|---|
| `overview.md` | Start here: identification from the outside, variants and serial ranges, factory changes, board map, known faults |
| Board or task files | One per board or job; the model's `overview.md` lists them in its board map |
| `tests.md` | Checks after work, with documented figures and who should do them |
| `source-register.md` | Every source for that model with its ID, where to find it, notes on conflicts, and credits |
| `verification-log.md` | Dated physical board checks; a BOM row may be `verified` only by citing an entry here |

Each model's parts data is in `../data/<model>-bom.csv`, with a generated `../data/<model>-shopping-list.md`.

## Source IDs

Cite a source by its ID and page, for example `Q606-S02 p21`. IDs are declared in the model's `source-register.md`. New models use a model prefix (`Q33-S01`, `Q405-S01`); physical observations use `O` in place of `S` (`Q606-O01`). The Quad 34's IDs are unprefixed because it was added first.

## Credits

| Who | Contribution |
|---|---|
| Quad Electroacoustics | Service data, circuit diagrams and instruction books |
| DADA Electronics — Stefaan & Joost | Illustrated upgrade kit guides for several models |
| Keith Snook (keith-snook.info) | Modification notes and redrawn schematics |
| Russ Andrews (RATA) | 1993 upgrade data sheets |
| Joost Plugge | Community modification notes |
| FRO | Annotated board image, released CC0 |
| Quad Facebook group | Collecting and sharing these documents |

Per-source credits are in each model's `source-register.md`.
