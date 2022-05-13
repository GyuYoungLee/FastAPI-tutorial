from datetime import datetime

from pydantic import BaseModel


class UserTokenInfo(BaseModel):
    id: int
    username: str
    email: str
    exp: datetime


class UserResponse(BaseModel):
    username: str
    email: str
