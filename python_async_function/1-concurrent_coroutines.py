#!/usr/bin/env python3
"""
function that return list of random delays
"""

import asyncio
import random
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    return list of random delays

    parameters:
        n: int
        max_delay: int

    returns:
        typing.List[float]
    """
    new_list = []

    for i in range(n):
        delay = await wait_random(max_delay)
        for j in range(len(new_list)):
            if delay < new_list[j]:
                new_list.insert(j, delay)
                break
        else:
            new_list.append(delay)
    return new_list
