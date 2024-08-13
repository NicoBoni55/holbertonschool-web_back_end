#!/usr/bin/env python3
"""
function that takes a float n as argument and returns a tuple:
"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    return a tuple with the first element str and the second float

    parameters:
    k (str)
    n (Union[int, float])

    return: Tuple[str, float]
    """
    return (k, pow(v, 2))
