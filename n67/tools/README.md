# Tools for n67

## verify_few.py

Checks Flammenkamp-style `.few` code words.

Example from the repository root:

```bash
python n67/tools/verify_few.py n67/candidates/best_10_conflicts_n67.few --n 67 --show-bad
```

Expected current output:

```text
n = 67
points = 134
row-count histogram = {2: 67}
column-count histogram = {2: 67}
bad lines = 10
solution = no
```

To export decoded points:

```bash
python n67/tools/verify_few.py n67/candidates/best_10_conflicts_n67.few --n 67 --write-points-csv n67/candidates/best_10_conflicts_n67_points.csv
```
