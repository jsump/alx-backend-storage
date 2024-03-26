#!/usr/bin/env python3
"""
Module: 9-insert_school.py

This module contains a function that inserts a new document
in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    This function insers a new document in a collection
    based on kwargs.

    mongo_collection will be pymongo collection object

    Returns the new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
