#!/usr/bin/env python3
"""Implemnteing duck type."""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Takes a list of any type and return the first element if the list \
    has a non None value and otherwise it returns None."""
    if lst:
        return lst[0]
    else:
        return None
