# Remaining bad lines in the best n=67 candidate

Candidate:

```text
.PbYjZbOWHldhhrDVAIOcivp@6pw@BCNURWdz4vgj1JAP56Jou#i&5H9n02Ta2o1wn#3G7%F$Ta$&Gumy0L39Fkxyetk%KN8z4QDcZgrs7BExEX8LRfltYqCMMQImXfSUKVSeqs
```

Coordinate convention: `(row, column)`.

The verifier reports 10 bad lines:

```text
line (2, -3, -137): [(1, 45), (49, 13), (52, 11)]
line (4, -9, -307): [(7, 31), (16, 27), (52, 11)]
line (3, -7, -238): [(7, 31), (21, 25), (49, 13)]
line (1, -1, -63): [(12, 51), (52, 11), (55, 8)]
line (2, -1, -115): [(25, 65), (46, 23), (52, 11)]
line (1, 1, -21): [(26, 5), (54, 33), (62, 41)]
line (1, -1, -87): [(39, 48), (49, 38), (54, 33)]
line (11, -5, -759): [(44, 55), (54, 33), (59, 22)]
line (4, 1, -183): [(49, 13), (54, 33), (56, 41)]
line (3, 1, -145): [(52, 11), (53, 14), (62, 41)]
```

Hot points by visual inspection of the bad-line list:

- `(52, 11)` appears often.
- `(49, 13)` appears often.
- `(54, 33)` appears often.
- `(62, 41)` appears more than once.
- Rows 49, 52, 54 and 62 are especially important.

This does not mean only these rows need to move. A local repair restricted to the visible conflict rows was checked and did not work while the rest of the board remained fixed.
