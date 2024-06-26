#!/usr/bin/env python3
"""Task 3's module.

This module contains the function `task_wait_random` which creates
an asynchronous task for the `wait_random` function.
"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asynchronous task for wait_random.

    Args:
        max_delay (int): The maximum delay for the wait_random function.

    Returns:
        asyncio.Task: An asynchronous task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
