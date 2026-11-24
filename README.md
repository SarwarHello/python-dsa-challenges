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
