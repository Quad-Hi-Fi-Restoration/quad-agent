# General practice

This is general bench practice for a competent restorer after the safety check in `safety.md`. Beginners should use these notes to understand the work and leave opening, soldering, internal measurements, and first power-up to a qualified technician. Follow model-specific sources for technical details. If a model reference, cited source, and the user's board disagree, stop and record the conflict; do not assume one is correct without evidence.

Explain unfamiliar part names and specifications in plain language. See `glossary.md`; use only the entries needed for the current task.

## Before you start
- Record a baseline: a listening note or recording. A competent restorer can also record a documented measurement. Upgrades are easier to judge against something.
- Photograph the board from above and at an angle so markings are readable.
- Work in small groups of parts, or one at a time. Bag and label removed parts until the job is tested.

## Choosing replacements

### Electrolytic capacitors
- Same capacitance unless the source says otherwise. In signal-coupling positions, changing the value changes low-frequency behaviour.
- Voltage rating equal or higher.
- 105 °C, long-life types are a sensible default.
- Check diameter and lead spacing will fit before ordering.

### Tantalum capacitors
- A common failure mode is going short. Replace with the type the source recommends (often aluminium electrolytic or film).

### Film and polystyrene capacitors in the RIAA / filter networks
- These set the equalisation curve. Tolerance matters as much as type.
- Only replace with the value and tolerance the source specifies, and ideally matched between channels.
- If they measure correctly, there may be no reason to change them — follow the board file.

### Resistors
- Metal film is a sensible default where a change is recommended.
- Precision resistors in equalisation networks: same value, same or tighter tolerance.

### Transistors and ICs
- Only substitute where the source names a replacement. Pinouts vary between types even with the same function — check against the datasheet and the PCB.

## Soldering
- Temperature-controlled iron, clean tip, fresh solder.
- Remove old solder fully (braid or pump) rather than pulling leads through; old pads lift easily.
- Don't overheat pads. If a track lifts, stop and repair it properly.
- Clean flux residue afterwards if the solder type needs it.

## After the work
- Follow `safety.md` for first power-up.
- Take the measurements in the model's `tests.md`.
- Compare with the baseline.
- Write the job record (SKILL.md, step 7).
