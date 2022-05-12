"""
http ':8000/users/gy?age=10'
"""

from fastapi import FastAPI

app = FastAPI()


# path 파라미터: name
# query 파라미터: age

@app.get("/users/{name}")
def get_user(name: str, age: int) -> dict:
    return {
        "name": name,
        "age": age,
    }
