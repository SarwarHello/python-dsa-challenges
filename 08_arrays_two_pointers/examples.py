"""Deterministic Day 8 examples; run after editable installation."""

from dsa_challenges.arrays import move_zeros, reverse_in_place
from dsa_challenges.two_pointers import pair_sum_sorted, sorted_squares


def main() -> None:
    """Show mutation separately from functions returning new results."""
    values = [1, 2, 3, 4]
    reverse_in_place(values)
    print(f"Reversed: {values}")
    values = [0, 1, 0, 3, 12]
    move_zeros(values)
    print(f"Zeros moved: {values}")
    print(f"Pair indices: {pair_sum_sorted([-5, -2, 0, 3, 8], 3)}")
    print(f"Sorted squares: {sorted_squares([-4, -1, 0, 3, 10])}")


if __name__ == "__main__":
    main()
