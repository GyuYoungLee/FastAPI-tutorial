"""
http -v -f POST :8000/upload file@9-backup/apple.jpeg
"""

from tempfile import NamedTemporaryFile
from typing import IO

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


async def save_file(file: IO):
    with NamedTemporaryFile("wb", delete=False) as temp_file:
        temp_file.write(file.read())
        return temp_file.name


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    path = await save_file(file.file)  # file.file
    return {
        "upload_path": path
    }
