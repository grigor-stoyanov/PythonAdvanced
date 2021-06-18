# type hinting highlights types used in functions if you call them with wrong type
# useful for tracking variables across files and long projects
from typing import Dict, Tuple


def print_tuple(my_tuple) -> Tuple[int, int]:
    return my_tuple


def sum_nums(a: int, b: int) -> int:
    return a + b


sum_nums(1.4, 5.5)
print_tuple((1.4, 5.6, 5.1))
