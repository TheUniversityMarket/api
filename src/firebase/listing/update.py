from src.models.Listing.Listing import Listing

def update_listing(db, updating_fields: dict, listing_id: str) -> bool:
    old_listing = db.collection(u'listings').document(f'{listing_id.id}').get()
    if not old_listing.exists:
        return False
    else:
        db.collection(u'listings').document(f'{listing_id}').update(updating_fields)
        return True