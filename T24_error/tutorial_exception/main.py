"""
http :8000/hello/gy
http :8000/hello/jay
http :8000/error
"""

from fastapi import FastAPI, Path
from fastapi.exceptions import RequestValidationError
from .utils import DefaultORJSONResponse
from .utils import ErrorHandler
from .utils import TutorialError

app = FastAPI(default_response_class=DefaultORJSONResponse)

app.add_exception_handler(RequestValidationError, ErrorHandler.http422_error_handler)
app.add_exception_handler(TutorialError, ErrorHandler.tutorial_error_handler)


@app.get("/hello/{name}")
def hello(name: str = Path(..., max_length=2)):
    return {
        "message": f"hello {name}"
    }


# 예외 클래스 정의 처리
@app.get("/error")
async def make_error():
    raise TutorialError(status_code=404, code="00001", type="greeting", message="hi")
