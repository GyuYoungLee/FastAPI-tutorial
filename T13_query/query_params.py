"""
http ':8000/users?age=10&grade=a'
"""

from enum import Enum

from fastapi import FastAPI

app = FastAPI()


class UserLevel(str, Enum):
    a = "a"
    b = "b"
    c = "c"


# 쿼리 파라미터: age, grade
@app.get("/users")
def get_users(age: int, grade: UserLevel = UserLevel.a):  # 추가: UserLevel 기본값
    return {"age": age, "grade": grade}
