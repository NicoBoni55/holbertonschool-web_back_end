#!/usr/bin/env python3
"""
function that generates random numbers
"""

import random
import typing


async def async_generator() -> typing.AsyncGenerator[float, None]:
    """
    generate random numbers between 0 and 10
    """
    for element in range(10):
        yield random.uniform(0, 10)
