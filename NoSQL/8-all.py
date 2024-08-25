#!/usr/bin/env python3
"""
lists all documents in a collection
"""

def list_all(mongo_collection: object) -> list:
    """
    lists all documents in a collection
    """
    if mongo_collection.find() is None:
        return []
    else:
        return mongo_collection.find()


    