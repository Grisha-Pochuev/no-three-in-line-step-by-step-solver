# n67 case: current near-miss search state

This folder records the current state of the search for a classical no-three-in-line configuration on a 67 x 67 grid.

Goal for n=67:

- place 134 points on the 67 x 67 grid;
- keep exactly 2 points in every row;
- keep exactly 2 points in every column;
- avoid every straight line containing 3 or more selected points.

Current result:

- no complete n=67 solution yet;
- best known candidate in this local search has 134 points;
- every row has exactly 2 points;
- every column has exactly 2 points;
- 10 bad lines remain.

Best candidate:

```text
.PbYjZbOWHldhhrDVAIOcivp@6pw@BCNURWdz4vgj1JAP56Jou#i&5H9n02Ta2o1wn#3G7%F$Ta$&Gumy0L39Fkxyetk%KN8z4QDcZgrs7BExEX8LRfltYqCMMQImXfSUKVSeqs
```

Files in this folder:

- `candidates/best_10_conflicts_n67.few` — best current candidate, 10 bad lines.
- `candidates/previous_13_conflicts_n67.few` — earlier candidate, 13 bad lines.
- `candidates/expanded_n65_18_conflicts_n67.few` — earlier expansion from n=65, 18 bad lines.
- `candidates/best_10_conflicts_n67_points.csv` — decoded point coordinates for the best candidate.
- `reports/verification_best_10_conflicts.txt` — independent verification output.
- `reports/status_2026-06-21.md` — human-readable work log.
- `reports/bad_lines_best_10.md` — the 10 remaining bad lines.
- `NEXT_STEPS.md` — suggested next search directions.
- `tools/verify_few.py` — verifier for Flammenkamp-style `.few` code words.

Important note:

This is not a proof and not a finished solution. It is a clean checkpoint for the n=67 search. The main value is that the best current candidate is compact, reproducible, and independently checkable.

Sources used for format and public context:

- Achim Flammenkamp, no-three-in-line problem: https://wwwhomes.uni-bielefeld.de/achim/no3in/readme.html
- Number table: https://wwwhomes.uni-bielefeld.de/achim/no3in/table.html
