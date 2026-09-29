"""Build one owner-friendly web page per supported model into docs/models/.

Each page is generated from the repository so it stays in step with the skill:
  - model name and status from quad-upgrade/reference/index.md
  - introduction and identification table from the model's overview.md
  - documents from the model's source-register.md (files in source-docs/)
  - parts from quad-upgrade/data/<model>-bom.csv

Run from the repository root:
  Windows: py -3 scripts/build_site.py [--check]
  macOS/Linux: python3 scripts/build_site.py [--check]
--check fails if a generated page is missing or out of date.
"""
import argparse
import csv
import html
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "quad-upgrade"
REF = SKILL / "reference"
DATA = SKILL / "data"
OUT = ROOT / "docs" / "models"
REPO = "https://github.com/Quad-Hi-Fi-Restoration/quad-agent"

CITATION = re.compile(r"\s*\((?:[A-Z][A-Z0-9]*-)?[SO]\d{1,3}\b[^()]*\)")
CATEGORY_NAMES = {
    "restoration": "Recap and restoration",
}


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def inline(md: str) -> str:
    """Convert the small amount of inline Markdown used in the reference files."""
    text = CITATION.sub("", md).strip()
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def table_rows(block: str):
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|") or set(line) <= set("|-: "):
            continue
        rows.append([cell.strip() for cell in line.strip("|").split("|")])
    return rows


