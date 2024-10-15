#!/usr/bin/env python3
"""
This module contains the definition of `async_comprehension`,
a coroutine that collects random numbers using
asynchronous comprehension over `async_generator`.
"""
from typing import List
from importlib import import_module as using

async_generator = using("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using asynchronous comprehension.

    Returns:
        List[float]: A list of 10 random float numbers
        collected from `async_generator`.
    """
    return [num async for num in async_generator()]
