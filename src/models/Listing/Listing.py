class Listing:
    def __init__(self, product_name, photo, description, userid, category, state, measurement, hashtags, date):
        self.product_name = product_name
        self.photo = photo
        self.description = description
        self.userid = userid
        self.category = category
        self.state = state
        self.measurement = measurement
        self.hashtags = hashtags
        self.date = date

    def serialize(self):
        return {
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



    