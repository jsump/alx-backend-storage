#!/usr/bin/env python3
"""
Module: 11-schools_by_topic.py

This module contains a function that retuns the list
of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    This function returns the list of school having
    a specific topic.

    mongo_collection: pymongo collection object
    topic(string): topic searched
    """
    matching_schools = list(mongo_collection.find({"topics": topic}))
    return matching_schools
