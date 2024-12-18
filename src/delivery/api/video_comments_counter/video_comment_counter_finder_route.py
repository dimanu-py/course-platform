from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.contexts.platform.shared.infra.persistence.sqlalchemy.session_maker import (
    SessionMaker,
)
from src.contexts.platform.video_comments_counter.application.find.find_video_comment_counter_query import (
    FindVideoCommentCounterQuery,
)
from src.contexts.platform.video_comments_counter.application.find.video_comment_counter_finder import (
    VideoCommentCounterFinder,
)
from src.contexts.platform.video_comments_counter.infra.persistence.postgres_video_comment_counter_repository import (
    PostgresVideoCommentCounterRepository,
)

from src.delivery.api.dependency_provider import session_maker_provider
from src.delivery.api.video_comments_counter.video_total_comments_response import (
    VideoTotalCommentsResponse,
)

router = APIRouter(prefix="/comments_counter", tags=["Comments"])


def finder_provider(
    session_maker: SessionMaker = Depends(session_maker_provider),
) -> VideoCommentCounterFinder:
    repository = PostgresVideoCommentCounterRepository(session_maker=session_maker)
    session_maker.create_tables()
    return VideoCommentCounterFinder(repository=repository)


@router.get("/{video_id}")
async def get_video_comment_counter(
    video_id: str,
    video_comment_counter_finder: VideoCommentCounterFinder = Depends(finder_provider),
) -> JSONResponse:
    query = FindVideoCommentCounterQuery(video_id=video_id)

    total_comments = video_comment_counter_finder(query)

    response = VideoTotalCommentsResponse(total_comments)
    return JSONResponse(status_code=status.HTTP_200_OK, content=response.model_dump())
