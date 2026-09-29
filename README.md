# Quad Upgrade Skill

**An AI agent skill for restoring and upgrading classic QUAD hi-fi, with cited sources, confidence labels, and clear stop points instead of guesswork.**

Give any AI assistant access to this skill folder and it can use it as a careful bench companion: identify the unit, work through safety and scope, explain what to replace and what to leave alone, build a parts list, and plan checks after the work. Every value it gives should come from a named source, with uncertainty made clear instead of guessed.

| Model | Status |
|---|---|
| **Quad 34** preamplifier | Draft coverage for recap, MM/MC disc modules, phono mods, disc-to-line conversion, output level, balance repair, and fault-finding. **Not yet tested with users or on a bench; no BOM rows have physical board verification yet.** |
| Quad 33, 303, 405 / 405-2, 306, 606 | Planned — contributions welcome |

---

## ⚠️ Safety

These units run from the mains and can retain dangerous voltage after unplugging. This skill is not electrical-safety training. If you are new to electronics or unsure how to work safely inside mains equipment, use it for external identification and planning, and have a qualified technician do internal work and first power-up. **You use this project at your own risk.**

---

## Use with an AI assistant

This is a portable set of Markdown instructions and reference files, not a hosted chatbot or platform-specific plugin. Give the assistant access to the complete `quad-upgrade/` folder, or import the `quad-upgrade.zip` from the latest [GitHub Release](https://github.com/Quad-Hi-Fi-Restoration/quad-agent/releases/latest) if it accepts skill bundles. If the platform has its own reusable-skill or knowledge import, follow that platform's instructions and include the whole folder so its references and data are available.

For a direct trial, start a new conversation with:

> Read `quad-upgrade/SKILL.md` and follow it to help me identify my QUAD 34.

An assistant that cannot read local files or import a folder can still use the skill if you provide `SKILL.md` and the relevant reference files in its context. Platform import methods differ; the skill content itself does not depend on a specific vendor.

---

## Using it

Just start talking about your unit:

> I've got a Quad 34 and I want to recap it and look at the phono stage.

It should first ask for the serial number and visible details. It must not ask an inexperienced user to open the unit to take a board photo; if internal inspection is needed, it should do the safety/competence check and may refer that step to a technician. QUAD changed the circuit several times, so parts depend on the actual board as well as the serial number.

### How much to trust the data

Every component row has a status:

| Status | Meaning |
|---|---|
| **verified** | Checked against a real board and recorded — for that unit/board only |
| **unverified** | Sourced but not checked against a physical board — shown as *provisional*; have a qualified technician confirm it against your board before ordering |
| **conflict** | Sources disagree — the skill explains both and won't pick one |

Where Quad's own service data disagrees with its diagrams, the skill explains the conflict and asks for technician-confirmed board information before choosing a part. It does not ask a beginner to open the unit to read it.

---

## Shopping lists

`quad-upgrade/data/quad-34-shopping-list.md` is generated from the component data: one list per job (full recap for your serial range, plus each optional mod). Rebuild it from the repository root with Python 3.10 or newer (no extra packages needed):

```
# Windows PowerShell
py -3 scripts/build_shopping_list.py

# macOS or Linux
python3 scripts/build_shopping_list.py
```

---

## Project page

A static, GitHub Pages-ready landing page lives in [`docs/`](docs/). It introduces the archive, links to the current guides and sources, and explains how to contribute. See [`docs/README.md`](docs/README.md) for local preview and Pages setup instructions. Publishing still needs to be enabled in the repository's GitHub Pages settings.

---

## Sources

The Quad 34 data is distilled from Quad's own service data and diagrams, plus upgrade guides by DADA Electronics, Keith Snook, Russ Andrews (RATA) and members of the Quad community. The full list, with what each source covers, is in [`quad-upgrade/reference/index.md`](quad-upgrade/reference/index.md). The QUAD 34 parts remain provisional until checked against physical boards; treat the list as a research aid, not a confirmed shopping order.

The source documents themselves — service data, circuit diagrams, DADA kit instructions and community notes for each model — are in [`source-docs/`](source-docs/).

---

## Repository layout

```
quad-upgrade/          the skill (this is what goes in the zip)
  SKILL.md             instructions the agent follows
  reference/           safety, general practice, per-model files
  data/                component BOMs, shopping lists, suppliers
scripts/               checks, shopping list builder, packager
source-docs/           source documents, one folder per model
templates/             starter files for adding another QUAD model
TESTING.md             how to test the skill
CONTRIBUTING.md        how to add data and new models
```

---

## Contributing

The most useful contributions are:

- **Board checks** — a competent restorer confirming BOM rows against a real unit (use the *Board verification* issue template).
- **Source documents** — service data, factory bulletins or upgrade sheets we don't have (use the *New source document* template).
- **New models** — see [CONTRIBUTING.md](CONTRIBUTING.md).

## Credits

Quad Electroacoustics (service data), DADA Electronics — Stefaan & Joost, Keith Snook, Russ Andrews Turntable Accessories, FRO (phono module image, CC0), and the Quad owners' community for collecting and sharing documents. Full credits in [`quad-upgrade/reference/index.md`](quad-upgrade/reference/index.md).

Quad is a registered trade mark of its owners. This project is not affiliated with or endorsed by Quad.

## Licence

- Skill text, reference files and data: [CC BY-SA 4.0](LICENSE-CONTENT.md)
- Scripts: [MIT](LICENSE)
- The phono module image is CC0 by FRO.
