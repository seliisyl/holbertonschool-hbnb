from .i_persistence_manager.py import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {}

    def save(self, entity):
        self.storage[entity.id] = entity

    def get(self, entity_id, entity_type):
        return self.storage.get(entity_id)

    def update(self, entity):
        self.storage[entity.id] = entity

    def delete(self, entity_id, entity_type):
        if entity_id in self.storage:
            del self.storage[entity_id]
