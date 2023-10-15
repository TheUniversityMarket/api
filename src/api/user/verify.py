from uuid import uuid4
from src.models.User.User import User
from src.mailjet import send_message

def get_verification_code(db, email, USERS_TO_VERIFY):
    try:
        if "@" not in email: 
            return {'success':False,'error': "Invalid email"}
        if "gatech" not in email:
            return {'success':False,'error': "Must use a Georgia Tech email"}
        code = str(uuid4())[0:6]
        USERS_TO_VERIFY.append({'email': email, 'code': code})

        # send email with code
        send_message(email, f"Your verification code is {code}", "UMarket Verification Code")
        return {'success':True,'error': None}
    except Exception as e:
        return {'success':False,'error': str(e)}

def check_verification_code(db, email, code, USERS_TO_VERIFY):
    for user in USERS_TO_VERIFY:
        if user['email'] == email  and user['code'] == code:
            USERS_TO_VERIFY.remove(user)
            return True
    return False