from typing import override

from src.contexts.content_creation.videos.domain.video import Video
from src.contexts.content_creation.videos.domain.video_id import VideoId
from src.contexts.content_creation.videos.domain.video_repository import VideoRepository
from src.contexts.content_creation.videos.infra.persistence.sqlalchemy.video_model import (
    VideoModel,
)
from src.contexts.content_creation.shared.infra.sqlalchemy.session_maker import (
    SessionMaker,
)


class PostgresVideoRepository(VideoRepository):
    _session_maker: SessionMaker

    def __init__(self, session_maker: SessionMaker) -> None:
        self._session_maker = session_maker

    @override
    def save(self, video: Video) -> None:
        with self._session_maker.get_session() as session:
            video_to_insert = VideoModel(**video.to_dict())
            session.add(video_to_insert)
            session.commit()

    @override
    def search(self, video_id: VideoId) -> Video | None:
        with self._session_maker.get_session() as session:
            video = (
                session.query(VideoModel)
                .filter(VideoModel.id == video_id.value)
                .first()
            )

        return (
            Video.create(str(video.id), video.title, video.description)  # type: ignore
            if video
            else None
        )
