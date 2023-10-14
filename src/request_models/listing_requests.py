from pydantic import BaseModel

class CreateListingRequest(BaseModel):
    product_name: str
    photo: str
    description: str
    user_id: str
    categories: list
    state: str
    measurement: str
    hashtags: list
    date: str
    price: float
