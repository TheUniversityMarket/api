from src.models.User.User import User

def get_user(db, user_id) -> User or None:
    user = db.collection(u'users').document(f'{user_id}').get()
    if user.exists:
        return User.readFromDict(user.to_dict())
    else:
        return None