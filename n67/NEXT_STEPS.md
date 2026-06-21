# Suggested next steps for n=67

## Main direction

Do not spend much more time on single swaps. The current 10-conflict candidate appears to be a genuine local trap.

The next search should rebuild a wider corridor while keeping most of the board fixed.

## Candidate repair zones

Start from rows that appear in the remaining bad lines:

```text
1, 7, 12, 16, 21, 25, 26, 39, 44, 46, 49, 52, 53, 54, 55, 56, 59, 62
```

Then enlarge the zone in a controlled way:

- include neighboring rows around 49, 52, 54 and 62;
- include rows whose columns collide with hot columns 11, 13, 33 and 41;
- allow the model to move at least 35-45 rows, not just the 18 visible rows.

## Search constraints worth keeping

Keep these constraints hard:

- 134 total points;
- exactly 2 points per row;
- exactly 2 points per column;
- no line with 3 or more points.

Possible softer constraints:

- keep most original row pairs unchanged;
- penalize moving points far from the current candidate;
- allow temporary conflicts during search, but require independent final verification.

## Useful immediate experiment

Build a CP/SAT-style repair model:

1. Fix all rows outside a selected repair zone.
2. For each row inside the zone, choose two columns.
3. Preserve global column counts.
4. Add all line constraints involving at least one movable point.
5. Minimize distance from the current candidate, or simply search for feasibility.

The earlier test suggests that the 18 visible rows alone are not enough. The first serious zone should probably contain at least 35 rows.

## Verification rule

Every alleged success must be checked with:

```bash
python tools/verify_few.py candidates/best_10_conflicts_n67.few --n 67 --show-bad
```

A fast local score is not enough. One false zero-conflict candidate was already rejected by independent verification.
