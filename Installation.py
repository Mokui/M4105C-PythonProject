"""
The Installation class file
"""
class Installation(object):
    """
    Docstring for Installation class:
    This Installation class consider a sports hall
    """ 
    def __init__(self, id, name, adress, postal_code, city, latitude, longitude):
        self.id = id
        self.name = name
        self.adress = adress
        self.postal_code = postal_code
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
    
    def __str__(self) :
        return "name"