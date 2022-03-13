"""
http -v :8000/hello X-Token:12345566
http -v :8000/hello
"""

from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()


def verify_token(x_token: str = Header(None)):
    if not x_token:
        raise HTTPException(401, detail='Not authorized')


@app.get("/hello", dependencies=[Depends(verify_token)])
def hello():
    return {"message": "Hello"}
