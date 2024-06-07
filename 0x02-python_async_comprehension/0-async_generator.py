#!/usr/bin/env python3
"""Task 0's module."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generates a sequence of 10 numbers.

    This coroutine will loop 10 times, each time asynchronously waiting
    for 1 second, then yielding a random number between 0 and 10.

    Yields:
        float: A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
