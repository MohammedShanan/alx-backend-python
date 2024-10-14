#!/usr/bin/env python3
"""
This module provides a function to create an asyncio Task from
an asynchronous coroutine.
"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task that wraps the wait_random coroutine with
    the specified max_delay.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: An asyncio Task wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
