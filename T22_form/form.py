"""
http -v -f POST :8000/login username=gy password=1234
http -v -f POST :8000/login username=gy password=1234 file@backup/apple.jpeg
"""

from fastapi import FastAPI, Form, File, UploadFile
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/login")
def login(username: str = Form(...),
          password: str = Form(...),
          file: UploadFile = File(None)):
    """
    Content-Type ( < 마임 타입 < 미디어 타입)
        파일 전송이 없으면: application/x-www-urlencoded
        파일 전송이 있으면: multipart/form-data
    """
    resp = {"username": username, "password": password}
    if file:
        resp.update({"filename": file.filename, "content": file.content_type})

    return resp
