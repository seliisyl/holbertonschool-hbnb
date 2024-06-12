from datetime import datetime
import uuid

class Place:
    def __init__(self, name, location, host):
        self.id = str(uuid.uuid4())
        self.name = name
        self.location = location
        self.host = host  # Should be an instance of User
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.amenities = []
        self.reviews = []

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)
            return True
        return False

    def add_review(self, review):
        self.reviews.append(review)

    def __str__(self):
        return f'Place({self.id}, {self.name}, {self.location}, {self.host})'
    
    def __init__(self, name, location, host):
        if not isinstance(host, User):
            raise ValueError("Host must be a User")
        self.host = host
