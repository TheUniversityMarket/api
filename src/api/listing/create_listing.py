from src.models.Listing.Listing import Listing

from src.firebase.listing.create import create_listing

def create_listing(db, product_name, photo, description, user_id, categories, state, measurement, hashtags, date, price) -> dict:
    try:
        # create listing object
        listing = Listing(product_name, photo, description, user_id, categories, state, measurement, hashtags, date, price)
    
        # checks - add more later!

        # firebase 
        create_listing(db, listing)

    except Exception as e:
        return {'success':False,'error': str(e)}
    
    return {'success':True,'error': None}