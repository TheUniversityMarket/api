from src.models.Listing.Listing import Listing

def delete_listing(db, listing_id) -> bool:
    listing = db.collection(u'listings').document(f'{listing_id}').get()
    if listing.exists:
        db.collection(u'listings').document(f'{listing_id}').delete()
        return True
    else:
        return False