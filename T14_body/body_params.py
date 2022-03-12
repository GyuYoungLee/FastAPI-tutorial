"""
http POST :8000/users name=gy age=10
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# 바디 파라미터: name, age

class User(BaseModel):
    name: str
    age: int


@app.post("/users")
def create_user(user: User):
    return {
        "name": user.name,
        "age": user.age,
    }
