"""
http :8000/test-error
"""

from typing import Optional, Any, Dict

from fastapi import FastAPI, HTTPException, status

app = FastAPI()


class SomeError(HTTPException):
    def __init__(self, name: str, code: int, status_code: int, detail: Any = None,
                 headers: Optional[Dict[str, Any]] = None) -> None:
        result = {
            "name": name,
            "code": code,
            "message": detail
        }
        super().__init__(status_code=status_code, detail=result, headers=headers)


@app.get("/test-error")
async def get_test_error():
    raise SomeError(name="test", code=100, status_code=status.HTTP_404_NOT_FOUND, detail="test error")
