import pytest
from expects import expect, equal

from src.contexts.platform.shared.infra.persistence.sqlalchemy.session_maker import (
    SessionMaker,
)
from src.contexts.platform.video_comments_counter.domain.video_comment_counter import (
    VideoCommentCounter,
)
from src.contexts.platform.video_comments_counter.infra.persistence.postgres_video_comment_counter_repository import (
    PostgresVideoCommentCounterRepository,
)
from src.contexts.platform.video_comments_counter.infra.persistence.sqlaclhemy.video_comment_counter_model import (
    VideoCommentCounterModel,
)


@pytest.mark.integration
class VideoCommentCounterModuleIntegrationTestConfig:
    NO_VIDEO_COMMENT_COUNTER = None

    def setup_method(self) -> None:
        self.session_maker = SessionMaker(
            "postgresql://admin:admin@localhost:5432/course-platform"
        )
        self.session_maker.create_tables()
        self.postgres_video_comment_counter_repository = (
            PostgresVideoCommentCounterRepository(self.session_maker)
        )

    def teardown_method(self) -> None:
        with self.session_maker.get_session() as session:
            session.query(VideoCommentCounterModel).delete()
            session.commit()

    def assert_video_comment_counters_match(
        self,
        video_comment_counter: VideoCommentCounter | None,
        expected_video_comment_counter: VideoCommentCounter | None,
    ) -> None:
        expect(video_comment_counter).to(equal(expected_video_comment_counter))

    def assert_has_not_found(
        self, video_comment_counter: VideoCommentCounter | None
    ) -> None:
        expect(video_comment_counter).to(equal(self.NO_VIDEO_COMMENT_COUNTER))
