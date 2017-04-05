#!/usr/bin/python3

"""
Activity class file
"""

class Activity(object):
    """
    An activity is a Sport that is practiced. 
    It's defined by a id (who will be the primary key in the database) and a name
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self) :
        return "name"