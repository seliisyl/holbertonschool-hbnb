from datetime import datetime
import uuid

class Country:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.cities = []

    def add_city(self, city):
        if city not in self.cities:
            self.cities.append(city)

    def __str__(self):
        return f'Country({self.id}, {self.name})'
