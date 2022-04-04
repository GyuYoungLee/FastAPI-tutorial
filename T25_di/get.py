"""
http ':8000/func?a=1&b=2'
http ':8000/class?a=1&b=2'
http ':8000/pydantic?a=1&b=2'
"""

from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


# 1. 함수 DI
def func_params(a: int, b: int) -> int:
    return a + b


@app.get("/func")
def sum_func(result: int = Depends(func_params)) -> dict:
    return {"result": result}


# 2. 클래스 DI
class ClassParams:
    def __init__(self, a: int, b: int) -> None:
        self.result = a + b


@app.get("/class")
def sum_class(params: ClassParams = Depends(ClassParams)) -> dict:
    return {"result": params.result}


# 3. pydantic DI
class PydanticParams(BaseModel):
    a: int
    b: int

    @property
    def result(self) -> int:
        return self.a + self.b


@app.get("/pydantic")
def sum_pydantic(params: PydanticParams = Depends()) -> dict:
    return {"result": params.result}
