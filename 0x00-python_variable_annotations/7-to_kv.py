#!/usr/bin/env python3
"""
Converts a key and its value to a tuple
of the key and the square of its value
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of an integer or float.

    Args:
        k (str): The string value.
        v (Union[int, float]): The integer or floating-point number to square.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string
        and the second element is the square of the number as a float.
    """
    return (k, float(v**2))
