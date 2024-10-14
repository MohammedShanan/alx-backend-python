#!/usr/bin/env python3
"""
This module provides an asynchronous function to
spawn multiple task_wait_random coroutines.
"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns a list of all the delays.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay for each task_wait_random.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    routine = [task_wait_random(max_delay) for i in range(n)]
    wait_times = await asyncio.gather(*routine)
    return sorted(wait_times)
