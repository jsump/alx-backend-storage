#!/usr/bin/env python3
"""
Module: exercise.py

This module contains a class Cache.
"""


import uuid
import redis
import pickle
from typing import Union


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
