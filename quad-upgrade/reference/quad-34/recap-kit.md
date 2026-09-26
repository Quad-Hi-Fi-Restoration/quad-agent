# Quad 34 — full recap and op-amp upgrade (DADA kit, S3)

The DADA Electronics kit replaces all electrolytic and tantalum capacitors and the op-amps (S3 p1). There are two kits, one for serial numbers below 8000 and one for 8000 onwards. As of September 2026 DADA's .eu website appears to have lapsed, so the kit may not be available — don't promise it. The user can source parts individually from `../../data/quad-34-shopping-list.md`.

## Tools (S3 p2)
Fine-tipped iron (max 30W) or soldering station, desoldering pump or station, micro cutters, wire strippers, small pliers, Philips No. 1 and No. 2 screwdrivers, tin/lead solder, multimeter. Kontakt LR PCB cleaner and Kontakt 61 contact spray are useful.

## Parts
See the BOM rows with `category=restoration`. Summary (S3 p2):

| | Serial < 8000 | Serial ≥ 8000 |
|---|---|---|
| OP07DP or OPA604 | IC3–IC10, IC12, IC13, IC19, IC20 (12) | IC7–IC10, IC12, IC13, IC19, IC20 (8) |
| LME49720 or OPA2604 | — | IC24–IC27 (4) |
| 100µF | C10, C11, C16, C17, C57, C59, C69, C77, C78 | same |
| 22µF | C58 | C58, C84 |
| 1000µF | C74 | C74 |
| 2.2µF | C18, C22 | C18, C22 |
| Wire links | C30, C31, C48, C54 | C30, C31, C48, C54, C89–C92 |
| 100nF decoupling | — | 4 (see `line-tone-filter.md`) |

## Order of work (S3 p3)
1. Remove all parts to be replaced in one channel, then the other. Photograph or sketch first.
2. Clean the board with PCB cleaner; remove old solder and resin.
3. Fit the new parts. Check op-amp pin 1 — marked by a dot or "1" on the copper side (S3 p4).
4. Fit wire links from the component side so it's obvious which capacitor was replaced (S3 p4).

## Polarity traps (S3 p4–5, p10)
**The PCB + and − markings are not always correct, or are missing.** Use this table:

| Capacitor | Placement |
|---|---|
| C10, C11, C18, C22, C57, C58, C59, C69, C74, C84 | As marked |
| C16, C17 | **Reverse** — positions differ by serial range; use the S3 p5 photos |
| C77, C78 | **Negative towards the output connector** (S3 p10; S5). S3's table says 'Ok' as marked, but S5 found C77 fitted reversed because the PCB was marked wrongly. Check the actual board against this rule, not the silkscreen |
| C30, C31, C48, C54, C89–C92 | Replace with wire link. If kept instead, note IC5/IC6 outputs are often negative so C30/C31 may need reversing (S5) |

Output capacitors: DADA fits them with the negative towards the output connector (S3 p10).

Before soldering each polarised part, ask the user to confirm orientation against the table and photo.

## Before swapping op-amps (S5)
Keith Snook's page (S5) gives cautions worth raising before fitting the DADA op-amps:
- The +8.6V / −9.4V asymmetry is deliberate. With the original parts it appears to make the output clip symmetrically, and makes op-amp outputs swing positive at switch-off to protect the original tantalums.
- After changing op-amp types, or linking out C30, C31, C48, C54, C77 or C78, the output may no longer clip symmetrically, and the supply voltages may need adjusting. S5 doesn't give values.
- If electrolytics are kept in circuit after changing op-amps, check their DC polarity with each input and filter button selected. IC5/IC6 outputs are often negative, IC19/IC20 often positive.
- With C30/C31 linked out, IC9 and IC10 outputs can sit positive or negative, which S5 notes could affect the sound.

Keith Snook's own approach was to leave the original op-amps in place (S5). Present both routes to the user.

## Pinouts (S3 p10)
Single op-amps (OP07, OPA604, LME49710): pin 2 −in, 3 +in, 4 V−, 6 out, 7 V+.
Dual op-amps (LME49720, OPA2604): 1 out A, 2 −in A, 3 +in A, 4 V−, 5 +in B, 6 −in B, 7 out B, 8 V+.
Pin 1 is next to the notch or dot.

## After
No calibration is needed (S3 p6). Follow `tests.md`.

## Alternative: RATA upgrade, January 1993 (S9)
Russ Andrews' 1993 data sheet for a post-8000 unit (it lists IC24–27 and C89–C92):

| Stage | Change |
|---|---|
| 1 | Mains lead upgrade; replace bridge D34 with 4 × 11DQ10 Schottky diodes; **remove C81 and C82**; replace C74 with 1000µF 25V electrolytic bypassed with 0.01µF film |
| 2 | All TL071 (9) → AD711JN or AD847JN; IC24–27 → AD712JN or AD827JN |
| 3 | C30, C31, C48, C54, C59, C77, C78, C89–C92 → 100µF **10V** electrolytic |

Points to raise with the user:
- **C74 voltage conflict:** RATA specifies 25V, but Quad's service data says C74 carries about 30V DC (S8 p4). A 25V part would be under-rated on that figure. Measure the voltage across C74 on the user's unit and choose a rating comfortably above it. Don't recommend 25V.
- C81/C82 were added by Quad at S/N 6001 to reduce RF clicks (S8 p21); RATA removes them. Present both.
- RATA's 10V rating for the 100µF coupling and decoupling caps is the only replacement voltage rating in the sources. The rails are +8.6V / −9.4V (S8).
- DADA links out C30, C31, C48, C54, C89–C92 where RATA replaces them. Different philosophies — let the user choose.

## Voltage ratings — what the sources say
- Quad's parts list (S8 p24–25) gives values and stock numbers but no voltage ratings. The stock codes differ between parts (e.g. C48/C54 are C100UKT, other 100µ parts C100UME), but the codes aren't decoded in any source — don't interpret them.
- Early units used 100µF 3V tantalums for coupling (S5).
- RATA used 10V for the 100µF parts (S9); see the C74 warning above.
