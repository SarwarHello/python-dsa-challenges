# Progress

Last updated: 25 November 2026 (Europe/London).
Local repository: E:\python-dsa-challenges.

## Day 8 - complete implementation

- Created independent Python 3.12+ src package, .venv, pinned development tools,
  repository instructions, roadmap and problem index. No runtime dependencies.
- Implemented reverse_in_place and move_zeros with explicit mutation contracts.
- Implemented pair_sum_sorted and sorted_squares, validating sorted order and
  preserving input. No duplicated core-mastery exercises.
- Added correctness arguments, complexity/space analysis, boundary tests,
  exhaustive independent-reference checks and deterministic examples.
- Validation: 36 pytest cases passed, 0 failed/skipped; Ruff lint/format and pip
  check passed; editable installation verified. Final demo/CI integration checked
  before publication. Windows local checks; Ubuntu CI result tracked separately.
- Commits: 76afa09 (package and in-place arrays), e219b48 (sorted two-pointer
  algorithms), and the commit containing the guide/example/CI integration.
- No backdating: original target was 19 October, actual completion is 24 November.
- Publication and remote CI outcomes are recorded in the central workspace log.

## Day 9 - complete implementation (25 November 2026)

- Added pair_sum_unsorted with deterministic earliest-second/earliest-first index
  selection, plus first_unique_index and stable multiset_intersection.
- Added 32 tests: duplicates, empty inputs, generators, collisions, non-mutation,
  object identity and exhaustive small-input checks against independent references.
- Full suite: 68 passed, 0 failed/skipped; Ruff lint/format passed. Both examples
  match their guides; pip check passed. No new dependencies.
- Added correctness proofs, expected/worst-case complexity and documented input
  contracts; updated CI to run the Day 9 example.
- Commits: da80fe7 (complement lookup), bcd0fbe (frequency algorithms),
  and the commit containing Day 9 guides/examples/CI integration.
- Original target date preserved; no backdating. Publication and actual remote CI
  results are recorded in the central workspace log after pushing.

## Next step

Day 10: binary search, when instructed.
