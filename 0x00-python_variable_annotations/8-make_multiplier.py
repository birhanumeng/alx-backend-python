#!/usr/bin/env python3
"""This module implement Callable to return a function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function take a float argument and returns a function. \
    And the returned function is returns a float number which is product of its \
    float argument and the 'multiplier' float.
    """
    def func(num: float) -> float:
        return num * multiplier
    
    return func
