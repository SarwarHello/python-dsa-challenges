# Day 8 - arrays and two pointers

Original exercises, not copied challenge solutions. Implementations are in
[src/dsa_challenges](../src/dsa_challenges); tests use independent reference methods.

```powershell
.venv\Scripts\python.exe 08_arrays_two_pointers/examples.py
```

```text
Reversed: [4, 3, 2, 1]
Zeros moved: [1, 3, 12, 0, 0]
Pair indices: (0, 4)
Sorted squares: [0, 1, 9, 16, 100]
```

## Problems and contracts

| Function | Problem | Mutation / result | Time | Space |
| --- | --- | --- | --- | --- |
| reverse_in_place | Reverse a list without a reversed copy | Same list mutated; None | O(n) | O(1) auxiliary |
| move_zeros | Put integer zeros last while preserving nonzero order | Same list mutated; None | O(n) | O(1) auxiliary |
| pair_sum_sorted | Find two distinct indices whose values sum to target | Input unchanged; index tuple or None | O(n) including validation | O(1) auxiliary |
| sorted_squares | Square a sorted integer sequence and keep results sorted | New list; input unchanged | O(n) including validation | O(n) output; O(1) working |

Python lists provide array-like indexing but are not fixed-size C arrays. Complexity
assumes constant-time indexing/comparisons/arithmetic; custom Sequence types may
have slower access, and large Python integers increase arithmetic cost. Functions
follow the annotated element types without runtime checks of every element.

Both sorted-input functions check nondecreasing order and reject inversions with
ValueError. They do not sort a copy, which would obscure original indices and add
O(n log n) work. Duplicates, negative values and empty input are supported. A pair
always has left < right, so one element is never reused. If several pairs exist,
return the first match from the endpoint scan, not necessarily the smallest pair
of indices. Squaring preserves duplicates. Reverse accepts arbitrary list elements.

## Why the algorithms work

**Reverse:** everything outside [left, right] is already in its final position.
Swapping endpoints places two more elements, then both pointers move inward. At
most floor(n/2) swaps occur. Empty/singleton lists need no swaps.

**Move zeros:** before processing read, values[:write] contains the original
nonzero elements seen so far, in order. Since write never exceeds read, copying a
nonzero backward cannot overwrite unread input. After the scan, zero-fill the
remaining suffix. Two linear passes still give O(n). Unlike core-mastery's ordered
deduplication, this preserves duplicate nonzero values and uses no set or output list.

**Pair sum:** if the endpoint sum is too small, pairing the current left value with
any remaining smaller right value cannot reach the target, so discard left. If it
is too large, pairing the current right value with any remaining larger left value
cannot reach the target, so discard right. Every step removes one impossible
endpoint; a solution cannot be skipped. For [-5,-2,0,3,8] and target 3, endpoints
already sum to 3, yielding indices (0,4).

**Sorted squares:** the largest remaining square is at one of the endpoints: the
most negative or most positive remaining value. Place that square in the last
unfilled result slot and advance only its pointer. The suffix stays sorted and
contains the largest squares, so filling backward yields a sorted result. Simply
squaring left-to-right fails for mixed signs.

## Verification and interview review

Tests cover empty/singleton inputs, even/odd reversal, object identity, duplicates,
negative/all-zero/no-zero inputs, absent/multiple pairs, unsorted rejection, tuple
input and large integers. Exhaustive small-input checks compare array transforms
with simple reference expressions and pair existence with a quadratic brute-force
oracle. These check correctness, not speed; there are no timing assertions.

Explain each loop invariant, why pointers move in their chosen direction, why
sorted input matters, and why output space differs from auxiliary space. A brute
force pair search costs O(n squared); a hash-based alternative belongs to Day 9.
