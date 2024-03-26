#!/usr/bin/env python3
"""
Module: 10-update_topics.py

This module contains a function that changes all topics
of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    This function changes all topics of a school
    document based on the name

    mongo_collection: pymongo collection object
    name(string): school name to update
    topics(list of strings(: list of topics approached in the school
    """
    result = mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
    return result.modified_count
