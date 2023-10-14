from src.models.User.User import User

def update_user(db, updating_fields: dict, user_id: str) -> bool:
    old_user = db.collection(u'users').document(f'{user_id.id}').get()
    if not old_user.exists:
        return False
    else:
        db.collection(u'users').document(f'{user_id}').update(updating_fields)
        return True