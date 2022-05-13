"""
http -f POST :8000/login username=gy password=1234
"""

from datetime import datetime, timedelta

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import bcrypt
from jose import jwt

from common.consts import fake_user_db, SECRET_KEY, ALGORITHM
from common.schemas import UserTokenInfo

app = FastAPI()


def create_token(user: dict) -> str:
    # pydantic 객체로 패스워드 제외함
    user_token_info = UserTokenInfo(**user, exp=datetime.utcnow() + timedelta(seconds=60 * 60 * 24))
    return jwt.encode(user_token_info.dict(), SECRET_KEY, ALGORITHM)


@app.post("/login")
def issue_token(input_data: OAuth2PasswordRequestForm = Depends()) -> dict:
    # DB 데이타 조회
    user = fake_user_db[input_data.username]
    if not bcrypt.checkpw(input_data.password.encode(), user["password"].encode()):
        raise HTTPException(401)

    # 토큰 발급
    return {
        "token": create_token(user)
    }
