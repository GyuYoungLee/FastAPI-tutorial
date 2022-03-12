"""
http :8000/users
http POST :8000/users name=gy age=10
"""

from typing import List

from fastapi import FastAPI, HTTPException

from T21_alchemy import models, schemas
from T21_alchemy.databases import engine, SessionLocal

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get("/users", response_model=List[schemas.UserResponse])
def get_users():
    db = SessionLocal()
    return db.query(models.User).all()


@app.post("/users", response_model=schemas.UserResponse)
def create_user(user_create: schemas.UserCreate):
    db = SessionLocal()

    existed_user = db.query(models.User).filter_by(name=user_create.name).first()
    if existed_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = models.User(**user_create.dict())
    db.add(user)
    db.commit()

    db.refresh(user)
    return user
