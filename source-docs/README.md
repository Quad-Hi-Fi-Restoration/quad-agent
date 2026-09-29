# Source documents and research intake

This folder holds source material used to build and verify the restoration guides. The QUAD 34 files are tracked by Git and will be included when the repository is published. The QUAD 33, 303, 306, 405, 44 and 606 folders are ignored local research collections; Git will not include them in a commit by default.

The project licence does not apply to third-party source documents. Online availability is not evidence of redistribution permission. The current QUAD 34 source list and rights notes are in [`quad-upgrade/reference/index.md`](../quad-upgrade/reference/index.md); the preliminary inventory for newer research is in [`research-register.md`](research-register.md).

## Adding or reviewing research

Keep a local copy until its provenance and redistribution rights are understood. Record the exact title, author or publisher, revision/date, original URL, relevant pages, file type, and permission or licence status. Do not commit or redistribute material just because it was downloadable. If permission is unknown, cite the source and page in the public guide without including the file.

Use `inbox/` for private copies that should remain ignored by Git. The model folders listed above are also ignored, so they can be reviewed in place without accidentally entering a normal `git add` or commit. Do not move or publish their contents automatically. If a specific file is cleared for redistribution, stage only that file explicitly with `git add -f <path>` and record its provenance and rights in the source register first.

Some documents are scanned images. Inspect page images when text extraction is empty or unclear. Record uncertainty and source conflicts; never fill gaps by guessing.
