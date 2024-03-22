#!/usr/bin/env python3

""" Task 0 Module """


import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    A coroutine that generates a sequence of 10 numbers
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
