#!/usr/bin/env python3
"""
This module contains the definition of `measure_runtime`,
a coroutine that measures the time taken to execute
`async_comprehension` four times in parallel.
"""
import asyncio
import time
from importlib import import_module as using

async_comprehension = using("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the runtime of executing
    `async_comprehension` four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
