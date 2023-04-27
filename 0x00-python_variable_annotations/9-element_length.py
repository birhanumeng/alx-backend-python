#!/usr/bin/env python3
"""Implenting duck type on iterable."""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """By taking iterable string list as an arguments, it returns \
    a  list of tuple with a tuple elements of the iterable string \
    and its length."""
    return [(i, len(i)) for i in lst]
