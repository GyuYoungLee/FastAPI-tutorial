import json
from typing import Any

from fastapi import Request, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel

from .error_class import CustomError


class MetaData(BaseModel):
    code: str
    type: str = None
    message: str = None


class DefaultJsonResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        code = f"{self.status_code}{'0' * 5}"

        return json.dumps({
            "data": content,
            "meta": MetaData(code=code).dict(exclude_unset=True),
        }).encode("utf-8")


class ErrorJsonResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        code = f"{self.status_code}{content.get('code')}"
        _type = content.get("type", None)
        message = content.get("message", None)

        return json.dumps({
            "data": {},
            "meta": MetaData(code=code, type=_type, message=message).dict(exclude_unset=True),
        }).encode("utf-8")


# validation error
def http422_error_handler(_: Request, e: RequestValidationError) -> ErrorJsonResponse:
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    content = {
        "code": "0" * 5,
        "type": e.errors()[0].get("type"),
        "message": e.errors()[0].get("msg")
    }
    return ErrorJsonResponse(status_code=status_code, content=content)


# http exception
def http_exception_handler(_: Request, e: HTTPException) -> ErrorJsonResponse:
    status_code = e.status_code
    content = {
        "code": "0" * 5,
        "message": e.detail
    }
    return ErrorJsonResponse(status_code=status_code, content=content)


# custom error
def custom_error_handler(_: Request, e: CustomError) -> ErrorJsonResponse:
    status_code = e.status_code
    content = {
        "code": e.code,
        "type": e.type,
        "message": e.message
    }
    return ErrorJsonResponse(status_code=status_code, content=content)
