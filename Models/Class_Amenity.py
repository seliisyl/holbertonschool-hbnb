from datetime import datetime
import uuid

class Amenity:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f'Amenity({self.id}, {self.name})'
