#!/usr/bin/env python3
""" task 0 module """


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random delay and returns the delay.

    Args:
        max_delay (int, optional): The maximum delay (in seconds
        that the function could potentially wait. Defaults to 10.

    Returns:
        float: The actual delay the function waited for.

    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
