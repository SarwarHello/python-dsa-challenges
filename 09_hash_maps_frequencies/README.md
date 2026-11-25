# Day 9: hash maps and frequency counting

These exercises use dictionaries to preserve information across a scan. They add
complement lookup, unique-position selection and multiplicity-limited matching,
without repeating the core repository's word counter. No runtime dependencies.

## Run

From the repository root, after the README installation steps:

```powershell
.venv\Scripts\python.exe 09_hash_maps_frequencies/examples.py
```

```text
Unsorted pair indices: (1, 3)
First unique index: 1
Multiset intersection: [2, 1, 2]
```

## Contracts and correctness

### pair_sum_unsorted(values, target)

Accept a finite iterable of integers and an integer target. Return distinct
zero-based indices `(i, j)` with `i < j`, or None when no pair exists. Choose the
smallest possible j, then the smallest i for that j. This is deliberately different
from Day 8's sorted endpoint scan: unsorted input keeps its original positions,
uses extra memory and requires no sorting. The function does not mutate input;
a one-shot iterator is consumed only through the match, or fully if no match exists.

Before processing index j, the dictionary contains the earliest index of each
value in the prefix before j. Looking up target minus the current value therefore
finds exactly a valid earlier partner. Looking up before inserting prevents reuse
of the same element. setdefault preserves the earliest partner among duplicates.
Scanning j in order proves the tie rule. Empty or single-item inputs return None;
[3, 3] with target 6 returns (0, 1).

### first_unique_index(values)

Accept a repeatable sequence of hashable values; return the index of the first
value with frequency one, or None. Input is unchanged. Build counts over the whole
sequence, then scan in original order. After counting, each dictionary entry is
exactly its value's multiplicity. The second scan therefore returns the earliest
unique value and cannot mistakenly choose an item repeated later. Empty and
all-repeated sequences return None. Strings are processed by Python code point,
without normalization or case folding, not by grapheme cluster.

### multiset_intersection(left, right)

Accept two finite iterables of hashable values with independent iteration state.
Fully consume right first, then left. Return original left objects in left order,
including each value at most min(left count, right count) times. Inputs are not
mutated, but iterators are consumed. Do not pass the same one-shot iterator twice;
passing the same repeatable list twice is valid. Empty/disjoint inputs return [].

The dictionary records each right value's unused allowance. A left value is emitted
only when its allowance is positive, then that allowance decreases by one. Thus
no right occurrence is reused, and every eligible left occurrence is included.
A set intersection would lose both multiplicity and this stable left order.

## Complexity and limits

| Algorithm | Expected time | Working space | Output space |
| --- | --- | --- | --- |
| pair_sum_unsorted | O(n) | O(n) | O(1) |
| first_unique_index | O(n) | O(k) | O(1) |
| multiset_intersection | O(n + m) | O(k_right) | O(r) |

k means distinct values, m is the right length and r the number of matches.
These bounds assume constant-cost hashing, equality and integer arithmetic.
Pathological hash collisions can make the first two O(n squared), and intersection
O((n + m) * max(1, k_right)). Large integers and expensive custom equality/hash
methods add their own costs. Dictionary collision handling preserves correctness;
equal hashes alone do not make keys equal.

Hashable values must obey Python's equality/hash contract and remain stable while
used as keys. Values that compare equal (such as 1 and True) share a count.
Unhashable values raise TypeError naturally. The functions follow type annotations
without coercion or broad runtime type validation. They do not catch exceptions
from custom hashing, equality or input iteration, and are not safe against concurrent
input mutation. Frequency counts need the complete input; they cannot establish
uniqueness in an infinite stream.

## Verification and interview prompts

Tests cover empty inputs, duplicates, negative/large integers, tie ordering,
non-mutation, independent generators, deliberate collisions, left-object identity
and unhashable inputs. Exhaustive small cases use quadratic pair search, list.count,
and list-removal matching as independent oracles. Tests make no timing assertions.

- Why must complement lookup happen before insertion?
- Why can a set not implement multiset matching?
- Why does first-unique selection need complete counts before returning?
- What does a collision change about correctness versus performance?
- When would Day 8's constant-space sorted scan be preferable?
