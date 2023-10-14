import json
from uuid import uuid4

class User:
    def __init__(self,username,password,email,verified,name,number,address,listings,language, salt = None) -> None:
        self.id = str(uuid4())
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
        return User(user_dict["username"], user_dict["password"], user_dict["email"], user_dict["verified"], user_dict["name"], user_dict["number"], user_dict["address"], user_dict["listings"], user_dict["language"], user_dict["salt"])
    
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
