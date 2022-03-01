"""
http ':8000/items/func?limit=1'
http ':8000/items/class?limit=1'
http ':8000/items/pydantic?limit=1'
"""

from typing import Optional

from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field

app = FastAPI()

items = ({"name": "Foo"}, {"name": "Bar"}, {"name": "Baz"})


# 1. 함수를 DI 추가
async def func_params(q: Optional[str] = None, offset: int = 0, limit: int = 100):
    return {"q": q, "offset": offset, "limit": limit}


@app.get("/items/func")
async def get_items_with_func(params: dict = Depends(func_params)):
    response = {}
    if params["q"]:
        response.update({"q": params["q"]})

    result = items[params["offset"]: params["offset"] + params["limit"]]
    response.update({"items": result})

    return response


# 2. 클래스를 DI 추가
class ClassParams:
    def __init__(self, q: Optional[str] = None, offset: int = 0, limit: int = 100):
        self.q = q
        self.offset = offset
        self.limit = limit


@app.get("/items/class")
async def get_items_with_class(params: ClassParams = Depends(ClassParams)):
    response = {}
    if params.q:
        response.update({"q": params.q})

    result = items[params.offset: params.offset + params.limit]
    response.update({"items": result})

    return response


# 3. pydantic DI 추가
class PydanticParams(BaseModel):
    q: Optional[str] = Field(None, min_length=2)
    offset: int = Field(0, ge=0)
    limit: int = Field(100, gt=0)


@app.get("/items/pydantic")
async def get_items_with_pydantic(params: PydanticParams = Depends()):
    response = {}
    if params.q:
        response.update({"q": params.q})

    result = items[params.offset: params.offset + params.limit]
    response.update({"items": result})

    return response
