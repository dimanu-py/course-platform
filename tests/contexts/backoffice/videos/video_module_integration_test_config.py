import pytest
from expects import expect, equal

from src.contexts.backoffice.videos.domain.video import Video
from src.contexts.backoffice.videos.infra.in_memory_video_repository import (
    InMemoryVideoRepository,
)
from tests.contexts.backoffice.videos.domain.video_mother import VideoMother


@pytest.mark.integration
class VideoModuleIntegrationTestConfig:
    NO_VIDEO = None
    video = VideoMother.create()

    def setup_method(self) -> None:
        self.repository = InMemoryVideoRepository()

    def _should_have(self, video: Video | None) -> None:
        expect(video).to(equal(self.video))

    def should_not_have(self, video: Video | None) -> None:
        expect(video).to(equal(self.NO_VIDEO))
