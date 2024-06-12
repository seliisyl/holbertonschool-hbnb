from datetime import datetime
import uuid

class Review:
    def __init__(self, content, user, place):
        self.id = str(uuid.uuid4())
        self.content = content
        self.user = user  # Should be an instance of User
        self.place = place  # Should be an instance of Place
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f'Review({self.id}, {self.content}, {self.user}, {self.place})'
