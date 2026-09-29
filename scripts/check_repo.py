"""Check skill metadata, internal links, source citations, BOMs and generated lists.

Run from the repository root:
  Windows: py -3 scripts/check_repo.py
  macOS/Linux: python3 scripts/check_repo.py
The check is read-only: it fails when a generated shopping list is stale.
"""
import csv
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "quad-upgrade"
INDEX = SKILL / "reference" / "index.md"
REQUIRED_BOM_COLUMNS = {
    "model", "variant", "board", "ref", "function", "original_value",
    "original_type", "voltage", "replacement_value", "replacement_type",
    "replacement_part", "supplier", "supplier_sku", "qty", "category",
    "status", "source", "notes",
}
problems = []


def problem(message: str) -> None:
    problems.append(message)


def internal_markdown_links(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        target = target.strip().split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("#", "/")):
            continue
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        relative = unquote(parsed.path)
        if not relative:
            continue
        destination = (path.parent / relative).resolve()
        try:
            destination.relative_to(ROOT.resolve())
        except ValueError:
            problem(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        if not destination.exists():
            problem(f"{path.relative_to(ROOT)}: missing link target: {target}")


# 1. Skill metadata and referenced files.
skill_file = SKILL / "SKILL.md"
if not skill_file.exists():
    problem("quad-upgrade/SKILL.md is missing")
else:
    skill_text = skill_file.read_text(encoding="utf-8")
    frontmatter = re.match(r"^---\n(.*?)\n---\n", skill_text, re.S)
    if not frontmatter:
        problem("quad-upgrade/SKILL.md: missing YAML frontmatter")
    else:
        fm = frontmatter.group(1)
        name = re.search(r"^name:\s*(\S+)", fm, re.M)
        desc = re.search(r"^description:\s*(.+)", fm, re.M)
        if not name or not re.fullmatch(r"[a-z0-9-]{1,64}", name.group(1)):
            problem("quad-upgrade/SKILL.md: name must be lowercase letters, digits and hyphens")
        if not desc or len(desc.group(1)) > 1024:
            problem("quad-upgrade/SKILL.md: description missing or over 1024 characters")

    model_dirs = [d for d in (SKILL / "reference").iterdir()
                  if d.is_dir() and not d.name.startswith("_")]
    for md in SKILL.rglob("*.md"):
        for ref in re.findall(r"`([A-Za-z0-9_./-]+\.(?:md|csv))`",
                              md.read_text(encoding="utf-8")):
            generic = "/" not in ref and model_dirs and all((d / ref).exists() for d in model_dirs)
            if not ((md.parent / ref).exists() or (SKILL / ref).exists() or generic):
                problem(f"{md.relative_to(ROOT)}: points to missing file {ref}")

# 2. Local Markdown links should resolve inside the repository.
for md in ROOT.rglob("*.md"):
    if ".git" not in md.parts and "dist" not in md.parts:
        internal_markdown_links(md)

# New-model starters must include every file required by the model workflow.
model_template_dir = ROOT / "templates" / "model"
required_model_templates = {
    "README.md", "overview.md", "board-template.md", "tests-template.md",
    "verification-log.md", "source-register.md", "bom-template.csv",
}
for filename in sorted(required_model_templates):
    if not (model_template_dir / filename).is_file():
        problem(f"templates/model is missing required starter file {filename}")
template_bom = model_template_dir / "bom-template.csv"
if template_bom.is_file():
    with template_bom.open(encoding="utf-8-sig", newline="") as stream:
        template_columns = set(csv.DictReader(stream).fieldnames or [])
    missing_template_columns = sorted(REQUIRED_BOM_COLUMNS - template_columns)
    if missing_template_columns:
        problem("templates/model/bom-template.csv: missing required columns: "
                + ", ".join(missing_template_columns))

# Generated lists are standalone artifacts, so retain the safety gate there too.
for shopping_list in sorted((SKILL / "data").glob("*-shopping-list.md")):
    list_text = shopping_list.read_text(encoding="utf-8")
    safety_markers = (
        "**Safety:**", "use this list for planning only", "qualified technician",
        "../reference/safety.md",
    )
    missing_safety = [marker for marker in safety_markers if marker not in list_text]
    if missing_safety:
        problem(f"{shopping_list.relative_to(ROOT)}: missing standalone safety guidance")

board_issue = ROOT / ".github" / "ISSUE_TEMPLATE" / "board-verification.md"
if not board_issue.is_file():
    problem(".github/ISSUE_TEMPLATE/board-verification.md is missing")
else:
    board_issue_text = board_issue.read_text(encoding="utf-8")
    board_safety_markers = (
        "**Safety:**", "competent to work safely inside mains-powered equipment",
        "Do not open, probe, or photograph", "qualified technician",
    )
    if any(marker not in board_issue_text for marker in board_safety_markers):
        problem(".github/ISSUE_TEMPLATE/board-verification.md: missing contributor safety guidance")

source_issue = ROOT / ".github" / "ISSUE_TEMPLATE" / "new-source.md"
if not source_issue.is_file():
    problem(".github/ISSUE_TEMPLATE/new-source.md is missing")
elif "Original URL or where it came from" not in source_issue.read_text(encoding="utf-8"):
    problem(".github/ISSUE_TEMPLATE/new-source.md: missing source-origin prompt")

# 3. All cited source IDs should be declared in the reference index or model registers.
source_id = re.compile(r"(?<![A-Za-z0-9])(?:[A-Z][A-Z0-9]*-)?(?:S|O)\d{1,3}\b")
observation_id = re.compile(r"(?<![A-Za-z0-9])(?:[A-Z][A-Z0-9]*-)?O\d{1,3}\b")
declared_sources = set()
registers = [INDEX] + sorted((SKILL / "reference").rglob("source-register.md"))
for register in registers:
    if not register.exists():
        continue
    register_text = register.read_text(encoding="utf-8")
    for line in register_text.splitlines():
        if line.startswith("|"):
            first_cell = line.split("|", 2)[1].strip()
            if re.fullmatch(source_id, first_cell):
                if first_cell in declared_sources:
                    problem(f"{register.relative_to(ROOT)}: duplicate source ID {first_cell}")
                declared_sources.add(first_cell)

if INDEX.exists():
    index_text = INDEX.read_text(encoding="utf-8")
    # Local source-document paths in the source table must match actual filenames.
    source_section = index_text.split("## Source documents", 1)[-1].split("## Credits", 1)[0]
    for ref in re.findall(r"`(source-docs/[^`]+)`", source_section):
        if not (ROOT / ref).exists():
            problem(f"quad-upgrade/reference/index.md: missing source copy {ref}")

# Physical verification must cite a logged observation, not only a document.
for bom in sorted((SKILL / "data").glob("*-bom.csv")):
    with bom.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not {"model", "status", "source"}.issubset(reader.fieldnames or []):
            continue
        for line_no, row in enumerate(reader, start=2):
            if (row.get("status") or "").strip() != "verified":
                continue
            obs_ids = set(observation_id.findall(row.get("source", "")))
            if not obs_ids:
                problem(f"{bom.name} line {line_no}: verified rows must cite a physical observation ID")
                continue
            model = (row.get("model") or "").strip()
            log = SKILL / "reference" / model / "verification-log.md"
            if not log.exists():
                problem(f"{bom.name} line {line_no}: missing verification log for {model!r}")
                continue
            log_text = log.read_text(encoding="utf-8")
            logged_ids = set(re.findall(
                r"^###\s+((?:[A-Z][A-Z0-9]*-)?O\d{1,3})\b", log_text, re.M
            ))
            for obs_id in sorted(obs_ids - logged_ids):
                problem(f"{bom.name} line {line_no}: {obs_id} is not recorded in {log.relative_to(ROOT)}")

for md in (SKILL / "reference").rglob("*.md"):
    if md == INDEX:
        continue
    citations = set(source_id.findall(md.read_text(encoding="utf-8")))
    unknown = sorted(citations - declared_sources)
    if unknown:
        problem(f"{md.relative_to(ROOT)}: undeclared source IDs: {', '.join(unknown)}")

# 4. BOM structure and citations.
required_columns = REQUIRED_BOM_COLUMNS
statuses = {"template", "unverified", "verified", "conflict"}
for bom in sorted((SKILL / "data").glob("*-bom.csv")):
    with bom.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        missing_columns = sorted(required_columns - set(reader.fieldnames or []))
        if missing_columns:
            problem(f"{bom.name}: missing columns: {', '.join(missing_columns)}")
            continue
        for line_no, row in enumerate(reader, start=2):
            status = (row.get("status") or "").strip()
            if status not in statuses:
                problem(f"{bom.name} line {line_no}: invalid status {status!r}")
                continue
            if status == "template":
                continue
            if not (row.get("source") or "").strip():
                problem(f"{bom.name} line {line_no}: source is required")
            if not (row.get("ref") or "").strip():
                problem(f"{bom.name} line {line_no}: reference designator is required")
            if not (row.get("qty") or "").strip().isdigit():
                problem(f"{bom.name} line {line_no}: quantity must be a whole number")
            if status != "conflict" and "TODO" in (row.get("replacement_value") or ""):
                problem(f"{bom.name} line {line_no}: replacement value is still TODO")
            unknown = sorted(set(source_id.findall(row.get("source", ""))) - declared_sources)
            if unknown:
                problem(f"{bom.name} line {line_no}: undeclared source IDs: {', '.join(unknown)}")

# 5. The generated list must already match its BOM; CI must not silently rewrite it.
builder = ROOT / "scripts" / "build_shopping_list.py"
result = subprocess.run([sys.executable, str(builder), "--check"],
                        capture_output=True, text=True, cwd=ROOT)
if result.returncode:
    problem("shopping-list check failed:\n" + (result.stdout + result.stderr).strip())

if problems:
    print("PROBLEMS FOUND:")
    for item in problems:
        print(f" - {item}")
    sys.exit(1)
print("All checks passed.")
