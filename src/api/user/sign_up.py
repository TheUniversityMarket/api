from vgem import EM

from src.models.User.User import User
from src.firebase.user.create import create_user
from src.api.user.verify import check_verification_code

def sign_up(db, username, password, email, name, number, address, language, verification_code, USERS_TO_VERIFY) -> dict:
    # check verification code
    if not check_verification_code(db, email, verification_code, USERS_TO_VERIFY):
        return {'success':False,'error': "Invalid verification code"}

    try:
        # hash password
        em = EM()
        hash_and_salt = em.hash(password, True)
        password = hash_and_salt['hash']
        salt = hash_and_salt['salt']

        # create user object
        user = User(username=username, password=password, salt=salt, email=email, verified=False, name=name, number=number, address=address, listings=[], language=language)
    
        # checks - add more later!

        # use python library
        if "@" not in user.email: 
         return {'success':False,'error': "Invalid email"}
        
        if "gatech" not in user.email:
            return {'success':False,'error': "Must use a Georgia Tech email"}
            
        # firebase 
        create_user(db, user)

    except Exception as e:
        return {'success':False,'error': str(e)}
    
    return {'success':True,'error': None, 'user': user}
