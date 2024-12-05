from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from src.contexts.content_creation.videos.application.create_video_command import (
    CreateVideoCommand,
)
from src.contexts.content_creation.videos.application.video_creator import VideoCreator
from src.contexts.content_creation.videos.infra.in_memory_video_repository import (
    InMemoryVideoRepository,
)
from src.delivery.api.videos.video_create_request import CreateVideoRequest

router = APIRouter(prefix="/videos", tags=["Videos"])


def creator_provider() -> VideoCreator:
    repository = InMemoryVideoRepository()
    return VideoCreator(repository)


@router.put("/{_id}")
async def create_video(
    _id: str,
    request: CreateVideoRequest,
    video_creator: VideoCreator = Depends(creator_provider),
) -> JSONResponse:
    command = CreateVideoCommand(_id, request.title, request.description)

    video_creator(command)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={})
