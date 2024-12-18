from typing import override

from src.contexts.platform.shared.infra.persistence.sqlalchemy.session_maker import (
    SessionMaker,
)
from src.contexts.platform.shared.infra.persistence.sqlalchemy.sqlalchemy_repository import (
    SqlAlchemyRepository,
)
from src.contexts.platform.video_comments_counter.domain.video_comment_counter import (
    VideoCommentCounter,
)
from src.contexts.platform.video_comments_counter.domain.video_comment_counter_repository import (
    VideoCommentCounterRepository,
)
from src.contexts.platform.video_comments_counter.infra.persistence.sqlaclhemy.video_comment_counter_model import (
    VideoCommentCounterModel,
)
from src.contexts.platform.videos.domain.video_id import VideoId


class PostgresVideoCommentCounterRepository(
    SqlAlchemyRepository[VideoCommentCounterModel], VideoCommentCounterRepository
):
    def __init__(self, session_maker: SessionMaker) -> None:
        super().__init__(
            session_maker=session_maker, model_class=VideoCommentCounterModel
        )

    @override
    def save(self, counter: VideoCommentCounter) -> None:
        self.persist(counter)

    @override
    def search(self, video_id: VideoId) -> VideoCommentCounter | None:
        return self.search_by_id(video_id)
