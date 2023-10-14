from vgem import EM

from src.models.User.User import User
from src.firebase.user.create import create_user

def sign_up(db, username, password, email, name, number, address, language) -> dict:
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
    
        # firebase 
        create_user(db, user)

    except Exception as e:
        return {'success':False,'error': str(e)}
    
    return {'success':True,'error': None, 'user': user}
