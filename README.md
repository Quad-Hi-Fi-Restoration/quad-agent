# Quad Upgrade Skill

**An AI agent skill that guides you through restoring and upgrading classic Quad hi-fi — using verified, sourced component data instead of guesswork.**

Point Claude (or another AI agent) at this skill and it becomes a careful bench companion: it identifies your exact unit, takes you through safety checks, tells you what to replace and what to leave alone, builds your parts list, and helps you test the result. Every value it gives comes from a named source document, and it will tell you when something hasn't been confirmed rather than make it up.

| Model | Status |
|---|---|
| **Quad 34** preamplifier | ✅ Full recap, MM/MC disc modules, phono mods, disc-to-line conversion, output level, balance repair, fault finding |
| Quad 33, 303, 405 / 405-2, 306, 606 | Planned — contributions welcome |

---

## ⚠️ Safety

These units run from the mains and contain capacitors that hold charge after unplugging. The skill runs a safety checklist with you before any hands-on work and before first power-up, but it does not replace competence. If you are not comfortable working inside mains equipment, have a qualified technician do the work. **You use this project at your own risk.**

---

## Install

### Claude (claude.ai or the Claude desktop app) — recommended

1. Download `quad-upgrade.zip` from the latest [Release](../../releases/latest).
2. In Claude go to **Settings → Capabilities**, make sure **Code execution and file creation** is on, then under **Skills** click **Upload skill** and choose the zip.
3. Switch the skill on.

Skills need a Pro, Max, Team or Enterprise plan.

### Claude Code

Copy the `quad-upgrade` folder into `~/.claude/skills/` (all projects) or `.claude/skills/` in a project.

### Other AI agents

Give the agent access to this folder and start with:

> Read `quad-upgrade/SKILL.md` and follow its instructions.

---

## Using it

Just start talking about your unit:

> I've got a Quad 34 and I want to recap it and look at the phono stage.

It will ask for the serial number, finish, socket type and which disc module is fitted, because Quad changed the circuit several times and the right parts depend on it. Photos of the serial label and the board help a lot.

### How much to trust the data

Every component row has a status:

| Status | Meaning |
|---|---|
| **verified** | Checked against a real board |
| **unverified** | From one source document — shown as *provisional*; check your board before ordering |
| **conflict** | Sources disagree — the skill explains both and won't pick one |

Where Quad's own service data disagrees with its diagrams (it happens), the skill tells you and asks you to read the part on your board.

---

## Shopping lists

`quad-upgrade/data/quad-34-shopping-list.md` is generated from the component data: one list per job (full recap for your serial range, plus each optional mod). Rebuild it with:

```
python scripts/build_shopping_list.py
```

---

## Sources

The Quad 34 data is distilled from Quad's own service data and diagrams, plus upgrade guides by DADA Electronics, Keith Snook, Russ Andrews (RATA) and members of the Quad community. The full list, with what each source covers, is in [`quad-upgrade/reference/index.md`](quad-upgrade/reference/index.md).

Copies of the source documents are kept in [`source-docs/`](source-docs/) for reference, with credits and original download locations. They remain the property of their authors. **If you own one of these documents and would like it removed, open an issue and it will be taken down promptly.**

---

## Repository layout

```
quad-upgrade/          the skill (this is what goes in the zip)
  SKILL.md             instructions the agent follows
  reference/           safety, general practice, per-model files
  data/                component BOMs, shopping lists, suppliers
scripts/               checks, shopping list builder, packager
source-docs/           the source documents, for reference
TESTING.md             how to test the skill
CONTRIBUTING.md        how to add data and new models
```

---

## Contributing

The most useful contributions are:

- **Board checks** — confirming BOM rows against a real unit (use the *Board verification* issue template).
- **Source documents** — service data, factory bulletins or upgrade sheets we don't have (use the *New source document* template; tell us if you have permission to share).
- **New models** — see [CONTRIBUTING.md](CONTRIBUTING.md).

## Credits

Quad Electroacoustics (service data), DADA Electronics — Stefaan & Joost, Keith Snook, Russ Andrews Turntable Accessories, FRO (phono module image, CC0), and the Quad owners' community for collecting and sharing documents. Full credits in [`quad-upgrade/reference/index.md`](quad-upgrade/reference/index.md).

Quad is a registered trade mark of its owners. This project is not affiliated with or endorsed by Quad.

## Licence

- Skill text, reference files and data: [CC BY-SA 4.0](LICENSE-CONTENT.md)
- Scripts: [MIT](LICENSE)
- The phono module image is CC0 by FRO.
