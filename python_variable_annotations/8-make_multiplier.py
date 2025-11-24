#!/usr/bin/env python3
"""
Return a function that multiplies a float by the givien multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier function
    """
    def multiply(n: float) -> float:
        return (n * multiplier)

    return multiply
