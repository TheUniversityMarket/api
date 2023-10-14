from fastapi import FastAPI
from src.firebase.auth import start_firebase

# Create the App Instances
app = FastAPI()
db = start_firebase()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# TESTS
from src.api.tests.listing_tests import *
from src.api.tests.user_tests import *

@app.get("/test/create_user")
def _test_sign_up():
    return test_sign_up(db)

@app.get("/test/sign_in")
def _test_sign_in():
    return test_sign_in(db)
    

