#!/usr/bin/env python3
"""
Return the sum of a list containing ints and floats as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed function
    """
    return sum(mxd_lst)
