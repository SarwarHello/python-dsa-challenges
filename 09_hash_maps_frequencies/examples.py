"""Deterministic Day 9 examples; run from the installed repository."""

from dsa_challenges.frequencies import first_unique_index, multiset_intersection
from dsa_challenges.hash_maps import pair_sum_unsorted

print("Unsorted pair indices:", pair_sum_unsorted([8, 3, 5, 3], 6))
print("First unique index:", first_unique_index("swiss"))
print("Multiset intersection:", multiset_intersection([2, 1, 2, 2], [2, 2, 1]))
