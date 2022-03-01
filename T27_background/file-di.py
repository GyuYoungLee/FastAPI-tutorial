"""
http POST ':8000/send-notification/gylee?q=abc'
"""

import pathlib
import time
from typing import Optional

from fastapi import FastAPI, status, Depends, BackgroundTasks

app = FastAPI()


# 백그라운드 작업
def write_log(message: str):
    time.sleep(2.0)

    current_dir = pathlib.Path(__file__).parent.resolve()
    with open(f"{current_dir}/log.txt", mode="a") as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: Optional[str] = None):
    if q:
        message = f"Found query: {q}\n"
        background_tasks.add_task(write_log, message)  # 백그라운드 작업 추가


@app.post("/send-notification/{email}", status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(get_query)])
async def send_notification(email: str, background_tasks: BackgroundTasks):
    message = f"Notification to {email}\n"
    background_tasks.add_task(write_log, message)  # 백그라운드 작업 추가

    return {"message": "Notification sent"}
