import pytest
from expects import expect, equal

from src.contexts.backoffice.videos.domain.video import Video
from src.contexts.backoffice.videos.infra.in_memory_video_repository import (
    InMemoryVideoRepository,
)
from tests.contexts.backoffice.videos.domain.video_mother import VideoMother


@pytest.mark.integration
class TestInMemoryVideoRepository:
    video = VideoMother.create()
    NO_VIDEO = None

    def setup_method(self) -> None:
        self.repository = InMemoryVideoRepository()

    def test_should_save_a_video(self) -> None:
        self.repository.save(self.video)

        saved_video = self.repository.search(self.video.id)
        self._should_have_saved(saved_video)

    def test_should_find_existing_video(self) -> None:
        self.repository.save(self.video)

        searched_video = self.repository.search(self.video.id)

        self._should_have_found(searched_video)

    def test_should_not_find_non_existing_video(self) -> None:
        searched_video = self.repository.search(self.video.id)

        expect(searched_video).to(equal(self.NO_VIDEO))

    def _should_have_saved(self, video: Video | None) -> None:
        self._compare_videos(video)

    def _should_have_found(self, video: Video | None) -> None:
        self._compare_videos(video)

    def _compare_videos(self, video: Video | None) -> None:
        expect(video).to(equal(self.video))
