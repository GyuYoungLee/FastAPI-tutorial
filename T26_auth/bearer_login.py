"""
http -f POST :8000/login username=gy password=1234
"""

from datetime import datetime, timedelta

import bcrypt
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

from .consts import fake_user_db, SECRET_KEY, ALGORITHM
from .schmas import UserPayload

app = FastAPI()


async def create_token(data: dict):
    # pydantic 객체로 패스워드 제외함
    user_info = UserPayload(**data, exp=datetime.utcnow() + timedelta(seconds=60 * 60 * 24))
    return jwt.encode(user_info.dict(), SECRET_KEY, ALGORITHM)


@app.post("/login")
async def issue_token(input_data: OAuth2PasswordRequestForm = Depends()):
    # DB 데이타 조회
    user = fake_user_db[input_data.username]
    if not bcrypt.checkpw(input_data.password.encode(), user["password"].encode()):
        raise HTTPException(401)

    # 토큰 발급
    return {
        "token": await create_token(user)
    }
