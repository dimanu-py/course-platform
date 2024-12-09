import pytest
from expects import expect, equal

from src.contexts.content_creation.videos.domain.video import Video
from src.contexts.content_creation.videos.infra.persistence.in_memory_video_repository import (
    InMemoryVideoRepository,
)
from src.contexts.content_creation.videos.infra.persistence.postgres_video_repository import (
    PostgresVideoRepository,
)
from src.contexts.content_creation.videos.infra.persistence.sqlalchemy.video_model import (
    VideoModel,
)
from src.contexts.content_creation.shared.infra.sqlalchemy.session_maker import (
    SessionMaker,
)


@pytest.mark.integration
class VideoModuleIntegrationTestConfig:
    NO_VIDEO = None

    def setup_method(self) -> None:
        self.in_memory_repository = InMemoryVideoRepository()
        self.session_maker = SessionMaker(
            "postgresql://admin:admin@localhost:5432/influencer-platform"
        )
        self.session_maker.create_tables()
        self.postgres_video_repository = PostgresVideoRepository(self.session_maker)

    def teardown_method(self) -> None:
        with self.session_maker.get_session() as session:
            session.query(VideoModel).delete()
            session.commit()

    def assert_videos_match(
        self, video: Video | None, expected_video: Video | None
    ) -> None:
        expect(video).to(equal(expected_video))

    def assert_has_not_found(self, video: Video | None) -> None:
        expect(video).to(equal(self.NO_VIDEO))
