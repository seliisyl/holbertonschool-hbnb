from datetime import datetime
import uuid
from .country import Country

class City:
    def __init__(self, name, country):
        if not isinstance(country, Country):
            raise ValueError("The country must be an instance of Country")
        
        self.id = str(uuid.uuid4())
        self.name = name
        self.country = country
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []

    def add_place(self, place):
        if place not in self.places:
            self.places.append(place)

    def __str__():
        return f'City({self.id}, {self.name}, {self.country})'
