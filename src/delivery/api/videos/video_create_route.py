from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_connection import (
    RabbitMqConnection,
)
from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_event_bus import (
    RabbitMqEventBus,
)
from src.contexts.platform.shared.infra.persistence.sqlalchemy.session_maker import (
    SessionMaker,
)
from src.contexts.platform.videos.application.create.create_video_command import (
    CreateVideoCommand,
)
from src.contexts.platform.videos.application.create.video_creator import VideoCreator
from src.contexts.platform.videos.infra.persistence.postgres_video_repository import (
    PostgresVideoRepository,
)
from src.delivery.api.dependency_provider import (
    session_maker_provider,
    rabbit_mq_connection_provider,
)
from src.delivery.api.videos.video_create_request import CreateVideoRequest

router = APIRouter(prefix="/videos", tags=["Videos"])


def creator_provider(
    session_maker: SessionMaker = Depends(session_maker_provider),
    rabbit_mq_client: RabbitMqConnection = Depends(rabbit_mq_connection_provider),
) -> VideoCreator:
    repository = PostgresVideoRepository(session_maker=session_maker)
    event_bus = RabbitMqEventBus(client=rabbit_mq_client, exchange_name="videos")
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
