# Python DSA Challenges

Original, tested Python algorithms for interview practice. Python 3.12+; no runtime
dependencies. Exercises specify behaviour and explain correctness and complexity.

## Setup (PowerShell, repository root)

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.venv\Scripts\python.exe -m pip install --no-build-isolation -e .
.venv\Scripts\python.exe -m pytest
.venv\Scripts\python.exe -m ruff check .
.venv\Scripts\python.exe -m ruff format --check .
```

On Linux/macOS use python3.12 and .venv/bin/python. Development pins use the tools
already validated in the core repository, installed into an independent environment.
No static type-checker pass is claimed. No license has been selected yet.

## Array exercises

`reverse_in_place` reverses a list using endpoint swaps and returns None.
`move_zeros` moves integer zeros to the end, keeping nonzero order, and returns None.
Both mutate the original list in O(n) time and O(1) auxiliary space. They follow
the annotated input contracts, without runtime element-type validation.

Package source lives in src/dsa_challenges; tests live in tests/. Python lists
serve as array-like random-access sequences; these are not fixed-size C arrays.

## Day 8: arrays and two pointers

[Worked exercises](08_arrays_two_pointers/README.md) explain all four algorithms,
loop invariants and edge cases. [Problem index](docs/problem-index.md) tracks topics.

```powershell
.venv\Scripts\python.exe 08_arrays_two_pointers/examples.py
```

```text
Reversed: [4, 3, 2, 1]
Zeros moved: [1, 3, 12, 0, 0]
Pair indices: (0, 4)
Sorted squares: [0, 1, 9, 16, 100]
```

pair_sum_sorted returns distinct zero-based indices or None; sorted_squares returns
a new list. Both reject unsorted input and run in O(n), including validation.
Pair search uses O(1) extra space; squares needs O(n) result space. Arithmetic costs
for large integers and nonconstant indexing may change these simple bounds.

68 tests include exhaustive small-input comparisons with independent reference
solutions. CI runs tests, lint, formatting and both examples on Python 3.12.
See [ROADMAP.md](ROADMAP.md) and [PROGRESS.md](PROGRESS.md) for actual work and next steps.

## Day 9: hash maps and frequency counting

[Worked exercises](09_hash_maps_frequencies/README.md) explain unsorted pair lookup,
first-unique indices and stable multiset intersection, including tie rules,
collision behaviour and expected versus worst-case complexity.

```powershell
.venv\Scripts\python.exe 09_hash_maps_frequencies/examples.py
```

Expected output: pair indices (1, 3), unique index 1, intersection [2, 1, 2].
