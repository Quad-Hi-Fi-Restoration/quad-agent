# Contributing

## The one rule

**No value goes in without a source.** Every row in a BOM CSV and every value in a reference file must cite where it came from: document title, revision/date if known, and page or section.

## Running the repository tools

The scripts use Python 3.10 or newer and require no additional packages. Run them from the repository root. In Windows PowerShell use `py -3 scripts/<script>.py`; on macOS or Linux use `python3 scripts/<script>.py`. If neither command is available, install Python 3.10 or newer and reopen the terminal.

## Status values

| status | meaning | appears on shopping list? |
|---|---|---|
| `template` | placeholder, not filled in yet | no |
| `unverified` | supported by one or more documents but not yet checked against a physical board | yes, marked PROVISIONAL |
| `verified` | checked by a competent restorer against a documented physical board; record unit, serial, board revision, date and observation in the model verification log | yes, as physically checked |
| `conflict` | sources disagree, or one source shows two values — note both in `notes` | no — listed under "Needs resolving" |

## Source documents

Source documents live in `source-docs/<model>/` (for example `source-docs/quad-606/`). Add new ones there and record the document title, author, edition/date, where it came from, and page numbers in the source register, so the guides can cite it and its authors get credit.

## Distilling documents with an AI assistant

Give an AI assistant access to the repository files and use a prompt like this:

> Read every document in `source-docs/quad-34/`. For the phono stage board, extract each component: circuit reference, function, original value and type, voltage rating, and any recommended replacement. Add them to `quad-upgrade/data/quad-34-bom.csv` with `status=unverified` and a `source` giving document title and page. Where two documents disagree, set `status=conflict` and record both values in `notes`. Do not guess anything that isn't in the documents. Then update `quad-upgrade/reference/quad-34/phono-stage.md` to match and run the shopping-list builder using the command for your platform above.

Only a person competent to work safely inside mains equipment should inspect a physical board. Do not open, probe or photograph a unit just to complete this step if you are inexperienced; work with a qualified technician. The restorer should record the inspection in the model verification log before promoting a row to `verified`. A second document can strengthen a claim, but does not by itself count as physical board verification. For anything not legible in the source scan, mark it as unresolved; do not reconstruct it from guesswork.

## Adding a new model

1. Copy `overview.md`, `source-register.md`, and `verification-log.md` from `templates/model/` into `quad-upgrade/reference/<model>/`. Copy `tests-template.md` there as `tests.md`; duplicate and rename `board-template.md` for each board or task.
2. Create `quad-upgrade/data/<model>-bom.csv` from `templates/model/bom-template.csv`; retain the column names so the shopping-list builder can process it.
3. Add a source entry to `quad-upgrade/reference/index.md` for every technical claim, with its author and where it came from.
4. Add the model and folder map to `quad-upgrade/reference/index.md`; keep the model marked planned until its sources and references are reviewed.
5. Run the shopping-list builder for your model and `check_repo.py` using the commands for your platform above.

## Credits

Add a line to the credits table in `quad-upgrade/reference/index.md` for every upgrade sheet or person whose work you use.
