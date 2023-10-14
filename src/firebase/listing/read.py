from src.models.User import User

def get_user(db, user_id) -> User or None:
    user = db.collection(u'users').document(f'{user_id}').get()
    if user.exists:
        return User(user.to_dict())
    else:
        return None