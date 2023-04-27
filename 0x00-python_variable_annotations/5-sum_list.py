#!/usr/bin/env python3
"""A module to sum a list of float numbers."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum list of float numbers and return the result"""
    sum = 0
    for fl in input_list:
        sum += fl

    return sum
