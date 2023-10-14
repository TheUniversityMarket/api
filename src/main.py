from fastapi import FastAPI
from src.firebase.auth import start_firebase

# Create the App Instances
app = FastAPI()
db = start_firebase()

@app.get("/")
def read_root():
    return {"Hello": "World"}