#!/usr/bin/env python3
"""
summation of lists
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): The list of floating-point numbers to sum.

    Returns:
        float: The sum of the list of floats.
    """
    return sum(input_list)
