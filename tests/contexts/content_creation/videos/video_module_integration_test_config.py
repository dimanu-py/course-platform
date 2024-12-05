import pytest
from expects import expect, equal

from src.contexts.content_creation.videos.domain.video import Video
from src.contexts.content_creation.videos.infra.in_memory_video_repository import (
    InMemoryVideoRepository,
)
from src.contexts.content_creation.videos.infra.postgres_video_repository import (
    PostgresVideoRepository,
)
from src.contexts.shared.infra.persistence.session_maker import SessionMaker
from tests.contexts.content_creation.videos.domain.video_mother import VideoMother


@pytest.mark.integration
class VideoModuleIntegrationTestConfig:
    NO_VIDEO = None
    video = VideoMother.create()

    def setup_method(self) -> None:
        self.in_memory_repository = InMemoryVideoRepository()
        self.session_maker = SessionMaker(
            "postgresql://admin:admin@localhost:5432/influencer-platform"
        )
        self.session_maker.create_tables()
        self.postgres_video_repository = PostgresVideoRepository(self.session_maker)

    def teardown_method(self) -> None:
        self.session_maker.close_session()
        self.session_maker.drop_tables()

    def assert_video_matches(self, video: Video | None) -> None:
        expect(video).to(equal(self.video))

    def assert_has_not_found(self, video: Video | None) -> None:
        expect(video).to(equal(self.NO_VIDEO))
