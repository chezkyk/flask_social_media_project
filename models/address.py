class Address:
    def __init__(self, street: str, suite: str, city: str, zipcode: str, geo: Geo):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo = geo