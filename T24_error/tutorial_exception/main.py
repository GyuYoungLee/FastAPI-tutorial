"""
http :8000/hello/gy
http :8000/hello/jay
http :8000/error
"""

from fastapi import FastAPI, Path
from fastapi.exceptions import RequestValidationError
from .response import DefaultORJSONResponse
from .handlers import TutorialError, ErrorHandler

app = FastAPI(default_response_class=DefaultORJSONResponse)

app.add_exception_handler(RequestValidationError, handler=ErrorHandler.http422_error_handler)
app.add_exception_handler(TutorialError, handler=ErrorHandler.tutorial_error_handler)


@app.get("/hello/{name}")
def hello(name: str = Path(..., max_length=2)) -> dict:
    return {
        "message": f"hello {name}"
    }


# 사용자 예외 클래스 raise
@app.get("/error")
async def make_error() -> None:
    raise TutorialError(status_code=404, code="00001", type="greeting", message="hi")
