from src.models.Listing.Listing import Listing

from firebase_admin.firestore import FieldFilter

def get_listing_by_id(db, listing_id) -> Listing or None:
    listing = db.collection(u'listings').document(f'{listing_id}').get()
    if listing.exists:
        return Listing.readFromDict(listing.to_dict())
    else:
        return None
    
def get_listings_by_user_id(db, user_id) -> list:
    listings = db.collection(u'listings').where(filter=FieldFilter("user_id", "==", user_id)).get()
    return [Listing.readFromDict(listing.to_dict()) for listing in listings]
    
def get_all_listings(db) -> list:
    listings = db.collection(u'listings').get()
    return [Listing.readFromDict(listing.to_dict()) for listing in listings]

def get_listings_by_categories(db, categories) -> list:
    listings = []
    for category in categories:
        listings += db.collection(u'listings').where(filter=FieldFilter("categories", "array_contains", category)).get()
    return [Listing.readFromDict(listing.to_dict()) for listing in listings]

def get_listings_by_search(db, search_term) -> list:
    listings = db.collection(u'listings').get()
    listings = [Listing.readFromDict(listing.to_dict()) for listing in listings]
    listings = [listing for listing in listings if (search_term.lower() in listing.product_name.lower() or search_term.lower() in listing.description.lower())]
    return listings