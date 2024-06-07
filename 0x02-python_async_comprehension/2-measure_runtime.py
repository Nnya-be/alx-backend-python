#!/usr/bin/env python3
"""Task 2's module.
"""
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes 4 times and measures the total execution time.

    This  will run four times concurrently and measure the total time

    Returns:
        float: The total time  for  four executions/seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
