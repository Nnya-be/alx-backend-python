#!/usr/bin/env python3
"""
Module to measure the runtime of wait_n.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

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
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
