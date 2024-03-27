#!/usr/bin/env python3
"""
Module: exercise.py

This module contains a class Cache.
"""


import uuid
import redis
import pickle
from typing import Union, Callable


class Cache:
    """
    This class contains a method that stores an instance
    of the Redis client as a private variable(using redis.Redis())
    and flush the instane using flushdb

    _redis: private variable
    """
    def __init__(self) -> None:
        """
        This mehod stores an instance of the Redis client as
        a private variable name and flush the instance
        """
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        This method takes a data argument and returns a string.

        The methould should generate a random key(e.g using uuid).

        Store the input data in Redis using the random key
        and return key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        This method takes a key string argument and an optiional
        Callable argument named fn.
        """
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    def get_str(self, key):
        """
        This callable function decodes the value as a UTF-8 string
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key):
        """
        This function converts the value to an integer
        """
        return self.get(key, fn=int)


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
