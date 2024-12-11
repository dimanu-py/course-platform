import pytest
from doublex import Spy
from doublex_expects import have_been_called_with
from expects import expect

from src.contexts.platform.shared.domain.event.event_bus import EventBus
from src.contexts.platform.video_comments.domain.video_comment import VideoComment
from src.contexts.platform.video_comments.domain.video_comment_repository import (
    VideoCommentRepository,
)


@pytest.mark.unit
class VideoCommentModuleUnitTestConfig:
    repository = Spy(VideoRepository)
    repository = Spy(VideoCommentRepository)

    def should_have_saved(self, video_comment: VideoComment) -> None:
        expect(self.repository.save).to(have_been_called_with(video_comment))
