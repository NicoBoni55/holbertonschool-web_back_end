#!/usr/bin/env python3
"""
function that returns a function that multiplies a float by a multiplier
"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    return a function that multiplies a float by a multiplier

    parameters:
    multiplier (float)

    return: Callable[[float], float]
    """
    def mul(n: float) -> float:
        """
        return the multiplication of n * multiplier

        parameters:
        n (float)

        return: float
        """
        return n * multiplier
    return mul
