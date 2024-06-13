# app/models.py

from datetime import datetime

class Amenity:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def update(self, name):
        self.name = name
        self.updated_at = datetime.utcnow()

amenities = []

