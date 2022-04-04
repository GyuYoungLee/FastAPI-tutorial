from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from .response import ErrorORJDefaultORJSONResponse


# -------------------------------
# error class
# -------------------------------
class TutorialError(Exception):
    def __init__(self, status_code: int, code: str, type: str, message: str) -> None:
        self.status_code = status_code
        self.code = code
        self.type = type
        self.message = message

    def __str__(self):
        return f"<{self.type}> error is occurred. code: {self.code}, message: {self.message}"


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
    async def tutorial_error_handler(_: Request, e: TutorialError) -> ErrorORJDefaultORJSONResponse:
        status_code = e.status_code
        detail = {
            "code": e.code,
            "type": e.type,
            "message": e.message
        }
        return ErrorORJDefaultORJSONResponse(status_code=status_code, content=detail)
