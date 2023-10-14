import json
from uuid import uuid4

class User:
    def __init__(self,username,password,email,verified,name,number,address,listings,language) -> None:
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

    # overload constructor to take in a firebase dictionary
    def __init__ (self, user_dict) -> None:
        self.id = user_dict["id"]
        self.username = user_dict["username"]
        self.password = user_dict["password"]
        self.email = user_dict["email"]
        self.verified = user_dict["verified"]
        self.name = user_dict["name"]
        self.number = user_dict["number"]
        self.address = user_dict["address"]
        self.listings = user_dict["listings"]
        self.language = user_dict["language"]
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "verified": self.verified,
            "name": self.name,
            "number": self.number,
            "address": self.address,
            "listings": self.listings,
            "language": self.language
        }

    


# new_user = User(username="john_doe", password="password123", email="john@example.com", 
#                 verified=True, name="John Doe", number="1234567890", 
#                 address="123 Main St", listings=[], language="English")
