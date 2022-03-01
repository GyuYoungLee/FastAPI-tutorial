"""
http -v :8000/cookie Cookie:name=gy
http -v :8000/header X-Token:abc123
"""

from fastapi import FastAPI, Cookie, Header

app = FastAPI()


@app.get("/cookie")
def get_cookies(name: str = Cookie(None)):
    return {"name": name}


@app.get("/header")
def get_headers(x_token: str = Header(None, title="토큰")):
    return {"X-Token": x_token}
