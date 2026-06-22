> Project status: archived.
>
> This repository was an exploratory step-by-step attempt to study the classical no-three-in-line problem.
> The project is no longer actively maintained, because the current computational frontier is better covered by specialized SAT-based work, including the public configurations collected by Achim Flammenkamp and recent solutions by Marijn Heule.
> 
# No-Three-In-Line Solver Step by Step

This repository is part of my personal project **The Open Mathematics Project**.

The idea of this project is simple: mathematical work should be open, reusable, and readable. I want to publish attempts, configurations, scripts, notes, and partial progress under an open license, so that other people can inspect the work, reuse it, correct it, and maybe continue the search further.

This repository is devoted to the classical **no-three-in-line problem**. I want to approach it gradually, by small pieces, beginning from the current working frontier and then moving further. The spirit of the work is close to the old saying: water wears away stone. Not by one dramatic move, but by many small, checked, reproducible steps.

## What is the no-three-in-line problem?

Imagine an `n × n` square grid. We want to choose as many grid points as possible, but with one simple rule:

> No three chosen points may lie on the same straight line.

The line may have any slope. It is not enough to avoid only rows, columns, and the two main diagonal directions. A forbidden triple can appear on a shallow line, a steep line, or any other straight line passing through three grid points.

For any `n × n` grid, there is an immediate upper bound of `2n`: if we choose more than `2n` points, then some row must contain at least three chosen points. The deeper question is whether this upper bound can actually be reached, and how the best configurations behave as `n` grows.

This is why the problem is easy to state but hard to finish. It looks like a puzzle, but it leads into discrete geometry, combinatorics, computation, and the study of extremal configurations.

## Video introduction

A good popular introduction to the problem is this video:

[Unsolved Math: The No-Three-In-Line Problem](https://www.youtube.com/watch?v=eFlATdsDaj4)

## Short history

The no-three-in-line problem is usually attributed to the British puzzle maker **Henry Ernest Dudeney**. An early version appeared around **1900** as a recreational puzzle about placing pawns on a chessboard so that no three of them lie in a straight line.

Later the problem became part of serious discrete geometry. Mathematicians studied upper bounds, lower bounds, explicit constructions, symmetry, computational searches, and related versions on different grids and finite geometric spaces.

So the problem is more than a century old. In its general form, it is still not fully resolved. The obvious upper bound `2n` is very simple, but the global behavior remains subtle. For many small grids one can find full `2n`-point configurations, while the large-scale picture is still much less clear.

## Why this problem matters

This problem is interesting for several reasons.

- It is a bridge between recreational mathematics and research mathematics.
- It is simple enough to explain without technical language.
- It produces hard finite search problems.
- It connects geometry, number theory, combinatorics, and algorithms.
- It is a good test case for computer-assisted mathematical exploration.
- It has links to graph drawing and to avoiding unwanted degeneracies in geometric configurations.

In practical terms, no-three-in-line sets can be used as clean point sets where straight-line coincidences are controlled. This kind of condition appears in graph drawing, computational geometry, and search problems where accidental collinearities create extra complications.

## What this repository is trying to do

This repository is not meant to present a finished solution from the first day. It is meant to grow gradually.

The current plan is to work through the problem in small pieces, beginning with the present frontier and then moving to further grid sizes. Some parts may be computational. Some parts may be mathematical notes. Some parts may be failed attempts that are still useful because they show what does not work.

The long-term aim is to make the search process transparent: not only to store final configurations, but also to show how they were found, checked, improved, or rejected.

## Project philosophy

This repository follows the spirit of **The Open Mathematics Project**:

- open notes,
- open license,
- reproducible steps,
- reusable results,
- clear intermediate records,
- honest records of dead ends,
- gradual progress instead of hidden final answers.

The point is not only to solve instances, but also to make the process visible. If something here helps another person move the problem even a little further, then the repository has already done part of its job.

## Further reading

- [No-three-in-line problem — Wikipedia](https://en.wikipedia.org/wiki/No-three-in-line_problem)
- [Achim Flammenkamp: The No-Three-in-Line Problem](https://wwwhomes.uni-bielefeld.de/achim/no3in/readme.html)
- [Wolfram MathWorld: No-Three-in-a-Line Problem](https://mathworld.wolfram.com/No-Three-in-a-Line-Problem.html)
- [OEIS A000769: number of inequivalent full configurations](https://oeis.org/A000769)
