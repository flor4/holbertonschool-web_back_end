#!/usr/bin/env python3

"""typing the following function:
    def element_length(lst):
    return [(i, len(i)) for i in lst]"""

from typing import Iterable, Sequence, List, Tuple
# Importing types from the typing module for type annotations:
# - Iterable: represents any object that can be iterated over (like list, tuple, set)
# - Sequence: represents ordered collections with a defined length (like list, tuple, string)
# - List: a concrete list type, where we can specify the type of its elements
# - Tuple: a fixed-size collection of elements, where we can specify the type of each element
# These imports help us clearly annotate function parameters and return values,
# improving code readability and allowing static type checkers like mypy to verify types.


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
