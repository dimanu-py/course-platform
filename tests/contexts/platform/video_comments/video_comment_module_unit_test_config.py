import pytest
from doublex import Spy
from doublex_expects import have_been_called_with
from expects import expect

from src.contexts.platform.shared.domain.event.event_bus import EventBus
from src.contexts.platform.video_comments.domain.video_comment import VideoComment
from src.contexts.platform.video_comments.domain.video_comment_created_domain_event import (
    VideoCommentCreatedDomainEvent,
)
from src.contexts.platform.video_comments.domain.video_comment_repository import (
    VideoCommentRepository,
)


@pytest.mark.unit
class VideoCommentModuleUnitTestConfig:
    repository = Spy(VideoCommentRepository)
    event_bus = Spy(EventBus)

    def should_have_saved(self, video_comment: VideoComment) -> None:
        expect(self.repository.save).to(have_been_called_with(video_comment))

    def should_have_published(
        self, events: list[VideoCommentCreatedDomainEvent]
    ) -> None:
        expect(self.event_bus.publish).to(have_been_called_with(events))
