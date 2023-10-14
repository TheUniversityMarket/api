from uuid import uuid4

class Listing:
    def __init__(self, product_name, photo, description, user_id, categories, state, measurement, hashtags, date, price, id=None):
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

    # overload constructor to take in a firebase dictionary
    @staticmethod
    def readFromDict(listing_dict):
        return Listing(listing_dict["id"], listing_dict["product_name"], listing_dict["photo"], listing_dict["description"], listing_dict["user_id"], listing_dict["categories"], listing_dict["state"], listing_dict["measurement"], listing_dict["hashtags"], listing_dict["date"], listing_dict["price"])

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
            "price": self.price
        }



    