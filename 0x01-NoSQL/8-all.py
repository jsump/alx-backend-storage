#!/usr/bin/env python3
"""
Module: 8-all.py

This module contains a function that lists all documents
in a collection
"""


def list_all(mongo_collection):
    """
    This function lists all documents in a collection
    Return an empty list
    mongo_collection will be the pymongo collection object
    """
    document_list = list(mongo_collection.find({}))
    return document_list
