# Contributing

## The one rule

**No value goes in without a source.** Every row in a BOM CSV and every value in a reference file must cite where it came from: document title, revision/date if known, and page or section.

## Status values

| status | meaning | appears on shopping list? |
|---|---|---|
| `template` | placeholder, not filled in yet | no |
| `unverified` | taken from a source but not yet cross-checked | yes, marked PROVISIONAL |
| `verified` | cross-checked against a physical board (or a second independent source) | yes, as confirmed |
| `conflict` | sources disagree, or one source shows two values — note both in `notes` | no — listed under "Needs resolving" |

## Where source documents live

Put your local copies of service manuals, factory update sheets and community upgrade sheets in `source-docs/<model>/`. That folder is git-ignored so nothing gets published by accident. Only commit a document there if you have permission from whoever owns it.

## Distilling documents with Claude Code

Open the repo in Claude Code and use a prompt like this:

> Read every document in `source-docs/quad-34/`. For the phono stage board, extract each component: circuit reference, function, original value and type, voltage rating, and any recommended replacement. Add them to `quad-upgrade/data/quad-34-bom.csv` with `status=unverified` and a `source` giving document title and page. Where two documents disagree, set `status=conflict` and record both values in `notes`. Do not guess anything that isn't in the documents. Then update `quad-upgrade/reference/quad-34/phono-stage.md` to match and run `python scripts/build_shopping_list.py`.

Then check the rows yourself against the board and promote them to `verified`.

## Adding a new model

1. Create `quad-upgrade/reference/<model>/` with an `overview.md` and one file per board (copy the Quad 34 files as templates).
2. Create `quad-upgrade/data/<model>-bom.csv` with the same header.
3. Add the model to `quad-upgrade/reference/index.md`.

## Credits

Add a line to the credits table in `quad-upgrade/reference/index.md` for every upgrade sheet or person whose work you use.
