import uvicorn
from fastapi import FastAPI

from consts.app_consts import HOST, PORT
from route import localization

app = FastAPI()
app.include_router(localization.router)


@app.get("/health")
def health() -> str:
    """
    Endpoint to check if the app works
    """
    return "App is working"


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
