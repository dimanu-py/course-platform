import pytest
from doublex import Mock
from doublex_expects import have_been_satisfied
from expects import expect

from src.contexts.platform.video_comments_counter.domain.video_comment_counter import (
    VideoCommentCounter,
)
from src.contexts.platform.video_comments_counter.domain.video_comment_counter_repository import (
    VideoCommentCounterRepository,
)


@pytest.mark.unit
class VideoCommentCounterModuleUnitTestConfig:
    repository = Mock(VideoCommentCounterRepository)

    def should_search(self, video_comment_counter: VideoCommentCounter) -> None:
        with self.repository as repository:
            repository.search(video_comment_counter.video_id).returns(
                video_comment_counter
            )

    def should_save(self, video_comment_counter: VideoCommentCounter) -> None:
        with self.repository as repository:
            repository.save(video_comment_counter)

    def should_have_saved(self) -> None:
        expect(self.repository).to(have_been_satisfied)
