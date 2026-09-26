# General practice

This is general bench practice. Where a model's reference file or a cited source says something different, the model file wins.

## Before you start
- Record a baseline: a listening note, a recording, or a measurement. Upgrades are easier to judge against something.
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
