from src.models.Listing.Listing import Listing

def create_listing(db, listing: Listing) -> None:
    db.collection(u'listings').document(f'{listing.id}').set(listing.serialize())
 