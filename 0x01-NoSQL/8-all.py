#!/usr/bin/env python3
""" List all documents in Python """


def list_all(mongo_collection):
    docs = mongo_collection.find()

    if docs.count() == 0:
        return []

    return docs
