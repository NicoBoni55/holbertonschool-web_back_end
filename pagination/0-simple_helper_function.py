#!/usr/bin/env python3
"""
function that return a tuple with the index
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    return a tuple with two index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
