#!/usr/bin/env python3
"""
Module: 12-log_stats.py

This module contains a fucntion that provides some stats about Ngix
stored in MongoDB
"""


from pymongo import MongoClient


def display_nginx_stats():
    """
    This function provides stats on Ngix logs stores
    in MongoDB

    Database: logs
    Collection: nginx
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    database = client.logs
    collection = database.nginx

    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")
    print(f"Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    status_count = collection.count_documents(
            {"method": "GET", "path": "/status"}
            )
    print(f"{status_count} status check")


if __name__ == "__main__":
    display_nginx_stats()
