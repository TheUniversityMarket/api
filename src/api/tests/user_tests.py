from src.models.User.User import User
from src.api.user.create_user import sign_up
from src.api.user.sign_in import sign_in

def test_sign_up(db) -> dict:
    new_user = User(username="test_sign_in", password="password123", email="john@example.com", verified=True, name="John Doe", number="1234567890", address="123 Main St", listings=[], language="English")
    return_value = sign_up(db, new_user.serialize())
    return return_value

def test_sign_in(db) -> dict:
    new_user = User(username="test_sign_up", password="password123", email="john2@example.com", verified=True, name="John Doe", number="1234567890", address="123 Main St", listings=[], language="English")
    return_value = sign_up(db, new_user.serialize())
    if return_value['success'] != True:
        return return_value
    return_value = sign_in(db, return_value['user'].id, new_user.password)
    return return_value
            