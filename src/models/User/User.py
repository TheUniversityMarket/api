import json

class User:
    def __init__(self,username,password,email,verified,name,number,address,listings,language) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.verified = verified
        self.name = name
        self.number = number
        self.address = address
        self.listings = listings
        self.language = language
    
    def serialize(self):
        return {
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
