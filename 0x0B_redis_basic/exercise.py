#!/usr/bin/env python3
"""
Create a chache class
"""

import redis
from typing import Callable, Union
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    counts calls
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper
        """
        self._redis.incr(key)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    call history
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper
        """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper


class Cache():
    """
    class Cache
    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method
        """
        ukey = str(uuid.uuid4())
        self._redis.set(ukey, data)
        return ukey

    def get(self, key: str, fn=None) -> str:
        """
        get value
        """

        value = self._redis.get(key)
        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str, fn=None) -> str:
        """
        get string
        """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str, fn=None) -> int:
        """
        get int
        """
        value = self._redis.get(key)
        return int(value.decode("utf-8"))
