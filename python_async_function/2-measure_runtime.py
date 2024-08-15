#!/usr/bin/env python3

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    total_time = time.time()
    return total_time / n
