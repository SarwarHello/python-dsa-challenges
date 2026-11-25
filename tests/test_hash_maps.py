"""Compare complement lookup with an independent quadratic search."""

from itertools import product

import pytest

from dsa_challenges.hash_maps import pair_sum_unsorted


@pytest.mark.parametrize(
    "values,target,expected",
    [
        ([], 0, None),
        ([3], 6, None),
        ([3, 3], 6, (0, 1)),
        ([2, 7, 11, 15], 9, (0, 1)),
        ([5, 1, 5, 4], 9, (0, 3)),
        ([1, 4, 2, 3], 5, (0, 1)),
        ([-3, 8, 2], -1, (0, 2)),
        ([0, 0], 0, (0, 1)),
        ([1, 2], 9, None),
        ([10**100, 1, -(10**100)], 0, (0, 2)),
    ],
)
def test_pair_sum(values, target, expected):
    before = values.copy()
    assert pair_sum_unsorted(values, target) == expected
    assert values == before


def test_generator_stops_at_match():
    values = iter([3, 3, 99])
    assert pair_sum_unsorted(values, 6) == (0, 1)
    assert next(values) == 99


def test_small_inputs_against_quadratic_reference():
    for size in range(6):
        for values in product((-1, 0, 1), repeat=size):
            for target in range(-3, 4):
                expected = next(
                    (
                        (i, j)
                        for j in range(len(values))
                        for i in range(j)
                        if values[i] + values[j] == target
                    ),
                    None,
                )
                assert pair_sum_unsorted(values, target) == expected
