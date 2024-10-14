#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine to
spawn multiple wait_random coroutines.
"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns a list of all the delays.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    routine = [wait_random(max_delay) for i in range(n)]
    wait_times = await asyncio.gather(*routine)
    return sorted(wait_times)
