from vgem import EM

from src.models.User.User import User
from src.firebase.user.create import create_user

def sign_up(db, user_dict) -> dict:
    try:
        # hash password
        em = EM()
        hash_and_salt = em.hash(user_dict['password'], True)
        user_dict['password'] = hash_and_salt['hash']
        user_dict['salt'] = hash_and_salt['salt']

        # create user object
        user = User.readFromDict(user_dict)
    
        # checks - add more later!

        # use python library
        if "@" not in user.email: 
         return {'success':False,'error': "Invalid email"}
    
        # firebase 
        create_user(db, user)

    except Exception as e:
        return {'success':False,'error': str(e)}
    
    return {'success':True,'error': None}
