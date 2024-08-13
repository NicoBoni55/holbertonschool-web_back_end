#!/usr/bin/env python3
"""
function that return the sum of a float and an integer
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    return the sum of the list of floats

    Parameters:
    mxd_list (List[Union[int, float]])

    return: sum of the list of floats
    """
    return float(sum(mxd_lst))
