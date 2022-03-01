"""
http -v :8000/items X-Token:12345566
http -v :8000/items X-Token:1234
"""

from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

items = ({"name": "Foo"}, {"name": "Bar"}, {"name": "Baz"})


async def verify_token(x_token: str = Header(...)):
    if len(x_token) < 5:
        raise HTTPException(401, detail="Not authorized")


@app.get("/items", dependencies=[Depends(verify_token)])
async def get_items():
    return items
