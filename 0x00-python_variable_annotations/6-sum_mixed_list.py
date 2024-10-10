#!/usr/bin/env python3
"""
summation of lists (mixed)
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats as a float.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers
        and floating-point numbers to sum.

    Returns:
        float: The sum of the list as a float.
    """
    return sum(mxd_lst)
