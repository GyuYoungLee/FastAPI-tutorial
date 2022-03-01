"""
http POST :8000/send-notification/gylee
"""

import pathlib
import time

from fastapi import FastAPI, status, BackgroundTasks

app = FastAPI()


# 백그라운드 작업
def write_log(message: str):
    time.sleep(2.0)

    current_dir = pathlib.Path(__file__).parent.resolve()
    with open(f"{current_dir}/log.txt", mode="a") as log:
        log.write(message)


@app.post("/send-notification/{email}", status_code=status.HTTP_202_ACCEPTED)
async def send_notification(email: str, background_tasks: BackgroundTasks):
    message = f"Notification to {email}\n"
    background_tasks.add_task(write_log, message)

    return {"message": "Notification sent"}
