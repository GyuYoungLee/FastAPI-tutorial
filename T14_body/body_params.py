"""
http POST :8000/users name=gy password=1234
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# 바디 파라미터: name, password
class User(BaseModel):
    name: str
    password: str


@app.post("/users")
def create_user(user: User):
    return user
