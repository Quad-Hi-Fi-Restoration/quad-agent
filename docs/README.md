# Project site

This is a dependency-free static landing page, ready for GitHub Pages. It follows the archive pattern of an introduction, model guide cards, provenance and community contribution links. Model status and safety wording should stay aligned with the repository README and reference files.

## Preview locally

From the repository root, run the command for your system:

```powershell
# Windows PowerShell
py -3 -m http.server 8000 --directory docs

# macOS or Linux
python3 -m http.server 8000 --directory docs
```

Then open `http://localhost:8000/` in a browser. Stop the server with Ctrl+C. Python 3.10 or newer is required; if neither command is available, install Python and reopen the terminal.

## Publish with GitHub Pages

After reviewing the page and merging it to the repository's default branch, a repository maintainer can enable Pages in **Settings → Pages** and choose **Deploy from a branch**, the default branch, and the `/docs` folder. GitHub Pages then serves the site under the repository's Pages address. This repository does not currently configure automatic publishing.

Keep third-party source files out of this site unless redistribution rights have been checked. Link to the source register and published project guidance instead of copying unreviewed material into `docs/`.
