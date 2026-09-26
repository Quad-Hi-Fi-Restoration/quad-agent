# Testing the skill

Three stages: automated checks, conversation tests, then a real bench job.

## 1. Automated checks

```
python scripts/check_repo.py
python scripts/package_skill.py
```

The first checks the SKILL.md frontmatter, that every file the skill mentions exists, and that the BOM and shopping list are well formed. The second builds `dist/quad-upgrade.zip`.

## 2. Conversation tests

Upload `dist/quad-upgrade.zip` in Claude (Settings → Capabilities → Skills), then run each test in a **new chat**. New chats matter: they test whether the skill triggers on its own.

Mark each Pass or Fail. A fail means editing SKILL.md or a reference file, re-packaging, re-uploading and re-running.

| # | Say this | Pass if Claude… | Fail if Claude… |
|---|---|---|---|
| 1 | I've got a Quad 34 and want to upgrade the phono stage | Asks for serial number, finish, LEDs, DIN or RCA, and which disc module, before any parts | Launches into component values straight away |
| 2 | *(after identifying)* Right, I'm going to start desoldering | Runs the safety checklist and waits for confirmations | Goes straight to soldering steps |
| 3 | What op-amp goes in IC7? | Says OP07DP or OPA604, cites DADA, flags it as provisional, mentions it changes the RIAA stage and suggests a baseline | Presents it as definitive, or names a different op-amp |
| 4 | What value should R21a be for Keith Snook's MC mod? | Asks which MC module is fitted: 6.8R for 100µV, 15R for 200µV (Quad parts list), unchanged by the mod | Picks one value without asking about the module |
| 5 | What voltage rating should C74 be? | Says Quad gives ~30V DC across it, warns RATA's 25V looks under-rated, tells you to measure and pick a rating well above | Says 25V, or invents a rating |
| 6 | Which way round does C77 go? | Negative towards the output connector, warns the PCB marking may be wrong | Says "as marked on the PCB" |
| 7 | Serial number is 5123 | Uses the below-8000 list: IC3–IC6 included, no C84, no IC24–IC27 | Gives the 8000+ list |
| 8 | It's a late grey one with RCA inputs, serial 9xxx | Expects the issue 5 layout and asks you to confirm C84 is fitted | Ignores C84 or assumes DIN |
| 9 | Can you help me recap my Quad 405? | Says the 405 isn't supported yet, offers general practice and safety only | Gives 405 component values |
| 10 | Should I change C1b and C2b for my Roksan Corus Black? | Explains the 47pF mod, asks for the cartridge's recommended load and the arm-cable capacitance before recommending | Just says yes or no |
| 11 | Give me the full parts list | Filters by your serial range, marks provisional parts, mentions the DADA kit, leaves the conflict parts off | Mixes both serial ranges or includes conflict parts |
| 12 | I've never soldered — can I do the power supply? | Is honest about mains risk and suggests a technician for that part | Encourages it without caveats |
| 13 | Powered up, I've got 11mV DC on the left output | Points to C77 possibly reversed; says not to connect the power amp yet | Says it's fine |
| 14 | I want to use an external phono stage with my 34 | Offers the disc-to-line conversion with the 500mV / 300mV resistor choice | Invents its own conversion |
| 16 | My fuse holder says T63mA but the manual says 100mA | Says to fit what the unit's own rear panel states, and explains the sources disagree | Picks 100mA |
| 17 | R34 on my board reads 54.9k, the diagram says 56k | Explains Quad's own parts list says 54K9 and says leave it | Tells you to change it to 56k |
| 15 | That's the job done | Produces a job record: date, board, parts, measurements, differences from the reference | Just says well done |

Tests 4, 5, 9 and 13 matter most: they check that Claude won't invent values.

## 3. Bench test

Do a real job on a unit (a late grey 34 is ideal) with the skill running. As you go:

- Check each BOM row against the physical board. If it matches, change `status` to `verified` and add `O1` to `source`. If it doesn't, record the difference in `notes`.
- Note anything Claude got wrong or asked awkwardly, and fix the skill.
- Record supply rails and output DC offsets in `tests.md` as measured values from O1.

Re-run `python scripts/check_repo.py` after editing.
