from tests.contexts.content_creation.videos.domain.video_mother import VideoMother
from tests.contexts.content_creation.videos.video_module_integration_test_config import (
    VideoModuleIntegrationTestConfig,
)


class TestInMemoryVideoRepository(VideoModuleIntegrationTestConfig):
    def test_should_save_a_video(self) -> None:
        video = VideoMother.create()

        self.in_memory_repository.save(video)

        saved_video = self.in_memory_repository.search(video.id)
        self.assert_videos_match(video, saved_video)

    def test_should_find_existing_video(self) -> None:
        video = VideoMother.create()
        self.in_memory_repository.save(video)

        searched_video = self.in_memory_repository.search(video.id)

        self.assert_videos_match(video, searched_video)

    def test_should_not_find_non_existing_video(self) -> None:
        video = VideoMother.create()

        searched_video = self.in_memory_repository.search(video.id)

        self.assert_has_not_found(searched_video)
