"""Opposite-end scans on nondecreasing integer sequences."""

from collections.abc import Sequence


def _check_sorted(values: Sequence[int]) -> None:
    if any(values[i] > values[i + 1] for i in range(len(values) - 1)):
        raise ValueError("values must be sorted in nondecreasing order")


def pair_sum_sorted(values: Sequence[int], target: int) -> tuple[int, int] | None:
    """Return distinct zero-based indices whose values sum to target, or None.

    Validate sorted order, then scan inward, returning the first match encountered.
    Multiple valid pairs need not give the lexicographically smallest index pair.
    Input is unchanged. O(n) time including validation, O(1) auxiliary space,
    assuming O(1) indexing/arithmetic and the annotated integer input contract.
    """
    _check_sorted(values)
    left, right = 0, len(values) - 1
    while left < right:
        total = values[left] + values[right]
        if total == target:
            return left, right
        if total < target:
            left += 1
        else:
            right -= 1
    return None


def sorted_squares(values: Sequence[int]) -> list[int]:
    """Return squared values in sorted order without sorting or mutating input.

    Reject descending adjacent values. Fill the result from the end by comparing
    squared endpoints. O(n) time, O(n) result space, O(1) additional working space,
    under constant-cost indexing/arithmetic. Python integers do not overflow, but
    arithmetic cost grows with their bit length.
    """
    _check_sorted(values)
    result = [0] * len(values)
    left, right = 0, len(values) - 1
    for output in range(len(values) - 1, -1, -1):
        low, high = values[left] ** 2, values[right] ** 2
        if low > high:
            result[output] = low
            left += 1
        else:
            result[output] = high
            right -= 1
    return result
