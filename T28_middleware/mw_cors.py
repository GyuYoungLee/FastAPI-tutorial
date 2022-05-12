"""
http OPTIONS :8000 Origin:http://localhost Access-Control-Request-Method:GET
http OPTIONS :8000 Origin:https://payhere.in Access-Control-Request-Method:GET
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# cors 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["OPTIONS", "GET"],
    allow_headers=["*"],
)


@app.get("/")
def hello():
    return {"message": "Hello World"}
