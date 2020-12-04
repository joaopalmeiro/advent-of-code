import re
from dataclasses import dataclass
from typing import Pattern


@dataclass
class PasswordPolicy:
    """Based on Martijn Pieters' solution: https://github.com/mjpieters/adventofcode."""

    min_: int
    max_: int
    letter: str
    password: str
    template: Pattern = re.compile(
        r"^(?P<min_>\d+)-(?P<max_>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)$"
    )

    # Forward references: https://www.python.org/dev/peps/pep-0484/#forward-references
    # https://stackoverflow.com/a/33533514
    @classmethod
    def get_policy(cls, policy: str) -> "PasswordPolicy":
        pass
