"""
http :8000/hello/gy
http :8000/hello/jay
http :8000/error
"""

from fastapi import FastAPI, HTTPException, Path
from fastapi.exceptions import RequestValidationError
from .utils import DefaultORJSONResponse
from .utils import ErrorHandler

app = FastAPI(default_response_class=DefaultORJSONResponse)

app.add_exception_handler(RequestValidationError, ErrorHandler.http422_error_handler)
app.add_exception_handler(HTTPException, ErrorHandler.http_error_handler)


@app.get("/hello/{name}")
def hello(name: str = Path(..., max_length=2)):
    return {
        "message": f"hello {name}"
    }


# HTTPException 이용
@app.get("/error")
async def make_error():
    raise HTTPException(status_code=404, detail={"code": "00001", "type": "greeting", "message": "hi"})