def section(md: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}[^\n]*\n(.*?)(?=^## |\Z)", md, re.S | re.M)
    return match.group(1) if match else ""


def models():
    index = (REF / "index.md").read_text(encoding="utf-8")
    for row in table_rows(section(index, "Supported models"))[1:]:
        folder = re.search(r"`(quad-[^/`]+)/`", row[2]) if len(row) > 2 else None
        if folder:
            yield folder.group(1), row[0], row[1]


def intro(overview: str) -> str:
    for para in overview.split("\n\n"):
        para = para.strip()
        if para.startswith("The ") and not para.startswith("The following"):
            first = re.split(r"(?<=\.)\s+(?=\*\*|[A-Z])", para)
            keep = [s for s in first if "safety.md" not in s and "Follow" not in s]
            return inline(" ".join(keep[:3]))
    return ""


def documents(slug: str):
    register = REF / slug / "source-register.md"
    docs = []
    if not register.exists():
        return docs
    for row in table_rows(register.read_text(encoding="utf-8"))[1:]:
        if len(row) < 3:
            continue
        paths = re.findall(r"`(source-docs/[^`]+)`", " | ".join(row))
        paths = [path for path in paths if (ROOT / path).exists()]
        for n, path in enumerate(paths, start=1):
            title = CITATION.sub("", row[1]).replace("**", "")
            if len(paths) > 1:
                title += f" (file {n} of {len(paths)})"
            docs.append((row[0], title, row[2], path))
    return docs


def bom_sections(slug: str):
    bom = DATA / f"{slug}-bom.csv"
    if not bom.exists():
        return [], []
    with bom.open(encoding="utf-8-sig", newline="") as stream:
        rows = [r for r in csv.DictReader(stream) if r.get("status") != "template"]
    groups, conflicts = defaultdict(list), []
    for r in rows:
        if r["status"] == "conflict":
            conflicts.append(r)
            continue
        variant = r["variant"].strip()
        label = CATEGORY_NAMES.get(r["category"], r["category"].replace("modification-", "Optional: ").replace("repair-", "Repair: ").replace("-", " "))
        if variant and variant != "all":
            shown = f"serial {variant}" if variant.startswith(("<", ">")) else variant
            label = f"{label} — {shown} only"
        groups[(r["category"] != "restoration", label)].append(r)
    return sorted(groups.items()), conflicts


def page(slug: str, name: str, status: str) -> str:
    overview = (REF / slug / "overview.md").read_text(encoding="utf-8")
    model_no = slug.removeprefix("quad-")
    title = f"Quad {model_no}"
    ident = table_rows(section(overview, "Identify the unit"))
    docs = documents(slug)
    groups, conflicts = bom_sections(slug)
    files = sorted(p.name for p in (REF / slug).glob("*.md"))

    out = [f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Restoring a {esc(title)}: where to start, the source documents, and the provisional parts list.">
    <title>{esc(title)} restoration | Quad Agent</title>
    <link rel="stylesheet" href="../styles.css">
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
    <!-- Generated by scripts/build_site.py. Do not edit by hand. -->
    <header class="site-header">
      <a class="brand" href="../index.html" aria-label="Quad Agent home">
        <span class="brand-mark" aria-hidden="true">Q</span>
        <span class="brand-name"><strong>QUAD AGENT</strong><small>RESTORATION ARCHIVE</small></span>
      </a>
      <nav aria-label="Page sections">
        <a href="#start">Start here</a>
        <a href="#documents">Documents</a>
        <a href="#parts">Parts</a>
        <a class="nav-repo" href="../index.html#guides">All models</a>
      </nav>
    </header>

    <main id="main" class="shell model-page">
      <section class="model-hero">
        <p class="eyebrow">{esc(name.upper())}</p>
        <h1>Restoring your {esc(title)}</h1>
        <p class="model-intro">{intro(overview)}</p>
        <p class="card-caveat model-status"><strong>Status:</strong> {inline(status)}</p>
      </section>

      <section class="three-things" aria-labelledby="three-title">
        <h2 id="three-title">You work from three things</h2>
        <ol class="three-list">
          <li><strong>Your unit</strong><span>What is actually fitted wins. Quad made running changes, and earlier owners may have too.</span></li>
          <li><strong>The documents</strong><span>Quad's service data and diagrams, and the DADA and community upgrade guides, listed below.</span></li>
          <li><strong>The AI guide</strong><span>An AI assistant with the Quad Agent skill cross-checks your unit against the documents and says where they disagree.</span></li>
        </ol>
      </section>

      <section class="safety-box" aria-labelledby="safety-title">
        <h2 id="safety-title">Safety first</h2>
        <p>This unit runs from the mains and can hold a dangerous charge after it is unplugged. If you are new to electronics, use this page to plan and to talk to a qualified technician: <strong>do not open the case, solder, measure inside or power it up after work yourself.</strong> <a href="{REPO}/blob/main/quad-upgrade/reference/safety.md">Read the safety guidance</a>.</p>
      </section>

      <section id="start" aria-labelledby="start-title">
        <h2 id="start-title">Start here</h2>
        <ol class="step-list">
          <li><strong>Identify it from the outside.</strong> Note the serial number and the details in the table below. Photos of the rear label help.</li>
          <li><strong>Ask the AI guide.</strong> Load the skill into your AI assistant and paste the prompt below. It will ask you questions before giving any values.</li>
          <li><strong>Decide the job.</strong> A like-for-like recap restores the unit; the optional upgrades change how it behaves. Choose deliberately.</li>
          <li><strong>Plan the parts.</strong> Use the provisional parts list below and the documents to check it. Have the actual board checked before ordering.</li>
          <li><strong>Get the work done safely.</strong> Internal work, adjustment and first power-up belong with a competent restorer or qualified technician.</li>
        </ol>
        <div class="prompt-box">
          <p class="eyebrow">PROMPT FOR YOUR AI ASSISTANT</p>
          <p><code>Read quad-upgrade/SKILL.md and follow it to help me restore my {esc(title)}. Start by helping me identify it from the outside.</code></p>
          <p class="prompt-note">Give the assistant the <a href="{REPO}/releases/latest">skill bundle</a> or the whole <a href="{REPO}/tree/main/quad-upgrade"><code>quad-upgrade</code> folder</a>.</p>
        </div>
"""]
    if len(ident) > 1:
        out.append('        <h3>What to look at</h3>\n        <div class="table-wrap"><table>\n'
                   f'          <thead><tr><th>{inline(ident[0][0])}</th><th>{inline(ident[0][1])}</th></tr></thead>\n          <tbody>\n')
        for row in ident[1:]:
            out.append(f"            <tr><td>{inline(row[0])}</td><td>{inline(row[1]) if len(row) > 1 else ''}</td></tr>\n")
        out.append("          </tbody>\n        </table></div>\n")
    out.append("      </section>\n")

    out.append(f"""
      <section id="documents" aria-labelledby="docs-title">
        <h2 id="docs-title">The documents</h2>
        <p class="section-note">Open a document to read it online, or download it. Many are scans, so they are images rather than searchable text.</p>
        <ul class="doc-list">
""")
    for sid, title_text, author, path in docs:
        url = f"{REPO}/blob/main/{quote(path)}"
        out.append(f'          <li><span class="doc-id">{esc(sid)}</span><span class="doc-title">{inline(title_text)}</span>'
                   f'<span class="doc-author">{inline(author)}</span>'
                   f'<span class="doc-links"><a href="{url}">Open</a> · <a href="{url}?raw=true">Download</a></span></li>\n')
    if not docs:
        out.append("          <li>No documents are in the repository for this model yet.</li>\n")
    out.append(f"""        </ul>
        <p class="section-note">All files: <a href="{REPO}/tree/main/source-docs/{slug}">source-docs/{slug}</a>.</p>
      </section>

      <section id="parts" aria-labelledby="parts-title">
        <h2 id="parts-title">Parts list</h2>
        <p class="card-caveat"><strong>Provisional.</strong> Every part below comes from a named document but has not yet been checked against a real board. Have a competent restorer confirm the parts against your actual board before ordering. Optional upgrades are listed separately from the recap.</p>
""")
    for (_, label), rows in groups:
        out.append(f'        <h3>{esc(label[0].upper() + label[1:])}</h3>\n        <div class="table-wrap"><table class="parts-table">\n'
                   "          <colgroup><col class=\"c-part\"><col class=\"c-orig\"><col class=\"c-new\"><col class=\"c-qty\"><col></colgroup>\n"
                   "          <thead><tr><th>Part</th><th>Original</th><th>Replacement</th><th>Qty</th><th>Notes</th></tr></thead>\n          <tbody>\n")
        for r in rows:
            original = "not stated in the sources" if r["original_value"].strip() == "TODO" else r["original_value"]
            if r["voltage"] and r["voltage"] not in original:
                original = f"{original} {r['voltage']}".strip()
            out.append(f"            <tr><td>{esc(r['ref'].replace(';', ', '))}</td><td>{esc(original)}</td>"
                       f"<td>{esc(r['replacement_value'])}</td><td>{esc(r['qty'])}</td><td>{inline(r['notes'])}</td></tr>\n")
        out.append("          </tbody>\n        </table></div>\n")
    if conflicts:
        out.append('        <h3>Needs resolving — sources disagree, do not order</h3>\n        <ul>\n')
        for r in conflicts:
            out.append(f"          <li><strong>{esc(r['ref'])}</strong>: {inline(r['notes'])}</li>\n")
        out.append("        </ul>\n")
    if not groups and not conflicts:
        out.append("        <p>No parts list yet.</p>\n")
    out.append(f"""      </section>

      <section class="tech-files" aria-labelledby="tech-title">
        <h2 id="tech-title">For restorers and AI assistants</h2>
        <p class="section-note">The detailed reference files the AI guide works from, with page citations for every value.</p>
        <ul class="file-list">
""")
    for name_md in files:
        out.append(f'          <li><a href="{REPO}/blob/main/quad-upgrade/reference/{slug}/{name_md}">{esc(name_md)}</a></li>\n')
    out.append(f'          <li><a href="{REPO}/blob/main/quad-upgrade/data/{slug}-bom.csv">{slug}-bom.csv</a> (parts data)</li>\n')
    out.append("""        </ul>
      </section>
    </main>

    <footer class="site-footer shell">
      <div><p>An independent community project. QUAD is a trade mark of its owners; this project is not affiliated with or endorsed by Quad.</p></div>
      <div class="footer-meta"><p><a href="../index.html">Back to all models</a></p></div>
    </footer>
  </body>
</html>
""")
    return "".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if a generated page is stale")
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    stale = []
    for slug, name, status in models():
        text = page(slug, name, status)
        target = OUT / f"{slug}.html"
        if args.check:
            if not target.exists() or target.read_text(encoding="utf-8") != text:
                stale.append(target.name)
        else:
            target.write_text(text, encoding="utf-8")
            print(f"Wrote {target.relative_to(ROOT)}")
    if stale:
        print("Stale site pages (run scripts/build_site.py): " + ", ".join(stale))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
