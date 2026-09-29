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


OWNERS = ROOT / "docs" / "owners"


def owner_text(slug: str) -> dict:
    """Read the plain-English page text in docs/owners/<model>.md into sections."""
    path = OWNERS / f"{slug}.md"
    if not path.exists():
        return {}
    sections, current = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    return {k: "\n".join(v).strip() for k, v in sections.items()}


def prose(md: str) -> str:
    """Render paragraphs and '- ' bullet lists from the owner text."""
    out, items = [], []
    for block in md.split("\n\n"):
        lines = [l for l in block.splitlines() if l.strip()]
        if lines and all(l.startswith("- ") for l in lines):
            out.append("<ul>" + "".join(f"<li>{inline(l[2:])}</li>" for l in lines) + "</ul>")
        elif lines:
            out.append(f"<p>{inline(' '.join(lines))}</p>")
    return "\n".join(out)


def parts_html(slug: str) -> str:
    groups, conflicts = bom_sections(slug)
    out = []
    for (_, label), rows in groups:
        out.append(f'<h4>{esc(label[0].upper() + label[1:])}</h4>\n<div class="table-wrap"><table class="parts-table">\n'
                   '<colgroup><col class="c-part"><col class="c-orig"><col class="c-new"><col class="c-qty"><col></colgroup>\n'
                   "<thead><tr><th>Part</th><th>Original</th><th>Replacement</th><th>Qty</th><th>Notes</th></tr></thead>\n<tbody>\n")
        for r in rows:
            original = "not stated in the sources" if r["original_value"].strip() == "TODO" else r["original_value"]
            if r["voltage"] and r["voltage"] not in original:
                original = f"{original} {r['voltage']}".strip()
            out.append(f"<tr><td>{esc(r['ref'].replace(';', ', '))}</td><td>{esc(original)}</td>"
                       f"<td>{esc(r['replacement_value'])}</td><td>{esc(r['qty'])}</td><td>{inline(r['notes'])}</td></tr>\n")
        out.append("</tbody>\n</table></div>\n")
    if conflicts:
        out.append("<h4>Sources disagree: do not order yet</h4>\n<ul>\n")
        for r in conflicts:
            out.append(f"<li><strong>{esc(r['ref'])}</strong>: {inline(r['notes'])}</li>\n")
        out.append("</ul>\n")
    return "".join(out) or "<p>No parts list yet.</p>\n"


