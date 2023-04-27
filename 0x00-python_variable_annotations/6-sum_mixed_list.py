#!/usr/bin/env python3
"""A module to sum a list of mixed type (integer and float) numbers."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum list of mixed type (integer and float) numbers \
    and return the result as a float number
    """
    sum = 0
    for num in input_list:
        sum += num

    return sum
