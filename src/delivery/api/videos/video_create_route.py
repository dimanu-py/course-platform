from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from src.contexts.platform.videos.application.create_video_command import (
    CreateVideoCommand,
)
from src.contexts.platform.videos.application.video_creator import VideoCreator
from src.contexts.platform.videos.infra.persistence.postgres_video_repository import (
    PostgresVideoRepository,
)
from src.contexts.platform.shared.infra.sqlalchemy.session_maker import (
    SessionMaker,
)
from src.delivery.api.videos.video_create_request import CreateVideoRequest

router = APIRouter(prefix="/videos", tags=["Videos"])


def creator_provider() -> VideoCreator:
    session_maker = SessionMaker(
        "postgresql://admin:admin@localhost:5432/influencer-platform"
    )
    repository = PostgresVideoRepository(session_maker)
    session_maker.create_tables()
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
