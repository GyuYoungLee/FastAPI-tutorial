"""
http -v :8000/users/me Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJneSIsImVtYWlsIjoiZ3lsZWVAcGF5aGVyZS5pbiIsImV4cCI6MTY0NjIyMzI2MH0.TW0N7HFhR1dGLB6I0GOdng0Zv8cyWY9bNstwoVzdL8g'
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTClaimsError

from .consts import fake_user_db, SECRET_KEY, ALGORITHM
from .schmas import User

app = FastAPI()
security = HTTPBearer()


async def get_user(cred: HTTPAuthorizationCredentials = Depends(security)):
    try:
        decoded_data = jwt.decode(cred.credentials, SECRET_KEY, ALGORITHM)
    except ExpiredSignatureError:
        raise HTTPException(401, "Expired")
    except JWTClaimsError:
        raise HTTPException(400, "Claim Error")

    # pydantic 객체로
    user_info = User(**decoded_data)
    return fake_user_db[user_info.username]


@app.get("/users/me", response_model=User)
async def get_current_user(user: dict = Depends(get_user)):
    return user
