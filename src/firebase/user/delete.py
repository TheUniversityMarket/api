from src.models.User.User import User

def delete_user(db, user_id) -> bool:
    user = db.collection(u'users').document(f'{user_id}').get()
    if user.exists:
        db.collection(u'users').document(f'{user_id}').delete()
        return True
    else:
        return False