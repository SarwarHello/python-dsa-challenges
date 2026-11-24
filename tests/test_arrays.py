"""Array behaviour and independent small-input reference checks."""

from itertools import product

import pytest

from dsa_challenges.arrays import move_zeros, reverse_in_place


@pytest.mark.parametrize(
    "values", [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 1, 2], ["a", None, "b"]]
)
def test_reverse(values):
    original = values.copy()
    alias = values
    assert reverse_in_place(values) is None
    assert values is alias
    assert values == original[::-1]
    reverse_in_place(values)
    assert values == original


def test_reverse_preserves_object_identity():
    first, second = [], {}
    values = [first, second]
    reverse_in_place(values)
    assert values[0] is second and values[1] is first


@pytest.mark.parametrize(
    "values,expected",
    [
        ([], []),
        ([0], [0]),
        ([1], [1]),
        ([0, 0], [0, 0]),
        ([1, 2], [1, 2]),
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([-1, 0, -1, 2, 0], [-1, -1, 2, 0, 0]),
    ],
)
def test_move_zeros(values, expected):
    alias = values
    assert move_zeros(values) is None
    assert values is alias
    assert values == expected


def test_small_arrays_against_independent_references():
    for length in range(6):
        for values in product((-1, 0, 1), repeat=length):
            reversed_values = list(values)
            reverse_in_place(reversed_values)
            assert reversed_values == list(reversed(values))
            compacted = list(values)
            move_zeros(compacted)
            assert compacted == [v for v in values if v != 0] + [0] * values.count(0)
