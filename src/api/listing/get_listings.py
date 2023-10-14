from src.models.Listing.Listing import Listing

from firebase_admin.firestore import FieldFilter

def get_listings(db, categories) -> list:
    listings = []
    for category in categories:
        listings += db.collection(u'listings').where(filter=FieldFilter("categories", "array_contains", category)).get()
    return [Listing.readfromDict(listing.to_dict()) for listing in listings]