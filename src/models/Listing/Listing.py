from uuid import uuid4

class Listing:
    def __init__(self, product_name, photo, description, user_id, number, address, email, categories, state, measurement, hashtags, date, price, id=None):
        if id is None:
            self.id = str(uuid4())
        else:
            self.id = id
        self.product_name = product_name
        self.photo = photo
        self.description = description
        self.user_id = user_id
        self.categories = categories
        self.state = state
        self.measurement = measurement
        self.hashtags = hashtags
        self.date = date
        self.price = price
        self.number = number
        self.address = address
        self.email = email

    # overload constructor to take in a firebase dictionary
    @staticmethod
    def readFromDict(listing_dict):
        return Listing(id=listing_dict["id"], product_name=listing_dict["product_name"], photo=listing_dict["photo"], description=listing_dict["description"], user_id=listing_dict["user_id"], categories=listing_dict["categories"], state=listing_dict["state"], measurement=listing_dict["measurement"], hashtags=listing_dict["hashtags"], date=listing_dict["date"], price=listing_dict["price"], number=listing_dict["number"], address=listing_dict["address"], email=listing_dict["email"])

    def serialize(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "photo": self.photo,
            "description": self.description,
            "user_id": self.user_id,
            "categories": self.categories,
            "state": self.state,
            "measurement": self.measurement,
            "hashtags": self.hashtags,
            "date": self.date,
            "price": self.price,
            "number": self.number,
            "address": self.address,
            "email": self.email
        }



    