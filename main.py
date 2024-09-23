from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles  # new
import uvicorn

from src.front_end.core.config import settings

from src.front_end.routers.base import api_router as web_app_router

# app = FastAPI()


def include_router(app):
    app.include_router(web_app_router)


def configure_static(app):  # new
    app.mount("/src/front_end/static", StaticFiles(directory="src/front_end/static"), name="static")


def start_application():

    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    return app

# @app.get("/")
# async def root():
#     return {"message": "Hello Bigger Applications!"}

app = start_application()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)
