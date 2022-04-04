from fastapi import Request, HTTPException, status
from fastapi.exceptions import RequestValidationError
from .response import ErrorORJDefaultORJSONResponse


# -------------------------------
# error handler class
# -------------------------------
class ErrorHandler:
    @staticmethod
    async def http422_error_handler(_: Request, e: RequestValidationError) -> ErrorORJDefaultORJSONResponse:
        status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        detail = {
            "code": "0" * 5,
            "type": e.errors()[0].get("type"),
            "message": e.errors()[0].get("msg")
        }
        return ErrorORJDefaultORJSONResponse(status_code=status_code, content=detail)

    @staticmethod
    async def http_error_handler(_: Request, e: HTTPException) -> ErrorORJDefaultORJSONResponse:
        return ErrorORJDefaultORJSONResponse(status_code=e.status_code, content=e.detail)
