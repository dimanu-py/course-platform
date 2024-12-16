from typing import override

from src.contexts.platform.shared.infra.persistence.sqlalchemy.sqlalchemy_repository import (
    SqlAlchemyRepository,
)
from src.contexts.platform.videos.domain.video import Video
from src.contexts.platform.videos.domain.video_id import VideoId
from src.contexts.platform.videos.domain.video_repository import VideoRepository
from src.contexts.platform.videos.infra.persistence.sqlalchemy.video_model import (
    VideoModel,
)
from src.contexts.platform.shared.infra.persistence.sqlalchemy.session_maker import (
    SessionMaker,
)


class PostgresVideoRepository(SqlAlchemyRepository[VideoModel], VideoRepository):
    _session_maker: SessionMaker

    def __init__(self, session_maker: SessionMaker) -> None:
        super().__init__(session_maker=session_maker, model_class=VideoModel)

    @override
    def save(self, video: Video) -> None:
        self.persist(video)

    @override
    def search(self, video_id: VideoId) -> Video | None:
        return self.search_by_id(video_id)
