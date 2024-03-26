#!/usr/bin/env python3
"""
Module: 101-students.py

This module contains a python function that returns all
students sorted by average score
"""


def top_students(mongo_collection):
    """
    This function returns all students sorted by average score

    mongo_collection: pymongo collection object

    The top mustbe ordered
    The average score must be part of each item returns
    with key = averageScore
    """
    pipeline = [
            {
                "$addFields": {
                    "averageScore": {"$avg": "$scores"}
                }
            },
            {
                "$sort": {"averageScore": -1}
            }
    ]
    sorted_students = list(mongo_collection.aggregate(pipeline))
    return sorted_students
