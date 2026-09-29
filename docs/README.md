# Project site

This is a dependency-free static landing page, ready for GitHub Pages. It follows the archive pattern of an introduction, model guide cards, provenance and community contribution links. Model status and safety wording should stay aligned with the repository README and reference files.

## Model pages

`docs/models/<model>.html` are generated from the skill by `scripts/build_site.py`: the introduction and identification table come from each model's `overview.md`, the document list from its `source-register.md`, and the parts tables from its BOM. Do not edit them by hand. After changing a guide, BOM or source register, rebuild them from the repository root:

```
# Windows PowerShell
py -3 scripts/build_site.py

# macOS or Linux
python3 scripts/build_site.py
```

`scripts/check_repo.py` fails if a page is out of date.

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
