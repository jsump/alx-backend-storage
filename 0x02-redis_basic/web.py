#!/usr/bin/env python3
"""
Module: web.py

This module wikk implement an expiring web cache and tracker
"""


import requests
import redis
import time
from typing import Callable


redis_clent = redis.Redis()


def get_page(url: str) -> str:
    """
    This function checks if the url has been accessed nefore
    """
    count_key = f"count:{url}"
    access_count = redis_client.get(count_key)

    if access_count is None:
        access_count = 1
    else:
        access_count = int(access_count) + 1

    page_content = requests.get(url).text
    redis_client.setex(count_key, 10, access_count)

    return page_content


url = "http://slowwly.robertomurray.co.uk"
print(get_page(url))

time.sleep(10)

print(get_page(url))
