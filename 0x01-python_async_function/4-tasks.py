#!/usr/bin/env python3
"""Task 4's module."""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times.

    Args:
        n (int): The number of times to execute task_wait_random.
        max_delay (int): The maximum delay for task_wait_random.

    Returns:
        List[float]: A list of wait times in ascending order.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
