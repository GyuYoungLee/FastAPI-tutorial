"""
http -v :8000/users/me Authorization:'Bearer '
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTClaimsError

from common.consts import fake_user_db, SECRET_KEY, ALGORITHM
from common.schemas import UserTokenInfo, UserResponse

app = FastAPI()

security = HTTPBearer()


def get_user(cred: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    try:
        decoded_data = jwt.decode(cred.credentials, SECRET_KEY, ALGORITHM)
    except ExpiredSignatureError:
        raise HTTPException(401, "Expired")
    except JWTClaimsError:
        raise HTTPException(400, "Claim Error")

    user_token_info = UserTokenInfo(**decoded_data)
    return fake_user_db[user_token_info.username]


@app.get("/users/me", response_model=UserResponse)
def get_current_user(user: dict = Depends(get_user)) -> dict:
    return user
