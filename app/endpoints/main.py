import sys
import os
from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, os.getenv("APP_PATH"))

from fastapi import FastAPI
from app.db import registration as rg


app = FastAPI()


@app.get('/signup')
async def sign_up():
    rg.registration("admin4", "test_password3")
    return {"message": "Test"}
