from fastapi import FastAPI
from src.firebase.auth import start_firebase

# Create the App Instances
app = FastAPI()
db = start_firebase()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# TESTS
from src.models.User.User import User
from src.api.user.create_user import sign_up

@app.get("/test/create_user")
def _sign_up():

    new_user = User(username="john_doe", password="password123", email="john@example.com", verified=True, name="John Doe", number="1234567890", address="123 Main St", listings=[], language="English")

    return_value = sign_up(db, new_user.serialize())

    return return_value

