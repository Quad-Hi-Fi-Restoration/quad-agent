# Quad 34 — overview

## Serial ranges
Quad made three major circuit releases. For replacement purposes they fall into two groups (S3 p1):

| Group | Differences that matter here | Source |
|---|---|---|
| Serial 1 – 7999 | Op-amps IC3–IC6 present; no C84, no C89–C92 | S3 p2 |
| Serial 8000 onwards | IC24–IC27 dual op-amps on line/tape inputs; C84; C89–C92 | S3 p2 |

Early units (below 8000) use single TL071 op-amps and no input buffers; zener diodes D3–D14 protect the CD4066 input switches. From serial 8001 input buffers were added (S5). Early units were built with 100µF 3V tantalum coupling capacitors, which S5 says don't leak; the track damage from leaking electrolytics is a later-model problem (S5).

**Always get the serial number first** — it decides which parts list applies. Positions of C16/C17 also differ between the two groups (S3 p5).

## Identifying the unit — ask all of these

| Question | What it tells you | Source |
|---|---|---|
| Serial number | **Decides the parts list**: below 8000 or 8000 onwards | S3 p1–2 |
| Finish and button colours | Early units: brown finish with brown/yellow buttons. Later units: grey | S5 |
| Front LEDs | Early: 5mm red/green LEDs. Later: 3mm LEDs in grey or black plastic bezels | S5 |
| Line inputs and output: DIN or RCA? | From 8001: DIN suggests diagram issue 3, RCA suggests issue 5. Late grey units have RCA inputs only, no DIN — expect the issue 5 layout, including C84 | S6, S1, O1 |
| C84 fitted beside C58? | Should be present from S/N 8001 (PCB iss 5) | S8 p21, p25 |
| Fuse rating on rear panel | Rear panel shows T63mA (S11); S8 parts list says 63mA; S8 assembly list and S11 text say 100mA. **Use whatever the unit's own rear panel states** | S8, S11 |
| Filter/Slope button colour | Red before S/N 4130, brown after (S8 p21) — helps date early units | S8 |
| CD button present? | From S/N 8305 (S8 p21) | S8 |
| Disc module panel marking | Four module types existed: MM 3mV (47K/220p), MC 100µV, MC 200µV (100Ω//22nF, supplied in the box), MC 400µV | S8 p27–28, S11 p10 |
| Previous work done | Earlier recaps may already have changed polarity or parts | — |

Finish and LEDs are clues to the era, not proof — parts get swapped over the years. The serial number and what's physically on the board decide.

## Production changes (S8 p21 — Quad's modifications page)

| Serial (approx.) | Date | Change |
|---|---|---|
| ~2000 | — | PCB iss 2: wire links replaced by printed copper links; two holes for redundant transformer tags (mechanical) |
| ~3700 | Feb 1983 | R55 and R60 changed 680K → 2M2 (improved bass response) |
| ~4000 | Mar 1983 | C83 added to decouple HT rails: 47n negative rail to earth on some units, 680n positive rail to earth on others, soldered on the rear of the PCB |
| 4130 | Mar 1983 | Red Filter 1, Filter 2 and Slope buttons replaced by brown buttons |
| 6001 | Jun 1983 | PCB iss 4: radio switch control direct from IC11 pin 10 (fewer clicks); C81, C82 47n added (RF clicks); R125 220Ω added to protect D32; C44 moved onto main PCB |
| 8001 | Nov 1983 | PCB iss 5: C83 removed; **C84 22µ added** (negative rail to earth) and C58 moved to positive rail to earth; tape and aux input circuits completely changed — aux sensitivity 300mV or 100mV by plug-in flag, suitable for CD |
| 8305 | Dec 1983 | CD select button fitted, chassis print changed |

Later: PCB iss 6 with RCA line inputs (S1, S9 p2).

## Circuit issues (S1, S6, S7, S8)

| Diagram | PCB | Differences noted |
|---|---|---|
| M12746 issue 1 (S8 p31) | M12730 issue 1 and 2 | Up to S/N 6000. DIN inputs; AUX input (C5/C6 330n) with zener protection |
| M12746 issue 2 (S8 p32; S7 redrawn) | M12730 issue 4 | Serial 6001–8000. No input buffers; RCA inputs; zeners D3–D14 6V8 protect the input switches; tape sensitivity set by links |
| M12746 issue 3 (S8 p33; S6) | M12730 issue 5 | From S/N 8001. CD, TAPE, RADIO and output on DIN; input buffers IC24–27; C84 fitted (the S6 print omits it — S8 is authoritative) |
| M12746 issue 4 (S9 p2) and issue 5 (S1) | M12730 issue 6 | Line inputs on RCA sockets (S11 back view); mains voltage link on S1 |

Both are marked as from S/N 8001. The disc stage is identical in both. If the user's unit has DIN line inputs, expect the issue 3 layout.

## Board map
All components are soldered directly to the motherboard; the disc input is a plug-in module connected by a flat cable (S3 p3, S2 p2).

| Area | File | Key refs | Source |
|---|---|---|---|
| Disc module (MM or MC) | `phono-stage.md` | module: R1–R24, C1–C15, T1–T4 with a/b suffix | S1 |
| RIAA amplifier on main board | `phono-stage.md` | C18–C29, R33–R44, IC7/IC8 | S1 |
| Power supply | `power-supply.md` | D34, C74, IC21, IC23, C57–C59, C69, C84 | S1 |
| Line, tone, filter, output | `line-tone-filter.md` | IC9–IC20, R118–R122, RV4 | S1, S3 |

PCB legend: left-channel refs printed in white, right-channel in yellow. The schematic is the same for both channels but the physical layout isn't (S3 p3).

Module identification: the MM module's panel reads "DISC 3mV 47K/220p" (S2 p2). The MC module input is 100µV (S1).

## Access
Remove the lid of the power supply compartment and the protective plastic plate under the motherboard (S3 p3). The board is double-sided: use a good desoldering pump or station, and clip old parts on the component side before removing the leads (S3 p3).

## Known faults

| Symptom | Cause | Fix | Source |
|---|---|---|---|
| Inputs switch by themselves or mix | Leaking coupling electrolytics have eaten tracks underneath | Bypass damaged tracks pin-to-pin with insulated wire | S3 p8 |
| Transformer problems on units before S/N 2000 | Mechanical mounting | Replacement transformer with redundant tags — see `fault-finding.md` | S8 p11 |
| D32 failure, particularly before S/N 6000 | R125 not fitted until iss 4 | See `fault-finding.md` | S8 p11, p21 |
| Balance control faulty | Original pots no longer available | Replace with fixed resistors — see `line-tone-filter.md` | S3 p9 |
| Low-frequency oscillation | Long supply tracks to op-amps | Add 100nF decoupling at IC9/IC10 | S3 p7 |
| MM input sounds lifeless vs other inputs | 220pF input capacitance too high with arm cable and modern MM cartridges | Reduce C1b/C2b to 47pF | S3 p10 |
| PCB polarity markings wrong or missing | Factory | Follow `recap-kit.md` polarity table, not the PCB | S3 p4; S5 |
| C77 leaking; small DC at output | C77 fitted reversed, following an incorrect PCB marking | Refit with negative towards output connector | S5 |
| C16/C17 fail early | They rely on the connected tape machine for a DC path; often fitted reversed | Fit correctly; S5 adds 100kΩ from each tape output to ground | S5 |
| Early units: stereo image collapses on 300mV AUX/TAPE inputs | Frequency-selective capacitive crosstalk around the input bus | Track cuts and grounded screen — see S5 (complex; experienced restorers only) | S5 |
