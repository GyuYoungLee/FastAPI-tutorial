"""
http ':8000/func?a=1&b=2'
http ':8000/class?a=1&b=2'
http ':8000/pydantic?a=1&b=2'
"""

from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field

app = FastAPI()


# 1. 함수를 DI 추가
def func_params(a: int, b: int):
    return a + b


@app.get("/func")
def sum_values_with_func(result: int = Depends(func_params)):
    return {"result": result}


# 2. 클래스를 DI 추가
class ClassParams:
    def __init__(self, a: int, b: int):
        self.result = a + b


@app.get("/class")
def sum_values_with_class(params: ClassParams = Depends(ClassParams)):
    return {"result": params.result}


# 3. pydantic DI 추가
class PydanticParams(BaseModel):
    a: int = Field(...)
    b: int = Field(...)

    @property
    def result(self):
        return self.a + self.b


@app.get("/pydantic")
def sum_values_with_pydantic(params: PydanticParams = Depends()):
    return {"result": params.result}
