#!/usr/bin/env python3
"""
function that waits for a random delay between 0 and 10 seconds
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and 10 seconds

    parameters:
        max_delay: int = 10

    returns:
        float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
