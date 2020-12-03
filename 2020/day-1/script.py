from typing import List


def sum_two_and_multiply(entries: List[int], target: int = 2020) -> int:
    for first_entry in entries:
        second_entry = target - first_entry
        if second_entry in entries:
            return first_entry * second_entry

    raise ValueError(f"There are not two entries that add up to {target}.")


def sum_three_and_multiply(entries: List[int], target: int = 2020) -> int:
    while entries:
        first_entry = entries.pop()
        intermediate_target = target - first_entry

        try:
            return first_entry * sum_two_and_multiply(
                entries, target=intermediate_target
            )
        except ValueError:
            continue

    raise ValueError(f"There are not three entries that add up to {target}.")


if __name__ == "__main__":
    with open("input.txt", "r") as reader:
        inp = list(map(int, reader))

    # Part One
    print(sum_two_and_multiply(inp))

    # Part Two
    print(sum_three_and_multiply(inp))
