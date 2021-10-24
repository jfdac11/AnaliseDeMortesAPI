from fastapi import FastAPI
from db_connection import DBConnection

DBConnection.create_connection()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

