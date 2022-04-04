from typing import Any

import orjson
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class MetaData(BaseModel):
    code: str
    type: str = None
    message: str = None


class DefaultORJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed to use ORJSONResponse"
        return orjson.dumps(self.formatter(content))

    def formatter(self, content: Any) -> dict[str, Any]:
        code = f"{self.status_code}{'0' * 5}"

        return {
            "data": content,
            "meta": MetaData(code=code).dict(exclude_unset=True)
        }


class ErrorORJDefaultORJSONResponse(DefaultORJSONResponse):
    def formatter(self, content: Any) -> dict[str, Any]:
        code = f"{self.status_code}{content.get('code')}"
        _type = content.get("type")
        message = content.get("message")

        return {
            "data": {},
            "meta": MetaData(code=code, type=_type, message=message).dict(exclude_unset=True)
        }
