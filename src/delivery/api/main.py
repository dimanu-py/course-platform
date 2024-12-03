from fastapi import FastAPI

from src.delivery.api import health_check
from src.delivery.api.videos import videos_put_route

app = FastAPI()

app.include_router(health_check.router)
app.include_router(videos_put_route.router)
