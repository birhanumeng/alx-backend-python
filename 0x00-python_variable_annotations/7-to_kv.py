#!/usr/bin/env python3
"""A module to append a string and a square of \
of integer or float numbers.
"""

import math
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A function takes a string and integer or float numbers \
    as argument. Then it returns a tuple conaiting a string and \
    squares of each numbers.
    """
    return (k, math.square(v))
