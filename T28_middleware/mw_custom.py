"""
http -v :8000
"""

import time
from fastapi import FastAPI, Request

app = FastAPI()


# 미들웨어 추가
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
def hello():
    return {"message": "Hello World"}
