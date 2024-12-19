from fastapi import FastAPI

from src.delivery.api import health_check
from src.delivery.api.students import student_create_route
from src.delivery.api.videos import video_create_route
from src.delivery.api.video_comments_counter import video_comment_counter_finder_route

app = FastAPI()

app.include_router(health_check.router)
app.include_router(video_create_route.router)
app.include_router(student_create_route.router)
app.include_router(video_comment_counter_finder_route.router)
