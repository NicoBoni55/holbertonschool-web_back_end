#!/usr/bin/env python3
"""
function that generates random numbers
"""

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    generate random numbers between 0 and 10
    """
    for element in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
