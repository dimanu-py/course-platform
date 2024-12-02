from fastapi import FastAPI

from src.delivery.api import health_check

app = FastAPI()

app.include_router(health_check.router)
