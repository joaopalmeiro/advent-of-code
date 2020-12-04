import re
from dataclasses import dataclass
from typing import Pattern

TEMPLATE: Pattern = re.compile(
    r"^(?P<min_>\d+)-(?P<max_>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)$"
)


@dataclass
class PasswordPolicy:
    """Based on Martijn Pieters' solution: https://github.com/mjpieters/adventofcode."""

    min_: int
    max_: int
    letter: str
    password: str

    # Forward references: https://www.python.org/dev/peps/pep-0484/#forward-references
    # More info: https://stackoverflow.com/a/33533514
    @classmethod
    def get_policy(cls, policy: str) -> "PasswordPolicy":
        match = TEMPLATE.search(policy)
        if match:
            return cls(
                int(match["min_"]),
                int(match["max_"]),
                match["letter"],
                match["password"],
            )
        else:
            raise ValueError("The policy does not follow the template.")

    def is_valid_count(self) -> bool:
        return self.min_ <= self.password.count(self.letter) <= self.max_

    def is_valid_position(self) -> bool:
        return (self.password[self.min_ - 1], self.password[self.max_ - 1]).count(
            self.letter
        ) == 1


if __name__ == "__main__":
    with open("input.txt", "r") as reader:
        inp = reader.read().splitlines()

    policies = [PasswordPolicy.get_policy(policy) for policy in inp]

    n_valid_count_policies = sum(policy.is_valid_count() for policy in policies)
    n_valid_position_policies = sum(policy.is_valid_position() for policy in policies)

    print("Number of valid count-based policies:", n_valid_count_policies)
    print("Number of valid position-based policies:", n_valid_position_policies)
