#!/usr/bin/env python3
"""
function that returns the sum of a list of floats
"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
    return the sum of the list of floats

    Parameters:
    input_list (List[float])

    return: sum of the list of floats
    """
    return sum(input_list)
