from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    age: int


class UserResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
