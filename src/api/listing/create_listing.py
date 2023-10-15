from src.models.Listing.Listing import Listing

from src.firebase.listing.create import create_listing

def post_listing(db, product_name, photo, description, user_id, categories, state, measurement, hashtags, date, price) -> dict:
    try:
        phone = db.collection(u'users').document(f'{user_id}').get().to_dict()["phone"]
        address = db.collection(u'users').document(f'{user_id}').get().to_dict()["address"]
        email = db.collection(u'users').document(f'{user_id}').get().to_dict()["email"]
        # create listing object
        listing = Listing(product_name=product_name, photo=photo, description=description, user_id=user_id, phone=phone, address=address, email=email, categories=categories, state=state, measurement=measurement, hashtags=hashtags, date=date, price=price)
    
        # checks - add more later!

        # firebase 
        create_listing(db, listing)

    except Exception as e:
        return {'success':False,'error': str(e)}
    
    return {'success':True,'error': None}