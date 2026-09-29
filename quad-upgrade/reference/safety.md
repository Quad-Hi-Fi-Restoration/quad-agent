# Safety

Go through this with the user before any hands-on work. Keep it conversational, but do not skip the competence check or ask the user to confirm a step they cannot safely carry out.

## Decide whether the user should work inside

Vintage QUAD equipment is mains-powered. Dangerous voltage may remain inside after unplugging. This skill is not electrical-safety training. If the user says they are new to electronics, unsure how to isolate equipment, or do not have suitable test equipment and experience, keep them to external identification and observation; recommend a qualified audio/electronics technician for opening, soldering, internal measurements, fault-finding, and first power-up. Never coach an inexperienced user through live probing.

Work on live equipment should be avoided wherever possible. A variac, dim-bulb tester, RCD, or unplugged mains lead does not by itself make internal work safe. Stop if the user's tools, experience, or the unit's condition do not support the next step.

## Before opening the unit

1. **Unplugged at the wall**, not just switched off. Remove the mains lead from the unit if detachable, and prevent someone reconnecting it while work is underway.
2. **Disconnected from everything else** — power amp, sources, speakers.
3. **Capacitors can retain charge.** Waiting does not prove a unit is safe. Only a person competent to work inside the equipment should verify stored voltage with an appropriately rated meter and probes before touching parts. If there is voltage, or they are not sure how to check or safely release stored energy, stop and use a qualified technician. Never use a screwdriver or an improvised discharge method.
4. **Know where mains is.** A competent restorer must identify the mains inlet, fuse, switch and transformer primary and keep hands and tools away from exposed mains circuitry. Do not alter mains wiring or earthing unless qualified and the task requires it.

## While working

5. **Photograph first**, from several angles, before removing anything.
6. **Polarity.** Aluminium electrolytics usually mark the *negative* lead with a stripe; tantalums usually mark the *positive*. Check the PCB legend and the reference file, and confirm orientation before soldering.
7. **Heat and fumes.** Ventilation, eye protection when clipping leads, a stable iron stand. Wash hands after handling leaded solder.
8. **Static.** Ground yourself before handling transistors and ICs.

## First power-up after work

9. **Visual check**: no solder bridges, no loose clippings, every polarised part the right way round, nothing left unsoldered.
10. **Powered work is for a competent restorer.** Quad's own service procedures may use a variac while watching current (see the model's `tests.md`); this is not a beginner procedure and a variac is not an isolation device. Confirm the fuse matches the rating stated on the unit's own rear panel before use.
11. **Nothing connected** to the outputs (no amplifier, no loudspeakers) for the first power-up.
12. **Measure** the checks in the model's `tests.md` (supply rails, DC at outputs) before connecting it to anything else — a power amplifier for a preamp, loudspeakers for a power amp.
13. **Smell, smoke, heat**: switch off at the wall immediately and investigate.

If any step can't be done safely with the user's tools or experience, recommend a qualified technician for that step.

## Further safety guidance

- UK Health and Safety Executive: [Work on electrical equipment](https://www.hse.gov.uk/electricity/withequip.htm) — competence, planning, isolation, and stored energy.
- UK Health and Safety Executive: [Frequently asked questions on electricity](https://www.hse.gov.uk/electricity/faq.htm) — live work and safe isolation.
