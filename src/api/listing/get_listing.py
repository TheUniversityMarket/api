from src.models.Listing.Listing import Listing

from firebase_admin.firestore import FieldFilter

def get_listing_by_id(db, listing_id) -> Listing or None:
    listing = db.collection(u'listings').document(f'{listing_id}').get()
    if listing.exists:
        return Listing.readfromDict(listing.to_dict())
    else:
        return None
    
def get_all_listings(db) -> list:
    listings = db.collection(u'listings').get()
    return [Listing.readfromDict(listing.to_dict()) for listing in listings]

def get_listings_by_categories(db, categories) -> list:
    listings = []
    for category in categories:
        listings += db.collection(u'listings').where(filter=FieldFilter("categories", "array_contains", category)).get()
    return [Listing.readfromDict(listing.to_dict()) for listing in listings]