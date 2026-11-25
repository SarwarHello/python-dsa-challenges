"""Frequency-based selection and stable multiset matching."""

from collections.abc import Hashable, Iterable, Sequence


def first_unique_index[T: Hashable](values: Sequence[T]) -> int | None:
    """Return the first index whose value occurs once, or None.

    Input is unchanged. Expected O(n) time and O(k) space for k distinct values,
    assuming constant-cost hashing, equality and sequence iteration.
    """
    counts: dict[T, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    for index, value in enumerate(values):
        if counts[value] == 1:
            return index
    return None


def multiset_intersection[T: Hashable](
    left: Iterable[T], right: Iterable[T]
) -> list[T]:
    """Return matches in left order, each at most its count in right.

    Fully consume right then left, each once. Inputs must be finite, with
    independent iteration state. Return original left objects without mutation.
    Expected O(n + m) time, O(k) working space for k distinct right values, plus
    O(r) output space for r matches. Hash/equality costs are assumed constant.
    """
    remaining: dict[T, int] = {}
    for value in right:
        remaining[value] = remaining.get(value, 0) + 1
    result: list[T] = []
    for value in left:
        if remaining.get(value, 0) > 0:
            result.append(value)
            remaining[value] -= 1
    return result
