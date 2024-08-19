#!/usr/bin/env python3
"""
function that return list of random numbers
"""

import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    return list of random numbers between 0 and 10
    """
    new_list = [num async for num in async_generator()]
    return new_list
