from uuid import uuid4

class Listing:
    def __init__(self, product_name, photo, description, userid, category, state, measurement, hashtags, date):
        self.id = str(uuid4())
        self.product_name = product_name
        self.photo = photo
        self.description = description
        self.userid = userid
        self.category = category
        self.state = state
        self.measurement = measurement
        self.hashtags = hashtags
        self.date = date

    # overload constructor to take in a firebase dictionary
    def __init__(self, listing_dict) -> None:
        self.id = listing_dict["id"]
        self.product_name = listing_dict["product_name"]
        self.photo = listing_dict["photo"]
        self.description = listing_dict["description"]
        self.userid = listing_dict["userid"]
        self.category = listing_dict["category"]
        self.state = listing_dict["state"]
        self.measurement = listing_dict["measurement"]
        self.hashtags = listing_dict["hashtags"]
        self.date = listing_dict["date"]

    def serialize(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "photo": self.photo,
            "description": self.description,
            "userid": self.userid,
            "category": self.category,
            "state": self.state,
            "measurement": self.measurement,
            "hashtags": self.hashtags,
            "date": self.date
        }



    