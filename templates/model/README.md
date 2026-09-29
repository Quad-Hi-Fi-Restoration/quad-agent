# New model starter files

Use these files to start a new model. Copy `overview.md`, `source-register.md`, and `verification-log.md` into `quad-upgrade/reference/<model>/`. Copy `tests-template.md` there as `tests.md`. Duplicate `board-template.md` once per board or restoration task and give each copy a descriptive filename, such as `power-supply.md`. Copy `bom-template.csv` to `quad-upgrade/data/<model>-bom.csv`. Replace every bracketed prompt. Keep the model marked **planned** until source-backed references and the BOM have been reviewed.

## Before writing repair instructions

1. Inventory the sources in `source-register.md`. Give new source IDs a model prefix, such as `Q33-S01` or `Q303-S01`, so citations cannot be confused with another model's IDs.
2. Identify model revisions and serial-number boundaries from primary service documents. If documents disagree, record the conflict instead of choosing a value.
3. Make an overview, a separate file for each distinct board/task, a test record, and a verification log. Only a person competent to work safely inside mains equipment may perform a physical board check; beginners must leave it to a qualified technician. Use `template` or `unverified` BOM status until a source or physical board supports a claim.
4. Put source documents in `source-docs/quad-<model>/`.
5. Add the model to `quad-upgrade/reference/index.md` and run the repository check.

## Files

- `overview.md` — identification, variants, and navigation.
- `board-template.md` — duplicate once per board or restoration task.
- `tests-template.md` — safe, source-cited checks after work.
- `verification-log.md` — dated physical board observations; required before any BOM row can be marked verified.
- `bom-template.csv` — exact column header required by the shopping-list builder.
- `source-register.md` — source identity and citations.
