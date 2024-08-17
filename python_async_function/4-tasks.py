#!/usr/bin/env python3
"""
function that new function task_wait_n
"""

import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    return list of random delays with task_wait_random

    parameters:
        n: int
        max_delay: int

    returns:
        typing.List[float]
    """
    new_list = []

    for i in range(n):
        delay = await task_wait_random(max_delay)
        for j in range(len(new_list)):
            if delay < new_list[j]:
                new_list.insert(j, delay)
                break
        else:
            new_list.append(delay)
    return new_list
