"""
http -v -f POST :8000/file/store file@9-backup/apple.jpeg
"""

from tempfile import NamedTemporaryFile
from typing import IO

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


async def save_file(file: IO):
    with NamedTemporaryFile("wb", delete=False) as temp_file:
        temp_file.write(file.read())
        return temp_file.name


@app.post("/file/store")
async def upload_file(file: UploadFile = File(...)):
    stored_path = await save_file(file.file)  # file: 비동기, file.file: 동기
    return {
        "filename": file.filename,
        "content": file.content_type,
        "stored_path": stored_path
    }
