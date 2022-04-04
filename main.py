from fastapi import FastAPI, Depends, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()


def verify_token(x_token: str = Header(None)) -> None:
    if not x_token:
        raise HTTPException(status_code=401, detail="Not authorized")


@app.get("/hello", dependencies=[Depends(verify_token)])
def hello():
    return {"message": "Hello"}


class Params(BaseModel):
    a: int
    b: int


def func_params(params: Params) -> int:
    return params.a + params.b


@app.post("/func")
def sum_func(result: int = Depends(func_params)):
    return {"result": result}


class ClassParams:
    def __init__(self, params: Params) -> None:
        self.result = params.a + params.b


@app.post("/class")
def sum_class(params: ClassParams = Depends(ClassParams)):
    return {"result": params.result}


class PydanticParams(BaseModel):
    params: Params

    @property
    def result(self) -> int:
        return self.params.a + self.params.b


@app.post("/pydantic")
def sum_pydantic(params: PydanticParams = Depends()):
    return {"result": params.result}
