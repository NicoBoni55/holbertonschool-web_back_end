#!/usr/bin/env python3
"""
function that return float
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure the runtime of wait_n
    """
    initial_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    final_time = time.time()
    total_time = final_time - initial_time
    return total_time / n
