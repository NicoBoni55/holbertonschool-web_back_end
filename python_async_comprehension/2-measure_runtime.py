#!/usr/bin/env python3
"""
function that measures the runtime
"""

import asyncio
import time
import typing
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure the runtime
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()
    return end - start
