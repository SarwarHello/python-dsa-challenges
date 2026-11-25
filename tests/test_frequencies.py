"""Frequency behaviour, deliberate collisions and independent references."""

from dataclasses import dataclass
from itertools import product

import pytest

from dsa_challenges.frequencies import first_unique_index, multiset_intersection


@pytest.mark.parametrize(
    "values,expected",
    [
        ([], None),
        ([1], 0),
        ([1, 1], None),
        ([2, 1, 2, 3], 1),
        ([1, 1, 2], 2),
        ("swiss", 1),
        ((None, None, "x"), 2),
        ([(1, 2), (3, 4), (1, 2)], 1),
    ],
)
def test_first_unique(values, expected):
    before = list(values)
    assert first_unique_index(values) == expected
    assert list(values) == before


@pytest.mark.parametrize(
    "left,right,expected",
    [
        ([], [], []),
        ([1], [], []),
        ([], [1], []),
        ([1], [2], []),
        ([2, 1, 2, 2], [2, 2, 1], [2, 1, 2]),
        ([1, 1], [1, 1, 1], [1, 1]),
        ([-1, 0, -1], [-1, 0], [-1, 0]),
        (["b", "a", "b"], ["a", "b"], ["b", "a"]),
    ],
)
def test_intersection(left, right, expected):
    before_left, before_right = left.copy(), right.copy()
    assert multiset_intersection(left, right) == expected
    assert left == before_left and right == before_right


def test_independent_generators():
    assert multiset_intersection(iter([3, 1, 3]), iter([3, 3])) == [3, 3]


@dataclass(frozen=True)
class CollidingKey:
    value: str

    def __hash__(self):
        return 0


def test_collisions_preserve_equality_and_left_identity():
    a, b, another_a = CollidingKey("a"), CollidingKey("b"), CollidingKey("a")
    assert first_unique_index([a, b, another_a]) == 1
    result = multiset_intersection([a, b, another_a], [CollidingKey("a"), b])
    assert len(result) == 2
    assert result[0] is a and result[1] is b


def test_unhashable_elements_raise():
    with pytest.raises(TypeError):
        first_unique_index([[]])
    with pytest.raises(TypeError):
        multiset_intersection([], [[]])
    with pytest.raises(TypeError):
        multiset_intersection([[]], [])


def test_small_inputs_against_list_references():
    samples = [values for size in range(5) for values in product((0, 1), repeat=size)]
    for left in samples:
        expected_index = next(
            (i for i, v in enumerate(left) if left.count(v) == 1), None
        )
        assert first_unique_index(left) == expected_index
        for right in samples:
            available = list(right)
            expected = []
            for value in left:
                if value in available:
                    expected.append(value)
                    available.remove(value)
            assert multiset_intersection(left, right) == expected
