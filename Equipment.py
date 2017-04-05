#/usr/bin/python3

"""
Equipment class file
"""

class Equipment(object):
    """
    Equipments are the objects available in an installation and usefull to an activity.
    An Equipment is defined by an id (who is the primary key in the DataBase) a name,
    an installation and a list of activities
    """
    def __init__(self, id, name, installation_id):
        self.id = id
        self.name = name
        self.installation_id = installation_id

    def __str__(self) :
        return "name"