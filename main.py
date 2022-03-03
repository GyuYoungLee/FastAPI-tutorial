from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello World"


@app.get("/health")
async def health():
    return {
        "health": "check!"
    }
