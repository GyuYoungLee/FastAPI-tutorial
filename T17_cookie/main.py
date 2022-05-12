"""
http -v :8000/cookie 'Cookie:name=gy;age=10'
http -v :8000/header X-Name:gy X-Age:10
"""

from fastapi import FastAPI, Cookie, Header

app = FastAPI()


# 쿠기: name

@app.get("/cookie")
def get_cookies(name: str = Cookie(...), age: int = Cookie(None)) -> dict:
    return {
        "name": name,
        "age": age,
    }


# 헤더: X-Token

@app.get("/header")
def get_headers(x_name: str = Header(...), x_age: int = Header(None)) -> dict:
    return {
        "name": x_name,
        "age": x_age,
    }
