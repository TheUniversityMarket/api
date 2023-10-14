from vgem import EM

from src.models.User.User import User

def sign_in(db, user_id, password) -> dict:
    try:
        # check if user exists
        if db.collection(u'users').document(f'{user_id}').get().exists:
            # get user
            user = User(db.collection(u'users').document(f'{user_id}').get().to_dict())
            
            # check hash
            em = EM()
            password_hash = em.hash(password, True)
            if em.check_hash(user.password, password_hash, user.salt, True):
                return {'success':True, 'error':None, "user": user.to_dict()}
            else:
                return {'success':False,'error': "Incorrect password"}
        else:
            return {'success':False,'error': "User does not exist"}

    except Exception as e:
        return {'success':False,'error': str(e)}
