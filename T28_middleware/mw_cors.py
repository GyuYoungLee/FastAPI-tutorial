"""
http OPTIONS :8000 Origin:http://localhost Access-Control-Request-Method:GET
http OPTIONS :8000 Origin:https://payhere.in Access-Control-Request-Method:GET
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000"
]

# 임포트 모듈을 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["OPTIONS", "GET"],
    allow_headers=["*"],
)


@app.get("/")
def hello():
    return {"message": "Hello World"}
