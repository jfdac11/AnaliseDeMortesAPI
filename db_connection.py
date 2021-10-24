from fastapi import FastAPI
import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv('./.env')


class DBConnection():

    def create_connection():
        client = motor.motor_asyncio.AsyncIOMotorClient(
            os.environ['MONGODB_URL'])
        db = client.config
        print(db)
