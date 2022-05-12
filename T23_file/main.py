"""
http -v -f POST :8000/file name=gy file@9-backup/apple.jpeg
"""

from tempfile import NamedTemporaryFile
from typing import IO

from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI()


async def save_file(file: IO) -> str:
    with NamedTemporaryFile(mode="wb", delete=False) as temp_file:
        temp_file.write(file.read())
        return temp_file.name


@app.post("/file")
async def create_user(name: str = Form(...), file: UploadFile = File(...)) -> dict:
    stored_path = await save_file(file=file.file)
    return {
        "name": name,
        "file": {
            "filename": file.filename,
            "content": file.content_type,
            "stored_path": stored_path,
        }
    }
