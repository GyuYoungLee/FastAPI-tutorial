"""
http :8000/users
http POST :8000/users name=gy age=10
"""

from fastapi import FastAPI
from pydantic import BaseModel

from sqlalchemy.orm import Session

from .databases import engine, SessionLocal
from .models import Base, User

app = FastAPI()
Base.metadata.create_all(bind=engine)


class UserRequest(BaseModel):
    name: str
    age: int


class UserResponse(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True


@app.post("/users", response_model=UserResponse)
def create_user(body: UserRequest) -> User:
    db: Session = SessionLocal()
    user = User(name=body.name, age=body.age)
    db.add(User)
    db.commit()

    db.refresh(user)
    return user  # sqlalchemy instance


@app.get("/users", response_model=list[UserResponse])
def get_users() -> list[User]:
    db: Session = SessionLocal()
    return db.query(User).all()  # sqlalchemy instance
