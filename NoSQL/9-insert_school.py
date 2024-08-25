#!/usr/bin/env python3
"""
inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection: object, **kwargs) -> str:
    """
    insert a new document in a collection based on kwargs
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
