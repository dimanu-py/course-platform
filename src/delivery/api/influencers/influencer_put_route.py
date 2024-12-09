from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from src.contexts.content_creation.influencers.application.create_influencer_command import (
    CreateInfluencerCommand,
)
from src.contexts.content_creation.influencers.application.influencer_creator import (
    InfluencerCreator,
)
from src.contexts.content_creation.influencers.infra.persistence.postgres_influencer_repository import (
    PostgresInfluencerRepository,
)
from src.contexts.content_creation.shared.infra.sqlalchemy.session_maker import (
    SessionMaker,
)
from src.delivery.api.influencers.influencer_create_request import (
    CreateInfluencerRequest,
)

router = APIRouter(prefix="/influencers", tags=["Influencers"])


async def creator_provider() -> InfluencerCreator:
    session_maker = SessionMaker(
        "postgresql://admin:admin@localhost:5432/influencer-platform"
    )
    session_maker.create_tables()
    repository = PostgresInfluencerRepository(session_maker)
    return InfluencerCreator(repository)


@router.put("/{id_}")
async def create_influencer(
    id_: str,
    request: CreateInfluencerRequest,
    influencer_creator: InfluencerCreator = Depends(creator_provider),
) -> JSONResponse:
    command = CreateInfluencerCommand(
        id_, request.name, request.username, request.email
    )

    influencer_creator(command)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={})
