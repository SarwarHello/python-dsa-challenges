"""Boundary cases and exhaustive comparisons with independent oracles."""

from itertools import combinations_with_replacement

import pytest

from dsa_challenges.two_pointers import pair_sum_sorted, sorted_squares


@pytest.mark.parametrize(
    "values,target,expected",
    [
        ([], 0, None),
        ([1], 2, None),
        ([1, 2], 3, (0, 1)),
        ([2, 2], 4, (0, 1)),
        ([-5, -2, 0, 3, 8], 3, (0, 4)),
        ([1, 2, 3, 4], 5, (0, 3)),
        ([1, 2, 3], 99, None),
        ([0, 0, 0], 0, (0, 2)),
    ],
)
def test_pair_sum_contract(values, target, expected):
    original = values.copy()
    assert pair_sum_sorted(values, target) == expected
    assert values == original


@pytest.mark.parametrize(
    "values,expected",
    [
        ([], []),
        ([0], [0]),
        ([-3], [9]),
        ([-5, -2], [4, 25]),
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-2, -2, 2], [4, 4, 4]),
        ([1, 2, 3], [1, 4, 9]),
    ],
)
def test_sorted_squares_contract(values, expected):
    original = values.copy()
    result = sorted_squares(values)
    assert result == expected
    assert values == original
    assert result is not values


@pytest.mark.parametrize("values", [[2, 1], [1, 3, 2], [0, -1]])
def test_unsorted_input_rejected_without_mutation(values):
    original = values.copy()
    with pytest.raises(ValueError, match="sorted"):
        pair_sum_sorted(values, 3)
    with pytest.raises(ValueError, match="sorted"):
        sorted_squares(values)
    assert values == original


def test_tuple_input_and_large_integers():
    big = 10**50
    values = (-big, 0, big)
    assert pair_sum_sorted(values, 0) == (0, 2)
    assert sorted_squares(values) == [0, big**2, big**2]


def test_small_sorted_inputs_against_brute_force():
    for length in range(6):
        for values in combinations_with_replacement(range(-3, 4), length):
            assert sorted_squares(values) == sorted(v * v for v in values)
            for target in range(-7, 8):
                exists = any(
                    values[i] + values[j] == target
                    for i in range(length)
                    for j in range(i + 1, length)
                )
                pair = pair_sum_sorted(values, target)
                assert (pair is not None) == exists
                if pair is not None:
                    left, right = pair
                    assert 0 <= left < right < length
                    assert values[left] + values[right] == target
