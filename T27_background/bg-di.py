"""
http POST ':8000/send/gylee'
"""

import pathlib
import time

from fastapi import FastAPI, status, BackgroundTasks, Depends

app = FastAPI()


# 백그라운드 작업
def write_log(message: str):
    time.sleep(2.0)

    current_dir = pathlib.Path(__file__).parent.resolve()
    with open(f"{current_dir}/log.txt", mode="a") as log:
        log.write(message)


def get_query(email: str, background_tasks: BackgroundTasks):
    message = f"Notification to {email}\n"
    background_tasks.add_task(write_log, message)


@app.post("/send/{email}", status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(get_query)])
async def send_notification():
    return {"message": "Notification sent"}
