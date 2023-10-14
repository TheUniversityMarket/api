import json
from uuid import uuid4

class User:
    def __init__(self,username,password,email,verified,name,number,address,listings,language, id = None, salt = None) -> None:
        if id is None:
            self.id = str(uuid4())
        else:
            self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.verified = verified
        self.name = name
        self.number = number
        self.address = address
        self.listings = listings
        self.language = language
        self.salt = salt

    # overload constructor to take in a firebase dictionary
    @staticmethod
    def readFromDict(user_dict) -> None:
        return User(id=user_dict["id"], username=user_dict["username"], password=user_dict["password"], email=user_dict["email"], verified=user_dict["verified"], name=user_dict["name"], number=user_dict["number"], address=user_dict["address"], listings=user_dict["listings"], language=user_dict["language"], salt=user_dict["salt"])
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "verified": self.verified,
            "name": self.name,
            "number": self.number,
            "address": self.address,
            "listings": self.listings,
            "language": self.language,
            "salt": self.salt
        }

    


# new_user = User(username="john_doe", password="password123", email="john@example.com", 
#                 verified=True, name="John Doe", number="1234567890", 
#                 address="123 Main St", listings=[], language="English")
