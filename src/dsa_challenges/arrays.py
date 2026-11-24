"""In-place array scans with constant auxiliary space."""


def reverse_in_place[T](values: list[T]) -> None:
    """Reverse the same list by endpoint swaps; O(n) time, O(1) extra space."""
    left, right = 0, len(values) - 1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1


def move_zeros(values: list[int]) -> None:
    """Move zeros to the end, preserving nonzero order; mutate and return None.

    Follow the annotated integer contract. O(n) time, O(1) auxiliary space.
    """
    write = 0
    for read in range(len(values)):
        if values[read] != 0:
            values[write] = values[read]
            write += 1
    for index in range(write, len(values)):
        values[index] = 0
