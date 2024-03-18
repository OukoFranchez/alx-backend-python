#!/usr/bin/env python3
""" Task 2 Module """


import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This module contains a function called `measure_time` that measures
the average time it takes to execute the `wait_n` function multiple times.

Example Usage:
    average_time = measure_time(5, 10)
    print(average_time)

In this example, the `measure_time` function is
called with `n=5` and `max_delay=10`.
It measures the average time it takes to execute the `wait_n`
function 5 times with a maximum delay of 10.

Inputs:
    n (int): The number of times to execute the `wait_n` function.
    max_delay (int): The maximum delay for
    each execution of the `wait_n` function.

Returns:
    float: The average time it takes to execute
    the `wait_n` function multiple times.
    """
    start_time = time.time()
    wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
