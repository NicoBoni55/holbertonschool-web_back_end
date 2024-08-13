#!/usr/bin/env python3
"""
function that return the length of an element
"""

import typing


def element_length(
    lst: typing.Iterable[typing.Sequence]
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    return the length of an element

    parameters:
    lst (Iterable[Sequence])

    return: List[Tuple[Sequence, int]]
    """
    return [(i, len(i)) for i in lst]

print(element_length.__annotations__)