#!/usr/bin/env python3
"""
    return list of school having a specific topic
"""


def schools_by_topic(mongo_collection: object, topic: str) -> list:
    """
    return list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
