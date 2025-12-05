#!/usr/bin/env python3

"""
Write a Python function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    return the list of school with a specific topic
    """
    cursor = mongo_collection.find({"topics": topic})

    result = []
    for value in cursor:
        result.append(value)

    return result
