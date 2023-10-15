from src.models.Listing.Listing import Listing

from src.api.listing.create_listing import post_listing
from src.api.listing.get_listing import *

def test_create_listing(db):
    return post_listing(db, product_name="test", photo=['1'], description="test", user_id="string", categories=['test'], state="test", measurement="test", hashtags=['test'], date="test", price=5.0)
