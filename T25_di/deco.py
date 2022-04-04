"""
http -v :8000/hello
http -v :8000/hello X-Token:12345566
"""

from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()


def verify_token(x_token: str = Header(None)) -> None:
    if not x_token:
        raise HTTPException(status_code=401, detail='Not authorized')


@app.get("/hello", dependencies=[Depends(verify_token)])
def hello() -> dict:
    return {"message": "Hello"}
