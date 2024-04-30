#!/usr/bin/env python3
"""A script to get the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """A script to get the list of school having a specific topic"""

    docs =  mongo_collection.find({"topics":topic})
    return [ d for d in docs]
