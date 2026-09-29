# Quad 405 — amplifier boards

**Status:** draft; all values provisional (unverified against a physical board).

The two amplifier boards are identical, one per channel, so every quantity in `../../data/quad-405-bom.csv` is for both boards. Do one board at a time and use the other as a reference (Q405-S01 p5).

## Applicability

- DADA's kit covers the 405 and 405-2; differences are noted below (Q405-S01 p1).
- Quad fitted several board issues (see `overview.md`). Original values below are from Quad's earliest parts list (p14, board M12368 iss 5/6) and the last 405-2 list (p24, M12565 iss 7). A board in between may differ; a technician should compare the fitted parts.
- Stop and ask if the board has previous repairs or values that differ from both lists.

## Restoration (both variants)

| Ref | Quad original | DADA replacement (Q405-S01 p2–3, p6) | Notes |
|---|---|---|---|
| IC1 | LM301A (early, p14); TL071 (405-2, p24) | OPA604 (OPA627 option) | Fit last to avoid static damage; handle with pliers (Q405-S01 p6) |
| D1, D2 | 12 V zener LR120C (early); 15 V LR150C from S/N 29,000 (Q405-S02 p8); BZY88C 15 V on 405-2 (p24) | 15 V 1.3 W zener | Set the op-amp supply. Watch the stripe. |
| C2 | 100 µF 3 V (p14); 100 µF on 405-2 (p24) | 100 µF 16 V, polarised | **Fit with + to signal ground.** DADA explains the op-amp input sits slightly negative, which is why Quad later used a non-polar part (Q405-S01 p3). |
| C5 | 100 µF 6 V (p14); 100 µF (p24) | 100 µF 25 V | Polarised |
| C10 | 47 µF 40 V (p14); 47 µF (p24) | 100 µF 63 V | Polarised |
| C17 | 10 µF (clamp circuit, p24) | 10 µF 35 V bipolar | On the main board, on the separate clamp board at the output terminals, or absent before S/N 9000 unless retrofitted (Q405-S01 p3, p6) |
| C18, C19 (405-2 only) | 47 µF (current limiter, p24) | 47 µF 16 V | Polarised. Not the same parts as the C18/C19 on early M12368 boards (Q405-S02 p8). |
| C3 | 3.3 pF (p14) | Remove | DADA removes it; it is omitted from board M12565.5 (Q405-S01 p6) |
| R7, R8 | 3K3 (p14, p24) | 3K 1 % | |

DADA's own voltage ratings are a minimum; "a higher voltage rating is no problem" (Q405-S01 p1). Re-check polarity of every electrolytic and diode, and look for solder bridges on both sides when finished (Q405-S01 p7). Appendix photos show capacitor polarity for the 405-1 and 405-2 boards (Q405-S01 p11).

## Zener decoupling (added parts)

After fitting the new zeners, DADA adds a 2K7 resistor across D2 and a 100 nF capacitor across D1, both on the **copper side**. The 2K7 reduces switch-off noise (Q405-S01 p3, p6).

## Input sensitivity (optional modification)

Quad's 405 gives 100 W for 0.5 V input (Q405-S02 p5, test 3). DADA lowers the sensitivity by changing local and DC feedback, which it says reduces noise and distortion by 9 dB (1.5 V) or 4.5 dB (0.775 V) (Q405-S01 p6). **Leave R4, R6 and C4 alone to keep 0.5 V** (Q405-S01 p2, p6).

| Sensitivity | R6 | R4 | C4 (10 mm pitch) |
|---|---|---|---|
| 0.5 V (factory) | as fitted (330K) | as fitted (10K early, 22K from M12368.7) | as fitted (47 nF) |
| 0.775 V | 220K 1 % | 15K 1 % | 68 nF |
| 1.5 V | 100K 1 % | 6K8 1 % | 150 nF |

Source for the new values: Q405-S01 p2, p6. Always change R6 and C4 together as a matched pair. Ask what the user's preamp delivers before recommending a lower sensitivity.

## Alternative parts list

A community parts list for the 405-2 (Q405-S03, author unknown) uses an OPA134 op-amp in a socket with 100 nF supply decoupling, a bipolar 100 µF C2 with a 100 nF film bypass, 100 µF 6.3 V for C5 with a 1 µF bypass, and 47 µF 63 V for C10. It disagrees with DADA on C2 polarity, C5 voltage and C10 value. Present it only as an alternative, never mixed with the DADA list.

## Transistors

Not part of the recap. Quad lists interchangeable types (Q405-S02 p8). Output transistors TR9/TR10 can be MJ15003; DADA offers these as an option (Q405-S01 p3).

## After the work

See `tests.md`.
