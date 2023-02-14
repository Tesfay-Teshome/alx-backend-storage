#!/usr/bin/env python3

""" List all documents in a collection """
def list_all(mongo_collection):
    return [list_doc for list_doc in mongo_collection.find()]
