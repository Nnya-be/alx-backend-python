#!/usr/bin/env python3
"""
Module to measure the runtime of wait_n.
"""

import asyncio
import time
from concurrent_coroutines import wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per task.
    
    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.
    
    Returns:
        float: Average execution time per task.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
