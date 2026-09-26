# Safety

Go through this with the user and get a confirmation for each point before hands-on work. Keep it conversational, not a lecture — but don't skip items.

## Before opening the unit

1. **Unplugged at the wall**, not just switched off. Mains lead removed from the unit if detachable.
2. **Disconnected from everything else** — power amp, sources, speakers.
3. **Wait, then measure.** Power supply capacitors can hold charge. With a meter on DC volts, measure across the main supply capacitors before touching anything. If there's significant voltage, discharge through a suitable resistor (not a screwdriver) and measure again.
4. **Know where mains is.** Identify the mains inlet, fuse, switch and transformer primary before you start, and keep hands and tools away from them. Don't alter mains wiring or earthing unless you are competent to and it's part of the job.

## While working

5. **Photograph first**, from several angles, before removing anything.
6. **Polarity.** Aluminium electrolytics usually mark the *negative* lead with a stripe; tantalums usually mark the *positive*. Check the PCB legend and the reference file, and confirm orientation before soldering.
7. **Heat and fumes.** Ventilation, eye protection when clipping leads, a stable iron stand. Wash hands after handling leaded solder.
8. **Static.** Ground yourself before handling transistors and ICs.

## First power-up after work

9. **Visual check**: no solder bridges, no loose clippings, every polarised part the right way round, nothing left unsoldered.
10. **Limit the current**: use a dim-bulb tester or a variac if available — Quad's own procedure brings the unit up on a variac while watching the current (Quad 34: S8 p15). At minimum, confirm the fuse fitted matches the rating on the unit's rear panel.
11. **Nothing connected** to the outputs for the first power-up.
12. **Measure** the checks in the model's `tests.md` (supply rails, DC at outputs) before connecting to a power amp.
13. **Smell, smoke, heat**: switch off at the wall immediately and investigate.

If any step can't be done safely with the user's tools or experience, recommend a qualified technician for that step.
