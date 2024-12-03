from tests.contexts.backoffice.videos.video_module_integration_test_config import (
    VideoModuleIntegrationTestConfig,
)


class TestInMemoryVideoRepository(VideoModuleIntegrationTestConfig):
    def test_should_save_a_video(self) -> None:
        self.repository.save(self.video)

        saved_video = self.repository.search(self.video.id)
        self._should_have(saved_video)

    def test_should_find_existing_video(self) -> None:
        self.repository.save(self.video)

        searched_video = self.repository.search(self.video.id)

        self._should_have(searched_video)

    def test_should_not_find_non_existing_video(self) -> None:
        searched_video = self.repository.search(self.video.id)

        self.should_not_have(searched_video)
