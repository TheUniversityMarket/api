from src.models.Listing.Listing import Listing

from src.firebase.listing.create import create_listing

def create_listing(db, listing_dict) -> dict:
    try:
        # create listing object
        listing = Listing.readFromDict(listing_dict)
    
        # checks - add more later!

        # firebase 
        create_listing(db, listing)

    except Exception as e:
        return {'success':False,'error': str(e)}
    
    return {'success':True,'error': None}