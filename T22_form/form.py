"""
http -v -f POST :8000/login username=gy password=1234
http -v -f POST :8000/login username=gy password=1234 file@images/apple.jpeg
"""

from fastapi import FastAPI, Form, File, UploadFile
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...), file: UploadFile = File(None)):
    response = {"username": username, "password": password}
    if file:
        response.update({"filename": file.filename, "content": file.content_type})

    return response
