#!/usr/bin/env python3
"""
Module: web.py

This module will implement an expiring web cache and tracker
"""


import requests
import redis
import time
from typing import Callable


redis_client = redis.Redis()


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

    try:
        response = requests.get(url)
        page_content = response.text
    except Exception as e:
        print(f"Failed to get URL: {url}. Error: {e}")
        return ""

    response.close()

    redis_client.setex(count_key, 10, access_count)

    return page_content


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    
    time.sleep(10)
    
    print(get_page(url))
