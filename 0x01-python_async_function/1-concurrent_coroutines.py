#!/usr/bin/env python3
""" Task 1 Module """

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for a random amount of time and returns a sorted list of delays.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of delays (float values) sorted in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    delays = sorted(delays)

    return delays
