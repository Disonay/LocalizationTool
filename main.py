import uvicorn
from fastapi import FastAPI

from consts.app_consts import HOST, PORT

app = FastAPI()


@app.get("/health")
def health() -> str:
    return "App is working"


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
