from typing import Any

import orjson
from fastapi import FastAPI
from fastapi.responses import JSONResponse


class DefaultORJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed to use ORJSONResponse"
        return orjson.dumps(self.formatter(content))

    def formatter(self, content: Any):
        return {
            "data": content,
            "meta": {
                "code": self.status_code
            }
        }


app = FastAPI(default_response_class=DefaultORJSONResponse)


@app.get("/")
def hello():
    return {
        "message": "hello"
    }
