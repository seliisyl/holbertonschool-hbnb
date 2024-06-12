from datetime import datetime
import uuid

class User:
    def __init__(self, email, name):
        self.id = str(uuid.uuid4())
        self.email = email
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f'User({self.id}, {self.email}, {self.name})'
    
    _user_emails = set()    

    def __init__(self, email, name):
        if email in User._user_emails:
            raise ValueError("Email already exists")
        User._user_emails.add(email)
