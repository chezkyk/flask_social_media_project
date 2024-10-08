class Geo:
    def __init__(self, lat: str, lng: str):
        self.lat = lat
        self.lng = lng

    def to_dict(self):
        return {
            'lat': self.lat,
            'lng': self.lng
        }