#!/usr/bin/env python3
"""
Module: exercise.py

This module contains a class Cache.
"""


import uuid
import redis
import pickle
import functools
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

    def count_calls(method: Callable) -> Callable:
        """
        This method implements a system to count how mnay times
        methods of the Cache class are called
        """
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            """ wrapper """
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    def call_history(method: Callable) -> Callable:
        """
        This method stored the history of inputs and outputs
        for a particular function
        """
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            """wrapper"""
            input_key = method.__qualname__ + ":inputs"
            output_key = method.__qualname__ + ":outputs"
            self._redis.rpush(input_key, str(args))
            result = method(self, *args, **kwargs)
            self._redis.rpush(output_key, str(result))
            return result
        return wrapper

    @count_calls
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

    def replay(self, method: Callable) -> None:
        """Replay"""
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":output"
        inputs = self._redis.lrange(input_key, 0, -1)
        outputs = self._redis.lrange(output_key, 0, -1)

        print(f"{method.__qualname__} was called {len(inputs)} times:")
        for input_args, output in zip(inputs, outputs):
            print(f"{method.__qualname__}(
            *{input_args.decode('utf-8')}
            ) -> {output.decode('utf-8')}")


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
