"""Package the portable skill folder as a zip bundle.

Run from the repository root:
  Windows: py -3 scripts/package_skill.py
  macOS/Linux: python3 scripts/package_skill.py
Output: dist/quad-upgrade.zip
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "quad-upgrade"
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)
out = DIST / "quad-upgrade.zip"

with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(SKILL.rglob("*")):
        if f.is_file() and "__pycache__" not in f.parts:
            z.write(f, f.relative_to(ROOT))
print(f"Wrote {out}")