def page(slug: str, name: str, status: str) -> str:
    text = owner_text(slug)
    model_no = slug.removeprefix("quad-")
    title = f"Quad {model_no}"
    docs = documents(slug)
    files = sorted(p.name for p in (REF / slug).glob("*.md"))
    kind = "power amplifier" if "power amplifier" in name.lower() else "preamplifier"
    what_it_is = prose(text.get("What it is", "")) or f"<p>{intro((REF / slug / 'overview.md').read_text(encoding='utf-8'))}</p>"

    doc_items = "".join(
        f'<li><span class="doc-title">{inline(t)}</span><span class="doc-author">{inline(a)}</span>'
        f'<span class="doc-links"><a href="{REPO}/blob/main/{quote(p)}">Open</a><a href="{REPO}/blob/main/{quote(p)}?raw=true">Download</a></span></li>\n'
        for _, t, a, p in docs) or "<li>No documents yet.</li>\n"
    file_items = "".join(f'<li><a href="{REPO}/blob/main/quad-upgrade/reference/{slug}/{f}">{esc(f)}</a></li>\n' for f in files)

    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="A simple, safe guide to restoring a {esc(title)} {esc(kind)}.">
    <title>Restoring your {esc(title)} | Quad Agent</title>
    <link rel="stylesheet" href="../styles.css">
  </head>
  <body class="owner">
    <a class="skip-link" href="#main">Skip to content</a>
    <!-- Generated by scripts/build_site.py from docs/owners/{slug}.md and the skill. Do not edit by hand. -->
    <header class="site-header">
      <a class="brand" href="../index.html" aria-label="Quad Agent home">
        <span class="brand-mark" aria-hidden="true">Q</span>
        <span class="brand-name"><strong>QUAD AGENT</strong><small>RESTORATION ARCHIVE</small></span>
      </a>
      <nav aria-label="Site">
        <a class="nav-repo" href="../index.html#guides">All models</a>
      </nav>
    </header>

    <main id="main" class="shell owner-page">
      <section class="owner-hero">
        <p class="eyebrow">{esc(title.upper())} · {esc(kind.upper())}</p>
        <h1>Restoring your {esc(title)}</h1>
        {what_it_is}
        <p class="new-note">This guide is new. Nobody has checked its parts list against a real {esc(title)} yet, so treat it as a starting point.</p>
      </section>

      <section class="safety-box" aria-labelledby="safety-title">
        <h2 id="safety-title">Before anything else: stay safe</h2>
        <p>This {esc(kind)} plugs into the mains. Parts inside can still give you a dangerous shock after it is unplugged.</p>
        <p><strong>If you are new to electronics, don't open it.</strong> You can do everything on this page from the outside. A qualified technician does the work inside.</p>
      </section>

      <section class="steps" aria-labelledby="steps-title">
        <h2 id="steps-title">Four steps</h2>

        <div class="step">
          <span class="step-no">1</span>
          <div class="step-body">
            <h3>Write down a few details</h3>
            <p>You can find all of these from the outside.</p>
            {prose(text.get("Write these down", "- The serial number."))}
          </div>
        </div>

        <div class="step">
          <span class="step-no">2</span>
          <div class="step-body">
            <h3>Talk it through with an AI assistant</h3>
            <p>An AI assistant with the Quad Agent guide checks your details against Quad's own documents and tells you what applies to your {esc(title)}. It asks questions first and never guesses part values.</p>
            <div class="prompt-box">
              <p class="prompt-label">Copy this into your AI assistant:</p>
              <p class="prompt-text">Read quad-upgrade/SKILL.md and follow it to help me restore my {esc(title)}. Start by helping me identify it from the outside.</p>
              <p class="prompt-note">It needs the guide files first. <a href="{REPO}/releases/latest">Download the guide</a> and add it to your assistant, or give it the <a href="{REPO}/tree/main/quad-upgrade">quad-upgrade folder</a>.</p>
            </div>
          </div>
        </div>

        <div class="step">
          <span class="step-no">3</span>
          <div class="step-body">
            <h3>Choose what you want done</h3>
            <h4>The recap</h4>
            {prose(text.get("What a recap does", ""))}
            <h4>Optional extras</h4>
            <p>These change how the {esc(title)} behaves. You don't need any of them.</p>
            {prose(text.get("Optional extras", "- None listed yet."))}
          </div>
        </div>

        <div class="step">
          <span class="step-no">4</span>
          <div class="step-body">
            <h3>Take it to a technician</h3>
            <p>Send them the link to this page. Everything they need is in the section below: the parts list, Quad's service documents and the upgrade guides.</p>
            <p>Ask them to check the parts against your actual {esc(title)} before ordering. Quad changed things during production, and earlier owners may have too.</p>
          </div>
        </div>
      </section>

      <section class="good-to-know" aria-labelledby="gtk-title">
        <h2 id="gtk-title">Good to know</h2>
        {prose(text.get("Good to know", ""))}
      </section>

      <section class="tech-section" aria-labelledby="tech-title">
        <h2 id="tech-title">For your technician</h2>
        <p>Detailed information, folded away. Tap a heading to open it.</p>

        <details>
          <summary>Parts list</summary>
          <div class="details-body">
            <p class="card-caveat"><strong>Provisional.</strong> Every part comes from a named document but has not yet been checked against a real board. Confirm against the actual board before ordering. The recap comes first; optional changes are listed separately.</p>
            {parts_html(slug)}
          </div>
        </details>

        <details>
          <summary>Service documents and upgrade guides ({len(docs)})</summary>
          <div class="details-body">
            <p>Many are scans, so they are pictures of pages rather than searchable text.</p>
            <ul class="doc-list">
{doc_items}            </ul>
          </div>
        </details>

        <details>
          <summary>Reference files with page citations</summary>
          <div class="details-body">
            <p>The detailed notes the AI assistant works from. Every value cites a document and page.</p>
            <ul class="file-list">
{file_items}              <li><a href="{REPO}/blob/main/quad-upgrade/data/{slug}-bom.csv">{slug}-bom.csv</a> (parts data)</li>
            </ul>
          </div>
        </details>
      </section>
    </main>

    <footer class="site-footer shell">
      <div><p>An independent community project. QUAD is a trade mark of its owners; this project is not affiliated with or endorsed by Quad.</p></div>
      <div class="footer-meta"><p><a href="../index.html#guides">Back to all models</a></p></div>
    </footer>
  </body>
</html>
"""


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
