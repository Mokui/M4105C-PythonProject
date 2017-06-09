"""
The Installation class file
"""
class Installation(object):
    """
    Docstring for Installation class:
    This Installation class consider a sports hall
    """
    def __init__(self, id, name, address, postal_code, city, latitude, longitude):
        self.id = id
        self.name = name
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return self.name
