"""
http -v :8000/error
"""

from fastapi import FastAPI, HTTPException, status

app = FastAPI()


@app.get("/error")
async def get_error():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error", headers={"X-Error": "my error"})
