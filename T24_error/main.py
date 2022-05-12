# http :8000/hello/gy
# http :8000/hello/jay
# http :8000/error

from fastapi import FastAPI, Path
from fastapi.exceptions import RequestValidationError

from .default_responses import DefaultJsonResponse, http422_error_handler, custom_error_handler
from .error_class import CustomError

app = FastAPI(default_response_class=DefaultJsonResponse)

app.add_exception_handler(RequestValidationError, handler=http422_error_handler)
app.add_exception_handler(CustomError, handler=custom_error_handler)


@app.get("/hello/{name}")
def hello(name: str = Path(..., max_length=2)) -> dict:
    return {
        "message": f"hello {name}"
    }


@app.get("/error")
def make_custom_error() -> None:
    raise CustomError(status_code=400, code="00001", type="greeting", message="hi")
