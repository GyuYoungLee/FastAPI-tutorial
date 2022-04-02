"""
http -v -f POST :8000/form name=gy age=10
http -v -f POST :8000/file name=gy age=10 file@9-backup/apple.jpeg
"""

from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI()


# Content 타입 (= Mime 타입, Media 타입): application/x-www-urlencoded

@app.post("/form")
def create_user(name: str = Form(...), age: int = Form(...)):
    return {
        "name": name,
        "age": age,
    }


# Content 타입 (= Mime 타입, Media 타입): multipart/form-data

@app.post("/file")
def create_user(name: str = Form(...), age: int = Form(...), file: UploadFile = File(...)):
    return {
        "name": name,
        "age": age,
        "file": {"filename": file.filename, "content": file.content_type}
    }
