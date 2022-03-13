"""
http POST :8000/func a=1 b=2
http POST :8000/class a=1 b=2
http POST :8000/pydantic a=1 b=2
"""

from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


class Params(BaseModel):
    a: int
    b: int


# 1. 함수를 DI 추가
def func_params(params: Params):
    return params.a + params.b


@app.post("/func")
def sum_values_with_func(result: int = Depends(func_params)):
    return {"result": result}


# 2. 클래스를 DI 추가
class ClassParams:
    def __init__(self, params: Params):
        self.result = params.a + params.b


@app.post("/class")
def sum_values_with_class(params: ClassParams = Depends(ClassParams)):
    return {"result": params.result}


# 3. pydantic DI 추가
class PydanticParams(BaseModel):
    params: Params

    @property
    def result(self):
        return self.params.a + self.params.b


@app.post("/pydantic")
def sum_values_with_pydantic(params: PydanticParams = Depends()):
    return {"result": params.result}
