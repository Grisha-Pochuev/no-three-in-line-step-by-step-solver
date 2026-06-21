#!/usr/bin/env python3
"""
Verify Flammenkamp-style no-three-in-line configurations.

For n=67 the current candidate is not a solution yet: it has 134 points,
2 points in every row and column, and 10 bad lines.

Usage:
    python tools/verify_few.py candidates/best_10_conflicts_n67.few --n 67 --show-bad

The code word format used here is the one described by Achim Flammenkamp:
first character = symmetry class, then 2*n symbols giving the selected
column positions row by row.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from dataclasses import dataclass
from math import gcd
from pathlib import Path

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$%&@?!()[]<>{}=*+|-/~^_:;, .".replace(" ", "")
# Equivalent visible form, without the spaces used in Flammenkamp's prose:
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$%&@?!()[]<>{}=*+|-/~^_:;,.

SYMMETRY_CLASSES = set(".:/-ocx+*")


@dataclass(frozen=True)
class VerificationResult:
    n: int
    point_count: int
    row_count_histogram: Counter
    column_count_histogram: Counter
    bad_lines: list[tuple[tuple[int, int, int], list[tuple[int, int]]]]

    @property
    def is_solution(self) -> bool:
        return (
            self.point_count == 2 * self.n
            and self.row_count_histogram == Counter({2: self.n})
            and self.column_count_histogram == Counter({2: self.n})
            and not self.bad_lines
        )


def read_codeword(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split()
    if not parts:
        raise ValueError(f"empty configuration file: {path}")
    return parts[0].strip()


def decode_few(codeword: str, n: int) -> list[tuple[int, int]]:
    if len(codeword) != 1 + 2 * n:
        raise ValueError(
            f"expected codeword length {1 + 2 * n} for n={n}, got {len(codeword)}"
        )

    symmetry = codeword[0]
    if symmetry not in SYMMETRY_CLASSES:
        raise ValueError(f"unknown symmetry-class character: {symmetry!r}")

    points: list[tuple[int, int]] = []
    for row in range(n):
        for offset in (0, 1):
            ch = codeword[1 + 2 * row + offset]
            try:
                col = ALPHABET.index(ch)
            except ValueError as exc:
                raise ValueError(f"symbol {ch!r} is not in the 90-character alphabet") from exc
            if not 0 <= col < n:
                raise ValueError(f"decoded column {col} outside n={n} at row {row}")
            points.append((row, col))
    return points


def line_key(p: tuple[int, int], q: tuple[int, int]) -> tuple[int, int, int]:
    row1, col1 = p
    row2, col2 = q
    dx = col2 - col1
    dy = row2 - row1
    g = gcd(abs(dx), abs(dy))
    dx //= g
    dy //= g

    # Canonical orientation: same geometric line gives same key.
    if dx < 0 or (dx == 0 and dy < 0):
        dx = -dx
        dy = -dy

    # Invariant for line through (col,row): dy*col - dx*row.
    c = dy * col1 - dx * row1
    return dx, dy, c


def verify(points: list[tuple[int, int]], n: int) -> VerificationResult:
    if len(set(points)) != len(points):
        duplicates = [p for p, count in Counter(points).items() if count > 1]
        raise ValueError(f"duplicate points: {duplicates}")

    row_hist = Counter(Counter(row for row, _ in points).values())
    col_hist = Counter(Counter(col for _, col in points).values())

    lines: dict[tuple[int, int, int], set[int]] = defaultdict(set)
    for i, p in enumerate(points):
        for j in range(i + 1, len(points)):
            q = points[j]
            key = line_key(p, q)
            lines[key].add(i)
            lines[key].add(j)

    bad_lines = []
    for key, idxs in lines.items():
        if len(idxs) >= 3:
            bad_lines.append((key, [points[i] for i in sorted(idxs)]))

    bad_lines.sort(key=lambda item: (len(item[1]), item[1], item[0]))
    return VerificationResult(n, len(points), row_hist, col_hist, bad_lines)


def write_points_csv(points: list[tuple[int, int]], path: Path) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["row", "col"])
        writer.writerows(points)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("few_file", type=Path)
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--show-bad", action="store_true")
    parser.add_argument("--write-points-csv", type=Path)
    args = parser.parse_args()

    codeword = read_codeword(args.few_file)
    points = decode_few(codeword, args.n)
    result = verify(points, args.n)

    print(f"n = {result.n}")
    print(f"points = {result.point_count}")
    print(f"row-count histogram = {dict(result.row_count_histogram)}")
    print(f"column-count histogram = {dict(result.column_count_histogram)}")
    print(f"bad lines = {len(result.bad_lines)}")
    print(f"solution = {'yes' if result.is_solution else 'no'}")

    if args.show_bad:
        for key, pts in result.bad_lines:
            print(f"line {key}: {pts}")

    if args.write_points_csv:
        write_points_csv(points, args.write_points_csv)
        print(f"wrote points CSV: {args.write_points_csv}")


if __name__ == "__main__":
    main()
