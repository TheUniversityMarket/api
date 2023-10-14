# config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.firebase.auth import start_firebase

# Create the App Instances
app = FastAPI()
db = start_firebase()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def _read_root():
    return {"Hello": "World"}

@app.get("/ping")
def _ping():
    return {"ping": "pong"}

# user routes
from src.request_models.user_requests import *

from src.api.user.sign_in import sign_in_by_username
@app.post("/sign_in")
def _sign_in(request: SignInRequest):
    return sign_in_by_username(db=db, username=request.username, password=request.password)

from src.api.user.sign_up import sign_up
@app.post("/sign_up")
def _sign_up(request: SignUpRequest):
    return sign_up(db=db, username=request.username, password=request.password, email=request.email, name=request.name, number=request.number, address=request.address, language=request.language)

# listing routes
from src.request_models.listing_requests import *

# TESTS
from src.api.tests.listing_tests import *
from src.api.tests.user_tests import *

@app.get("/test/create_user")
def _test_sign_up():
    return test_sign_up(db)

@app.get("/test/sign_in_by_id")
def _test_sign_in_by_id():
    return test_sign_in_by_id(db)

@app.get("/test/sign_in_by_username")
def _test_sign_in_by_username():
    return test_sign_in_by_username(db)

    

