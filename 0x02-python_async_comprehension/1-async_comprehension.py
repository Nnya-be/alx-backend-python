#!/usr/bin/env python3
"""Task 1's module."""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Creates a list of 10 numbers from a 10-number generator.

    This coroutine will collect 10 random numbers asynchronously generated
    by async_generator and return them as a list.

    Returns:
        List[float]: A list of 10 random float numbers between 0 and 10.
    """
    return [num async for num in async_generator()]
