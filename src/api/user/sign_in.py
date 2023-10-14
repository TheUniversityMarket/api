from vgem import EM

from src.models.User.User import User

def sign_in_by_id(db, user_id, password) -> dict:
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
    
def sign_in_by_username(db, username, password):
    id = db.collection(u'users').where(u'username', u'==', username).get()
    if len(id) == 0:
        return {'success':False,'error': "User does not exist"}
    else:
        return sign_in_by_id(db, id[0].id, password)
