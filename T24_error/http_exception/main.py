"""
http :8000/hello/gy
http :8000/hello/jay
http :8000/error
"""

from fastapi import FastAPI, HTTPException, Path
from fastapi.exceptions import RequestValidationError
from .response import DefaultORJSONResponse
from .handlers import ErrorHandler

app = FastAPI(default_response_class=DefaultORJSONResponse)

app.add_exception_handler(RequestValidationError, handler=ErrorHandler.http422_error_handler)
app.add_exception_handler(HTTPException, handler=ErrorHandler.http_error_handler)


@app.get("/hello/{name}")
def hello(name: str = Path(..., max_length=2)) -> dict:
    return {
        "message": f"hello {name}"
    }


# HTTPException 이용 raise
@app.get("/error")
async def make_error() -> None:
    raise HTTPException(status_code=404, detail={"code": "00001", "type": "greeting", "message": "hi"})
