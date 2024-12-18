from tests.contexts.platform.video_comments_counter.domain.video_comment_counter_mother import (
    VideoCommentCounterMother,
)
from tests.contexts.platform.video_comments_counter.video_comment_counter_module_integration_test_config import (
    VideoCommentCounterModuleIntegrationTestConfig,
)


class TestPostgresVideoCommentCounterRepository(
    VideoCommentCounterModuleIntegrationTestConfig
):
    def test_should_save_a_video_comment_counter(self) -> None:
        video_comment_counter = VideoCommentCounterMother.create()

        self.postgres_video_comment_counter_repository.save(video_comment_counter)

        saved_video_comment_counter = (
            self.postgres_video_comment_counter_repository.search(
                video_comment_counter.video_id
            )
        )
        self.assert_video_comment_counters_match(
            video_comment_counter, saved_video_comment_counter
        )

    def test_should_find_existing_video(self) -> None:
        video_comment_counter = VideoCommentCounterMother.create()
        self.postgres_video_comment_counter_repository.save(video_comment_counter)

        searched_video_comment_counter = (
            self.postgres_video_comment_counter_repository.search(
                video_comment_counter.video_id
            )
        )

        self.assert_video_comment_counters_match(
            video_comment_counter, searched_video_comment_counter
        )

    def test_should_not_find_non_existing_video(self) -> None:
        video_comment_counter = VideoCommentCounterMother.create()

        searched_video_comment_counter = (
            self.postgres_video_comment_counter_repository.search(
                video_comment_counter.video_id
            )
        )

        self.assert_has_not_found(searched_video_comment_counter)
