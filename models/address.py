from models.geo import Geo

class Address:
    def __init__(self, street: str, suite: str, city: str, zipcode: str, geo: Geo):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo = geo
    def to_dict(self):
        return {
            'street': self.street,
            'suite': self.suite,
            'city': self.city,
            'zipcode': self.zipcode,
            'geo': self.geo.to_dict()
        }