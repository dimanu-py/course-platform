import pytest
from doublex import Spy
from doublex_expects import have_been_called_with
from expects import expect

from src.contexts.platform.shared.domain.event.domain_event import DomainEvent
from src.contexts.platform.shared.domain.event.event_bus import EventBus
from src.contexts.platform.videos.domain.video import Video
from src.contexts.platform.videos.domain.video_repository import VideoRepository


@pytest.mark.unit
class VideoModuleUnitTestConfig:
    repository = Spy(VideoRepository)
    event_bus = Spy(EventBus)

    def should_have_saved(self, video: Video):
        expect(self.repository.save).to(have_been_called_with(video))

    def should_have_published(self, domain_event: list[DomainEvent]) -> None:
        expect(self.event_bus.publish).to(have_been_called_with(domain_event))
