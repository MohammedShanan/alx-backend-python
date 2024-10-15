#!/usr/bin/env python3
"""
This module contains the definition of `async_generator`, a coroutine
that generates 10 random numbers asynchronously.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that yields 10 random numbers asynchronously.

    Returns:
        Generator[float, None, None]: An asynchronous generator of
        random float numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
