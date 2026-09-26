"""Sanity-check the skill before packaging.

Usage: python scripts/check_repo.py
Checks: SKILL.md frontmatter, every referenced .md file exists,
BOM rows are well formed, and the shopping list builds.
"""
import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "quad-upgrade"
problems = []

# 1. Frontmatter
text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not m:
    problems.append("SKILL.md: missing YAML frontmatter")
else:
    fm = m.group(1)
    name = re.search(r"^name:\s*(\S+)", fm, re.M)
    desc = re.search(r"^description:\s*(.+)", fm, re.M)
    if not name or not re.fullmatch(r"[a-z0-9-]{1,64}", name.group(1)):
        problems.append("SKILL.md: name must be lowercase letters, digits and hyphens")
    if not desc or len(desc.group(1)) > 1024:
        problems.append("SKILL.md: description missing or over 1024 characters")

# 2. Referenced files exist (relative to the file, then to the skill root)
for md in SKILL.rglob("*.md"):
    for ref in re.findall(r"`([A-Za-z0-9_./-]+\.(?:md|csv))`", md.read_text(encoding="utf-8")):
        if "<" in ref:
            continue
        # generic names like `overview.md` mean "the model's file" - must exist for every model
        model_dirs = [d for d in (SKILL / "reference").iterdir() if d.is_dir()]
        generic = "/" not in ref and all((d / ref).exists() for d in model_dirs)
        if not ((md.parent / ref).exists() or (SKILL / ref).exists() or generic):
            problems.append(f"{md.relative_to(ROOT)}: points to missing file {ref}")

# 3. BOM rows
for bom in (SKILL / "data").glob("*-bom.csv"):
    rows = list(csv.DictReader(bom.open(encoding="utf-8", newline="")))
    for n, r in enumerate(rows, start=2):
        if r["status"] not in {"template", "unverified", "verified", "conflict"}:
            problems.append(f"{bom.name} line {n}: bad status {r['status']}")
        if r["status"] != "template" and not r["source"].strip():
            problems.append(f"{bom.name} line {n}: no source")

# 4. Shopping list builds
res = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_shopping_list.py")],
                     capture_output=True, text=True)
if res.returncode:
    problems.append("build_shopping_list.py failed:\n" + res.stdout)

if problems:
    print("PROBLEMS FOUND:")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("All checks passed.")
