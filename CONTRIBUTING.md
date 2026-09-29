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

## Source documents and permissions

This repository already tracks QUAD 34 source documents under `source-docs/`; they are visible to anyone who can access the repository. A document being available online does not mean it can be redistributed. The source index records what is known about each copy. Do not add another source file to a tracked folder unless you have permission to publish it or it has a clear reuse licence.

For research copies that are not cleared for redistribution, use `source-docs/inbox/<model>/` or the ignored `source-docs/quad-<model>/` research collections. Those files stay on your computer by default. Record the document title, author, edition/date, original URL or owner, and page numbers while extracting facts. Cite the source in the reference/BOM and leave the copy local unless permission is established. If an individual file is later cleared for redistribution, explicitly force-add only that file (`git add -f <path>`) and update the source register; never force-add an entire research folder.

## Distilling documents with an AI assistant

Give an AI assistant access to the repository files and use a prompt like this:

> Read every document in `source-docs/quad-34/`. For the phono stage board, extract each component: circuit reference, function, original value and type, voltage rating, and any recommended replacement. Add them to `quad-upgrade/data/quad-34-bom.csv` with `status=unverified` and a `source` giving document title and page. Where two documents disagree, set `status=conflict` and record both values in `notes`. Do not guess anything that isn't in the documents. Then update `quad-upgrade/reference/quad-34/phono-stage.md` to match and run the shopping-list builder using the command for your platform above.

Only a person competent to work safely inside mains equipment should inspect a physical board. Do not open, probe or photograph a unit just to complete this step if you are inexperienced; work with a qualified technician. The restorer should record the inspection in the model verification log before promoting a row to `verified`. A second document can strengthen a claim, but does not by itself count as physical board verification. For anything not legible in the source scan, mark it as unresolved; do not reconstruct it from guesswork.

## Adding a new model

1. Copy `overview.md`, `source-register.md`, and `verification-log.md` from `templates/model/` into `quad-upgrade/reference/<model>/`. Copy `tests-template.md` there as `tests.md`; duplicate and rename `board-template.md` for each board or task.
2. Create `quad-upgrade/data/<model>-bom.csv` from `templates/model/bom-template.csv`; retain the column names so the shopping-list builder can process it.
3. Add a source entry to `quad-upgrade/reference/index.md` for every technical claim and identify copyright/redistribution status.
4. Add the model and folder map to `quad-upgrade/reference/index.md`; keep the model marked planned until its sources and references are reviewed.
5. Run the shopping-list builder for your model and `check_repo.py` using the commands for your platform above.

## Credits

Add a line to the credits table in `quad-upgrade/reference/index.md` for every upgrade sheet or person whose work you use.
