from src.models.User import User

def create_user(db, user: User) -> None:
    db.collection(u'users').document(f'{user.id}').set(user.serialize())
 