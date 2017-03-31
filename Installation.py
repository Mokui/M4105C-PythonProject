"""
The Installation class file
"""
class Installation :
   """
   Docstring for Installation class:
   This Installation class consider a sports hall
   """ 
    def __init__(self, id, name, adress, postalcode, city, latitude, longitude):
        self.id = id
        self.name = name
        self.adress = adress
        self.postalcode = postalcode
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
    