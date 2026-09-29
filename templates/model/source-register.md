# [MODEL] — source register

Assign each source a stable, model-prefixed ID (for example `Q33-S01`). Cite IDs plus exact page/figure/section in the reference files and BOM. Keep rights and availability separate from technical reliability.

| ID | Title | Author / publisher | Revision / date | Original URL or archive | Local copy | Pages used | Technical role | Licence / permission to redistribute | Notes |
|---|---|---|---|---|---|---|---|---|---|
| [MODEL]-S01 | [exact title] | [author] | [date/revision] | [URL] | [inbox path or none] | [pages] | [factory / service / modification / community] | [licence, permission, or unknown] | [legibility, conflicts, provenance] |

Do not treat "found online" as a redistribution licence. Keep uncleared copies in `source-docs/inbox/<model>/` and out of Git.

## Physical board observations

Only a person competent to work safely inside mains-powered equipment should inspect a physical board. Beginners should have a qualified technician perform this check. Assign each completed physical observation a unique, model-prefixed ID (for example `Q33-O01`). Declare the ID here and use it in a level-three heading (`### Q33-O01`) in that model's `verification-log.md`. A BOM row may be marked `verified` only if its `source` cites a recorded observation that actually checked the relevant component or claim. A second document alone does not count as physical verification.

| ID | Model / serial | Board revision | Date | Verification-log heading | What this observation checks |
|---|---|---|---|---|---|
| [MODEL]-O01 | [model and serial] | [marking] | [date] | [exact ID heading] | [specific parts / values / assembly fact checked] |
