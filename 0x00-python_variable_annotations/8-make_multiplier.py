#!/usr/bin/env python3
"""
Creates a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns its product with the multiplier.
    """

    def multiply_by_multiplier(x: float) -> float:
        return x * multiplier

    return multiply_by_multiplier
