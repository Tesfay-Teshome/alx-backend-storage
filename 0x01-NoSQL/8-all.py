#!/usr/bin/env python3
""" List all documents in a collection """


def list_all(mongo_collection):
    list_docs = mongo_collection.find()

    if list_docs.count() == 0:
        return []

    return list_docs
