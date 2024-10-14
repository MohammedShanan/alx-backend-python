#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive) seconds
    and returns the delay.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay time in seconds.
    """
    random_num = random.uniform(1, max_delay)
    await asyncio.sleep(random_num)
    return random_num
