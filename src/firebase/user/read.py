from src.models.Listing.Listing import Listing

def get_listing(db, listing_id) -> Listing or None:
    listing = db.collection(u'listings').document(f'{listing_id}').get()
    if listing.exists:
        return Listing(listing.to_dict())
    else:
        return None