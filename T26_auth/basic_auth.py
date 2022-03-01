"""
http -v :8000/users/me Authorization:'Basic Z3k6MTIzNA=='
http -v 'gy:1234@localhost:8000/users/me'
"""

from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()


@app.get("/users/me")
def get_current_user(cred: HTTPBasicCredentials = Depends(security)):
    # DB 데이타 조회
    return {"username": cred.username, "password": cred.password}
