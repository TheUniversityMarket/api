from vgem import EM

from src.models.User.User import User

def sign_in(db, user_id, password) -> dict:
    try:
        # check if user exists
        if db.collection(u'users').document(f'{user_id}').get().exists:
            # get user
            user = User.readFromDict(db.collection(u'users').document(f'{user_id}').get().to_dict())
            
            # check hash
            em = EM()
            try:
                if em.check_hash(password, user.password, user.salt, True) is None:
                    return {'success':True, 'error':None, "user": user.serialize()}
            except:
                return {'success':False,'error': "Incorrect password"}
        else:
            return {'success':False,'error': "User does not exist"}

    except Exception as e:
        return {'success':False,'error': str(e)}
