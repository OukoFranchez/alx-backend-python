#!/usr/bin/env python3
""" Task 4 Module """

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Similar to the wait_n coroutine but uses the task
        returned by task_wait_random to return the list
        of awaited times
    """
    delays = []
    for _ in range(n):
        delays.append(await task_wait_random(max_delay))
    return sorted(delays)
