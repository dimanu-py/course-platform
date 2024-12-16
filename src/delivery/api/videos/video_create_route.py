from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from src.contexts.platform.shared.domain.event.event_bus import EventBus
from src.contexts.platform.videos.application.create.create_video_command import (
    CreateVideoCommand,
)
from src.contexts.platform.videos.application.create.video_creator import VideoCreator
from src.contexts.platform.videos.infra.persistence.postgres_video_repository import (
    PostgresVideoRepository,
)
from src.contexts.platform.shared.infra.persistence.sqlalchemy.session_maker import (
    SessionMaker,
)
from src.delivery.api.videos.video_create_request import CreateVideoRequest

router = APIRouter(prefix="/videos", tags=["Videos"])


def creator_provider() -> VideoCreator:
    session_maker = SessionMaker(
        url="postgresql://admin:admin@localhost:5432/influencer-platform"
    )
    repository = PostgresVideoRepository(session_maker=session_maker)
    event_bus = EventBus()
    session_maker.create_tables()
    return VideoCreator(repository=repository, event_bus=event_bus)


@router.put("/{id_}")
async def create_video(
    id_: str,
    request: CreateVideoRequest,
    video_creator: VideoCreator = Depends(creator_provider),
) -> JSONResponse:
    command = CreateVideoCommand(
        id=id_, title=request.title, description=request.description
    )

    video_creator(command)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={})
