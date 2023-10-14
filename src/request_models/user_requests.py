from pydantic import BaseModel

class SignInRequest(BaseModel):
    username: str
    password: str

class SignUpRequest(BaseModel):
    username: str
    password: str
    email: str
    name: str
    number: str
    address: str
    language: str