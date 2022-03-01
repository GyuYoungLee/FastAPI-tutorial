"""
http :8000/users
http POST :8000/users email=gy password=111
"""

from typing import List

from fastapi import FastAPI, HTTPException

from . import models, schemas
from .databases import engine, SessionLocal

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get("/users", response_model=List[schemas.User])
def get_users():
    db = SessionLocal()
    return db.query(models.User).all()


@app.post("/users", response_model=schemas.User)
# def insert_users(user: schemas.UserCreate = Depends()):
def insert_users(input_data: schemas.UserCreate):
    db = SessionLocal()

    existed_user = db.query(models.User).filter_by(email=input_data.email).first()
    if existed_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = models.User(email=input_data.email, password=input_data.password)
    db.add(user)
    db.commit()

    db.refresh(user)  # 안하면 에러남 ??
    return user
