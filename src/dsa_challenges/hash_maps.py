"""Complement lookup without sorting or losing original indices."""

from collections.abc import Iterable


def pair_sum_unsorted(values: Iterable[int], target: int) -> tuple[int, int] | None:
    """Return the pair with earliest second index, then earliest first index.

    Return None if absent. Consume input once, stopping at the first match; do not
    mutate it. Expected O(n) time and O(n) space with constant-cost integer hashing
    and arithmetic; pathological collisions can make time O(n squared).
    """
    first_seen: dict[int, int] = {}
    for right, value in enumerate(values):
        complement = target - value
        if complement in first_seen:
            return first_seen[complement], right
        first_seen.setdefault(value, right)
    return None
