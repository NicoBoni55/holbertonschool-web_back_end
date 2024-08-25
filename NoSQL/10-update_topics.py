#!/usr/bin/env python3
"""
    changes all topics of a school document based on the name
"""
import typing


def update_topics(mongo_collection: object, name: str, topics: list[str]):
    """
    changes all topics of a school document based on the name
    """
    update = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return update.modified_count
