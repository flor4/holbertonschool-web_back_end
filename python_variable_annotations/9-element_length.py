#!/usr/bin/env python3

"""
typing the following function:
    def element_length(lst):
    return [(i, len(i)) for i in lst]
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length function
    """
    return [(i, len(i)) for i in lst]
