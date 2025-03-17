#!/usr/bin/env python3
"""
Create a chache class
"""

import redis
from typing import Union
import uuid


class Cache():
    """
    class Cache
    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method
        """
        ukey = str(uuid.uuid4())
        self._redis.set(ukey, data)
        return ukey
