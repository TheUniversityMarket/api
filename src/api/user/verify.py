from uuid import uuid4
from src.models.User.User import User
from src.main import USERS_TO_VERIFY

def get_verification_code(db, email, user_id):
    code = str(uuid4())[0:6]
    USERS_TO_VERIFY.append({'email': email, 'user_id': user_id, 'code': code})
    return code

def check_verification_code(db, email, user_id, code):
    for user in USERS_TO_VERIFY:
        if user['email'] == email and user['user_id'] == user_id and user['code'] == code:
            USERS_TO_VERIFY.remove(user)
            return True
    return False